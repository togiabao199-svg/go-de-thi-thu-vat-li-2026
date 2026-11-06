#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Giai đoạn 5 — soát tự động một file đề luyện thi đã soạn (so với kho/phan-bo.csv và ngân hàng).

Kiểm:
  - không còn ghi chú soạn `%@`, chỗ đặt hình `[[HINH`, \\includegraphics, \\immini, tkz-euclide;
  - đủ 3 phần, \\Opensolutionfile ans/<tên>-1..3, số câu 12 / 4 / 6;
  - dòng đầu mỗi câu là `% <mã câu>` đúng thứ tự trong kho/phan-bo.csv;
  - đáp án (\\True, \\shortans) khớp đáp án sau kiểm chứng trong ngân hàng (câu có `% KIỂM TRA` chỉ cảnh báo);
  - TN đúng 4 phương án, đúng 1 \\True; Đúng/Sai 4 mệnh đề, lời giải itemchoice 4 \\itemch, nhãn Đúng/Sai khớp \\True;
  - trả lời ngắn: \\par riêng dòng, giá trị số nguyên/thập phân (dấu phẩy {,}), tối đa 4 ký tự;
  - mọi câu có \\loigiai, lời giải có "Vậy"; không gõ "Chọn A/B/C/D"; không $$, \\heva, \\hoac, cases;
  - cảnh báo: \\int không có \\displaystyle, số thập phân dấu chấm, câu thiếu \\Needspace (mọi câu đều cần,
    câu đầu phần đặt trên tiêu đề phần — xem tools/dan_trang/dan_trang.py).

