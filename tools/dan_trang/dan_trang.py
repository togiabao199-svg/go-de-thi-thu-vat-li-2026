#!/usr/bin/env python3
"""
DÀN TRANG ĐỀ (bản đề ưu tiên, bản lời giải vẫn ổn). Chép từ dự án 40 đề Toán; dự án Vật lí luôn gọi bằng đường dẫn file .tex.

Các bước (chạy từ gốc repo, XX = số đề 01..40 hoặc đường dẫn file .tex bất kỳ — ví dụ file mã đề sau khi trộn;
nhiều đề cách nhau dấu cách):

  python3 tools/dan_trang/dan_trang.py do-hinh XX     đo kích thước mọi hình (bản lời giải), xuất ảnh soát hình
  python3 tools/dan_trang/dan_trang.py thu-hinh XX    thu nhỏ hình theo quy tắc (sửa file .tex), đo lại tối đa 3 lần
  python3 tools/dan_trang/dan_trang.py needspace XX   đo độ cao khối câu ở bản đề, ghi \\Needspace vừa đúng (sửa file .tex)
  python3 tools/dan_trang/dan_trang.py kiem XX        biên dịch bản đề + bản lời giải, soát ngắt câu, khoảng trống, xuất ảnh trang
  python3 tools/dan_trang/dan_trang.py xuat XX        như kiem, rồi chép PDF vào thanh-pham/ (<tên>.pdf, <tên>-DE.pdf) và đóng gói zip
  python3 tools/dan_trang/dan_trang.py tat-ca XX      thu-hinh → needspace → kiem (không xuất)

Quy tắc hình (CLAUDE.md, mục HÌNH VẼ):
  - đồ thị (pgfplots) và hình phẳng, sơ đồ: cao 3,5–4,5 cm → hình cao hơn 4,5 cm thu về khoảng 4,2 cm;
  - hình không gian (mã dạng 1H*, 2H* hoặc hình có trục z): cao 3,5–4 cm → hình cao hơn 4 cm thu về khoảng 3,8 cm;
  - bảng tkz-tab: hàng thường 0,6 cm (0,9 cm nếu có phân số), hàng biến thiên 1,5 cm (2 cm nếu có phân số, căn);
  - hình nhỏ hơn ngưỡng giữ nguyên; tikz thu bằng scale=..., pgfplots thu bằng x=..., y=... của axis
    (chữ trong hình giữ cỡ \\footnotesize nên phải soát lại nhãn đè nét bằng ảnh soat-hinh-*.png).

Quy tắc \\Needspace (CLAUDE.md, mục HÌNH VẼ; cập nhật 05/11/2026):
  - mỗi câu có \\NeedspaceCau{n\\baselineskip} ngay trên \\begin{ex}, n = độ cao khối câu ở bản đề (câu dẫn + hình +
    phương án / bảng Đúng/Sai / ô KQ, đo bằng zref-savepos) cộng 0,2 dòng, làm tròn lên 0,1 dòng; câu đầu mỗi PHẦN:
    đặt trên tiêu đề phần (tiêu đề + câu đầu);
  - câu Đúng/Sai: thêm \\NeedspaceBang{<cao bảng>}% ngay trước \\choiceTFt (bảng không tách giữa hai trang); câu nào
    để nguyên khối làm trang trước trống quá 1/4 thì được chọn tách: \\NeedspaceCau[<cao câu dẫn + hình>]{<cả khối>}
    (câu dẫn + hình cuối trang, bảng sang trang sau); câu đầu Phần II không tách;
  - tự bật công tắc \\def\\TachCauDS{1}, \\def\\TachCauLG{1} (preamble-eduzy-v2) trước \\input; bản lời giải
    (\\TachCauLG) chỉ đòi tối đa 1/3 trang nên phần đề câu cao hơn 1/3 trang được tách.

Comment trong câu (giữa \\begin{ex} và \\end{ex}; thêm 05/11/2026, kho/sua-hinh.md):
  - % giuhinh : hình của câu giữ cỡ đã đặt tay (được lớn hơn quy định) — thu-hinh không thu, do-hinh và kiem không báo
    lệch cỡ;
  - % tachDS  : câu Đúng/Sai luôn được tách câu dẫn / bảng khi không vừa trang, kể cả câu đầu Phần II (tiêu đề phần +
    câu dẫn + hình ở cuối trang trước, bảng Phát biểu sang trang sau).

Soát (kiem): bản đề — câu Phần I, III không bị ngắt; câu Đúng/Sai chỉ được ngắt giữa câu dẫn và bảng; không trang
nào trống quá 1/4 chiều cao vùng chữ (6,6 cm), trừ trang cuối và trang ngay trước tiêu đề phần (ghi LƯU Ý);
bản lời giải — trang trống quá 1/3 là LỖI, từ 1/4 đến 1/3 là LƯU Ý; hình cao hơn trần quy định (trừ câu % giuhinh)
ghi LƯU Ý lệch cỡ. Ảnh: de/<tên>/bien-dich/dan-trang/{de,loigiai}/trang-*.png và soat-de-*.png (ghép 3×2).
"""
import csv
import json
import math
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
PT_PER_CM = 72.27 / 2.54
SP = 65536.0
BS_PT = 14.5 * 1.1          # \baselineskip của nội dung (12pt, \baselinestretch 1.1)
LE_DONG = 0.2               # phần dư (dòng) cộng vào độ cao khối câu (phòng chênh font), làm tròn lên 0,1 dòng
G_DAU_TRANG = 6.0           # bù khoảng cách bị bỏ khi câu đứng đầu trang (pt; đo thực tế 0–4,4 pt)
G_DAU_PHAN = 20.0           # như trên cho khối tiêu đề phần + câu đầu (khoảng trước tiêu đề bị bỏ, đo 15–20 pt)
HE_SO_SAN = 0.6             # thu-hinh không tự thu hình dưới 0,6 lần cỡ gốc (sơ đồ nhiều chữ dễ chồng nhãn)
TRAN_TREN = {'phang': 4.5, 'do-thi': 4.5, 'khong-gian': 4.0}
DICH = {'phang': 4.2, 'do-thi': 4.2, 'khong-gian': 3.8}


def ten_de(xx):
    if str(xx).endswith('.tex'):
        return os.path.basename(xx)[:-4]
    return 'LuyenDe-TN2027-De%02d' % int(xx)


def duong_dan(xx):
    if str(xx).endswith('.tex'):
        return os.path.abspath(xx)
    t = ten_de(xx)
    return os.path.join(ROOT, 'de', t, t + '.tex')


