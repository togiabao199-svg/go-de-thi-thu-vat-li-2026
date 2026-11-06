# -*- coding: utf-8 -*-
"""
Đọc file PDF đáp án (xuất từ Word) khi không có file Word đáp án — hiện chỉ dùng cho TT32
(TT32-de.docx là đề, TT32-dap-an.pdf là đề + lời giải).

Lấy được:
  - Phần I: chữ cái phương án được gạch chân (Word xuất nét gạch chân thành hình chữ nhật mảnh ngay dưới chữ);
  - Phần II: kết luận "mệnh đề a) đúng/sai" hoặc "a) Đúng." trong lời giải;
  - Phần III: các chữ số ghi trong ô "Trả lời:";
  - Lời giải: văn bản thô (công thức trong PDF mất cấu trúc: phân số, căn, chỉ số bị tách dòng) -> cần gõ lại.

    python3 tools/pdf_dap_an.py kho/de-tu-soan/thi-thu/TT32-dap-an.pdf
"""
import re
import sys
import warnings

warnings.filterwarnings('ignore')
import pymupdf  # noqa: E402

RE_PART = re.compile(r'^\s*PHẦN\s+(I{1,3})\b')
RE_CAU = re.compile(r'^\s*Câu\s*(\d{1,2})\s*[:.]')
RE_LG = re.compile(r'^\s*Lời giải\s*$')
RE_TL = re.compile(r'^\s*Trả lời\s*:?\s*$')
HEADER_FOOTER = re.compile(r'CHINH PHỤC KỲ THI|MÔN TOÁN 2026|Eduzy\.com\.vn|TRÊN CON ĐƯỜNG THÀNH CÔNG|'
                           r'TOÁN HỌC LÀ NGÔN NGỮ|GV\. Tô Gia Bảo')
RE_VERDICT = re.compile(r'(?:mệnh đề|ý)\s*([a-dA-D])\s*\)?\s*(?:là\s+)?(đúng|sai)', re.I)
RE_VERDICT_HEAD = re.compile(r'^\s*([a-d])\)\s*(Đúng|Sai)\b')


TOP, BOT = 45, 790  # vùng đầu trang / chân trang (pt)


def lines_of(doc):
    """-> danh sách dòng: (trang, y0, y1, chuỗi, [span...]) theo thứ tự đọc, bỏ đầu/chân trang"""
    out = []
    for pno, pg in enumerate(doc):
        d = pg.get_text('dict')
        for b in d['blocks']:
            for l in b.get('lines', []):
                spans = [s for s in l['spans'] if s['text'].strip()]
                if not spans:
                    continue
                t = ' '.join(s['text'] for s in spans)
                y0, y1 = l['bbox'][1], l['bbox'][3]
                if y1 < TOP or y0 > BOT or HEADER_FOOTER.search(t):
                    continue
                out.append((pno, y0, y1, t, spans))
    return out


def underlines(pg):
    res = []
    for dr in pg.get_drawings():
        r = dr['rect']
        if r.height < 2.5 and 3 < r.width < 40 and dr.get('fill') is not None:
            res.append(r)
    return res


def region_text(pdf, doc, a, b):
    """văn bản giữ bố cục (pdftotext -layout) từ vị trí a=(trang, y) đến b=(trang, y)"""
    import subprocess
    out = []
    pa, ya = a
    pb, yb = b
    for p in range(pa, pb + 1):
        y0 = ya if p == pa else TOP
        y1 = yb if p == pb else BOT
        if y1 - y0 < 2:
            continue
        W = int(doc[p].rect.width)
        r = subprocess.run(['pdftotext', '-layout', '-f', str(p + 1), '-l', str(p + 1), '-x', '0', '-y',
                            str(int(y0)), '-W', str(W), '-H', str(int(y1 - y0)), pdf, '-'],
                           capture_output=True, text=True)
        out.append(r.stdout)
    txt = '\n'.join(out)
    lines = [ln.rstrip() for ln in txt.split('\n')]
    # bỏ thụt lề chung, dòng trống liên tiếp
    ind = min((len(ln) - len(ln.lstrip()) for ln in lines if ln.strip()), default=0)
    res = []
    for ln in lines:
        ln = ln[ind:] if ln.strip() else ''
        if ln == '' and (not res or res[-1] == ''):
            continue
        res.append(ln.replace('\f', ''))
    return '\n'.join(res).strip()


def parse(pdf):
    doc = pymupdf.open(pdf)
    ul = {p: underlines(doc[p]) for p in range(len(doc))}
    lines = lines_of(doc)
    part = 0
    qs = []
    cur = None
    phase = None
    for (p, y0, y1, t, spans) in lines:
        m = RE_PART.match(t)
        if m:
            part = {'I': 1, 'II': 2, 'III': 3}[m.group(1)]
            if cur:
                cur['end'] = (p, y0)
            cur = None
            continue
        m = RE_CAU.match(t)
        if m and part:
            if cur:
                cur['end'] = (p, y0)
            cur = {'phan': part, 'so': int(m.group(1)), 'start': (p, y0), 'lg': None, 'tl': None,
                   'end': None, 'gach': None}
            qs.append(cur)
            phase = 'de'
            continue
        if cur is None:
            continue
        if RE_LG.match(t):
            phase = 'giai'
            cur['lg'] = (p, y1)
            cur['lg_top'] = (p, y0)
            continue
        if RE_TL.match(t) and part == 3:
            cur['tl'] = (p, y1)
            continue
        if phase == 'de' and part == 1:
            for s in spans:
                mm = re.match(r'^([A-D])\s*\.', s['text'].strip())
                if not mm:
                    continue
                bx = s['bbox']
                for r in ul[p]:
                    if abs(r.y0 - bx[3]) < 3.5 and r.x0 < bx[0] + 6 and r.x1 > bx[0] + 2:
                        cur['gach'] = mm.group(1)
    if cur:
        cur['end'] = (len(doc) - 1, BOT)
    out = {}
    for q in qs:
        giai = region_text(pdf, doc, q['lg'], q['end']) if q['lg'] else ''
        rec = {'loi_giai_pdf': giai}
        if q['phan'] == 1:
            rec['dap_an'] = q['gach']
        elif q['phan'] == 2:
            v = [None] * 4
            for line in giai.split('\n'):
                mh = RE_VERDICT_HEAD.match(line)
                if mh:
                    v['abcd'.index(mh.group(1))] = mh.group(2) == 'Đúng'
            for mm in RE_VERDICT.finditer(re.sub(r'\s+', ' ', giai)):
                L = 'abcd'.index(mm.group(1).lower())
                if v[L] is None:
                    v[L] = mm.group(2).lower() == 'đúng'
            rec['dap_an'] = [None if x is None else ('Đ' if x else 'S') for x in v]
        else:
            s = ''
            if q['tl']:
                s = region_text(pdf, doc, q['tl'], q.get('lg_top') or q['end']).replace(' ', '').replace('\n', '')
            s = s.replace('.', ',')
            rec['dap_an'] = s if re.fullmatch(r'-?\d+(,\d+)?', s or '') else None
        out[(q['phan'], q['so'])] = rec
    return out


if __name__ == '__main__':
    r = parse(sys.argv[1])
    for k in sorted(r):
        print(k, r[k]['dap_an'], '|', r[k]['loi_giai_pdf'][:100].replace('\n', ' / '))
