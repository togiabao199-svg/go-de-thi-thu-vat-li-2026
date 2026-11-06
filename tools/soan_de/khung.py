#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Giai đoạn 5 — sinh KHUNG đề luyện thi từ kho/phan-bo.csv để soạn tiếp.

Khung có đúng bố cục mau-de-thi-thu.tex (preamble v2, 3 phần, \\Opensolutionfile ans/<tên>-k, bảng đáp án
để comment). Mỗi câu lấy từ ngân hàng (kho/ngan-hang/), đã áp đáp án sau kiểm chứng (giai đoạn 4):
  - dòng `% <mã câu>` ngay sau \\begin{ex} (giữ lại trong thành phẩm để tra cứu);
  - các dòng `%@ ...` là GHI CHÚ SOẠN (vị trí, ghi chú chấm, kết quả kiểm chứng, chỗ sửa lời văn đã duyệt,
    mô tả hình theo kho/danh-gia/hinh.tsv kèm đường dẫn ảnh gốc). PHẢI XÓA HẾT khi soạn xong;
  - hình: khối \\begin{center} ... \\end{center} chứa dòng `%@ HÌNH k ...` để thay bằng TikZ/pgfplots/tkz-tab;
  - lời giải gốc đặt trong \\loigiai (cần viết lại theo QUY CHUẨN LỜI GIẢI của CLAUDE.md).
Ảnh gốc tách ra thư mục --anh (mặc định <scratch>/anh-goc/DeXX/), không đặt trong de/.

Dùng (chạy từ gốc repo):
    python3 tools/soan_de/khung.py 01 02 03 [--anh <thư mục>] [--ghi-de] [--thu-muc <thư mục>]