# ---------------------------------------------------------------- biên dịch
def chuan_bi(thu_muc):
    os.makedirs(os.path.join(thu_muc, 'ans'), exist_ok=True)
    for f in os.listdir(ROOT):
        if f.startswith('preamble') and f.endswith('.tex'):   # preamble-eduzy-v2, preamble-vatli-hinh...
            shutil.copy(os.path.join(ROOT, f), thu_muc)
    shutil.copy(os.path.join(ROOT, 'ex_test.sty'), thu_muc)
    shutil.copy(os.path.join(HERE, 'do_khoi.tex'), thu_muc)
    if subprocess.run(['kpsewhich', 'uesvect.fd'], capture_output=True).returncode == 0:
        shutil.copy(os.path.join(ROOT, 'esvect.sty'), thu_muc)
    else:
        with open(os.path.join(thu_muc, 'esvect.sty'), 'w') as g:
            g.write('\\ProvidesPackage{esvect}[sandbox]\n\\let\\EZarrow\\overrightarrow\n'
                    '\\newcommand{\\vv}[1]{\\EZarrow{#1}}\n')
    if (subprocess.run(['kpsewhich', 'fontawesome.sty'], capture_output=True).returncode != 0 and
            subprocess.run(['kpsewhich', 'fontawesome5.sty'], capture_output=True).returncode != 0):
        with open(os.path.join(thu_muc, 'fontawesome.sty'), 'w') as g:
            g.write('\\ProvidesPackage{fontawesome}[sandbox]\n')
    src_dir = os.path.dirname
    return thu_muc


def ban_do(noi_dung, che_do, do=True, hinh=True):
    """Bản để biên dịch: đổi \\CheDo, chèn bộ đo (do_khoi.tex) và mốc trước mỗi hình, mỗi tiêu đề phần."""
    s = re.sub(r'\\def\\CheDo\{[^}]*\}', r'\\def\\CheDo{%s}' % che_do, noi_dung, count=1)
    if not do:
        return s
    s = s.replace('\\input{preamble-eduzy-v2}', '\\input{preamble-eduzy-v2}\\input{do_khoi}', 1)
    dong = s.split('\n')
    trong_than = False
    for i, d in enumerate(dong):
        if '\\begin{document}' in d:
            trong_than = True
            continue
        if not trong_than or d.lstrip().startswith('%'):
            continue
        if hinh and '\\begin{tikzpicture}' in d:
            dong[i] = d.replace('\\begin{tikzpicture}', '\\EZhinh{%d}\\begin{tikzpicture}' % (i + 1))
        if '\\subsection*' in d:
            j = i - 1 if i > 0 and dong[i - 1].strip() == '\\noindent' else i
            dong[j] = '\\EZphan{%d}' % (i + 1) + dong[j]
        if re.match(r'^\s*\\NeedspaceBang\{', d):
            dong[i] = re.sub(r'^(\s*)', r'\1\\EZbangcuoi', d, count=1)
        if re.match(r'^\s*\\choiceTFt', d):
            truoc = dong[i - 1] if i > 0 else ''
            moc = '\\EZbangdau' if 'NeedspaceBang' in truoc else '\\EZbangcuoi\\EZbangdau'
            dong[i] = re.sub(r'^(\s*)', lambda m: m.group(1) + moc, d, count=1)
    return '\n'.join(dong)


def bien_dich(noi_dung, thu_muc, ten, lan=2):
    chuan_bi(thu_muc)
    with open(os.path.join(thu_muc, ten + '.tex'), 'w') as g:
        g.write(noi_dung)
    src_hinh = None
    env = dict(os.environ)
    env['TEXINPUTS'] = thu_muc + '//:' + ROOT + '//:' + env.get('TEXINPUTS', '')
    for _ in range(lan):
        r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', ten + '.tex'],
                           cwd=thu_muc, capture_output=True, env=env)
        if r.returncode != 0:
            break
    log = open(os.path.join(thu_muc, ten + '.log'), encoding='utf-8', errors='replace').read()
    loi = re.findall(r'^!.*(?:\n.*){0,3}', log, re.M)
    pdf = os.path.join(thu_muc, ten + '.pdf')
    return log, (pdf if os.path.exists(pdf) and not loi else None), loi


def doc_aux(thu_muc, ten):
    vt = {}
    p = os.path.join(thu_muc, ten + '.aux')
    if not os.path.exists(p):
        return vt
    for m in re.finditer(r'\\zref@newlabel\{(EZ[a-z]+\d+)\}\{\\posx\{(-?\d+)\}\\posy\{(-?\d+)\}\\abspage\{(\d+)\}\}',
                         open(p, encoding='utf-8', errors='replace').read()):
        vt[m.group(1)] = (int(m.group(2)) / SP, int(m.group(3)) / SP, int(m.group(4)))
    return vt


def hinh_hoc_trang(log):
    m = re.search(r'EZTRANG:([\d.]+)pt:([\d.]+)pt:([\d.]+)pt', log)
    cao, tren, chu = (float(x) for x in m.groups())
    return {'cao': cao, 'ytop': cao - tren, 'ybot': cao - tren - chu, 'chu': chu}


# ---------------------------------------------------------------- phân tích nguồn
def cau_trong_nguon(dong):
    """Danh sách câu: dòng \\begin{ex}, dòng \\end{ex}, mã câu, phần (1..3), có phải câu đầu phần."""
    cau = []
    phan = 0
    dau_phan = False
    mo = None
    for i, d in enumerate(dong):
        s = d.strip()
        if s.startswith('%'):
            continue
        if '\\subsection*' in s:
            phan += 1
            dau_phan = True
        if s.startswith('\\begin{ex}'):
            mo = {'bd': i, 'phan': phan, 'dau_phan': dau_phan, 'ma': ''}
            dau_phan = False
            for k in range(i + 1, min(i + 4, len(dong))):
                m = re.match(r'\s*%\s*([A-Z]{2}\d+[A-Za-z]*-[IV]+-\d+)', dong[k])
                if m:
                    mo['ma'] = m.group(1)
                    break
        elif s.startswith('\\end{ex}') and mo is not None:
            mo['kt'] = i
            cau.append(mo)
            mo = None
    for k, c in enumerate(cau):
        c['so'] = sum(1 for x in cau[:k + 1] if x['phan'] == c['phan'])
        than = dong[c['bd']:c['kt'] + 1]
        c['giuhinh'] = any(RE_GIUHINH.search(d) for d in than)
        c['tachDS'] = any(RE_TACHDS.search(d) for d in than)
    return cau


RE_GIUHINH = re.compile(r'%.*\bgiuhinh\b')   # comment % giuhinh trong câu: giữ cỡ hình đặt tay
RE_TACHDS = re.compile(r'%.*\btachDS\b')     # comment % tachDS trong câu Đúng/Sai: cho tách kể cả câu đầu Phần II


