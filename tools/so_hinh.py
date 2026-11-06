#!/usr/bin/env python3
"""Tách mọi tikzpicture của file đề ra ảnh riêng, ghép cạnh ảnh gốc: so-hinh/<stt>-cau-<câu>.png
(cạnh file đề). Câu đánh dạng I.2, II.4, III.5 theo thứ tự \begin{ex} trong từng PHẦN.
Dùng (từ gốc repo):
  python3 tools/so_hinh.py de/<tên>/<tên>.tex <thư mục ảnh gốc> "I.2=image2.png,II.4=image54.jpeg,..."
Ảnh gốc của đề Word: unzip -j "<file.docx>" 'word/media/*' -d /tmp/anh-goc   (đề PDF: cắt từ ảnh trang)
Macro hình lấy từ khối "%===================== MACRO HÌNH" trong file đề (nếu đã chuyển sang
preamble-vatli-hinh.tex thì sửa biến macro bên dưới cho đọc file đó). Biên dịch bằng xelatex.
"""
import os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

src, goc, anhxa = sys.argv[1], sys.argv[2], sys.argv[3]
ax = dict(x.split('=') for x in anhxa.split(','))
s = open(src, encoding='utf8').read()
macro = s[s.index('%===================== MACRO HÌNH'):s.index('\\begin{document}')]
body = s[s.index('\\begin{document}'):]
# vị trí câu: đếm \begin{ex} theo phần
hinh = []
phan, cau = 'I', 0
for m in re.finditer(r'PHẦN (I+)\.|\\begin\{ex\}|\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', body, re.S):
    t = m.group(0)
    if t.startswith('PHẦN'):
        phan, cau = m.group(1), 0
    elif t.startswith('\\begin{ex}'):
        cau += 1
    else:
        hinh.append(('%s.%d' % (phan, cau), t))
ra = os.path.join(os.path.dirname(os.path.abspath(src)), 'so-hinh')
os.makedirs(ra, exist_ok=True)
doc = ['\\documentclass[tikz,border=6pt]{standalone}',
       '\\usepackage{amsmath,amssymb,mathpazo}', '\\usepackage[no-math]{fontspec}',
       '\\setmainfont{TeX Gyre Pagella}', '\\usepackage{pgfplots}\\pgfplotsset{compat=1.17}',
       '\\usetikzlibrary{calc,arrows.meta,decorations.markings,shadows,patterns}',
       '\\providecommand{\\vv}[1]{\\overrightarrow{#1}}', macro, '\\begin{document}']
doc += [h for _, h in hinh] + ['\\end{document}']
tex = os.path.join(ra, 'hinh.tex')
open(tex, 'w', encoding='utf8').write('\n'.join(doc))
subprocess.run(['xelatex', '-interaction=nonstopmode', 'hinh.tex'], cwd=ra, capture_output=True)
subprocess.run(['pdftoppm', '-r', '220', '-png', 'hinh.pdf', 'tikz'], cwd=ra)
anh = sorted(f for f in os.listdir(ra) if f.startswith('tikz-'))
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26)
except Exception:
    font = ImageFont.load_default()
for i, (vt, _) in enumerate(hinh):
    b = Image.open(os.path.join(ra, anh[i])).convert('RGB')
    a = Image.open(os.path.join(goc, ax[vt])).convert('RGB') if vt in ax else Image.new('RGB', (10, 10), 'white')
    h = 520
    a = a.resize((max(1, int(a.width * h / a.height)), h))
    b = b.resize((max(1, int(b.width * h / b.height)), h))
    W = a.width + b.width + 90
    c = Image.new('RGB', (W, h + 70), 'white')
    d = ImageDraw.Draw(c)
    d.text((20, 15), 'Câu %s — GỐC' % vt, fill='black', font=font)
    d.text((a.width + 70, 15), 'VẼ LẠI (TikZ)', fill='black', font=font)
    c.paste(a, (20, 60)); c.paste(b, (a.width + 70, 60))
    d.line([(a.width + 45, 60), (a.width + 45, h + 60)], fill=(180, 180, 180), width=3)
    c.save(os.path.join(ra, '%02d-cau-%s.png' % (i + 1, vt.replace('.', '-'))))
    print('%02d  Câu %s' % (i + 1, vt))
for f in anh:
    os.remove(os.path.join(ra, f))
