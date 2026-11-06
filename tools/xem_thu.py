# -*- coding: utf-8 -*-
"""
Xuất file .tex XEM THỬ kết quả trích xuất (giai đoạn 1) từ kho/ngan-hang/*.json.

Dùng (chạy từ gốc repo):
    python3 tools/xem_thu.py TT01 NC05 TS039 ... [--ten XemThu-TrichXuat]
Kết quả: de/<tên>/<tên>.tex và de/<tên>/hinh/ (ảnh gốc tách từ file Word, đổi WMF/EMF sang PNG).
Biên dịch: bash bien-dich.sh de/<tên>/<tên>.tex

Đây là bản để SOÁT TRÍCH XUẤT, không phải đề: ảnh gốc được chèn bằng \\includegraphics để đối chiếu;
ở đề thật mọi hình sẽ vẽ lại bằng TikZ. Mỗi câu có dòng thông tin (mã câu, nguồn đáp án, mô tả hình)
và dòng cảnh báo màu đỏ nếu script phát hiện vấn đề.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KHO = os.path.join(GOC, 'kho', 'ngan-hang')


def find_json(ma):
    for sub in ('tu-soan', 'truong-so'):
        p = os.path.join(KHO, sub, ma + '.json')
        if os.path.exists(p):
            return p
    return None


def tex_esc(s):
    return (s or '').replace('\\', r'\textbackslash{}').replace('%', r'\%').replace('&', r'\&') \
        .replace('#', r'\#').replace('_', r'\_').replace('{', r'\{').replace('}', r'\}').replace('$', r'\$')


class Images:
    def __init__(self, outdir):
        self.outdir = outdir
        os.makedirs(outdir, exist_ok=True)
        self.todo = []  # (zip, name, dest)

    def get(self, docx, ma, name):
        if not name:
            return None
        base, ext = os.path.splitext(name)
        ext = ext.lower()
        z = zipfile.ZipFile(docx)
        try:
            data = z.read('word/media/' + name)
        except KeyError:
            return None
        if ext not in ('.png', '.jpg', '.jpeg', '.wmf', '.emf', '.pdf'):
            ext = sniff(data)  # vd ảnh lưu đuôi .tmp, .gif, .bmp, .tif
        if ext in ('.gif', '.bmp', '.tif', '.tiff', '.webp'):
            dest = '%s-%s.png' % (ma, base)
            full = os.path.join(self.outdir, dest)
            if not os.path.exists(full):
                try:
                    import io
                    from PIL import Image
                    Image.open(io.BytesIO(data)).convert('RGB').save(full)
                except Exception:  # noqa
                    return None
            return 'hinh/' + dest
        if ext is None:
            return None
        dest = '%s-%s.png' % (ma, base) if ext in ('.wmf', '.emf') else '%s-%s%s' % (ma, base, ext)
        full = os.path.join(self.outdir, dest)
        if not os.path.exists(full):
            if ext in ('.wmf', '.emf'):
                name = base + ext
                tmp = tempfile.mkdtemp()
                src = os.path.join(tmp, name)
                open(src, 'wb').write(data)
                subprocess.run(['soffice', '--headless', '--convert-to', 'png', '--outdir', tmp, src],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
                png = os.path.join(tmp, base + '.png')
                if os.path.exists(png):
                    shutil.move(png, full)
                shutil.rmtree(tmp, ignore_errors=True)
                if not os.path.exists(full):
                    return None
            else:
                open(full, 'wb').write(data)
        return 'hinh/' + dest


def sniff(data):
    """đoán định dạng ảnh theo byte đầu"""
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return '.png'
    if data[:2] == b'\xff\xd8':
        return '.jpg'
    if data[:4] in (b'GIF8',):
        return '.gif'
    if data[:2] == b'BM':
        return '.bmp'
    if data[:4] in (b'II*\x00', b'MM\x00*'):
        return '.tif'
    if data[:4] == b'\xd7\xcd\xc6\x9a' or data[:2] in (b'\x01\x00', b'\x02\x00'):
        return '.wmf'
    if data[40:44] == b' EMF':
        return '.emf'
    if data[:4] == b'RIFF':
        return '.webp'
    return None


def fig_block(h, imgs, q):
    desc = tex_esc(h.get('mo_ta', ''))
    if h['loai'] == 'anh':
        path = imgs.get(os.path.join(GOC, q['file_goc']), q['de_goc'], h.get('file'))
        if path:
            w = 7.0
            if h.get('kich_thuoc_cm'):
                try:
                    w = min(float(h['kich_thuoc_cm'].split('x')[0]), 12.0)
                except ValueError:
                    pass
            return ('\\begin{center}\n\\includegraphics[width=%.1fcm,height=7cm,keepaspectratio]{%s}\\\\\n'
                    '{\\scriptsize\\itshape\\color{gray}[Hình gốc %d: %s; %s]}\n\\end{center}') % (
                max(w, 1.5), path, h['so'], tex_esc(h.get('file')), desc)
        return '\\begin{center}\\fbox{\\scriptsize Hình gốc %d (%s): không tách được ảnh}\\end{center}' % (
            h['so'], tex_esc(h.get('file')))
    if h.get('anh_dung') and os.path.exists(os.path.join(GOC, h['anh_dung'])):
        dest = os.path.join(imgs.outdir, os.path.basename(h['anh_dung']))
        shutil.copy(os.path.join(GOC, h['anh_dung']), dest)
        return ('\\begin{center}\n\\includegraphics[width=%.1fcm,height=7cm,keepaspectratio]{hinh/%s}\\\\\n'
                '{\\scriptsize\\itshape\\color{gray}[Hình gốc %d: vẽ bằng shape Word, ảnh dựng từ trang %s '
                'bản LibreOffice; %s]}\n\\end{center}') % (
            min(max(h.get('kich_thuoc_cm') and float(h['kich_thuoc_cm'].split('x')[0]) or 7.0, 2.0), 12.0),
            os.path.basename(h['anh_dung']), h['so'], h.get('trang_goc'), desc)
    label = tex_esc(h.get('chu_trong_hinh', ''))[:150]
    return ('\\begin{center}\\fbox{\\parbox{9cm}{\\centering\\scriptsize Hình gốc %d vẽ bằng shape Word '
            '(xem file gốc)%s\\\\ \\itshape %s}}\\end{center}') % (
        h['so'], ('; chữ trong hình: ' + label) if label else '', desc)


def put_figs(s, q, imgs):
    def rep(m):
        k = int(m.group(1))
        h = q['hinh'][k - 1] if 0 < k <= len(q['hinh']) else None
        return fig_block(h, imgs, q) if h else ''
    return re.sub(r'\[\[HINH (\d+)\]\]', rep, s)


def indent(s, n):
    pre = '\t' * n
    return '\n'.join(pre + ln if ln.strip() else ln for ln in s.split('\n'))


def info_line(q):
    bits = ['%s (câu %d gốc)' % (q['id'], q['so_cau_goc'])]
    if q['loai'] == 'DS':
        bits.append('đáp án: %s' % ''.join(x or '?' for x in q['dap_an']))
    else:
        bits.append('đáp án: %s' % (q['dap_an'] or '?'))
    if q.get('nguon_dap_an'):
        bits.append('lấy từ %s' % q['nguon_dap_an'])
    if q['hinh']:
        bits.append('%d hình (đề: %d)' % (len(q['hinh']), sum(h['vi_tri'] != 'loi-giai' for h in q['hinh'])))
    if q.get('bang'):
        bits.append('%d bảng trong đề' % q['bang'])
    s = '{\\scriptsize\\color{gray}\\ttfamily[%s]}' % tex_esc(' · '.join(bits))
    if q['canh_bao']:
        s += '\\\\\n{\\scriptsize\\color{red}[Cảnh báo: %s]}' % tex_esc('; '.join(q['canh_bao']))
    return s + '\\\\'


def shortans_val(a):
    if not a:
        return ''
    return a.replace(',', '{,}')


def ex_block(q, imgs):
    L = []
    if q['hinh'] and any(h['vi_tri'] != 'loi-giai' for h in q['hinh']):
        L.append('\\Needspace{16\\baselineskip}')
    L.append('\\begin{ex}')
    L.append('\t%% %s' % q['id'])
    body = []
    body.append(info_line(q))
    body.append(put_figs(q['noi_dung'], q, imgs))
    if q['loai'] == 'TN':
        if len(q['phuong_an']) == 4:
            body.append('\\choice')
            for k, o in enumerate(q['phuong_an']):
                o = put_figs(o, q, imgs).replace('\n', ' ')
                tr = '\\True ' if q['dap_an'] == 'ABCD'[k] else ''
                body.append('{%s%s}' % (tr, o))
        lg = put_figs(q['loi_giai'], q, imgs)
        body.append('\\loigiai{\n%s\n}' % indent(lg or '(Bản gốc không có lời giải.)', 1))
    elif q['loai'] == 'DS':
        if len(q['menh_de']) == 4:
            body.append('\\choiceTFt')
            for k, o in enumerate(q['menh_de']):
                o = put_figs(o, q, imgs).replace('\n', ' ')
                tr = '\\True ' if q['dap_an'][k] == 'Đ' else ''
                body.append('{%s%s}' % (tr, o))
        lg = q['loi_giai']
        parts = []
        if lg.get('chung'):
            parts.append(put_figs(lg['chung'], q, imgs))
        if lg.get('y'):
            items = ['\\begin{itemchoice}']
            for k, y in enumerate(lg['y']):
                v = q['dap_an'][k]
                head = '{\\bf Đúng.}' if v == 'Đ' else ('{\\bf Sai.}' if v == 'S' else '{\\bf ???}')
                items.append('\t\\itemch %s\\\\\n%s' % (head, indent(put_figs(y, q, imgs) or '(trống)', 1)))
            items.append('\\end{itemchoice}')
            parts.append('\n'.join(items))
        body.append('\\loigiai{\n%s\n}' % indent('\n'.join(parts) or '(Bản gốc không có lời giải.)', 1))
    else:
        body.append('\\par\\shortans[oly]{%s}' % shortans_val(q['dap_an']))
        lg = put_figs(q['loi_giai'], q, imgs)
        body.append('\\loigiai{\n%s\n}' % indent(lg or '(Bản gốc không có lời giải.)', 1))
    txt = re.sub(r'(\\\\\s*)\[', r'\1{}[', '\n'.join(body))  # "\\" + "[" -> không hiểu nhầm tham số
    L.append(indent(txt, 1))
    L.append('\\end{ex}')
    return '\n'.join(L)


PART_TITLE = {1: 'PHẦN I. Trắc nghiệm nhiều phương án lựa chọn', 2: 'PHẦN II. Trắc nghiệm đúng sai',
              3: 'PHẦN III. Trắc nghiệm trả lời ngắn'}


def main(argv):
    ten = 'XemThu-TrichXuat'
    if '--ten' in argv:
        i = argv.index('--ten')
        ten = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    od = os.path.join(GOC, 'de', ten)
    if '--thu-muc' in argv:
        i = argv.index('--thu-muc')
        od = os.path.abspath(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    mas = [a for a in argv if not a.startswith('-')]
    shutil.rmtree(os.path.join(od, 'hinh'), ignore_errors=True)
    imgs = Images(os.path.join(od, 'hinh'))
    out = []
    out.append('%' + '=' * 69)
    out.append('% BẢN XEM THỬ TRÍCH XUẤT -- GIAI ĐOẠN 1 (dự án 40 đề, xem du-an-40-de.md)')
    out.append('%% Sinh tự động bằng: python3 tools/xem_thu.py %s' % ' '.join(mas))
    out.append('% Không phải đề thi: ảnh gốc chèn bằng \\includegraphics chỉ để đối chiếu.')
    out.append('%' + '=' * 69)
    out.append('\\def\\CheDo{solcolor}')
    out.append('\\def\\tenchuong{Bản xem thử trích xuất -- Giai đoạn 1}')
    out.append('\\input{preamble-eduzy-v2}')
    out.append('\\begin{document}')
    tong = {'TN': 0, 'DS': 0, 'TLN': 0, 'cb': 0, 'hinh': 0}
    rows = []
    for ma in mas:
        p = find_json(ma)
        if not p:
            print('Không thấy JSON của', ma, '(chạy tools/tach_cau.py trước)')
            continue
        d = json.load(open(p, encoding='utf8'))
        t = d['thong_tin']
        for k in ('TN', 'DS', 'TLN'):
            tong[k] += t['so_cau'][k]
        tong['cb'] += t['cau_co_canh_bao']
        tong['hinh'] += t['hinh']
        rows.append((ma, t))
    out.append('\t\\khungtieude{BẢN XEM THỬ TRÍCH XUẤT -- GIAI ĐOẠN 1}{Ngân hàng câu hỏi -- dự án 40 đề}'
               '{(%d đề nguồn: %d câu trắc nghiệm, %d câu đúng-sai, %d câu trả lời ngắn)}'
               '{Ảnh gốc chèn để đối chiếu; đề thật sẽ vẽ lại hình bằng TikZ.}' % (
                   len(rows), tong['TN'], tong['DS'], tong['TLN']))
    out.append('')
    out.append('\t\\muc{Tóm tắt}')
    out.append('\t\\begin{center}\\footnotesize')
    out.append('\t\\begin{tabular}{|c|l|c|c|c|c|c|c|}')
    out.append('\t\\hline')
    out.append('\t\\textbf{Mã} & \\textbf{Đề gốc} & \\textbf{TN} & \\textbf{ĐS} & \\textbf{TLN} & '
               '\\textbf{CT} & \\textbf{Hình} & \\textbf{C.báo}\\\\')
    out.append('\t\\hline')
    for ma, t in rows:
        ten_goc = t['ten_goc']
        if len(ten_goc) > 34:
            ten_goc = ten_goc[:32] + '...'
        out.append('\t%s & %s & %d & %d & %d & %d & %d & %d\\\\' % (
            ma, tex_esc(ten_goc), t['so_cau']['TN'], t['so_cau']['DS'], t['so_cau']['TLN'],
            t['cong_thuc'], t['hinh'], t['cau_co_canh_bao']))
        out.append('\t\\hline')
    out.append('\t\\end{tabular}')
    out.append('\t\\end{center}')
    out.append('\tDòng xám đầu mỗi câu: mã câu trong ngân hàng, đáp án và nơi lấy đáp án, số hình. '
               'Dòng đỏ: cảnh báo của script (cần soát). Hình trong khung chữ nhật là hình vẽ bằng shape '
               'của Word, script chưa tách ra ảnh được.')
    for ma, t in rows:
        d = json.load(open(find_json(ma), encoding='utf8'))
        out.append('')
        out.append('\t\\newpage')
        out.append('\t\\subsection*{\\indam{%s -- %s}}' % (ma, tex_esc(t['ten_goc'])))
        out.append('\t{\\footnotesize File gốc: \\texttt{%s}}' % tex_esc(t['file_goc']))
        for part in (1, 2, 3):
            qs = [q for q in d['cau'] if q['phan'] == part]
            if not qs:
                continue
            out.append('')
            out.append('\t\\muc{%s (%d câu)}' % (PART_TITLE[part], len(qs)))
            out.append('\t\\setcounter{ex}{0}')
            out.append('\t\\Opensolutionfile{ans}[ans/%s-%s-%d]' % (ten, ma, part))
            for q in qs:
                out.append('')
                out.append(indent(ex_block(q, imgs), 1))
            out.append('\t\\Closesolutionfile{ans}')
    out.append('\\end{document}')
    os.makedirs(od, exist_ok=True)
    fn = os.path.join(od, ten + '.tex')
    with open(fn, 'w', encoding='utf8') as f:
        f.write('\n'.join(out) + '\n')
    print('Đã ghi', os.path.relpath(fn, GOC), '| ảnh:', len(os.listdir(imgs.outdir)))


if __name__ == '__main__':
    main(sys.argv[1:])