def lech_co(hinh):
    """Hình cao hơn trần quy định (bỏ bảng tkz-tab và hình của câu % giuhinh)."""
    return ['%s%s %s %.2f cm (> %.1f)' % (h['cau'], ' LG' if h['loigiai'] else '', h['loai'], h['cao_cm'],
                                          TRAN_TREN[h['loai']])
            for h in hinh if h['loai'] != 'bang' and not h.get('giuhinh')
            and h['cao_cm'] > TRAN_TREN[h['loai']] + 0.05]


def ma_dang():
    md = {}
    for f in ('kho/phan-bo.csv', 'kho/du-phong.csv'):
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding='utf-8')):
                md[r['id']] = r.get('ma_dang', '')
    return md


def khoi_hinh(dong, i):
    """Từ dòng i (có \\begin{tikzpicture}) tìm dòng \\end{tikzpicture} tương ứng; trả (i, j, văn bản)."""
    sau = 0
    for j in range(i, len(dong)):
        sau += dong[j].count('\\begin{tikzpicture}') - dong[j].count('\\end{tikzpicture}')
        if sau <= 0:
            return i, j, '\n'.join(dong[i:j + 1])
    return i, len(dong) - 1, '\n'.join(dong[i:])


def trong_loigiai(dong, cau, i):
    """Dòng i nằm trong \\loigiai của câu?"""
    for c in cau:
        if c['bd'] <= i <= c['kt']:
            for k in range(c['bd'], i + 1):
                if '\\loigiai' in dong[k]:
                    return c, True
            return c, False
    return None, False


def loai_hinh(van_ban, ma):
    if '\\tkzTab' in van_ban:
        return 'bang'
    if '\\begin{axis}' in van_ban:
        return 'do-thi'
    tuy_chon = van_ban.split('\n')[0]
    if ma[:2] == '1H' or re.search(r'\bz\s*=', tuy_chon):
        return 'khong-gian'
    if ma[:2] != '2H' and 'dashed' in van_ban and re.search(r"[A-Z]'", van_ban):
        return 'khong-gian'   # hình khối (lăng trụ, hộp...) trong câu thực tiễn không mang mã 1H/2H
    # 2H (vectơ, tọa độ trong không gian): mặc định hình không gian; riêng hình nhìn từ trên mặt phẳng Oxy
    # (có trục $x$, $y$, không có trục $z$) tính là hình phẳng
    if ma[:2] == '2H':
        if '$x$' in van_ban and '$y$' in van_ban and '$z$' not in van_ban:
            return 'phang'
        return 'khong-gian'
    return 'phang'


# ---------------------------------------------------------------- đo hình
def do_hinh(xx, in_ra=True):
    src = duong_dan(xx)
    t = ten_de(xx)
    nd = open(src, encoding='utf-8').read()
    dong = nd.split('\n')
    tm = os.path.join(os.path.dirname(src), 'bien-dich', 'dan-trang', 'do-hinh')
    if os.path.isdir(tm):
        shutil.rmtree(tm)
    log, pdf, loi = bien_dich(ban_do(nd, 'solcolor'), tm, t)
    if loi:
        print('LỖI biên dịch %s:\n%s' % (t, '\n'.join(loi[:3])))
        return None
    vt = doc_aux(tm, t)
    cau = cau_trong_nguon(dong)
    md = ma_dang()
    hinh = []
    for m in re.finditer(r'EZHINH:(\d+):([\d.]+)pt:([\d.]+)pt', log):
        ln, w, h = int(m.group(1)), float(m.group(2)), float(m.group(3))
        i, j, vb = khoi_hinh(dong, ln - 1)
        c, lg = trong_loigiai(dong, cau, ln - 1)
        ma = md.get(c['ma'], '') if c else ''
        p = vt.get('EZh%d' % ln)
        hinh.append({'dong': ln, 'dong_cuoi': j + 1, 'rong_cm': round(w / PT_PER_CM, 2), 'cao_cm': round(h / PT_PER_CM, 2),
                     'loai': loai_hinh(vb, ma), 'cau': ('%s.%d' % ('I' * c['phan'], c['so'])) if c else '?',
                     'ma': c['ma'] if c else '', 'ma_dang': ma, 'loigiai': lg,
                     'trang': p[2] if p else None, 'x': p[0] if p else None, 'y': p[1] if p else None,
                     'w': w, 'h': h, 'baseline': 'baseline' in vb.split('\n')[0],
                     'giuhinh': bool(c and c['giuhinh'])})
    json.dump(hinh, open(os.path.join(tm, 'hinh.json'), 'w'), ensure_ascii=False, indent=1)
    if in_ra:
        for hh in hinh:
            print('  %-6s d%-4d %-10s %5.2f x %4.2f cm %s%s' % (hh['cau'], hh['dong'], hh['loai'], hh['rong_cm'],
                                                              hh['cao_cm'], '(lời giải)' if hh['loigiai'] else '',
                                                              ' (giuhinh)' if hh['giuhinh'] else ''))
        for x in lech_co(hinh):
            print('  LỆCH CỠ: ' + x)
    return hinh, pdf, tm, log


def anh_soat_hinh(xx, hinh, pdf, tm):
    """Cắt từng hình từ PDF bản lời giải, ghép thành soat-hinh-k.png (mỗi ảnh tối đa 8 hình)."""
    from PIL import Image, ImageDraw
    dpi = 110
    trang = sorted({h['trang'] for h in hinh if h['trang']})
    for p in trang:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(p), '-l', str(p), '-png', '-singlefile', pdf,
                        os.path.join(tm, 'p%d' % p)], check=True)
    s = dpi / 72.27
    cat = []
    for h in hinh:
        if not h['trang']:
            continue
        im = Image.open(os.path.join(tm, 'p%d.png' % h['trang']))
        H = im.size[1]
        y0 = h['y'] - (h['h'] / 2 if h['baseline'] else 0)
        box = (max(0, int((h['x'] - 8) * s)), max(0, int(H - (y0 + h['h'] + 8) * s)),
               min(im.size[0], int((h['x'] + h['w'] + 8) * s)), min(H, int(H - (y0 - 8) * s)))
        c = im.crop(box).convert('RGB')
        nhan = '%s d%d %s %.1fx%.1fcm%s' % (h['cau'], h['dong'], h['loai'], h['rong_cm'], h['cao_cm'],
                                           ' LG' if h['loigiai'] else '')
        khung = Image.new('RGB', (max(c.size[0], 330) + 10, c.size[1] + 30), 'white')
        khung.paste(c, (5, 25))
        d = ImageDraw.Draw(khung)
        d.text((5, 5), nhan, fill=(200, 0, 0))
        d.rectangle([0, 0, khung.size[0] - 1, khung.size[1] - 1], outline=(150, 150, 150))
        cat.append(khung)
    out = []
    k = 0
    while cat:
        nhom, cat = cat[:8], cat[8:]
        k += 1
        rong = 1500
        x = y = cao_hang = 0
        vi_tri = []
        for c in nhom:
            if x + c.size[0] > rong and x > 0:
                x = 0
                y += cao_hang + 6
                cao_hang = 0
            vi_tri.append((x, y))
            x += c.size[0] + 6
            cao_hang = max(cao_hang, c.size[1])
        m = Image.new('RGB', (rong, y + cao_hang), 'white')
        for c, (a, b) in zip(nhom, vi_tri):
            m.paste(c, (a, b))
        f = os.path.join(tm, 'soat-hinh-%d.png' % k)
        m.save(f)
        out.append(f)
    return out