Kết quả: de/LuyenDe-TN2027-DeXX/LuyenDe-TN2027-DeXX.tex (không ghi đè file đã có nếu thiếu --ghi-de);
--thu-muc ghi ra <thư mục>/LuyenDe-TN2027-DeXX/ thay cho de/ (vd lấy khung câu thay thế cho đề đã soạn).
"""
import csv
import os
import re
import sys

GOC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(GOC, 'tools'))
sys.path.insert(0, os.path.join(GOC, 'tools', 'danh_gia'))
import xem_thu as xt  # noqa: E402
from chung import doc_de  # noqa: E402

TIEN_TO = 'LuyenDe-TN2027-De'
NHOM = {'cb': 'mức cơ bản', 'tt': 'mức thi thật'}
TIEU_DE = {
    'I': 'PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn. Thí sinh trả lời từ câu 1 đến câu 12. '
         'Mỗi câu hỏi thí sinh chỉ chọn một phương án.',
    'II': 'PHẦN II. Câu trắc nghiệm đúng sai. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) '
          'ở mỗi câu, thí sinh chọn đúng hoặc sai.',
    'III': 'PHẦN III. Câu trắc nghiệm trả lời ngắn. Thí sinh trả lời từ câu 1 đến câu 6.',
}


def doc_tsv(fn, khoa='id', nhieu=False):
    t = {}
    p = os.path.join(GOC, fn)
    if not os.path.exists(p):
        return t
    for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'):
        if nhieu:
            t.setdefault(r[khoa], []).append(r)
        else:
            t[r[khoa]] = r
    return t


_cache = {}


def lay_cau(id_):
    ma = id_.split('-')[0]
    if ma not in _cache:
        _cache[ma] = {q['id']: q for q in doc_de(ma)['cau']}
    return _cache[ma][id_]


def mot_dong(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()


class Ctx:
    def __init__(self, anh_dir):
        self.hinh = doc_tsv('kho/danh-gia/hinh.tsv', nhieu=True)
        self.kc = doc_tsv('kho/kiem-chung.tsv')
        self.dk = doc_tsv('kho/danh-gia/do-kho-tln.tsv')
        th = os.path.join(GOC, 'kho', 'danh-gia', 'tong-hop.csv')
        self.cham = {r['id']: r for r in csv.DictReader(open(th, encoding='utf-8'))} if os.path.exists(th) else {}
        self.anh_dir = anh_dir
        self.imgs = xt.Images(anh_dir) if anh_dir else None


def anh_goc(q, h, ctx):
    """Tách ảnh gốc ra thư mục ảnh, trả về đường dẫn tuyệt đối (hoặc '')."""
    if not ctx.imgs:
        return ''
    try:
        if h['loai'] == 'anh':
            p = ctx.imgs.get(os.path.join(GOC, q['file_goc']), q['de_goc'], h.get('file'))
            return os.path.join(os.path.dirname(ctx.anh_dir), p) if p else ''
        if h.get('anh_dung'):
            return os.path.join(GOC, h['anh_dung'])
    except Exception as e:  # noqa
        return '(lỗi tách ảnh: %s)' % e
    return ''


def khoi_hinh(q, k, ctx):
    h = q['hinh'][k - 1] if 0 < k <= len(q['hinh']) else None
    if not h:
        return ''
    mt = [r for r in ctx.hinh.get(q['id'], []) if r['so'] == str(k)]
    ve = mt[0]['ve_lai'] if mt else '?'
    mo_ta = mot_dong(mt[0]['mo_ta']) if mt else mot_dong(h.get('mo_ta'))
    duong = anh_goc(q, h, ctx)
    dong = ['\\begin{center}',
            '\t%%@ HÌNH %d [%s] (vị trí: %s): %s' % (k, ve, h['vi_tri'], mo_ta)]
    if duong:
        dong.append('\t%%@ ẢNH GỐC: %s' % duong)
    dong.append('\\end{center}')
    return '\n'.join(dong)


def dat_hinh(s, q, ctx):
    return re.sub(r'\[\[HINH (\d+)\]\]', lambda m: khoi_hinh(q, int(m.group(1)), ctx), s or '')


def ghi_chu_soan(q, p, ctx):
    L = []
    bits = ['vị trí %s' % p['vi_tri'], 'ô %s (%s)' % (p['o'], p['muc_o']), p['ma_dang'], 'mức ' + p['muc']]
    if p['muc_y']:
        bits.append('mức ý ' + p['muc_y'])
    if p.get('diem_con'):
        bits.append('điểm con ' + p['diem_con'])
    bits += [p['kieu'], p['chat_luong']]
    L.append('%@ ' + ' | '.join(bits))
    if p.get('ghi_chu'):
        L.append('%@ GHI CHÚ CHẤM: ' + mot_dong(p['ghi_chu']))
    c = ctx.cham.get(q['id'])
    if c and c.get('ghi_chu') and mot_dong(c['ghi_chu']) != mot_dong(p.get('ghi_chu')):
        L.append('%@ GHI CHÚ GIAI ĐOẠN 2: ' + mot_dong(c['ghi_chu']))
    d = ctx.dk.get(q['id'])
    if d and d.get('ly_do'):
        L.append('%@ ĐỘ KHÓ: ' + mot_dong(d['ly_do']))
    k = ctx.kc.get(q['id'])
    if k:
        L.append('%%@ KIỂM CHỨNG (giai đoạn 4): %s | %s' % (k['ket_qua'], mot_dong(k['ghi_chu'])))
        if k.get('dap_an_moi'):
            L.append('%%@ ĐÁP ÁN ĐÃ SỬA (đã duyệt): gốc %s -> mới %s (khung đã gắn \\True theo đáp án mới; '
                     'ghi "%% KIỂM TRA: <gốc> / <mới>" ngay sau dòng mã câu)' % (k['dap_an_goc'], k['dap_an_moi']))
        if k.get('sua_de'):
            L.append('%@ SỬA LỜI VĂN/LỜI GIẢI (đã duyệt, PHẢI ÁP DỤNG): ' + mot_dong(k['sua_de']))
    for cb in q.get('canh_bao') or []:
        L.append('%@ CẢNH BÁO TRÍCH XUẤT: ' + mot_dong(cb))
    return L


def loi_giai_goc(q, ctx):
    if q['loai'] == 'DS':
        lg = q.get('loi_giai') or {}
        parts = []
        if isinstance(lg, dict):
            if lg.get('chung'):
                parts.append(dat_hinh(lg['chung'], q, ctx))
            items = ['\\begin{itemchoice}']
            ys = lg.get('y') or [''] * 4
            for i in range(4):
                v = q['dap_an'][i]
                head = '{\\bf Đúng.}' if v == 'Đ' else '{\\bf Sai.}'
                y = ys[i] if i < len(ys) else ''
                items.append('\t\\itemch %s\\\\\n%s' % (head, xt.indent(dat_hinh(y, q, ctx) or '%@ (trống)', 1)))
            items.append('\\end{itemchoice}')
            parts.append('\n'.join(items))
        s = '\n'.join(parts)
    else:
        s = dat_hinh(q.get('loi_giai') or '', q, ctx)
    if not s.strip() and q.get('loi_giai_pdf'):
        s = '\n'.join('%@ LG PDF: ' + ln for ln in q['loi_giai_pdf'].splitlines() if ln.strip())
    if not s.strip():
        s = '%@ (Bản gốc không có lời giải: tự giải.)'
    return '%@ LỜI GIẢI GỐC bên dưới: viết lại đầy đủ theo QUY CHUẨN LỜI GIẢI (CLAUDE.md), kết thúc "Vậy ..."\n' + s


def ex_khung(q, p, ctx):
    L = []
    if any(h['vi_tri'] != 'loi-giai' for h in q.get('hinh') or []):
        L.append('\\Needspace{16\\baselineskip}')
    L.append('\\begin{ex}')
    body = ['% ' + q['id']]
    body += ghi_chu_soan(q, p, ctx)
    body.append(dat_hinh(q['noi_dung'], q, ctx))
    if q['loai'] == 'TN':
        body.append('\\choice')
        for i, o in enumerate(q['phuong_an']):
            o = dat_hinh(o, q, ctx)
            body.append('{%s%s}' % ('\\True ' if q['dap_an'] == 'ABCD'[i] else '', o))
    elif q['loai'] == 'DS':
        body.append('\\choiceTFt')
        for i, o in enumerate(q['menh_de']):
            o = dat_hinh(o, q, ctx)
            body.append('{%s%s}' % ('\\True ' if q['dap_an'][i] == 'Đ' else '', o))
    else:
        body.append('\\par')
        body.append('\\shortans[oly]{%s}' % xt.shortans_val(q['dap_an']))
    body.append('\\loigiai{\n%s\n}' % xt.indent(loi_giai_goc(q, ctx), 1))
    txt = re.sub(r'(\\\\\s*)\[', r'\1{}[', '\n'.join(body))
    L.append(xt.indent(txt, 1))
    L.append('\\end{ex}')
    return '\n'.join(L)


def xuat(so, rows, ctx, ghi_de=False, thu_muc=None):
    rr = [r for r in rows if r['de'] == so]
    if not rr:
        raise SystemExit('Không có Đề %s trong kho/phan-bo.csv' % so)
    nhom = rr[0]['nhom']
    ten = TIEN_TO + so
    od = os.path.join(thu_muc, ten) if thu_muc else os.path.join(GOC, 'de', ten)
    fn = os.path.join(od, ten + '.tex')
    if os.path.exists(fn) and not ghi_de:
        print('Bỏ qua (đã có, thêm --ghi-de để ghi đè):', os.path.relpath(fn, GOC))
        return fn
    os.makedirs(od, exist_ok=True)
    out = ['%' + '=' * 69,
           '%% ĐỀ LUYỆN THI TỐT NGHIỆP THPT NĂM 2027 -- ĐỀ SỐ %s (%s) -- dự án 40 đề' % (so, NHOM[nhom]),
           '% Câu lấy theo kho/phan-bo.csv; mã câu nguồn ghi ở dòng comment ngay sau \\begin{ex}.',
           '%' + '=' * 69,
           '\\def\\CheDo{solcolor}% loigiai | dethi',
           '\\def\\tenchuong{Luyện thi tốt nghiệp THPT năm 2027 -- Đề số %s}' % so,
           '\\input{preamble-eduzy-v2}',
           '\\begin{document}',
           '\t\\khungtieude{ĐỀ LUYỆN THI TỐT NGHIỆP THPT NĂM 2027 -- ĐỀ SỐ %s}{Môn Toán}'
           '{(Đề thi gồm: 12 câu trắc nghiệm, 04 câu đúng-sai, 06 câu trả lời ngắn)}'
           '{Thời gian làm bài: 90 phút (không kể thời gian phát đề).}' % so]
    for k, phan in enumerate(('I', 'II', 'III'), 1):
        out.append('\t')
        if phan == 'I':
            out.append('\t\\noindent')
        out.append('\t\\subsection*{\\indam{%s}}' % TIEU_DE[phan])
        out.append('\t\\setcounter{ex}{0}')
        out.append('\t\\Opensolutionfile{ans}[ans/%s-%d]' % (ten, k))
        for p in sorted((r for r in rr if r['phan'] == phan), key=lambda r: int(r['thu_tu'])):
            out.append('\t')
            out.append(xt.indent(ex_khung(lay_cau(p['id']), p, ctx), 1))
        out.append('\t')
        if phan == 'III':
            out.append('\t\\centerline{--- HẾT ---}')
        out.append('\t\\Closesolutionfile{ans}')
    out += ['\t',
            '\t%===================== BẢNG ĐÁP ÁN =====================',
            '\t%\\newpage',
            '\t%\\begin{center}\\indam{BẢNG ĐÁP ÁN}\\end{center}',
            '\t%\\noindent\\indam{PHẦN I.}\\\\',
            '\t%%\\inputansbox{6}{ans/%s-1}' % ten,
            '\t%\\noindent\\indam{PHẦN II.}\\\\',
            '\t%%\\inputansbox{2}{ans/%s-2}' % ten,
            '\t%\\noindent\\indam{PHẦN III.}\\\\',
            '\t%%\\inputansbox{6}{ans/%s-3}' % ten,
            '\\end{document}']
    with open(fn, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print('Đã ghi', fn if thu_muc else os.path.relpath(fn, GOC))
    return fn


def main(argv):
    a = list(argv)
    ghi_de = '--ghi-de' in a
    if ghi_de:
        a.remove('--ghi-de')
    thu_muc = None
    if '--thu-muc' in a:
        i = a.index('--thu-muc'); thu_muc = os.path.abspath(a[i + 1]); del a[i:i + 2]
    anh = None
    if '--anh' in a:
        i = a.index('--anh'); anh = a[i + 1]; del a[i:i + 2]
    so_de = ['%02d' % int(x) for x in a if x.isdigit()]
    rows = list(csv.DictReader(open(os.path.join(GOC, 'kho', 'phan-bo.csv'), encoding='utf-8')))
    for so in so_de:
        d = os.path.join(anh, 'De' + so) if anh else None
        ctx = Ctx(os.path.join(d, 'hinh') if d else None)
        xuat(so, rows, ctx, ghi_de, thu_muc)


if __name__ == '__main__':
    main(sys.argv[1:])
