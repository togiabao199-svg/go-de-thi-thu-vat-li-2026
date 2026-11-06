# -*- coding: utf-8 -*-
"""
GIAI ĐOẠN 1 – TRÍCH XUẤT: đọc đề Word trong kho/, tách từng câu hỏi ra JSON.

Dùng (chạy từ gốc repo):
    python3 tools/tach_cau.py TT01 NC05 TS039 ...      # theo mã đề
    python3 tools/tach_cau.py --tat-ca                 # toàn bộ kho (chỉ chạy khi đã duyệt)
Kết quả: kho/ngan-hang/<tu-soan|truong-so>/<MÃ>.json  (+ báo cáo tóm tắt in ra màn hình)

Mỗi câu trong JSON gồm: id, nguon, kho, de_goc, file_goc, ten_goc, phan, so_cau_goc, loai (TN/DS/TLN),
noi_dung (LaTeX), phuong_an / menh_de, dap_an, nguon_dap_an, loi_giai, hinh (có hình hay không, hình gì),
bang (số bảng trong đề bài), canh_bao.
Trong noi_dung / phuong_an / loi_giai, vị trí hình gốc đánh dấu bằng dòng [[HINH k]] (k là số thứ tự trong
danh sách "hinh" của câu); hình sẽ được vẽ lại bằng TikZ ở giai đoạn soạn đề.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_doc import DocxReader  # noqa: E402
from mtef import join as mjoin  # noqa: E402

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KHO = os.path.join(GOC, 'kho')

MATH = '\uE000'   # ký hiệu giữ chỗ cho công thức trong chuỗi dò mẫu
IMG = '\uE001'    # ký hiệu giữ chỗ cho hình
TBL = '\uE002'    # bảng dữ liệu (đã đổi sang tabular)

TEXT_ESC = {'\\': r'\textbackslash{}', '%': r'\%', '&': r'\&', '#': r'\#', '_': r'\_', '{': r'\{',
            '}': r'\}', '$': r'\$', '^': r'\^{}', '~': r'\~{}', '\u00a0': ' ', '\u200b': '',
            '\u2028': ' ', '\uf0b7': '', '\u2003': ' ', '\u2002': ' '}
CHECKBOX = set('\u2610\u2611\u2612\u25a1\u25a0\u274f\u2713\u2714')


# ====================================================================== nguyên tử của đoạn văn
class Para:
    """Một đoạn văn: dãy nguyên tử (ký tự chữ / công thức / hình) + chuỗi dò mẫu song song."""

    def __init__(self, atoms, src=None):
        self.atoms = atoms
        self.src = src or {}
        self.s = ''.join(a[0] for a in atoms)

    @staticmethod
    def from_block(b):
        atoms = []
        lab = b.get('numlabel') or ''
        for ch in lab:
            atoms.append((ch, {'auto': True}))
        if lab:
            atoms.append((' ', {'auto': True}))
        for it in b['items']:
            t = it['t']
            if t == 'text':
                for ch in it['s']:
                    if ch in CHECKBOX or '\ue000' <= ch <= '\uf8ff':
                        continue
                    atoms.append((ch, it))
            elif t == 'tab':
                atoms.append(('\t', it))
            elif t == 'br':
                atoms.append(('\n', it))
            elif t == 'math':
                s = it.get('s') or ''
                m = re.match(r'^\s*(?:\\text\{\s*)?([A-D])\s*\.\s*\}?\s*(.+)$', s)
                if m and (not atoms or atoms[-1][0] in ' \t') and not re.match(r'^[A-D]\.[A-Z]', s):
                    # nhãn phương án gõ lẫn trong công thức ("A.4.")
                    atoms += [(m.group(1), {}), ('.', {}), (' ', {})]
                    atoms.append((MATH, dict(it, s=m.group(2))))
                else:
                    atoms.append((MATH, it))
            elif t in ('img', 'shape'):
                atoms.append((IMG, it))
            elif t == 'textbox':
                atoms.append((IMG, dict(it, t='shape', desc='text box: ' + it['s'][:80])))
        return Para(atoms, b)

    def sub(self, i, j=None):
        return Para(self.atoms[i:j], self.src)

    def strip(self):
        i, j = 0, len(self.atoms)
        while i < j and self.atoms[i][0] in ' \t\n\u00a0':
            i += 1
        while j > i and self.atoms[j - 1][0] in ' \t\n\u00a0':
            j -= 1
        return self.sub(i, j)

    def is_empty(self):
        return self.s.strip(' \t\n\u00a0') == ''

    def items_of(self, kind):
        return [a[1] for a in self.atoms if a[0] == kind]

    def underlined_at(self, i):
        a = self.atoms[i][1]
        return bool(a.get('u')) if isinstance(a, dict) else False


# ====================================================================== sang LaTeX
DISPLAY_HINT = re.compile(r'\\d?frac|\\int|\\begin|\\lim|\\sum|\\sqrt|\\left')


def esc_text(s):
    return ''.join(TEXT_ESC.get(c, c) for c in s)


def split_punct(lt):
    """tách dấu câu cuối công thức (giữ \\right. và \\, \\;) -> (công thức, dấu câu)"""
    tail = ''
    while True:
        m = re.search(r'([.,;:])\s*$', lt)
        if not m:
            break
        before = lt[:m.start()]
        if before.endswith('\\'):
            break
        if m.group(1) == '.' and re.search(r'\\right\s*$', before):
            break
        tail = m.group(1) + tail
        lt = re.sub(r'(\\\s)+$', '', before).rstrip()
    return lt, tail


def math_inline(lt):
    """$...$ với dấu câu cuối công thức đưa ra ngoài"""
    if lt is None:
        return '$\\text{\\textbf{???}}$', True
    lt, tail = split_punct(lt)
    if not lt.strip():
        return tail, False
    return '$%s$%s' % (lt, tail), False


class Render:
    """Chuyển Para -> LaTeX; gom hình vào danh sách chung của câu."""

    def __init__(self, ctx):
        self.ctx = ctx          # dict câu: chứa 'hinh', 'canh_bao'
        self.where = 'de'
        self.inline_only = False  # phương án, mệnh đề: không dùng \[...\]

    def add_img(self, it, near_text):
        lst = self.ctx['hinh']
        k = len(lst) + 1
        d = {'so': k, 'vi_tri': self.where}
        if it['t'] == 'img':
            d['loai'] = 'anh'
            d['file'] = it.get('name')
            if it.get('w'):
                d['kich_thuoc_cm'] = '%.1fx%.1f' % (it['w'], it['h'])
        else:
            d['loai'] = 'hinh-ve-word'
            d['mo_ta_goc'] = it.get('desc', '')
            if it.get('docpr'):
                d['docpr'] = it['docpr']
            if it.get('label'):
                d['chu_trong_hinh'] = it['label']
            if it.get('w'):
                d['kich_thuoc_cm'] = '%.1fx%.1f' % (it['w'], it['h'])
        d['mo_ta'] = guess_figure(near_text, self.where)
        lst.append(d)
        return k

    def para(self, p, near=''):
        """trả về danh sách dòng LaTeX (đoạn có hình bị tách thành nhiều dòng)"""
        out_lines = []
        cur = []
        atoms = p.atoms
        i = 0
        n = len(atoms)
        text_buf = []
        math_count = 0
        plain_len = 0

        def flush_text():
            if text_buf:
                cur.append(('t', esc_text(''.join(text_buf))))
                text_buf.clear()

        while i < n:
            ch, it = atoms[i]
            if ch == MATH:
                flush_text()
                # gộp các công thức đứng liền nhau
                lts = [it.get('s')]
                warn = list(it.get('warn') or [])
                j = i + 1
                while j < n and atoms[j][0] == MATH:
                    lts.append(atoms[j][1].get('s'))
                    warn += atoms[j][1].get('warn') or []
                    j += 1
                if any(x is None for x in lts):
                    self.ctx['canh_bao'].append('công thức không đọc được (%s)' % it.get('ole'))
                    lt = None
                else:
                    lt = ''
                    for x in lts:
                        lt = mjoin(lt, x)
                for w in warn:
                    if w not in ('công thức rỗng', 'công thức OMML (Word Equation)'):
                        self.ctx['canh_bao'].append('MathType: %s' % w)
                cur.append(('m', lt))
                math_count += 1
                i = j
                continue
            if ch == IMG:
                flush_text()
                if cur:
                    out_lines.append(cur)
                    cur = []
                k = self.add_img(it, near + ' ' + p.s)
                out_lines.append([('img', k)])
                i += 1
                continue
            if ch == TBL:
                flush_text()
                if cur:
                    out_lines.append(cur)
                    cur = []
                out_lines.append([('tbl', it)])
                i += 1
                continue
            if ch == '\t':
                text_buf.append(' ')
            elif ch == '\n':
                flush_text()
                cur.append(('br', None))
            else:
                text_buf.append(ch)
                plain_len += 1
            i += 1
        flush_text()
        if cur:
            out_lines.append(cur)
        res = []
        for line in out_lines:
            res.append(self.line_latex(line))
        return [r for r in res if r.strip()]

    def line_latex(self, parts):
        if len(parts) == 1 and parts[0][0] == 'img':
            return '[[HINH %d]]' % parts[0][1]
        if len(parts) == 1 and parts[0][0] == 'tbl':
            return parts[0][1]
        # công thức đứng riêng một dòng -> \[...\] nếu dài/cao
        txt = [p for p in parts if p[0] == 't' and p[1].strip(' .,;:')]
        maths = [p for p in parts if p[0] == 'm']
        if not txt and len(maths) == 1 and maths[0][1] and not self.inline_only:
            lt = maths[0][1]
            if len(lt) > 45 or DISPLAY_HINT.search(lt):
                return '\\[\n%s\n\\]' % split_punct(lt)[0]
        s = ''
        for kind, v in parts:
            if kind == 't':
                piece = v
                if s.endswith('$') and piece[:1].isalpha():
                    piece = ' ' + piece
                s += piece
            elif kind == 'm':
                piece, _ = math_inline(v)
                if s and (s[-1].isalpha() or s[-1] in ')') and piece.startswith('$'):
                    s += ' '
                elif s.endswith('$') and piece.startswith('$'):
                    s += ' '
                s += piece
            elif kind == 'br':
                s += '\\\\\n'
        s = re.sub(r'[ \t]{2,}', ' ', s).strip()
        return s


def fix_newline_bracket(s):
    """'\\\\' rồi xuống dòng mà dòng sau mở đầu bằng '[' -> LaTeX hiểu nhầm là tham số độ dài: chèn {}"""
    return re.sub(r'(\\\\\s*)\[', r'\1{}[', s)


def join_lines(lines):
    """nối các dòng LaTeX: dòng thường cách nhau bằng \\\\, trừ quanh \\[...\\], bảng, hình"""
    out = ''
    prev_block = True
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        is_block = ln.startswith('\\[') or ln.startswith('[[HINH') or ln.startswith('\\begin{center}') \
            or ln.startswith('\\begin{tabular}')
        if out:
            if is_block or prev_block or out.endswith('\\\\'):
                out += '\n'
            else:
                out += '\\\\\n'
        out += ln
        prev_block = is_block or ln.endswith('\\]') or ln.startswith('[[HINH') or ln.endswith('\\end{center}')
    return out


# ====================================================================== đoán mô tả hình
FIG_RULES = [
    (r'bảng biến thiên', 'bảng biến thiên'),
    (r'bảng xét dấu', 'bảng xét dấu'),
    (r'đồ thị (của )?(hàm số )?(y\s*=\s*)?f\s*\'|đồ thị[^.]{0,20}đạo hàm|f\'\(x\)[^.]{0,40}đồ thị',
     'đồ thị hàm đạo hàm'),
    (r'đồ thị|đường cong|parabol|hypebol', 'đồ thị hàm số'),
    (r'biểu đồ', 'biểu đồ thống kê'),
    (r'hình phẳng|diện tích hình|miền', 'hình phẳng (miền giới hạn bởi các đường)'),
    (r'hình chóp|tứ diện|lăng trụ|hình hộp|lập phương|khối chóp|khối lăng trụ|chóp cụt|kim tự tháp',
     'hình không gian (khối đa diện)'),
    (r'hình nón|hình trụ|mặt cầu|khối cầu|khối nón|khối trụ', 'hình không gian (khối tròn xoay)'),
    (r'Oxyz|hệ trục|hệ tọa độ', 'hình minh họa trong hệ tọa độ'),
    (r'sơ đồ|mạng lưới|con đường|đường đi|bản đồ', 'sơ đồ'),
    (r'tam giác|hình vuông|hình chữ nhật|đường tròn|hình thang|hình thoi', 'hình học phẳng'),
    (r'sơ đồ hình cây|sơ đồ cây', 'sơ đồ hình cây'),
]


def guess_figure(text, where):
    t = text or ''
    for pat, desc in FIG_RULES:
        if re.search(pat, t, re.I):
            return desc + ' (đoán theo ngữ cảnh)'
    return 'hình minh họa (chưa rõ loại, cần xem ảnh gốc)'


# ====================================================================== bảng
def cell_text(cell):
    return ' '.join(Para.from_block(b).s for b in cell if b['kind'] == 'p').strip()


def table_kind(t):
    rows = t['rows']
    if not rows:
        return 'empty'
    texts = [[cell_text(c) for c in r] for r in rows]
    flat = ' '.join(' '.join(r) for r in texts)
    ncol = max(len(r) for r in rows)
    has_img = any(IMG in Para.from_block(b).s for r in rows for c in r for b in c if b['kind'] == 'p')
    has_sub = any(b['kind'] == 'tbl' for r in rows for c in r for b in c)
    # bảng mệnh đề Đúng/Sai
    lab_rows = [r for r in texts if r and re.match(r'^\s*[a-dA-D]\s*[).]', r[0] or (r[1] if len(r) > 1 else ''))]
    if len(lab_rows) >= 3 and ncol >= 3:
        return 'ds'
    if re.search(r'(Mệnh đề|Khẳng định|Phát biểu|Nội dung)', flat) and re.search(r'Đúng', flat) and \
            re.search(r'Sai', flat) and len(rows) >= 4:
        return 'ds'
    # ô trả lời ngắn: 1 hàng, các ô 0-2 ký tự
    if len(rows) == 1 and 2 <= ncol <= 6 and all(len(x.replace(' ', '')) <= 2 for x in texts[0]) and \
            all(re.fullmatch(r'[\d,.\-\s]*', x) for x in texts[0]):
        return 'tln'
    # bảng chứa phương án A. B. C. D. hoặc chứa hình -> bảng bố cục
    if re.search(r'(^|\s)A\s*\.', flat) and re.search(r'(^|\s)B\s*\.', flat) and \
            re.search(r'(^|\s)C\s*\.', flat):
        return 'layout'
    if has_img or has_sub:
        return 'layout'
    if len(rows) == 1 and ncol <= 2 and len(flat) > 60:
        return 'layout'
    if len(rows) == 1 and ncol == 1:
        return 'layout'
    return 'data'


def table_to_latex(t, rnd):
    keep = rnd.inline_only
    rnd.inline_only = True  # trong ô bảng không dùng \[...\]
    try:
        return _table_to_latex(t, rnd)
    finally:
        rnd.inline_only = keep


def _table_to_latex(t, rnd):
    rows = t['rows']
    ncol = max(len(r) for r in rows)
    lines = []
    for r in rows:
        cells = []
        for c in r:
            parts = []
            for b in c:
                if b['kind'] == 'p':
                    parts += rnd.para(Para.from_block(b).strip())
                else:
                    parts.append('[bảng lồng]')
            cells.append(' '.join(x for x in parts if not x.startswith('[[HINH')).replace('\\\\\n', ' '))
        cells += [''] * (ncol - len(cells))
        lines.append(' & '.join(cells) + '\\\\')
    spec = '|' + 'c|' * ncol
    body = '\n\\hline\n'.join(lines)
    return '\\begin{center}\n\\begin{tabular}{%s}\n\\hline\n%s\n\\hline\n\\end{tabular}\n\\end{center}' % (spec, body)


def ds_table(t):
    """-> [(nhãn, ô mệnh đề (list block), đúng?: True/False/None)]"""
    rows = t['rows']
    texts = [[cell_text(c) for c in r] for r in rows]
    # tìm cột Đúng / Sai từ hàng tiêu đề
    col_d = col_s = None
    for r in texts[:2]:
        for k, x in enumerate(r):
            if re.fullmatch(r'\s*Đúng\s*', x, re.I):
                col_d = k
            if re.fullmatch(r'\s*Sai\s*', x, re.I):
                col_s = k
    out = []
    for r, rt in zip(rows, texts):
        if not rt:
            continue
        m = re.match(r'^\s*([a-dA-D])\s*[).]\s*', rt[0])
        if m and len(rt[0].strip()) <= 3 and len(r) >= 2:
            lab, cell = m.group(1).lower(), r[1]
        elif m:
            lab, cell = m.group(1).lower(), r[0]
        else:
            continue
        val = None
        if col_d is not None and col_s is not None and len(rt) > max(col_d, col_s):
            xd = rt[col_d].strip().upper()
            xs = rt[col_s].strip().upper()
            if xd in ('X', 'Đ', '✓', 'x') and not xs:
                val = True
            elif xs in ('X', 'S', '✓') and not xd:
                val = False
        out.append((lab, cell, val, m.group(0) if cell is r[0] else ''))
    return out


def tln_answer(t):
    cells = [cell_text(c).replace(' ', '') for c in t['rows'][0]]
    s = ''.join(cells)
    return s


# ====================================================================== trải phẳng khối
def flatten(blocks):
    """-> danh sách đơn vị: ('p', Para) | ('tbl', bảng, loại)"""
    out = []
    for b in blocks:
        if b['kind'] == 'p':
            out.append(('p', Para.from_block(b)))
        else:
            k = table_kind(b)
            if k == 'layout':
                for r in b['rows']:
                    for c in r:
                        out.extend(flatten(c))
            elif k == 'empty':
                continue
            else:
                out.append(('tbl', b, k))
    return out


# ====================================================================== mẫu nhận diện
RE_PART = re.compile(r'^\s*(PHẦN|Phần|PHÂN)\s*(IV|I{1,3}|[1234])\b\s*[.:\-–]?', re.U)
RE_CAU = re.compile(r'^\s*(Câu|CÂU|Bài)\s*(\d{1,2})\s*[.:)]?\s*')
RE_LG = re.compile(r'^\s*(Lời giải|LỜI GIẢI|Hướng dẫn giải|HƯỚNG DẪN GIẢI|Hướng dẫn|Giải)\s*[:.]?\s*', re.U)
RE_TRALOI = re.compile(r'^\s*(Trả lời|Đáp số|Đáp án|ĐÁP ÁN|Kết quả)\s*[:.]\s*', re.U)
RE_END = re.compile(r'^\s*(-+\s*)?(HẾT|Hết|BẢNG ĐÁP ÁN|ĐÁP ÁN THAM KHẢO|PHẦN ĐÁP ÁN)\b')
RE_OPT = re.compile(r'(?:^|(?<=[\s\t]))([A-D])\s*[.)](?=\s|' + MATH + '|' + IMG + '|$|\\S)')
RE_STMT = re.compile(r'^\s*([a-d])\s*\)\s*')
RE_CHON = re.compile(r'^\s*(Chọn|Đáp án)\s*:?\s*([A-D])\s*\.?\s*$')
ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, '1': 1, '2': 2, '3': 3, '4': 4}


PART_KW = re.compile(r'trắc nghiệm|đúng\s*[-/]?\s*sai|trả lời ngắn|tự luận|câu hỏi|nhiều phương án|thí sinh', re.I)


def part_of(p):
    """tiêu đề phần -> loại phần: 1 TN, 2 Đúng/Sai, 3 trả lời ngắn, 4 tự luận (theo từ khóa, rồi mới theo số)"""
    m = RE_PART.match(p.s)
    if not m:
        return None
    rest = p.s[m.end():]
    # "Phần 1 (từ x=0 ...)" trong lời giải không phải tiêu đề phần
    if not re.match(r'\s*[.:\-–]', p.s[m.end(2):]) and not PART_KW.search(rest[:80]) and rest.strip():
        return None
    if not PART_KW.search(rest[:120]) and rest.strip():
        return None
    low = rest[:150].lower()
    if 'tự luận' in low:
        return 4
    if 'trả lời ngắn' in low:
        return 3
    if re.search(r'đúng\s*[-/]?\s*sai', low):
        return 2
    if 'trắc nghiệm' in low or 'nhiều phương án' in low:
        return 1
    return ROMAN[m.group(2)]


# ====================================================================== tách câu
def segment(units):
    """-> danh sách câu thô: {'phan', 'so', 'de': [đv], 'giai': [đv], 'traloi': [đv]}"""
    qs = []
    part = 0
    cur = None
    phase = None
    ended = False
    for u in units:
        if u[0] == 'p':
            p = u[1]
            s = p.s
            pp = part_of(p)
            if pp and len(s) < 400 and not RE_CAU.match(s):
                part = pp
                cur = None
                ended = False
                continue
            if RE_END.match(s) and len(s) < 80:
                cur = None
                ended = True
                continue
            m = RE_CAU.match(s)
            if m and part:
                ended = False
                cur = {'phan': part, 'so': int(m.group(2)), 'de': [], 'giai': [], 'traloi': []}
                qs.append(cur)
                phase = 'de'
                rest = p.sub(m.end()).strip()
                if not rest.is_empty():
                    cur['de'].append(('p', rest))
                continue
            if cur is None or ended:
                continue
            # "Lời giải" (có thể đứng sau một hình/khoảng trắng ở đầu đoạn)
            lead = len(s) - len(s.lstrip(' \t\u00a0' + IMG))
            s2 = s[lead:]
            m = RE_LG.match(s2)
            if m and (len(s2.strip()) <= 20 or s2.strip().startswith(('Lời giải', 'LỜI GIẢI'))):
                phase = 'giai'
                if lead and p.items_of(IMG):
                    cur['giai'].append(('p', p.sub(0, lead)))
                rest = p.sub(lead + m.end()).strip()
                if not rest.is_empty():
                    cur['giai'].append(('p', rest))
                continue
            m = RE_TRALOI.match(s)
            if m and phase == 'de':
                rest = p.sub(m.end()).strip()
                if not rest.is_empty():
                    cur['traloi'].append(('p', rest))
                phase = 'traloi'
                continue
            if p.is_empty() and not p.items_of(IMG):
                continue
            if phase == 'traloi':
                phase = 'de'
            cur[phase if phase != 'traloi' else 'de'].append(u)
        else:
            if cur is None or ended:
                continue
            if u[2] == 'tln' and phase in ('de', 'traloi'):
                cur['traloi'].append(u)
                phase = 'de'
                continue
            cur['giai' if phase == 'giai' else 'de'].append(u)
    return qs


# ====================================================================== dựng câu hoàn chỉnh
def render_units(units, rnd, near=''):
    return fix_newline_bracket(_render_units(units, rnd, near))


def _render_units(units, rnd, near=''):
    lines = []
    ctx_text = near
    for u in units:
        if u[0] == 'p':
            lines += rnd.para(u[1], ctx_text)
            ctx_text = (ctx_text + ' ' + u[1].s)[-300:]
        else:
            lines.append(table_to_latex(u[1], rnd))
            rnd.ctx['bang_' + rnd.where] = rnd.ctx.get('bang_' + rnd.where, 0) + 1
    return join_lines(lines)


def split_options(units):
    """tìm A. B. C. D. trong phần đề -> (đơn vị thân đề, [4 danh sách đơn vị], chữ cái gạch chân)"""
    # tìm đoạn đầu tiên bắt đầu bằng "A."
    start = None
    for k, u in enumerate(units):
        if u[0] == 'p':
            m = re.match(r'^[\s\t]*A\s*[.)]', u[1].s)
            if m:
                start = k
                break
            # "A." nằm giữa đoạn (sau tab) khi thân đề cùng dòng
            m = re.search(r'\tA\s*\.\s', u[1].s)
            if m and re.search(r'\tB\s*\.', u[1].s):
                start = k
                break
    if start is None:
        return units, None, None
    stem = list(units[:start])
    opts = {}
    order = []
    under = None
    curk = None
    first = units[start][1]
    m0 = re.match(r'^[\s\t]*A\s*[.)]', first.s)
    if not m0:
        i0 = first.s.index('\tA')
        stem.append(('p', first.sub(0, i0)))
    for u in units[start:]:
        if u[0] != 'p':
            if curk:
                opts[curk].append(u)
            continue
        p = u[1]
        marks = []
        for m in RE_OPT.finditer(p.s):
            L = m.group(1)
            expect = 'ABCD'[len(order) + len(marks)] if len(order) + len(marks) < 4 else None
            if L == expect:
                # chữ cái phải đứng đầu dòng hoặc sau tab/khoảng trắng
                if m.start(1) == 0 or p.s[m.start(1) - 1] in ' \t\u00a0':
                    marks.append((L, m.start(1), m.end()))
        if not marks:
            if curk:
                opts[curk].append(u)
            continue
        # phần trước nhãn đầu tiên thuộc phương án trước
        if curk and marks[0][1] > 0:
            pre = p.sub(0, marks[0][1]).strip()
            if not pre.is_empty():
                opts[curk].append(('p', pre))
        for idx, (L, a, b) in enumerate(marks):
            e = marks[idx + 1][1] if idx + 1 < len(marks) else len(p.atoms)
            body = p.sub(b, e).strip()
            opts[L] = [('p', body)] if not body.is_empty() else []
            order.append(L)
            curk = L
            if p.underlined_at(a):
                under = L
        if len(order) >= 4 and False:
            break
    if len(order) != 4:
        return units, None, None
    return stem, [opts[L] for L in 'ABCD'], under


def split_statements(units):
    """tìm a) b) c) d) trong phần đề (bảng mệnh đề hoặc đoạn văn)."""
    for k, u in enumerate(units):
        if u[0] == 'tbl' and u[2] == 'ds':
            rows = ds_table(u[1])
            if len(rows) >= 4:
                stmts = []
                vals = []
                for lab, cell, val, pref in rows[:4]:
                    us = []
                    for b in cell:
                        if b['kind'] == 'p':
                            p = Para.from_block(b)
                            if pref:
                                m = RE_STMT.match(p.s)
                                if m:
                                    p = p.sub(m.end())
                            us.append(('p', p.strip()))
                        else:
                            us.append(('tbl', b, table_kind(b)))
                    stmts.append(us)
                    vals.append(val)
                stem = units[:k]
                after = units[k + 1:]
                return stem + after, stmts, vals
    # đoạn văn a) ... b) ...
    idx = []
    for k, u in enumerate(units):
        if u[0] == 'p':
            m = RE_STMT.match(u[1].s)
            if m and m.group(1) == 'abcd'[len(idx)] if len(idx) < 4 else False:
                idx.append((k, m.end()))
    if len(idx) == 4:
        stem = units[:idx[0][0]]
        stmts = []
        for n, (k, e) in enumerate(idx):
            nxt = idx[n + 1][0] if n + 1 < 4 else len(units)
            us = [('p', units[k][1].sub(e).strip())] + list(units[k + 1:nxt])
            stmts.append(us)
        return stem, stmts, [None] * 4
    return units, None, None


RE_XET = re.compile(r'^\s*(?:Xét\s+)?(?:m\S{0,5}\s+đề|ý|câu|khẳng định)?\s*([a-d])\s*\)\s*[:.]?\s*', re.I)
RE_VERDICT_HEAD = re.compile(r'^\s*(Đúng|Sai)\b\s*[.:]?\s*', re.I)
RE_CONCL = re.compile(r'^\s*(?:Do đó|Vậy|Suy ra|Nên)?\s*,?\s*(?:mệnh đề|ý|khẳng định)\s*[a-d]\s*\)\s*(?:là\s+)?'
                      r'(?:đúng|sai)\s*\.?\s*$', re.I)
RE_VERDICT_TAIL = re.compile(r'(?:mệnh đề|ý|khẳng định|phát biểu)\s*([a-d])\s*\)?\s*(là\s+)?(đúng|sai)', re.I)


def split_ds_solution(units):
    """lời giải Đúng/Sai -> (phần chung, [4 danh sách đơn vị], [4 kết luận])"""
    # ứng viên nhãn ý; dòng kết luận kiểu "Mệnh đề b) sai." / "Do đó mệnh đề a) đúng." không phải nhãn
    cands = []
    for k, u in enumerate(units):
        if u[0] != 'p':
            continue
        m = RE_XET.match(u[1].s)
        if m:
            concl = bool(RE_CONCL.match(u[1].s))
            cands.append((k, 'abcd'.index(m.group(1).lower()), m.end(), concl))

    def pick(cs):
        found = {}
        last = -1
        for k, L, e, _c in cs:
            if L > last and L not in found:
                found[L] = (k, e)
                last = L
        return found
    found = pick([c for c in cands if not c[3]])
    if len(found) < 3:
        found = pick(cands)
    if len(found) < 3:
        return units, None, [None] * 4
    # thiếu nhãn một ý (vd gõ sai "Xét mện đề d)"): ý đó để trống, ghi cảnh báo ở bước sau
    idx = [found.get(L) for L in range(4)]
    if None in idx:
        return split_ds_partial(units, idx)
    common = units[:idx[0][0]]
    parts = []
    verdicts = []
    for n, (k, e) in enumerate(idx):
        nxt = idx[n + 1][0] if n + 1 < 4 else len(units)
        first = units[k][1].sub(e).strip()
        v = None
        m = RE_VERDICT_HEAD.match(first.s)
        if m:
            v = m.group(1).lower() == 'đúng'
            first = first.sub(m.end()).strip()
        us = ([('p', first)] if not first.is_empty() else []) + list(units[k + 1:nxt])
        if v is None:
            alltxt = ' '.join(x[1].s for x in us if x[0] == 'p')
            ms = list(RE_VERDICT_TAIL.finditer(alltxt))
            for mm in ms:
                if mm.group(1).lower() == 'abcd'[n]:
                    v = mm.group(3).lower() == 'đúng'
            if v is None:
                m2 = re.search(r'\b(Đúng|Sai)\s*\.?\s*$', alltxt.strip())
                if m2:
                    v = m2.group(1) == 'Đúng'
        parts.append(us)
        verdicts.append(v)
    return common, parts, verdicts


def split_ds_partial(units, idx):
    present = [(L, v) for L, v in enumerate(idx) if v is not None]
    common = units[:present[0][1][0]]
    parts = [[] for _ in range(4)]
    verdicts = [None] * 4
    for n, (L, (k, e)) in enumerate(present):
        nxt = present[n + 1][1][0] if n + 1 < len(present) else len(units)
        first = units[k][1].sub(e).strip()
        us = ([('p', first)] if not first.is_empty() else []) + list(units[k + 1:nxt])
        alltxt = ' '.join(x[1].s for x in us if x[0] == 'p')
        for mm in RE_VERDICT_TAIL.finditer(alltxt):
            if mm.group(1).lower() == 'abcd'[L]:
                verdicts[L] = mm.group(3).lower() == 'đúng'
        parts[L] = us
    return common, parts, verdicts


def clean_solution_units(units):
    """bỏ dòng 'Chọn A' trong lời giải, trả về (đơn vị, chữ cái chọn)"""
    out = []
    chon = None
    for u in units:
        if u[0] == 'p':
            m = RE_CHON.match(u[1].s)
            if m:
                chon = m.group(2)
                continue
        out.append(u)
    return out, chon


def _norm_math(s):
    s = re.sub(r'\\[dt]?frac', 'frac', s)
    s = re.sub(r'\\left|\\right|\\displaystyle|\\limits|\\,|\s|\$|[{}]', '', s)
    return s


def infer_answer(opts, lg):
    """phương án duy nhất có công thức xuất hiện trong 2 dòng cuối lời giải (ưu tiên) hoặc cả lời giải"""
    if not lg or len(opts) != 4:
        return None
    no = [_norm_math(o) for o in opts]
    if any(len(x) < 1 for x in no) or len(set(no)) < 4:
        return None
    # các phương án cùng vế trái ("P=..."): so vế phải, yêu cầu đứng sau dấu =
    lhs = [x.split('=', 1)[0] for x in no]
    if all('=' in x for x in no) and len(set(lhs)) == 1:
        no = ['=' + x.split('=', 1)[1] for x in no]
    lines = [x for x in lg.split('\n') if x.strip()]
    for scope in ('\n'.join(lines[-2:]), lg):
        ns = _norm_math(scope)
        hit = [k for k, x in enumerate(no) if x in ns]
        # tránh phương án là chuỗi con của phương án khác (vd 2 và 12)
        hit = [k for k in hit if not any(k != j and no[k] in no[j] and no[j] in ns for j in hit)]
        if len(hit) == 1 and len(no[hit[0]]) >= 1:
            # phương án quá ngắn (một chữ số) chỉ chấp nhận khi đứng sau dấu = ở kết luận
            x = no[hit[0]]
            if len(x) <= 2 and not re.search(r'(=|là|bằng)' + re.escape(x) + r'(?![\d])', ns):
                continue
            return 'ABCD'[hit[0]]
    return None


def normalize_tln(s):
    s = s.strip().replace('.', ',')
    s = re.sub(r'\s', '', s)
    return s


def build_question(raw, meta, qid):
    q = {'id': qid}
    q.update(meta)
    q['phan'] = raw['phan']
    q['so_cau_goc'] = raw['so']
    q['loai'] = {1: 'TN', 2: 'DS', 3: 'TLN', 4: 'TL'}[raw['phan']]
    q['hinh'] = []
    q['canh_bao'] = []
    rnd = Render(q)
    de = raw['de']
    giai, chon = clean_solution_units(raw['giai'])
    if q['loai'] == 'TN':
        stem, opts, under = split_options(de)
        rnd.where = 'de'
        q['noi_dung'] = render_units(stem, rnd)
        if opts is None:
            q['canh_bao'].append('không tách được 4 phương án A, B, C, D')
            q['phuong_an'] = []
        else:
            rnd.where = 'phuong-an'
            rnd.inline_only = True
            q['phuong_an'] = [render_units(o, rnd, q['noi_dung'][-200:]) for o in opts]
            rnd.inline_only = False
            q['phuong_an'] = [re.sub(r'\s*[.;,]\s*$', '', x) for x in q['phuong_an']]
        ans = under
        src = 'gạch chân chữ cái phương án'
        if chon and under and chon != under:
            q['canh_bao'].append('đáp án gạch chân %s khác dòng "Chọn %s"' % (under, chon))
        if not ans and chon:
            ans, src = chon, 'dòng "Chọn" trong lời giải'
        lg_tmp = None
        if not ans and opts is not None:
            rnd.where = 'loi-giai'
            lg_tmp = render_units(giai, rnd)
            ans = infer_answer(q['phuong_an'], lg_tmp)
            if ans:
                src = 'suy từ lời giải (phương án xuất hiện ở kết luận)'
                q['canh_bao'].append('bản gốc không gạch chân đáp án; đáp án %s suy từ lời giải, cần kiểm' % ans)
        q['dap_an'] = ans
        q['nguon_dap_an'] = src if ans else None
        if not ans:
            q['canh_bao'].append('không tìm thấy đáp án')
        if lg_tmp is not None:
            # đã dựng lời giải (và đánh số hình) ở trên
            q['loi_giai'] = lg_tmp
        else:
            rnd.where = 'loi-giai'
            q['loi_giai'] = render_units(giai, rnd)
    elif q['loai'] == 'DS':
        stem, stmts, vals = split_statements(de)
        rnd.where = 'de'
        q['noi_dung'] = render_units(stem, rnd)
        if stmts is None:
            q['canh_bao'].append('không tách được 4 mệnh đề a), b), c), d)')
            q['menh_de'] = []
            vals = [None] * 4
        else:
            rnd.where = 'menh-de'
            rnd.inline_only = True
            q['menh_de'] = [re.sub(r'\s*[.;,]\s*$', '', render_units(s, rnd)) for s in stmts]
            rnd.inline_only = False
        common, parts, verdicts = split_ds_solution(giai)
        if None in verdicts:
            # kết luận nằm lẫn sang ý khác (vd thiếu dòng "Xét mệnh đề d)"): tìm trong toàn lời giải
            alltxt = ' '.join(x[1].s for x in giai if x[0] == 'p')
            for mm in RE_VERDICT_TAIL.finditer(alltxt):
                L = 'abcd'.index(mm.group(1).lower())
                if verdicts[L] is None:
                    verdicts[L] = mm.group(3).lower() == 'đúng'
                    if parts and not parts[L]:
                        q['canh_bao'].append('lời giải ý %s nằm lẫn trong ý khác (bản gốc thiếu nhãn)' % 'abcd'[L])
        rnd.where = 'loi-giai'
        lg = {'chung': render_units(common, rnd)}
        if parts:
            lg['y'] = [render_units(pu, rnd) for pu in parts]
        else:
            q['canh_bao'].append('không tách được lời giải theo từng ý a), b), c), d)')
            lg['y'] = []
        q['loi_giai'] = lg
        ans = []
        srcs = set()
        for k in range(4):
            v_tab = vals[k] if vals else None
            v_lg = verdicts[k]
            if v_tab is not None and v_lg is not None and v_tab != v_lg:
                q['canh_bao'].append('ý %s: bảng đánh dấu %s nhưng lời giải kết luận %s' % (
                    'abcd'[k], 'Đúng' if v_tab else 'Sai', 'Đúng' if v_lg else 'Sai'))
            v = v_tab if v_tab is not None else v_lg
            if v_tab is not None:
                srcs.add('bảng đánh dấu X')
            elif v_lg is not None:
                srcs.add('kết luận trong lời giải')
            ans.append(None if v is None else ('Đ' if v else 'S'))
        q['dap_an'] = ans
        q['nguon_dap_an'] = ', '.join(sorted(srcs)) or None
        if None in ans:
            q['canh_bao'].append('thiếu kết luận Đúng/Sai ở ý ' + ', '.join(
                'abcd'[k] for k in range(4) if ans[k] is None))
    elif q['loai'] == 'TL':
        rnd.where = 'de'
        q['noi_dung'] = render_units(de, rnd)
        q['dap_an'] = None
        q['nguon_dap_an'] = None
        rnd.where = 'loi-giai'
        q['loi_giai'] = render_units(giai, rnd)
        q['canh_bao'].append('câu tự luận (Phần 4), ngoài cấu trúc đề TN THPT')
    else:
        rnd.where = 'de'
        q['noi_dung'] = render_units(de, rnd)
        ans = None
        for u in raw['traloi']:
            if u[0] == 'tbl':
                ans = normalize_tln(tln_answer(u[1])) or None
            elif u[0] == 'p' and ans is None:
                t = u[1].s.replace(MATH, '')
                maths = [x.get('s') for x in u[1].items_of(MATH)]
                cand = (t + ''.join(m or '' for m in maths)).strip()
                cand = cand.replace('{,}', ',')
                if re.fullmatch(r'-?[\d.,]+', cand.strip(' .')):
                    ans = normalize_tln(cand.strip(' .'))
        q['dap_an'] = ans
        q['nguon_dap_an'] = 'ô trả lời trong đề' if ans else None
        if not ans:
            q['canh_bao'].append('không tìm thấy đáp án trả lời ngắn')
        elif len(ans) > 4:
            q['canh_bao'].append('đáp án "%s" dài quá 4 ký tự' % ans)
        rnd.where = 'loi-giai'
        q['loi_giai'] = render_units(giai, rnd)
    if not giai:
        q['canh_bao'].append('không có lời giải gốc')
    q['co_hinh'] = bool(q['hinh'])
    q['co_hinh_de'] = any(h['vi_tri'] != 'loi-giai' for h in q['hinh'])
    q['bang'] = q.pop('bang_de', 0) + q.pop('bang_phuong-an', 0) + q.pop('bang_menh-de', 0)
    q.pop('bang_loi-giai', None)
    # gom cảnh báo trùng
    seen = []
    for w in q['canh_bao']:
        if w not in seen:
            seen.append(w)
    q['canh_bao'] = seen
    order = ['id', 'nguon', 'kho', 'de_goc', 'file_goc', 'ten_goc', 'phan', 'so_cau_goc', 'loai', 'noi_dung',
             'phuong_an', 'menh_de', 'dap_an', 'nguon_dap_an', 'loi_giai', 'loi_giai_pdf', 'co_hinh', 'co_hinh_de',
             'hinh', 'bang', 'canh_bao']
    return {k: q[k] for k in order if k in q}


# ====================================================================== danh sách đề
PDF_DAP_AN = {}  # mã đề -> PDF đáp án (khi file Word đáp án hỏng, vd TT32)
GHI_CHU = {'TS161': 'Cùng một đề với TS162 (Sở GD&ĐT Cần Thơ, chia 2 file). Giữ hai file riêng vì mỗi file '
                    'đánh số câu riêng, đủ Phần 1-4 (có tự luận).',
           'TS162': 'Cùng một đề với TS161 (Sở GD&ĐT Cần Thơ, chia 2 file). Giữ hai file riêng vì mỗi file '
                    'đánh số câu riêng, đủ Phần 1-4 (có tự luận).'}


def merge_pdf(qs, pdf):
    """bổ sung đáp án, lời giải từ PDF đáp án (TT32)"""
    from pdf_dap_an import parse
    info = parse(pdf)
    rel = os.path.relpath(pdf, GOC)
    drop = ('không có lời giải gốc', 'không tìm thấy đáp án', 'không tìm thấy đáp án trả lời ngắn',
            'không tách được lời giải theo từng ý a), b), c), d)')
    for q in qs:
        r = info.get((q['phan'], q['so_cau_goc']))
        if not r:
            q['canh_bao'].append('không thấy câu này trong PDF đáp án')
            continue
        q['canh_bao'] = [w for w in q['canh_bao'] if w not in drop and not w.startswith('thiếu kết luận')]
        if q['loai'] == 'DS':
            old = q.get('dap_an') or [None] * 4
            q['dap_an'] = [o or n for o, n in zip(old, r['dap_an'])]
            if None in q['dap_an']:
                q['canh_bao'].append('PDF đáp án thiếu kết luận ý ' + ', '.join(
                    'abcd'[k] for k in range(4) if q['dap_an'][k] is None))
            q['loi_giai'] = {'chung': '', 'y': []}
        else:
            if not q.get('dap_an'):
                q['dap_an'] = r['dap_an']
            if not q['dap_an']:
                q['canh_bao'].append('PDF đáp án không có đáp án đọc được')
            q['loi_giai'] = ''
        q['nguon_dap_an'] = 'PDF đáp án %s (%s)' % (rel, {1: 'gạch chân', 2: 'kết luận trong lời giải',
                                                          3: 'ô trả lời'}.get(q['phan'], ''))
        q['loi_giai_pdf'] = r['loi_giai_pdf']
        q['canh_bao'].append('lời giải chỉ có trong PDF (văn bản thô, công thức mất cấu trúc), cần gõ lại')


def load_list():
    """mã đề -> (đường dẫn docx, nguồn, kho, tên gốc)"""
    res = {}
    ds = os.path.join(KHO, 'de-tu-soan', 'DANH-SACH.md')
    if os.path.exists(ds):
        for line in open(ds, encoding='utf8'):
            m = re.match(r'\|\s*(TT\d+\w*|NC\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|', line)
            if m:
                ma = m.group(1).strip()
                parts = [x.strip() for x in m.group(2).strip().split(' + ')]
                rel = parts[0]
                sub = 'thi-thu' if ma.startswith('TT') else ''
                path = os.path.join(KHO, 'de-tu-soan', rel if '/' in rel else os.path.join(sub, rel))
                for extra in parts[1:]:
                    if extra.endswith('.pdf'):
                        PDF_DAP_AN[ma] = os.path.join(os.path.dirname(path), os.path.basename(extra))
                goc = m.group(3).strip().split('/')
                ten = ' -- '.join(goc[:2]) if len(goc) >= 2 else goc[0]
                if ma == 'TT30plus':
                    ten += ' (plus)'
                res[ma] = (path, 'tu-soan', ma[:2], ten)
    ds = os.path.join(KHO, 'de-truong-so', 'DANH-SACH.md')
    if os.path.exists(ds):
        for line in open(ds, encoding='utf8'):
            m = re.match(r'\|\s*(TS\d+)\s*\|\s*([^|]+)\|\s*([^|]*)\|', line)
            if m:
                ma = m.group(1).strip()
                res[ma] = (os.path.join(KHO, 'de-truong-so', ma + '.docx'), 'truong-so', 'TS',
                           m.group(2).strip().replace('.docx', ''))
    return res


def extract(ma, info):
    path, nguon, kho, ten = info
    rd = DocxReader(path)
    blocks = rd.read()
    units = flatten(blocks)
    raws = segment(units)
    meta = {'nguon': nguon, 'kho': kho, 'de_goc': ma,
            'file_goc': os.path.relpath(path, GOC), 'ten_goc': ten}
    qs = []
    seen = {}
    for r in raws:
        tag = {1: 'I', 2: 'II', 3: 'III', 4: 'IV'}[r['phan']]
        base = '%s-%s-%02d' % (ma, tag, r['so'])
        seen[base] = seen.get(base, 0) + 1
        qid = base if seen[base] == 1 else '%s-%d' % (base, seen[base])
        qs.append(build_question(r, meta, qid))
    if ma in PDF_DAP_AN:
        merge_pdf(qs, PDF_DAP_AN[ma])
    if DUNG_HINH:
        ids = [h['docpr'] for q in qs for h in q['hinh'] if h['loai'] == 'hinh-ve-word' and h.get('docpr')]
        if ids:
            from hinh_word import render
            got = render(path, ma, ids)
            for q in qs:
                for h in q['hinh']:
                    g = got.get(h.get('docpr'))
                    if h['loai'] != 'hinh-ve-word':
                        continue
                    if g:
                        h['anh_dung'] = g['anh']
                        h['trang_goc'] = g['trang']
                        h['anh_trang'] = g['anh_trang']
                    else:
                        q['canh_bao'].append('không dựng được ảnh cho hình vẽ bằng shape Word')
    rep = {'de_goc': ma, 'file_goc': meta['file_goc'], 'ten_goc': ten,
           'so_cau': {'TN': sum(q['loai'] == 'TN' for q in qs), 'DS': sum(q['loai'] == 'DS' for q in qs),
                      'TLN': sum(q['loai'] == 'TLN' for q in qs), 'TL': sum(q['loai'] == 'TL' for q in qs)},
           'cong_thuc': rd.stats['math'], 'cong_thuc_loi': rd.stats['math_fail'],
           'hinh': sum(len(q['hinh']) for q in qs),
           'cau_co_canh_bao': sum(1 for q in qs if q['canh_bao'])}
    if ma in PDF_DAP_AN:
        rep['file_dap_an_pdf'] = os.path.relpath(PDF_DAP_AN[ma], GOC)
    if ma in GHI_CHU:
        rep['ghi_chu'] = GHI_CHU[ma]
    return {'thong_tin': rep, 'cau': qs}


DUNG_HINH = True  # dựng ảnh đối chiếu cho hình vẽ bằng shape Word (cần LibreOffice)


def main(argv):
    global DUNG_HINH
    if '--khong-dung-hinh' in argv:
        DUNG_HINH = False
    lst = load_list()
    if '--tat-ca' in argv:
        mas = sorted(lst)
    else:
        mas = [a for a in argv if not a.startswith('-')]
    for ma in mas:
        if ma not in lst:
            print('Không thấy mã đề', ma)
            continue
        res = extract(ma, lst[ma])
        sub = lst[ma][1]
        od = os.path.join(KHO, 'ngan-hang', sub)
        os.makedirs(od, exist_ok=True)
        with open(os.path.join(od, ma + '.json'), 'w', encoding='utf8') as f:
            json.dump(res, f, ensure_ascii=False, indent=1)
        t = res['thong_tin']
        print('%-9s TN %2d  DS %d  TLN %d | công thức %4d (lỗi %d) | hình %2d | câu có cảnh báo %d' % (
            ma, t['so_cau']['TN'], t['so_cau']['DS'], t['so_cau']['TLN'], t['cong_thuc'], t['cong_thuc_loi'],
            t['hinh'], t['cau_co_canh_bao']))


if __name__ == '__main__':
    main(sys.argv[1:])