# ---------------------------------------------------------------- thu nhỏ hình
def so(x):
    return ('%.3f' % x).rstrip('0').rstrip('.')


def tim_tuy_chon(vb):
    """Vị trí [..] ngay sau \\begin{tikzpicture} (trả (a, b) bao cả ngoặc) hoặc None."""
    k = vb.index('\\begin{tikzpicture}') + len('\\begin{tikzpicture}')
    if k < len(vb) and vb[k] == '[':
        sau = 0
        for j in range(k, len(vb)):
            if vb[j] == '[' or vb[j] == '{':
                sau += 1
            elif vb[j] == ']' or vb[j] == '}':
                sau -= 1
                if sau == 0:
                    return k, j + 1
    return None


def tach_tuy_chon(s):
    """Tách danh sách khóa ở mức ngoài cùng."""
    phan, sau, cur = [], 0, ''
    for ch in s:
        if ch in '{(':
            sau += 1
        elif ch in '})':
            sau -= 1
        if ch == ',' and sau == 0:
            phan.append(cur)
            cur = ''
        else:
            cur += ch
    if cur.strip():
        phan.append(cur)
    return phan


def thu_tikz(vb, f):
    tc = tim_tuy_chon(vb)
    if tc is None:
        k = vb.index('\\begin{tikzpicture}') + len('\\begin{tikzpicture}')
        return vb[:k] + '[scale=%s]' % so(f) + vb[k:]
    a, b = tc
    ds = tach_tuy_chon(vb[a + 1:b - 1])
    co = False
    for i, x in enumerate(ds):
        m = re.match(r'(\s*)scale\s*=\s*([\d.]+)\s*$', x)
        if m:
            ds[i] = '%sscale=%s' % (m.group(1), so(float(m.group(2)) * f))
            co = True
    if not co:
        ds.insert(0, 'scale=%s' % so(f))
    return vb[:a] + '[' + ','.join(ds) + ']' + vb[b:]


def thu_axis(vb, f):
    """Nhân x=..cm, y=..cm trong \\begin{axis}[...] với f. Trả None nếu không có đơn vị dạng đó."""
    m = re.search(r'\\begin\{axis\}\[', vb)
    if not m:
        return None
    a = m.end() - 1
    sau = 0
    for j in range(a, len(vb)):
        if vb[j] in '[{':
            sau += 1
        elif vb[j] in ']}':
            sau -= 1
            if sau == 0:
                b = j + 1
                break
    tc = vb[a:b]
    dem = [0]

    def doi(mm):
        dem[0] += 1
        return '%s=%scm' % (mm.group(1), so(float(mm.group(2)) * f))
    tc2 = re.sub(r'(?<![a-z])([xy])\s*=\s*([\d.]+)\s*cm', doi, tc)
    if dem[0] < 2:
        return None
    return vb[:a] + tc2 + vb[b:]


def gon_bang(vb):
    """Thu gọn chiều cao các hàng của \\tkzTabInit."""
    m = re.search(r'\\tkzTabInit(\[[^\]]*\])?\{', vb)
    if not m:
        return vb, False
    a = m.end() - 1
    sau = 0
    for j in range(a, len(vb)):
        if vb[j] == '{':
            sau += 1
        elif vb[j] == '}':
            sau -= 1
            if sau == 0:
                b = j + 1
                break
    hang = tach_tuy_chon(vb[a + 1:b - 1])
    # giá trị hàng x (đối số thứ hai)
    c = b
    gia_tri = ''
    if c < len(vb) and vb[c] == '{':
        sau = 0
        for j in range(c, len(vb)):
            if vb[j] == '{':
                sau += 1
            elif vb[j] == '}':
                sau -= 1
                if sau == 0:
                    gia_tri = vb[c:j + 1]
                    break
    bien_thien = ' '.join(re.findall(r'\\tkzTabVar\{.*', vb))
    moi = []
    doi = False
    for i, x in enumerate(hang):
        mm = re.match(r'(.*)/\s*([\d.]+)\s*$', x, re.S)
        if not mm:
            moi.append(x)
            continue
        nhan, cao = mm.group(1), float(mm.group(2))
        phan_so = re.compile(r'\\dfrac|\\frac|\\sqrt|\\overline|\^\{')
        if cao >= 1.4:
            ds = 2.0 if phan_so.search(bien_thien) else 1.5
        else:
            co = phan_so.search(nhan) or (i == 0 and re.search(r'\\dfrac|\\frac', gia_tri))
            ds = 0.9 if co else 0.6
        ds = min(ds, cao)
        if abs(ds - cao) > 1e-6:
            doi = True
        moi.append('%s/%s' % (nhan, so(ds)))
    return vb[:a + 1] + ','.join(moi) + vb[b - 1:], doi