Dùng:  python3 tools/soan_de/kiem_tra.py de/LuyenDe-TN2027-De01/LuyenDe-TN2027-De01.tex [...]
Mã thoát 0 nếu không có LỖI (cảnh báo không tính).
"""
import csv
import os
import re
import sys

GOC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(GOC, 'tools', 'danh_gia'))
from chung import doc_de  # noqa: E402

_cache = {}


def lay_cau(id_):
    ma = id_.split('-')[0]
    if ma not in _cache:
        _cache[ma] = {q['id']: q for q in doc_de(ma)['cau']}
    return _cache[ma].get(id_)


def bo_comment(s):
    """Bỏ phần comment % (không tính \\%)."""
    return '\n'.join(re.sub(r'(?<!\\)%.*', '', ln) for ln in s.split('\n'))


def doc_nhom(s, i):
    """s[i] == '{' -> trả (nội dung, chỉ số sau dấu } tương ứng)."""
    assert s[i] == '{'
    d = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            d += 1
        elif c == '}':
            d -= 1
            if d == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError('thiếu dấu }')


def cac_nhom(s, i, n):
    """Đọc n nhóm {..} liên tiếp từ vị trí i (bỏ khoảng trắng)."""
    out = []
    for _ in range(n):
        while i < len(s) and s[i] in ' \t\n':
            i += 1
        if i >= len(s) or s[i] != '{':
            break
        g, i = doc_nhom(s, i)
        out.append(g)
    return out, i


def lay_lenh(s, lenh):
    k = s.find(lenh)
    if k < 0:
        return None
    i = k + len(lenh)
    while i < len(s) and s[i] in ' \t\n':
        i += 1
    if i < len(s) and s[i] == '{':
        return doc_nhom(s, i)[0]
    return None


def kiem(fn):
    loi, cb = [], []
    raw = open(fn, encoding='utf-8').read()
    ten = os.path.basename(fn)[:-4]
    so = re.search(r'De(\d\d)$', ten)
    so = so.group(1) if so else None

    for k, ln in enumerate(raw.split('\n'), 1):
        if re.match(r'\s*%@', ln):
            loi.append('dòng %d: còn ghi chú soạn %%@: %s' % (k, ln.strip()[:90]))
    s = bo_comment(raw)
    for pat, ten_loi in [(r'\[\[HINH', 'còn chỗ đặt hình [[HINH'), (r'\\includegraphics', '\\includegraphics'),
                         (r'\\immini', '\\immini'), (r'tkz-euclide|\\tkzDefPoint|\\tkzDrawPoint', 'tkz-euclide'),
                         (r'\$\$', '$$'), (r'\\heva\b', '\\heva'), (r'\\hoac\b', '\\hoac'),
                         (r'\\begin\{cases\}', 'cases'), (r'\\emptyset', '\\emptyset (dùng \\varnothing)'),
                         (r'\\vec\{', '\\vec (dùng \\overrightarrow)'),
                         (r'Chọn\s+(đáp án|phương án)?\s*\(?[ABCD]\b', 'gõ tay "Chọn A/B/C/D" trong lời giải')]:
        for m in re.finditer(pat, s):
            line = s[:m.start()].count('\n') + 1
            loi.append('dòng %d: %s' % (line, ten_loi))

    # công tắc tách câu (preamble-eduzy-v2) phải bật khi dùng \NeedspaceCau[..] / \NeedspaceBang
    if ('\\NeedspaceBang' in s or '\\NeedspaceCau[' in s) and not ('\\def\\TachCauDS{1}' in s and '\\def\\TachCauLG{1}' in s):
        cb.append('dùng \\NeedspaceCau / \\NeedspaceBang nhưng chưa bật \\def\\TachCauDS{1}, \\def\\TachCauLG{1} trước \\input{preamble-eduzy-v2}')

    # phần
    for k in (1, 2, 3):
        if '\\Opensolutionfile{ans}[ans/%s-%d]' % (ten, k) not in s:
            loi.append('thiếu \\Opensolutionfile{ans}[ans/%s-%d]' % (ten, k))
    phan = re.split(r'\\subsection\*', s)[1:]
    if len(phan) != 3:
        loi.append('số phần = %d (cần 3)' % len(phan))

    rows = []
    if so:
        rows = [r for r in csv.DictReader(open(os.path.join(GOC, 'kho', 'phan-bo.csv'), encoding='utf-8'))
                if r['de'] == so]
    can = {p: [r['id'] for r in sorted((r for r in rows if r['phan'] == p), key=lambda r: int(r['thu_tu']))]
           for p in ('I', 'II', 'III')}

    blocks = list(re.finditer(r'^[ \t]*\\begin\{ex\}(.*?)\\end\{ex\}', raw, re.S | re.M))
    # gán khối vào phần theo vị trí \subsection*
    vt_phan = [m.start() for m in re.finditer(r'^[ \t]*\\subsection\*', raw, re.M)]
    theo_phan = {'I': [], 'II': [], 'III': []}
    for b in blocks:
        idx = sum(1 for v in vt_phan if v < b.start())
        if 1 <= idx <= 3:
            theo_phan[('I', 'II', 'III')[idx - 1]].append(b)
    for p, n in (('I', 12), ('II', 4), ('III', 6)):
        if len(theo_phan[p]) != n:
            loi.append('Phần %s có %d câu (cần %d)' % (p, len(theo_phan[p]), n))

    for p in ('I', 'II', 'III'):
        for k, b in enumerate(theo_phan[p], 1):
            body = b.group(1)
            line = raw[:b.start()].count('\n') + 1
            nhan = 'Phần %s câu %d (dòng %d)' % (p, k, line)
            m = re.match(r'\s*%\s*(\S+)', body)
            cid = m.group(1) if m else None
            if not cid or not re.match(r'^(TT|NC|TS)\d', cid or ''):
                loi.append('%s: dòng đầu không phải "%% <mã câu>"' % nhan)
                continue
            nhan += ' [%s]' % cid
            if can.get(p) and (k > len(can[p]) or can[p][k - 1] != cid):
                loi.append('%s: mã câu không khớp phan-bo.csv (cần %s)' % (
                    nhan, can[p][k - 1] if k <= len(can[p]) else '?'))
            q = lay_cau(cid)
            co_kt = 'KIỂM TRA' in body
            nd = bo_comment(body)
            lg = lay_lenh(nd, '\\loigiai')
            if lg is None:
                loi.append('%s: thiếu \\loigiai' % nhan)
            elif 'Vậy' not in lg:
                cb.append('%s: lời giải không có câu "Vậy ..."' % nhan)
            de_bai = nd.split('\\loigiai')[0]
            # \Needspace vừa đúng khối câu (tools/dan_trang): ngay trên \begin{ex}, riêng câu đầu phần đặt trên tiêu đề phần
            truoc = raw[max(0, b.start() - 60):b.start()]
            if k == 1:
                vp = vt_phan[('I', 'II', 'III').index(p)]
                truoc = raw[max(0, vp - 80):vp] + truoc
            if '\\Needspace' not in truoc:
                cb.append('%s: thiếu \\Needspace (chạy tools/dan_trang/dan_trang.py needspace)' % nhan)
            if p == 'II' and '\\choiceTFt' in de_bai and not re.search(r'\\NeedspaceBang\{[^}]*\}%?\s*\n\s*\\choiceTFt', body):
                cb.append('%s: thiếu \\NeedspaceBang ngay trước \\choiceTFt (chạy tools/dan_trang/dan_trang.py needspace)' % nhan)
            if q is None:
                loi.append('%s: không thấy câu trong ngân hàng' % nhan)
                continue
            da = q['dap_an']
            if p == 'I':
                k2 = nd.find('\\choice')
                if k2 < 0 or nd[k2:k2 + 10] == '\\choiceTF':
                    loi.append('%s: thiếu \\choice' % nhan)
                    continue
                opts, _ = cac_nhom(nd, k2 + len('\\choice'), 5)
                if len(opts) < 4:
                    loi.append('%s: \\choice có %d phương án' % (nhan, len(opts)))
                    continue
                opts = opts[:4]
                tr = [i for i, o in enumerate(opts) if o.lstrip().startswith('\\True')]
                if len(tr) != 1:
                    loi.append('%s: số \\True = %d' % (nhan, len(tr)))
                elif 'ABCD'[tr[0]] != da:
                    (cb if co_kt else loi).append('%s: \\True ở %s, ngân hàng %s' % (nhan, 'ABCD'[tr[0]], da))
                for o in opts:
                    oo = o.rstrip()
                    if oo.endswith(('.', ';', ',')):
                        cb.append('%s: phương án có dấu câu cuối: %s' % (nhan, o.strip()[-30:]))
            elif p == 'II':
                k2 = nd.find('\\choiceTFt')
                if k2 < 0:
                    loi.append('%s: thiếu \\choiceTFt' % nhan)
                    continue
                md, _ = cac_nhom(nd, k2 + len('\\choiceTFt'), 4)
                if len(md) != 4:
                    loi.append('%s: \\choiceTFt có %d mệnh đề' % (nhan, len(md)))
                    continue
                v = ['Đ' if o.lstrip().startswith('\\True') else 'S' for o in md]
                if v != list(da):
                    (cb if co_kt else loi).append('%s: \\True %s, ngân hàng %s' % (nhan, ''.join(v), ''.join(da)))
                for o in md:
                    oo = o.rstrip()
                    if oo.endswith(('.', ';', ',')):
                        cb.append('%s: mệnh đề có dấu câu cuối' % nhan)
                if lg is not None:
                    if '\\begin{itemchoice}' not in lg:
                        loi.append('%s: lời giải Đúng/Sai thiếu itemchoice' % nhan)
                    heads = re.findall(r'\\itemch\s*\{\\bf\s*(Đúng|Sai)\.\}', lg)
                    if len(heads) != 4:
                        loi.append('%s: lời giải có %d \\itemch {\\bf Đúng./Sai.}' % (nhan, len(heads)))
                    elif ['Đ' if h == 'Đúng' else 'S' for h in heads] != v:
                        loi.append('%s: nhãn lời giải %s không khớp \\True %s' % (
                            nhan, ''.join('Đ' if h == 'Đúng' else 'S' for h in heads), ''.join(v)))
            else:
                m2 = re.search(r'\\shortans\[oly\]\{((?:[^{}]|\{,\})*)\}', nd)
                if not m2:
                    loi.append('%s: thiếu \\shortans[oly]{...}' % nhan)
                    continue
                if not re.search(r'\\par\s*\n\s*\\shortans', nd):
                    cb.append('%s: \\par không đứng riêng dòng ngay trước \\shortans' % nhan)
                val = m2.group(1)
                hien = val.replace('{,}', ',')
                if not re.match(r'^-?\d+(,\d+)?$', hien):
                    loi.append('%s: giá trị \\shortans không hợp lệ: %s' % (nhan, val))
                if len(hien) > 4:
                    loi.append('%s: đáp số quá 4 ký tự: %s' % (nhan, hien))
                if hien != (da or ''):
                    (cb if co_kt else loi).append('%s: \\shortans %s, ngân hàng %s' % (nhan, hien, da))
                if ',' in hien and not re.search(r'làm tròn|chính xác đến|hàng phần', de_bai):
                    cb.append('%s: đáp số thập phân nhưng đề không thấy yêu cầu làm tròn' % nhan)
            # cảnh báo ký hiệu
            for m3 in re.finditer(r'(?<!displaystyle)\\int(?!er)', nd):
                trc = nd[max(0, m3.start() - 14):m3.start()]
                if 'displaystyle' not in trc:
                    cb.append('%s: \\int không có \\displaystyle' % nhan)
                    break
            nd_chu = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', '', nd, flags=re.S)
            for m3 in re.finditer(r'\$[^$]*\$', nd_chu):
                if re.search(r'(?<![A-Za-z.])\d+\.\d+(?![A-Za-z])', m3.group(0)):
                    cb.append('%s: số thập phân dấu chấm? %s' % (nhan, m3.group(0)[:40]))
                    break
    return loi, cb


def main(argv):
    tong = 0
    for fn in argv:
        loi, cb = kiem(fn)
        print('=====', fn)
        for x in loi:
            print('  LỖI     ', x)
        for x in cb:
            print('  cảnh báo', x)
        if not loi and not cb:
            print('  sạch')
        tong += len(loi)
    sys.exit(1 if tong else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
