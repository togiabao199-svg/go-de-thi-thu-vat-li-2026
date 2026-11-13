#!/usr/bin/env python3
r"""Tách mọi tikzpicture (kể cả circuitikz) của file đề ra ảnh riêng, ghép cạnh ảnh gốc:
so-hinh/<stt>-cau-<câu>.png (cạnh file đề). Câu đánh dạng I.2, II.4, III.5 theo thứ tự \begin{ex} trong từng PHẦN.

Dùng (từ gốc repo):
  python3 tools/so_hinh.py de/<tên>/<tên>.tex <thư mục ảnh gốc> "I.2=image2.png,II.4=image54.jpeg,..."
  - ảnh gốc của đề Word: unzip -j "<file.docx>" 'word/media/*' -d <thư mục>
  - đề PDF: xuất ảnh trang (pdftoppm -r 150 -png <file.pdf> <thư mục>/trang) rồi chỉ vùng cắt sau dấu @:
      "I.5=trang-2.png@0.08:0.31:0.55:0.52"   (x0:y0:x1:y1, giá trị ≤ 1 là tỉ lệ khổ ảnh, > 1 là pixel)
  - câu không ghi ảnh gốc: chỉ in hình vẽ lại (ô gốc để trắng).

Macro hình: \input{preamble-vatli-hinh} (gốc repo) + các dòng khai báo riêng của đề nằm giữa các dòng \input{preamble...}
và \begin{document} (đề cũ còn khối "%===================== MACRO HÌNH" cũng đọc được). Màu blue, cyan, teal được đổi
sang tông vàng như preamble-eduzy-v2 để ảnh so khớp màu bản in. Biên dịch bằng xelatex.
"""
import os
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if len(sys.argv) < 3:
    print(__doc__)
    sys.exit(1)
src, goc = sys.argv[1], sys.argv[2]
anhxa = sys.argv[3] if len(sys.argv) > 3 else ''
ax = dict(x.split('=', 1) for x in anhxa.split(',') if '=' in x)
s = open(src, encoding='utf8').read()
bd = s.index('\\begin{document}')
dau = s[:bd]
# khai báo riêng của đề: sau dòng \input{preamble...} cuối cùng (hoặc khối MACRO HÌNH cũ)
if '%===================== MACRO HÌNH' in dau:
    rieng = dau[dau.index('%===================== MACRO HÌNH'):]
else:
    ms = list(re.finditer(r'\\input\{preamble[^}]*\}', dau))
    rieng = dau[ms[-1].end():] if ms else ''
dung_chung = '\\input{preamble-vatli-hinh}' if 'MACRO HÌNH' not in rieng else ''
body = s[bd:]
# vị trí câu: đếm \begin{ex} theo phần; bỏ dòng comment
body_sach = '\n'.join(d for d in body.split('\n') if not d.lstrip().startswith('%'))
hinh = []
phan, cau = 'I', 0
for m in re.finditer(r'PHẦN (I+)\.|\\begin\{ex\}|\\begin\{(tikzpicture|circuitikz)\}.*?\\end\{\2\}', body_sach, re.S):
    t = m.group(0)
    if t.startswith('PHẦN'):
        phan, cau = m.group(1), 0
    elif t.startswith('\\begin{ex}'):
        cau += 1
    else:
        hinh.append(('%s.%d' % (phan, cau), t))
ra = os.path.join(os.path.dirname(os.path.abspath(src)), 'so-hinh')
os.makedirs(ra, exist_ok=True)
doc = ['\\documentclass[12pt,tikz,border=6pt]{standalone}',
       '\\usepackage{amsmath,amssymb,mathpazo}', '\\usepackage[no-math]{fontspec}',
       '\\setmainfont{TeX Gyre Pagella}', '\\usepackage{pgfplots}\\pgfplotsset{compat=1.17}',
       '\\usetikzlibrary{math,calc,intersections,angles,quotes,shapes,shapes.geometric,arrows,patterns,arrows.meta,'
       'decorations.shapes,decorations.markings,shadows,decorations.pathreplacing}',
       '\\definecolor{gold1}{RGB}{126,96,0}\\definecolor{gold2}{RGB}{192,144,3}\\definecolor{gold3}{RGB}{255,215,99}',
       '\\definecolor{gold4}{RGB}{255,231,153}\\definecolor{gold5}{RGB}{255,243,205}',
       '\\colorlet{blue}{gold1}\\colorlet{cyan}{gold2}\\colorlet{teal}{gold2}',
       '\\providecommand{\\vv}[1]{\\overrightarrow{#1}}', dung_chung, rieng, '\\begin{document}']
doc += [h for _, h in hinh] + ['\\end{document}']
tex = os.path.join(ra, 'hinh.tex')
open(tex, 'w', encoding='utf8').write('\n'.join(doc))
env = dict(os.environ)
env['TEXINPUTS'] = ROOT + '//:' + env.get('TEXINPUTS', '')
subprocess.run(['xelatex', '-interaction=nonstopmode', 'hinh.tex'], cwd=ra, capture_output=True, env=env)
log = open(os.path.join(ra, 'hinh.log'), encoding='utf8', errors='replace').read()
loi = re.findall(r'^!.*(?:\n.*){0,3}', log, re.M)
if loi or not os.path.exists(os.path.join(ra, 'hinh.pdf')):
    print('LỖI biên dịch hình (%s):\n%s' % (os.path.join(ra, 'hinh.log'), '\n'.join(loi[:3])))
    sys.exit(1)
subprocess.run(['pdftoppm', '-r', '220', '-png', 'hinh.pdf', 'tikz'], cwd=ra)
anh = sorted(f for f in os.listdir(ra) if f.startswith('tikz-'))
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26)
except Exception:
    font = ImageFont.load_default()


def mo_goc(spec):
    ten, _, vung = spec.partition('@')
    a = Image.open(os.path.join(goc, ten)).convert('RGB')
    if vung:
        v = [float(x) for x in vung.split(':')]
        v = [x * (a.width if i % 2 == 0 else a.height) if x <= 1 else x for i, x in enumerate(v)]
        a = a.crop(tuple(int(x) for x in v))
    return a


for i, (vt, _) in enumerate(hinh):
    b = Image.open(os.path.join(ra, anh[i])).convert('RGB')
    a = mo_goc(ax[vt]) if vt in ax else Image.new('RGB', (10, 10), 'white')
    h = 520
    a = a.resize((max(1, int(a.width * h / a.height)), h))
    b = b.resize((max(1, int(b.width * h / b.height)), h))
    W = a.width + b.width + 90
    c = Image.new('RGB', (W, h + 70), 'white')
    d = ImageDraw.Draw(c)
    d.text((20, 15), 'Câu %s — GỐC' % vt, fill='black', font=font)
    d.text((a.width + 70, 15), 'VẼ LẠI (TikZ)', fill='black', font=font)
    c.paste(a, (20, 60))
    c.paste(b, (a.width + 70, 60))
    d.line([(a.width + 45, 60), (a.width + 45, h + 60)], fill=(180, 180, 180), width=3)
    c.save(os.path.join(ra, '%02d-cau-%s.png' % (i + 1, vt.replace('.', '-'))))
    print('%02d  Câu %s' % (i + 1, vt))
for f in anh:
    os.remove(os.path.join(ra, f))
for f in os.listdir(ra):
    if f.startswith('hinh.'):
        os.remove(os.path.join(ra, f))   # giữ lại khi biên dịch lỗi (đã thoát ở trên) để xem hinh.log