def thu_hinh(xx, lan_toi_da=3):
    src = duong_dan(xx)
    t = ten_de(xx)
    nhat_ky = []
    he_so = {}       # dòng bắt đầu -> hệ số đã nhân (cộng dồn)
    # bảng: thu gọn một lần theo quy tắc
    dong = open(src, encoding='utf-8').read().split('\n')
    cau0 = cau_trong_nguon(dong)
    i = 0
    while i < len(dong):
        if '\\begin{tikzpicture}' in dong[i] and not dong[i].lstrip().startswith('%'):
            a, b, vb = khoi_hinh(dong, i)
            c0, _ = trong_loigiai(dong, cau0, i)
            if c0 is not None and c0['giuhinh']:
                i = b + 1
                continue
            if '\\tkzTabInit' in vb:
                vb2, doi = gon_bang(vb)
                if doi:
                    dong[a:b + 1] = vb2.split('\n')
                    nhat_ky.append('d%d bảng tkz-tab: thu gọn hàng' % (a + 1))
            i = b + 1
        else:
            i += 1
    open(src, 'w', encoding='utf-8').write('\n'.join(dong))
    for lan in range(lan_toi_da):
        kq = do_hinh(xx, in_ra=False)
        if kq is None:
            return None
        hinh = kq[0]
        dong = open(src, encoding='utf-8').read().split('\n')
        sua = 0
        for h in sorted(hinh, key=lambda z: -z['dong']):
            if h['loai'] == 'bang' or h['giuhinh']:
                continue
            tren, dich = TRAN_TREN[h['loai']], DICH[h['loai']]
            if h['cao_cm'] <= tren + 0.05:
                continue
            f = dich / h['cao_cm']
            if lan > 0:
                f = min(f * 0.97, 0.98)
            da = he_so.get(h['dong'], 1.0)
            if da * f < HE_SO_SAN:
                f = HE_SO_SAN / da
                if f > 0.995:
                    nhat_ky.append('d%d %s: CHẠM SÀN %.1f (còn %.2f cm) — thu tay nếu cần, soát chồng nhãn'
                                   % (h['dong'], h['cau'], HE_SO_SAN, h['cao_cm']))
                    continue
            a, b, vb = khoi_hinh(dong, h['dong'] - 1)
            if h['loai'] == 'do-thi':
                vb2 = thu_axis(vb, f)
                if vb2 is None:
                    nhat_ky.append('d%d %s: KHÔNG TỰ THU ĐƯỢC (axis không có x=..cm, y=..cm) — sửa tay' % (h['dong'], h['cau']))
                    continue
            else:
                vb2 = thu_tikz(vb, f)
            dong[a:b + 1] = vb2.split('\n')
            he_so[h['dong']] = he_so.get(h['dong'], 1.0) * f
            sua += 1
            nhat_ky.append('d%d %s %s: %.2f cm -> x%.3f' % (h['dong'], h['cau'], h['loai'], h['cao_cm'], f))
        open(src, 'w', encoding='utf-8').write('\n'.join(dong))
        if sua == 0:
            break
    kq = do_hinh(xx, in_ra=False)
    hinh, pdf, tm, log = kq
    for d, f in he_so.items():
        if f < 0.5:
            nhat_ky.append('d%d: hệ số cộng dồn %.2f < 0,5 — soát kỹ nhãn' % (d, f))
    for h in hinh:
        if h['loai'] != 'bang' and not h['giuhinh'] and h['cao_cm'] > TRAN_TREN[h['loai']] + 0.05:
            nhat_ky.append('CÒN CAO: d%d %s %s %.2f cm' % (h['dong'], h['cau'], h['loai'], h['cao_cm']))
    giu = sorted({h['cau'] for h in hinh if h['giuhinh']})
    if giu:
        nhat_ky.append('giữ cỡ (%% giuhinh, không thu): %s' % ', '.join(giu))
    anh = anh_soat_hinh(xx, hinh, pdf, tm)
    print('== %s: thu hình' % t)
    for x in nhat_ky:
        print('  ' + x)
    for h in hinh:
        print('  %-6s d%-4d %-10s %5.2f x %4.2f cm %s%s' % (h['cau'], h['dong'], h['loai'], h['rong_cm'], h['cao_cm'],
                                                          '(lời giải)' if h['loigiai'] else '',
                                                          ' (giuhinh)' if h['giuhinh'] else ''))
    print('  Ảnh soát hình: ' + ' '.join(os.path.relpath(a, ROOT) for a in anh))
    return hinh


# ---------------------------------------------------------------- Needspace
def do_khoi(xx, nd, tm):
    t = ten_de(xx)
    if os.path.isdir(tm):
        shutil.rmtree(tm)
    log, pdf, loi = bien_dich(ban_do(nd, 'dethi', hinh=False), tm, t)
    if loi:
        print('LỖI biên dịch %s:\n%s' % (t, '\n'.join(loi[:3])))
        return None
    vt = doc_aux(tm, t)
    tr = hinh_hoc_trang(log)
    so_khoi = {}
    for m in re.finditer(r'EZKHOI:(\d+):(\d+)', log):
        so_khoi[int(m.group(1))] = int(m.group(2))
    return vt, tr, so_khoi, pdf, log


RE_NS = re.compile(r'^\s*(?:\\par)?\\Needspace(?:Cau)?(?:\[([^\]]*)\])?\{([^}]*)\}\s*%?\s*$')
RE_BANG = re.compile(r'^\s*\\NeedspaceBang\{([^}]*)\}\s*%?\s*$')
CONG_TAC = ['\\def\\TachCauDS{1}% câu Đúng/Sai được tách câu dẫn / bảng Phát biểu khi cần (preamble-eduzy-v2, tools/dan_trang)',
            '\\def\\TachCauLG{1}% bản lời giải: phần đề câu cao hơn 1/3 trang được tách']


def so_dong(s):
    m = re.match(r'^\s*([\d.]+)\\baselineskip\s*$', s or '')
    return float(m.group(1)) if m else None


def dong_bang(dong, c):
    """Dòng \\choiceTFt (phần đề, trước \\loigiai) của câu c, hoặc None."""
    for i in range(c['bd'], c['kt'] + 1):
        st = dong[i].strip()
        if st.startswith('%'):
            continue
        if '\\loigiai' in st:
            return None
        if st.startswith('\\choiceTFt'):
            return i
    return None


def them_cong_tac(dong):
    """Bật hai công tắc tách câu (trước \\input{preamble-eduzy-v2}) nếu file chưa có."""
    co = '\n'.join(dong)
    for ct in CONG_TAC:
        ten = ct.split('{')[0]
        if ten + '{' in co:
            continue
        for i, d in enumerate(dong):
            if d.strip().startswith('\\input{preamble-eduzy-v2}'):
                dong.insert(i, ct)
                break
    return dong


def chen_needspace(dong, cau, gia_tri, che_do=None, bang=None):
    """gia_tri[k] = số dòng cả khối; che_do[k] = (số dòng câu dẫn) nếu câu được tách; bang[k] = số dòng bảng."""
    che_do = che_do or {}
    bang = bang or {}
    them = []
    for k, c in enumerate(cau):
        n = gia_tri.get(k)
        if n is None:
            continue
        i = c['bd']
        if c['dau_phan']:
            for j in range(i, -1, -1):
                if '\\subsection*' in dong[j]:
                    i = j - 1 if j > 0 and dong[j - 1].strip() == '\\noindent' else j
                    break
        lui = re.match(r'^(\s*)', dong[i]).group(1)
        tach = che_do.get(k)
        if tach is not None:
            them.append((i, '%s\\NeedspaceCau[%s\\baselineskip]{%s\\baselineskip}' % (lui, so(tach), so(n))))
        else:
            them.append((i, '%s\\NeedspaceCau{%s\\baselineskip}' % (lui, so(n))))
        jb = dong_bang(dong, c)
        if jb is not None and bang.get(k) is not None:
            lui2 = re.match(r'^(\s*)', dong[jb]).group(1)
            them.append((jb, '%s\\NeedspaceBang{%s\\baselineskip}%%' % (lui2, so(bang[k]))))
    out = list(dong)
    for i, t in sorted(them, key=lambda z: -z[0]):
        out.insert(i, t)
    return '\n'.join(out)


def len_dong(h):
    return math.ceil((h + LE_DONG * BS_PT) / BS_PT * 10 - 1e-6) / 10


def cap_nhat(gt, tc, k, n, q):
    """Thay giá trị theo độ tin cậy: 3 giữa trang > 2 đầu trang > 1 ước lượng khi bị ngắt. Trả True nếu đổi."""
    cu_n, cu_q = gt.get(k), tc.get(k, 0)
    if q == 1:
        moi = n if cu_n is None or cu_q < 1 else max(n, cu_n)
        q_moi = max(cu_q, 1)
    elif q >= cu_q:
        moi, q_moi = n, q
    else:
        moi, q_moi = cu_n, cu_q
    gt[k], tc[k] = moi, q_moi
    return moi != cu_n


def moc(vt, cau2, ns_dong, k):
    """Các mốc của khối k: A (đầu khối, câu đầu phần lấy mốc tiêu đề), T (cuối câu dẫn Đúng/Sai), U (đầu bảng), C (cuối)."""
    A = vt.get('EZa%d' % (k + 1))
    if cau2[k]['dau_phan']:
        for i in range(cau2[k]['bd'], -1, -1):
            if '\\subsection*' in ns_dong[i]:
                A = vt.get('EZp%d' % (i + 1)) or A
                break
    return A, vt.get('EZt%d' % (k + 1)), vt.get('EZu%d' % (k + 1)), vt.get('EZc%d' % (k + 1))


def trang_trong(vt, tr, cau2, ns_dong):
    """Khoảng trống cuối mỗi trang (cm) theo mốc, và trang nào được miễn (trang cuối, trang ngay trước tiêu đề phần).
    Trả về dict trang -> (cm, miễn, khối đầu trang sau)."""
    thap = {}
    dau_trang = {}
    for k in range(len(cau2)):
        A, T, U, C = moc(vt, cau2, ns_dong, k)
        for m in (C,) + ((T,) if T and U and T[2] != U[2] else ()):
            if m:
                thap[m[2]] = min(thap.get(m[2], 1e9), m[1])
        if A and A[2] not in dau_trang:
            dau_trang[A[2]] = k
        if U and T and U[2] != T[2] and U[2] not in dau_trang:
            dau_trang[U[2]] = ('bang', k)
    so_trang = max(thap) if thap else 0
    kq = {}
    for p in range(1, so_trang + 1):
        cm = (thap.get(p, tr['ytop']) - tr['ybot']) / PT_PER_CM
        sau = dau_trang.get(p + 1)
        mien = p == so_trang or (isinstance(sau, int) and cau2[sau]['dau_phan'])
        kq[p] = (cm, mien, sau)
    return kq


def needspace(xx, lan_toi_da=8):
    """Đo và ghi \\NeedspaceCau (trên mỗi câu) và \\NeedspaceBang (trước bảng Đúng/Sai). Giá trị thay theo độ tin cậy
    đo; câu Đúng/Sai (trừ câu đầu Phần II) chỉ được chọn tách câu dẫn / bảng khi để nguyên khối làm trang trước trống
    quá 1/4 (không tính trang ngay trước tiêu đề phần)."""
    src = duong_dan(xx)
    t = ten_de(xx)
    tm = os.path.join(os.path.dirname(src), 'bien-dich', 'dan-trang', 'do-khoi')
    dong = open(src, encoding='utf-8').read().split('\n')
    dong = them_cong_tac(dong)
    cau = cau_trong_nguon(dong)
    # gỡ \Needspace / \NeedspaceCau / \NeedspaceBang ngoài lời giải, nhớ giá trị cũ
    giu, cu_ca, cu_bang = [], [], {}
    for i, d in enumerate(dong):
        m, mb = RE_NS.match(d), RE_BANG.match(d)
        if m or mb:
            c, lg = trong_loigiai(dong, cau, i)
            if c is not None and lg:
                giu.append(d)
                continue
            if mb and c is not None:
                cu_bang[cau.index(c)] = so_dong(mb.group(1))
            elif m and c is None:
                cu_ca.append((i, so_dong(m.group(2)), so_dong(m.group(1)) if m.group(1) else None))
            continue
        giu.append(d)
    gia_tri, che_do, bang = {}, {}, {}
    for i, v, vs in cu_ca:
        for k, c in enumerate(cau):
            if c['bd'] > i:
                gia_tri.setdefault(k, v)
                if vs is not None:
                    che_do[k] = vs
                break
    for k, v in cu_bang.items():
        bang[k] = v
    dong = giu
    cau = cau_trong_nguon(dong)
    co_bang = {k for k, c in enumerate(cau) if dong_bang(dong, c) is not None}
    tc_ca, tc_dan, tc_bang = {}, {}, {}
    dan = dict(che_do)
    # câu Đúng/Sai có % tachDS: luôn ở chế độ tách (kể cả câu đầu Phần II); lần đo đầu chưa có độ cao câu dẫn
    for k in sorted(co_bang):
        if cau[k]['tachDS'] and k not in che_do:
            che_do[k] = True
    gioi_han = None
    for lan in range(lan_toi_da):
        nd = chen_needspace(dong, cau, gia_tri, {k: dan.get(k) for k in che_do}, bang)
        kq = do_khoi(xx, nd, tm)
        if kq is None:
            return None
        vt, tr, so_khoi, pdf, log = kq
        gioi_han = 0.25 * tr['chu'] / PT_PER_CM
        ns_dong = nd.split('\n')
        cau2 = cau_trong_nguon(ns_dong)
        if len(so_khoi) != len(cau2):
            print('CẢNH BÁO: số khối đo (%d) khác số câu (%d)' % (len(so_khoi), len(cau2)))
        doi = ngat = 0

        def do(P, Q, g):
            """(số dòng, độ tin cậy) cho đoạn P -> Q."""
            if P[2] == Q[2]:
                h = P[1] - Q[1]
                if abs(P[1] - tr['ytop']) < 2.0:
                    return len_dong(h + g), 2
                return len_dong(h), 3
            h = (P[1] - tr['ybot']) + (tr['ytop'] - Q[1]) + g + tr['chu'] * (Q[2] - P[2] - 1)
            return len_dong(h), 1

        for k in range(len(cau2)):
            A, T, U, C = moc(vt, cau2, ns_dong, k)
            if not A or not C:
                continue
            g = G_DAU_PHAN if cau2[k]['dau_phan'] else G_DAU_TRANG
            tach_hop_le = (k in che_do and k in co_bang and T and U and T[2] != U[2]
                           and A[2] == T[2] and U[2] == C[2])
            if tach_hop_le:
                # câu được chọn tách và đã tách đúng chỗ: cả khối không đo được, giữ giá trị cũ (hoặc dẫn + bảng)
                if gia_tri.get(k) is None and dan.get(k) is not None and bang.get(k) is not None:
                    gia_tri[k] = round(dan[k] + bang[k], 1)
            else:
                n, q = do(A, C, g)
                if q == 1:
                    ngat += 1
                doi += cap_nhat(gia_tri, tc_ca, k, n, q)
            if k in co_bang and T and U:
                n, q = do(A, T, g)
                if q == 1:
                    ngat += 1
                doi += cap_nhat(dan, tc_dan, k, n, q)
                n, q = do(U, C, G_DAU_TRANG)
                if q == 1:
                    ngat += 1
                doi += cap_nhat(bang, tc_bang, k, n, q)
        print('  lần %d: %d chỗ ngắt chưa hợp lệ, %d giá trị đổi, %d câu Đúng/Sai được tách'
              % (lan + 1, ngat, doi, len(che_do)))
        if any(dan.get(k) is None for k in che_do):
            continue      # câu % tachDS vừa có độ cao câu dẫn: đo lại với chế độ tách
        if doi or ngat:
            continue
        # chọn thêm câu Đúng/Sai được tách: trang trống quá 1/4 (không miễn) mà trang sau mở đầu bằng câu Đúng/Sai
        moi = []
        # khoảng trống theo điểm ảnh (cùng cách đo với kiem) để không sót trang sát ngưỡng
        try:
            anh = khoang_trong(pdf, tr, tm, 'trang-do')
        except Exception:
            anh = []
        for p, (cm, mien, sau) in trang_trong(vt, tr, cau2, ns_dong).items():
            if p - 1 < len(anh):
                cm = max(cm, anh[p - 1][1])
            if mien or cm <= gioi_han - 0.2 or not isinstance(sau, int):
                continue
            if sau in co_bang and not cau2[sau]['dau_phan'] and sau not in che_do:
                che_do[sau] = True
                moi.append('%s.%d' % ('I' * cau2[sau]['phan'], cau2[sau]['so']))
        if not moi:
            break
        print('  tách câu dẫn / bảng: ' + ', '.join(moi))
    nd = chen_needspace(dong, cau, gia_tri, {k: dan.get(k) for k in che_do}, bang)
    open(src, 'w', encoding='utf-8').write(nd)
    print('== %s: \\NeedspaceCau (dòng): %s' % (t, ' '.join(
        '%s.%d:%s%s' % ('I' * c['phan'], c['so'], so(gia_tri[k]) if gia_tri.get(k) is not None else '?',
                        ('[dẫn %s|bảng %s]' % (so(dan.get(k) or 0), so(bang.get(k) or 0))) if k in che_do else '')
        for k, c in enumerate(cau))))
    return gia_tri


# ---------------------------------------------------------------- soát
def khoang_trong(pdf, tr, thu_muc, ten_anh, dpi=60):
    """Ảnh từng trang + khoảng trống cuối mỗi trang (cm), đo bằng điểm ảnh tối trong vùng chữ."""
    from PIL import Image
    for f in os.listdir(thu_muc):
        if f.startswith(ten_anh + '-') and f.endswith('.png'):
            os.remove(os.path.join(thu_muc, f))
    subprocess.run(['pdftoppm', '-r', str(dpi), '-png', pdf, os.path.join(thu_muc, ten_anh)], check=True)
    anh = sorted([f for f in os.listdir(thu_muc) if f.startswith(ten_anh + '-') and f.endswith('.png')],
                 key=lambda z: int(re.search(r'-(\d+)\.png$', z).group(1)))
    s = dpi / 72.27
    kq = []
    for f in anh:
        im = Image.open(os.path.join(thu_muc, f)).convert('L')
        W, H = im.size
        y_tren = int(H - tr['ytop'] * s) + 2
        y_duoi = int(H - tr['ybot'] * s)
        px = im.load()
        thap = None
        for y in range(y_duoi, y_tren, -1):
            if any(px[x, y] < 110 for x in range(int(0.05 * W), int(0.95 * W))):
                thap = y
                break
        trong = (y_duoi - thap) / s / PT_PER_CM if thap else tr['chu'] / PT_PER_CM
        kq.append((os.path.join(thu_muc, f), round(trong, 1)))
    return kq


def ghep(anh, ra, cot=3):
    from PIL import Image
    ims = [Image.open(a) for a, _ in anh]
    out = []
    for k in range(0, len(ims), cot * 2):
        nhom = ims[k:k + cot * 2]
        w, h = nhom[0].size
        m = Image.new('RGB', (w * cot, h * ((len(nhom) + cot - 1) // cot)), 'white')
        for i, im in enumerate(nhom):
            m.paste(im, ((i % cot) * w, (i // cot) * h))
        f = '%s-%d.png' % (ra, k // (cot * 2) + 1)
        m.save(f)
        out.append(f)
    return out


def kiem(xx, xuat=False):
    src = duong_dan(xx)
    t = ten_de(xx)
    nd = open(src, encoding='utf-8').read()
    goc = os.path.join(os.path.dirname(src), 'bien-dich', 'dan-trang')
    loi_tong = []
    # bản đề (có bộ đo để soát ngắt câu)
    tm_de = os.path.join(goc, 'de')
    if os.path.isdir(tm_de):
        shutil.rmtree(tm_de)
    log, pdf_de, loi = bien_dich(ban_do(nd, 'dethi', hinh=False), tm_de, t)
    if loi:
        print('LỖI biên dịch bản đề %s:\n%s' % (t, '\n'.join(loi[:3])))
        return False
    vt = doc_aux(tm_de, t)
    tr = hinh_hoc_trang(log)
    dong = nd.split('\n')
    cau = cau_trong_nguon(dong)
    tach = []

    def ngat(P, Q):
        # P ở sát cuối trang trước mà nội dung bắt đầu ở trang sau thì không tính là ngắt
        return P and Q and P[2] != Q[2] and not (Q[2] == P[2] + 1 and P[1] - tr['ybot'] < 30)

    for k, c in enumerate(cau):
        A, T, U, C = moc(vt, cau, dong, k)
        nhan = '%s.%d' % ('I' * c['phan'], c['so'])
        if dong_bang(dong, c) is not None and T and U:
            if ngat(A, T):
                loi_tong.append('bản đề: câu %s bị ngắt giữa câu dẫn / hình (%d → %d)' % (nhan, A[2], T[2]))
            if ngat(U, C):
                loi_tong.append('bản đề: câu %s bị ngắt giữa bảng Phát biểu (%d → %d)' % (nhan, U[2], C[2]))
            if T[2] != U[2]:
                tach.append('%s (câu dẫn tr. %d, bảng tr. %d)' % (nhan, T[2], U[2]))
        elif ngat(A, C):
            loi_tong.append('bản đề: câu %s bị ngắt trang (%d → %d)' % (nhan, A[2], C[2]))
    mien = {p for p, (cm, m, sau) in trang_trong(vt, tr, cau, dong).items() if m}
    kt_de = khoang_trong(pdf_de, tr, tm_de, 'trang')
    # bản đề sạch (không bộ đo) để xuất
    tm_de2 = os.path.join(goc, 'de-sach')
    if os.path.isdir(tm_de2):
        shutil.rmtree(tm_de2)
    _, pdf_de2, loi = bien_dich(ban_do(nd, 'dethi', do=False), tm_de2, t)
    # bản lời giải (nguyên file)
    tm_lg = os.path.join(goc, 'loigiai')
    if os.path.isdir(tm_lg):
        shutil.rmtree(tm_lg)
    log2, pdf_lg, loi2 = bien_dich(nd, tm_lg, t)
    if loi2 or not pdf_de2:
        print('LỖI biên dịch bản lời giải/bản đề %s:\n%s' % (t, '\n'.join((loi2 or loi)[:3])))
        return False
    kt_lg = khoang_trong(pdf_lg, tr, tm_lg, 'trang', dpi=40)
    # cỡ hình (bản lời giải có mốc hình, thư mục do-hinh): hình cao hơn trần, trừ câu % giuhinh
    kq_hinh = do_hinh(xx, in_ra=False)
    lech = lech_co(kq_hinh[0]) if kq_hinh else []
    tran = re.findall(r'Overfull \\hbox \((\d+\.\d+)pt', log2)
    tran = [float(x) for x in tran if float(x) > 7]
    gioi_han = 0.25 * tr['chu'] / PT_PER_CM
    gioi_han_lg = tr['chu'] / 3 / PT_PER_CM
    luu_y = []
    for i, (f, cm) in enumerate(kt_de[:-1]):
        if cm > gioi_han:
            if i + 1 in mien:
                luu_y.append('bản đề: trang %d trống %.1f cm, ngay trước tiêu đề phần mới (được miễn)' % (i + 1, cm))
            else:
                loi_tong.append('bản đề: trang %d trống %.1f cm cuối trang (> 1/4 = %.1f cm)' % (i + 1, cm, gioi_han))
    for x in lech:
        luu_y.append('hình lệch cỡ: ' + x)
    for i, (f, cm) in enumerate(kt_lg[:-1]):
        if cm > gioi_han_lg:
            loi_tong.append('bản lời giải: trang %d trống %.1f cm cuối trang (> 1/3 = %.1f cm)' % (i + 1, cm, gioi_han_lg))
        elif cm > gioi_han:
            luu_y.append('bản lời giải: trang %d trống %.1f cm (từ 1/4 đến 1/3 trang)' % (i + 1, cm))
    # bản đề sạch (để xuất) phải dàn trang giống bản đo
    kt_sach = khoang_trong(pdf_de2, tr, tm_de2, 'trang')
    if [round(c) for _, c in kt_sach] != [round(c) for _, c in kt_de]:
        loi_tong.append('bản đề xuất (không bộ đo) dàn trang khác bản đo: %s / %s'
                        % (' '.join(str(c) for _, c in kt_sach), ' '.join(str(c) for _, c in kt_de)))
    anh = ghep(kt_de, os.path.join(tm_de, 'soat-de'))
    print('== %s: bản đề %d trang, bản lời giải %d trang' % (t, len(kt_de), len(kt_lg)))
    print('  trống cuối trang bản đề (cm): ' + ' '.join('%s' % cm for _, cm in kt_de))
    print('  trống cuối trang bản lời giải (cm): ' + ' '.join('%s' % cm for _, cm in kt_lg))
    if tach:
        print('  câu Đúng/Sai tách câu dẫn / bảng (bản đề): ' + '; '.join(tach))
    if tran:
        print('  tràn lề > 7pt ở bản lời giải: %s' % ', '.join('%.1f' % x for x in tran))
    for x in luu_y:
        print('  LƯU Ý: ' + x)
    for x in loi_tong:
        print('  LỖI: ' + x)
    if not loi_tong:
        print('  ĐẠT: không câu bị ngắt sai quy tắc, không trang trống quá 1/4 (trừ trang cuối, trang trước tiêu đề phần).')
    print('  Ảnh soát bản đề: ' + ' '.join(os.path.relpath(a, ROOT) for a in anh))
    if xuat:
        tp = os.path.join(ROOT, 'thanh-pham')
        shutil.copy(pdf_de2, os.path.join(tp, t + '-DE.pdf'))
        shutil.copy(pdf_lg, os.path.join(tp, t + '.pdf'))
        r = subprocess.run(['bash', os.path.join(ROOT, 'dong-goi.sh'), src], capture_output=True, text=True, cwd=ROOT)
        print('  ' + r.stdout.strip().split('\n')[0])
        print('  Đã chép thanh-pham/%s.pdf, thanh-pham/%s-DE.pdf' % (t, t))
    return not loi_tong


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    lenh, ds = sys.argv[1], sys.argv[2:]
    ok = True
    for xx in ds:
        if lenh == 'do-hinh':
            kq = do_hinh(xx)
            if kq:
                print('  Ảnh soát hình: ' + ' '.join(os.path.relpath(a, ROOT) for a in anh_soat_hinh(xx, kq[0], kq[1], kq[2])))
        elif lenh == 'thu-hinh':
            thu_hinh(xx)
        elif lenh == 'needspace':
            needspace(xx)
        elif lenh == 'kiem':
            ok = kiem(xx) and ok
        elif lenh == 'xuat':
            ok = kiem(xx, xuat=True) and ok
        elif lenh == 'tat-ca':
            thu_hinh(xx)
            needspace(xx)
            ok = kiem(xx) and ok
        else:
            print(__doc__)
            sys.exit(1)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
