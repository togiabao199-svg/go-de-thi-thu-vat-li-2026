# -*- coding: utf-8 -*-
"""
Giải mã công thức MathType (OLE "Equation.DSMT4", định dạng MTEF v5) ra mã LaTeX.

Dùng:
    from mtef import ole_to_latex
    latex, canhbao = ole_to_latex(du_lieu_oleObject_bin)

Kết quả theo quy chuẩn ký hiệu của CLAUDE.md (\\dfrac, \\overrightarrow, \\leq, {,} cho số
thập phân, \\displaystyle\\int\\limits, \\left\\{\\begin{aligned}...\\end{aligned}\\right. ...).
Các ký tự chưa biết được ghi vào danh sách cảnh báo để soát lại.
"""
import io
import re
import struct

import olefile

# ---------------------------------------------------------------- bảng ký hiệu
SYM = {
    0x2212: '-', 0x2013: '-', 0x2014: '-', 0x00B1: r'\pm', 0x2213: r'\mp',
    0x00D7: r'\times', 0x00F7: r'\div', 0x22C5: r'\cdot', 0x00B7: r'\cdot', 0x2219: r'\cdot',
    0x2022: r'\cdot', 0x2217: '*',
    0x2264: r'\leq', 0x2265: r'\geq', 0x2260: r'\neq', 0x2248: r'\approx', 0x2261: r'\equiv',
    0x2A7D: r'\leq', 0x2A7E: r'\geq', 0x226A: r'\ll', 0x226B: r'\gg',
    0x2245: r'\cong', 0x223C: r'\sim', 0x2243: r'\simeq', 0x221D: r'\propto', 0x2250: r'\doteq',
    0x221E: r'\infty', 0x2202: r'\partial', 0x2207: r'\nabla',
    0x2192: r'\to', 0x2190: r'\leftarrow', 0x2194: r'\leftrightarrow', 0x2191: r'\uparrow',
    0x2193: r'\downarrow', 0x21D2: r'\Rightarrow', 0x21D0: r'\Leftarrow', 0x21D4: r'\Leftrightarrow',
    0x27F9: r'\Rightarrow', 0x27FA: r'\Leftrightarrow', 0x27F6: r'\to', 0x21A6: r'\mapsto',
    0x21C4: r'\rightleftarrows', 0x2197: r'\nearrow', 0x2198: r'\searrow',
    0x2208: r'\in', 0x2209: r'\notin', 0x220B: r'\ni', 0x2282: r'\subset', 0x2283: r'\supset',
    0x2286: r'\subseteq', 0x2287: r'\supseteq', 0x2284: r'\not\subset', 0x222A: r'\cup',
    0x2229: r'\cap', 0x2205: r'\varnothing', 0x2200: r'\forall', 0x2203: r'\exists', 0x2204: r'\nexists',
    0x2216: r'\setminus', 0x00AC: r'\neg', 0x2227: r'\wedge', 0x2228: r'\vee',
    0x22A5: r'\perp', 0x27C2: r'\perp', 0x2225: r'\parallel', 0x2226: r'\nparallel', 0x2220: r'\angle',
    0x2221: r'\measuredangle', 0x25B3: r'\triangle', 0x2206: r'\triangle', 0x25B5: r'\triangle',
    0x2218: r'\circ', 0x25CB: r'\circ', 0x2299: r'\odot', 0x2295: r'\oplus',
    0x2032: "'", 0x2033: "''", 0x2034: "'''", 0x00B4: "'", 0x2019: "'",
    0x2026: r'\ldots', 0x22EF: r'\cdots', 0x22EE: r'\vdots', 0x22F1: r'\ddots',
    0x2211: r'\sum', 0x220F: r'\prod', 0x2210: r'\coprod', 0x222B: r'\int', 0x222C: r'\iint',
    0x222D: r'\iiint', 0x222E: r'\oint', 0x22C3: r'\bigcup', 0x22C2: r'\bigcap',
    0x221A: r'\surd', 0x2223: r'\mid', 0x2016: r'\|', 0x2224: r'\nmid',
    0x211D: r'\mathbb{R}', 0x2115: r'\mathbb{N}', 0x2124: r'\mathbb{Z}', 0x211A: r'\mathbb{Q}',
    0x2102: r'\mathbb{C}', 0x2113: r'\ell', 0x210F: r'\hbar', 0x2135: r'\aleph',
    0x00B0: r'^\circ', 0x2103: r'^\circ\mathrm{C}', 0x2030: r'\textperthousand', 0x0025: r'\%',
    0x27E8: r'\langle', 0x27E9: r'\rangle', 0x2329: r'\langle', 0x232A: r'\rangle',
    0x230A: r'\lfloor', 0x230B: r'\rfloor', 0x2308: r'\lceil', 0x2309: r'\rceil',
    0x2234: r'\therefore', 0x2235: r'\because', 0x22A2: r'\vdash', 0x2201: r'\complement',
    0x2223 + 0x10000: r'\mid',
    0x00A0: '~', 0x2009: r'\,', 0x200A: r'\,', 0x2002: r'\ ', 0x2003: r'\quad', 0x2005: r'\;',
    0x200B: '', 0x2061: '', 0x2062: '', 0x2063: '',
    0x002A: '*', 0x2288: r'\nsubseteq', 0x2289: r'\nsupseteq', 0x210B: r'\mathcal{H}',
    0x2322: r'\frown', 0x2323: r'\smile', 0x223D: r'\backsim', 0x22C6: r'\star',
    0x2112: r'\mathcal{L}', 0x2131: r'\mathcal{F}', 0x2133: r'\mathcal{M}', 0x212C: r'\mathcal{B}',
}
GREEK = {
    0x03B1: 'alpha', 0x03B2: 'beta', 0x03B3: 'gamma', 0x03B4: 'delta', 0x03B5: 'varepsilon',
    0x03F5: 'epsilon', 0x03B6: 'zeta', 0x03B7: 'eta', 0x03B8: 'theta', 0x03D1: 'vartheta',
    0x03B9: 'iota', 0x03BA: 'kappa', 0x03BB: 'lambda', 0x03BC: 'mu', 0x03BD: 'nu', 0x03BE: 'xi',
    0x03BF: 'o', 0x03C0: 'pi', 0x03D6: 'varpi', 0x03C1: 'rho', 0x03F1: 'varrho', 0x03C3: 'sigma',
    0x03C2: 'varsigma', 0x03C4: 'tau', 0x03C5: 'upsilon', 0x03C6: 'varphi', 0x03D5: 'phi',
    0x03C7: 'chi', 0x03C8: 'psi', 0x03C9: 'omega',
    0x0393: 'Gamma', 0x0394: 'Delta', 0x0398: 'Theta', 0x039B: 'Lambda', 0x039E: 'Xi',
    0x03A0: 'Pi', 0x03A3: 'Sigma', 0x03A5: 'Upsilon', 0x03A6: 'Phi', 0x03A8: 'Psi', 0x03A9: 'Omega',
    0x0391: 'A', 0x0392: 'B', 0x0395: 'E', 0x0396: 'Z', 0x0397: 'H', 0x0399: 'I', 0x039A: 'K',
    0x039C: 'M', 0x039D: 'N', 0x039F: 'O', 0x03A1: 'P', 0x03A4: 'T', 0x03A7: 'X', 0x2126: 'Omega',
    0x00B5: 'mu',
}
# ký tự riêng của MathType (vùng Private Use, font MT Extra)
PUA = {
    # khoảng trắng của MathType: bỏ (LaTeX tự giãn cách trong công thức), giữ em-space
    0xEF00: '', 0xEF01: '', 0xEF02: '', 0xEF03: '', 0xEF04: r'\quad ', 0xEF05: '',
    0xEF06: r'\qquad ', 0xEF07: '', 0xEF08: '', 0xEF09: '',
    0xEB00: r'\leftarrow', 0xEB01: r'\to', 0xEB02: r'\leftrightarrow',
    0xEC00: r'\ldots', 0xEC01: r'\cdots', 0xEC02: r'\vdots', 0xEC03: r'\ddots',
    0xE900: r'\langle', 0xE901: r'\rangle',
    0xF8FF: '', 0xE98F: r'\parallel', 0xE98E: r'\perp', 0xE93A: r'\subset',
    0xE922: r'\Leftrightarrow', 0xE921: r'\Rightarrow',
    0xE10C: r'\parallel', 0xE134: r'\Rightarrow', 0xE13B: r'\Leftrightarrow',
    0xEB0E: r'\nearrow',
    0xEF0A: '', 0x0009: '',
}
# chữ hoa kiểu Script của MathType (U+F100 + thứ tự chữ cái), vd D trong "D = R\{-1}"
for _k in range(26):
    PUA[0xF100 + _k] = chr(ord('A') + _k)
SPECIAL_TEXT = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '%': r'\%', '#': r'\#',
                '&': r'\&', '_': r'\_', '$': r'\$', '^': r'\^{}', '~': r'\~{}'}
SPECIAL_MATH = {'{': r'\{', '}': r'\}', '%': r'\%', '#': r'\#', '&': r'\&', '_': r'\_',
                '$': r'\$', '~': r'\sim ', '\\': r'\setminus '}

FUNCS = {'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'arcsin', 'arccos', 'arctan', 'sinh', 'cosh',
         'tanh', 'coth', 'ln', 'log', 'lg', 'exp', 'lim', 'max', 'min', 'sup', 'inf', 'det', 'deg',
         'dim', 'gcd', 'ker', 'arg', 'Pr', 'hom'}
FUNC_ALIAS = {'tg': r'\tan', 'cotg': r'\cot', 'arctg': r'\arctan', 'arccotg': r'\operatorname{arccot}',
              'cosec': r'\csc'}

# typeface
FN_TEXT, FN_FUNCTION, FN_VARIABLE, FN_LCGREEK, FN_UCGREEK, FN_SYMBOL, FN_VECTOR, FN_NUMBER = 1, 2, 3, 4, 5, 6, 7, 8
FN_USER1, FN_USER2, FN_MTEXTRA, FN_TEXT_FE, FN_EXPAND, FN_MARKER, FN_SPACE = 9, 10, 11, 12, 22, 23, 24

# template selectors
TM = dict(ANGLE=0, PAREN=1, BRACE=2, BRACK=3, BAR=4, DBAR=5, FLOOR=6, CEILING=7, OBRACK=8,
          INTERVAL=9, ROOT=10, FRACT=11, UBAR=12, OBAR=13, ARROW=14, INTEG=15, SUM=16, PROD=17,
          COPROD=18, UNION=19, INTER=20, INTOP=21, SUMOP=22, LIM=23, HBRACE=24, HBRACK=25,
          LDIV=26, SUB=27, SUP=28, SUBSUP=29, DIRAC=30, VEC=31, TILDE=32, HAT=33, ARC=34,
          JSTATUS=35, STRIKE=36, BOX=37)
FENCES = {0: (r'\langle', r'\rangle'), 1: ('(', ')'), 2: (r'\{', r'\}'), 3: ('[', ']'),
          4: ('|', '|'), 5: (r'\|', r'\|'), 6: (r'\lfloor', r'\rfloor'), 7: (r'\lceil', r'\rceil'),
          8: ('[', '['), }


class MTEFError(Exception):
    pass


# ---------------------------------------------------------------- cây đối tượng
class Line:
    def __init__(self, items=None, null=False):
        self.items = items or []
        self.null = null


class Char:
    def __init__(self, typeface, code, embells, func_start, fontpos=None):
        self.typeface = typeface
        self.code = code
        self.embells = embells
        self.func_start = func_start
        self.fontpos = fontpos


class Tmpl:
    def __init__(self, sel, var, opt, subs):
        self.sel, self.var, self.opt, self.subs = sel, var, opt, subs


class Pile:
    def __init__(self, halign, valign, lines):
        self.halign, self.valign, self.lines = halign, valign, lines


class Matrix:
    def __init__(self, rows, cols, cells, valign, hjust, vjust, rowparts=None, colparts=None):
        self.rows, self.cols, self.cells = rows, cols, cells
        self.valign, self.hjust, self.vjust = valign, hjust, vjust
        self.rowparts, self.colparts = rowparts or [], colparts or []


class Ctrl:
    """bản ghi điều khiển (cỡ chữ, màu...) — không in ra"""
    def __init__(self, kind):
        self.kind = kind


# ---------------------------------------------------------------- bộ đọc nhị phân
class Reader:
    def __init__(self, data):
        self.d = data
        self.p = 0

    def u8(self):
        if self.p >= len(self.d):
            raise MTEFError('hết dữ liệu')
        v = self.d[self.p]
        self.p += 1
        return v

    def u16(self):
        if self.p + 2 > len(self.d):
            raise MTEFError('hết dữ liệu')
        v = struct.unpack_from('<H', self.d, self.p)[0]
        self.p += 2
        return v

    def s16(self):
        v = struct.unpack_from('<h', self.d, self.p)[0]
        self.p += 2
        return v

    def cstr(self):
        e = self.d.index(b'\x00', self.p)
        s = self.d[self.p:e]
        self.p = e + 1
        return s.decode('latin-1')

    def peek(self):
        return self.d[self.p] if self.p < len(self.d) else 0


OPT_NUDGE = 0x08
OPT_CHAR_EMBELL = 0x01
OPT_CHAR_FUNC_START = 0x02
OPT_CHAR_ENC_CHAR_8 = 0x04
OPT_CHAR_ENC_CHAR_16 = 0x10
OPT_CHAR_ENC_NO_MTCODE = 0x20
OPT_LINE_NULL = 0x01
OPT_LP_RULER = 0x02
OPT_LINE_LSPACE = 0x04
OPT_COLOR_CMYK = 0x01
OPT_COLOR_NAME = 0x04


class Parser:
    def __init__(self, data):
        self.r = Reader(data)
        self.fonts = []
        self.encodings = []

    def nudge(self, opt):
        if opt & OPT_NUDGE:
            dx, dy = self.r.u8(), self.r.u8()
            if dx == 128 and dy == 128:
                self.r.s16()
                self.r.s16()

    def ruler(self):
        n = self.r.u8()
        for _ in range(n):
            self.r.u8()
            self.r.s16()

    def read_record(self):
        """đọc một bản ghi; trả về đối tượng, None (bản ghi phụ) hoặc 'END'"""
        r = self.r
        tag = r.u8()
        if tag == 0:
            return 'END'
        if tag == 1:  # LINE
            opt = r.u8()
            self.nudge(opt)
            if opt & OPT_LINE_LSPACE:
                r.s16()
            if opt & OPT_LP_RULER:
                self.ruler()  # thước kẻ đi liền, không có byte tag
            if opt & OPT_LINE_NULL:
                return Line(null=True)
            return Line(self.read_list())
        if tag == 2:  # CHAR
            opt = r.u8()
            self.nudge(opt)
            tf = r.u8() - 128
            code = None
            fontpos = None
            if not (opt & OPT_CHAR_ENC_NO_MTCODE):
                code = r.u16()
            if opt & OPT_CHAR_ENC_CHAR_8:
                fontpos = r.u8()
            if opt & OPT_CHAR_ENC_CHAR_16:
                fontpos = r.u16()
            embells = []
            if opt & OPT_CHAR_EMBELL:
                for o in self.read_list():
                    if isinstance(o, tuple) and o[0] == 'EMBELL':
                        embells.append(o[1])
            return Char(tf, code, embells, bool(opt & OPT_CHAR_FUNC_START), fontpos)
        if tag == 3:  # TMPL
            opt = r.u8()
            self.nudge(opt)
            sel = r.u8()
            v = r.u8()
            if v & 0x80:
                v = (v & 0x7F) | (r.u8() << 8)
            topt = r.u8()
            subs = self.read_list()
            return Tmpl(sel, v, topt, subs)
        if tag == 4:  # PILE
            opt = r.u8()
            self.nudge(opt)
            ha, va = r.u8(), r.u8()
            if opt & OPT_LP_RULER:
                self.ruler()
            lines = [o for o in self.read_list() if isinstance(o, (Line, Pile, Matrix))]
            return Pile(ha, va, lines)
        if tag == 5:  # MATRIX
            opt = r.u8()
            self.nudge(opt)
            va, hj, vj = r.u8(), r.u8(), r.u8()
            rows, cols = r.u8(), r.u8()
            nb = ((rows + 1) * 2 + 7) // 8
            rp = [r.u8() for _ in range(nb)]
            nb = ((cols + 1) * 2 + 7) // 8
            cp = [r.u8() for _ in range(nb)]
            cells = [o for o in self.read_list() if isinstance(o, (Line, Pile, Matrix))]
            return Matrix(rows, cols, cells, va, hj, vj, rp, cp)
        if tag == 6:  # EMBELL
            opt = r.u8()
            self.nudge(opt)
            return ('EMBELL', r.u8())
        if tag == 7:  # RULER
            self.ruler()
            return None
        if tag == 8:  # FONT_STYLE_DEF
            r.u8()
            r.u8()
            return None
        if tag == 9:  # SIZE
            ls = r.u8()
            if ls == 101:
                r.s16()
            elif ls == 100:
                r.u8()
                r.s16()
            else:
                r.u8()
            return None
        if tag in (10, 11, 12, 13, 14):  # FULL SUB SUB2 SYM SUBSYM
            return None
        if tag == 15:  # COLOR
            r.u8()
            return None
        if tag == 16:  # COLOR_DEF
            opt = r.u8()
            for _ in range(4 if opt & OPT_COLOR_CMYK else 3):
                r.u16()
            if opt & OPT_COLOR_NAME:
                r.cstr()
            return None
        if tag == 17:  # FONT_DEF
            enc = r.u8()
            self.fonts.append((enc, r.cstr()))
            return None
        if tag == 18:  # EQN_PREFS
            r.u8()
            n = r.u8()
            self.skip_nibbles(n)
            n = r.u8()
            self.skip_nibbles(n)
            n = r.u8()
            for _ in range(n):
                f = r.u8()
                if f:
                    r.u8()
            return None
        if tag == 19:  # ENCODING_DEF
            self.encodings.append(r.cstr())
            return None
        if tag >= 100:  # FUTURE: độ dài 1 byte, 0xFF thì 2 byte độ dài theo sau
            ln = r.u8()
            if ln == 0xFF:
                ln = r.u16()
            r.p += ln
            return None
        raise MTEFError('bản ghi lạ %d tại %d' % (tag, r.p - 1))

    def skip_nibbles(self, count):
        done = 0
        while done < count:
            b = self.r.u8()
            for nb in (b >> 4, b & 0xF):
                if done < count and nb == 0xF:
                    done += 1

    def read_list(self):
        out = []
        while True:
            o = self.read_record()
            if o == 'END':
                return out
            if o is not None:
                out.append(o)

    def parse(self):
        r = self.r
        ver = r.u8()
        if ver != 5:
            raise MTEFError('MTEF phiên bản %d (chỉ hỗ trợ 5)' % ver)
        r.u8(); r.u8(); r.u8(); r.u8()
        r.cstr()
        r.u8()
        objs = []
        while r.p < len(r.d):
            o = self.read_record()
            if o == 'END':
                break
            if o is not None:
                objs.append(o)
        return objs


# ---------------------------------------------------------------- sinh LaTeX
CTRL_WORD_END = re.compile(r'\\[A-Za-z]+$')


def join(a, b):
    """nối hai mảnh LaTeX, chèn dấu cách nếu mảnh trước kết thúc bằng lệnh chữ"""
    if not a:
        return b
    if not b:
        return a
    if CTRL_WORD_END.search(a) and (b[0].isalpha()):
        return a + ' ' + b
    return a + b


def braced(s):
    s = s.strip()
    if len(s) == 1 and s.isalnum():
        return s
    return '{' + s + '}'


TALL = re.compile(r'\\d?frac|\\int|\\sum|\\prod|\\begin|\\lim\\limits|\\sqrt\{[^}]*\\frac')


class Emitter:
    def __init__(self):
        self.warn = []
        self.fence = 0  # đang ở trong ngoặc (hệ, tuyển): ma trận 1 cột -> aligned

    # --- ký tự
    def char_latex(self, c, in_script=False):
        code = c.code
        tf = c.typeface
        if code is None:
            if c.fontpos is not None and 32 <= c.fontpos < 127:
                code = c.fontpos
            else:
                self.warn.append('ký tự không mã (font %s pos %s)' % (tf, c.fontpos))
                return ''
        ch = chr(code) if code < 0x110000 else ''
        if tf in (FN_TEXT, FN_TEXT_FE) and code not in GREEK:
            return ('text', SPECIAL_TEXT.get(ch, ch))
        if code in GREEK:
            g = GREEK[code]
            return '\\' + g if len(g) > 1 else g
        if code in SYM:
            return SYM[code]
        if code in PUA:
            return PUA[code]
        if 0x20 <= code < 0x7F:
            if ch in SPECIAL_MATH:
                return SPECIAL_MATH[ch]
            if ch == ' ':
                return ''
            return ch
        if 0xC0 <= code < 0x2000 and ch.isalpha():
            # chữ Việt có dấu trong công thức: đưa về \text
            return ('text', ch)
        if 0xE000 <= code <= 0xF8FF:
            self.warn.append('ký tự riêng MathType U+%04X' % code)
            return ''
        self.warn.append('ký tự chưa ánh xạ U+%04X' % code)
        return ch

    def embell(self, base, embs):
        for e in embs:
            if e == 2:
                base = r'\dot{%s}' % base
            elif e == 3:
                base = r'\ddot{%s}' % base
            elif e == 4:
                base = r'\dddot{%s}' % base
            elif e == 5:
                base = base + "'"
            elif e == 6:
                base = base + "''"
            elif e == 7:
                base = "'" + base
            elif e == 18:
                base = base + "'''"
            elif e == 8:
                base = r'\tilde{%s}' % base
            elif e == 9:
                base = r'\hat{%s}' % base
            elif e == 10:
                base = r'\not' + base
            elif e in (11, 14):
                base = r'\overrightarrow{%s}' % base
            elif e in (12, 15):
                base = r'\overleftarrow{%s}' % base
            elif e == 13:
                base = r'\overleftrightarrow{%s}' % base
            elif e == 17:
                base = r'\overline{%s}' % base
            elif e == 16:
                base = r'\overline{%s}' % base
            elif e == 19:
                base = r'\overset{\frown}{%s}' % base
            elif e == 21:
                base = r'\not' + base
            else:
                self.warn.append('trang trí lạ %d' % e)
        return base

    # --- dòng
    def line(self, ln, ctx=''):
        if ln is None or getattr(ln, 'null', False):
            return ''
        if isinstance(ln, Pile):
            return self.pile(ln, ctx)
        if isinstance(ln, Matrix):
            return self.matrix(ln, ctx)
        return self.items(ln.items, ctx)

    def items(self, items, ctx=''):
        out = ''
        i = 0
        n = len(items)
        textbuf = None  # gom chữ văn bản
        prev_piece = ''

        def flush_text():
            nonlocal out, textbuf
            if textbuf is not None:
                t = textbuf
                textbuf = None
                if t.strip() == '':
                    out = join(out, r'\ ' if t else '')
                else:
                    out = join(out, r'\text{%s}' % t)

        while i < n:
            it = items[i]
            if isinstance(it, Char):
                if it.typeface == FN_FUNCTION and it.code is not None and chr(it.code).isalpha() and not it.embells:
                    # gom tên hàm
                    j = i
                    name = ''
                    while j < n and isinstance(items[j], Char) and items[j].typeface == FN_FUNCTION \
                            and items[j].code is not None and chr(items[j].code).isalpha() \
                            and not items[j].embells and (j == i or not items[j].func_start):
                        name += chr(items[j].code)
                        j += 1
                    flush_text()
                    out = join(out, self.func_name(name))
                    i = j
                    continue
                r = self.char_latex(it, ctx == 'script')
                if isinstance(r, tuple):
                    if textbuf is None:
                        textbuf = ''
                    textbuf += r[1]
                    i += 1
                    continue
                flush_text()
                if it.embells:
                    r = self.embell(r, it.embells)
                out = join(out, r)
            elif isinstance(it, Tmpl):
                flush_text()
                piece = self.tmpl(it, ctx)
                if it.sel in (TM['SUB'], TM['SUP'], TM['SUBSUP']) and i > 0 and isinstance(items[i - 1], Tmpl) \
                        and items[i - 1].sel in (TM['SUB'], TM['SUP'], TM['SUBSUP']) \
                        and script_kinds(prev_piece) & script_kinds(piece):
                    piece = '{}' + piece  # hai chỉ số dưới (trên) liền nhau: v_0 rồi _{Min} -> tránh "Double subscript"
                prev_piece = piece
                out = join(out, piece)
            elif isinstance(it, Pile):
                flush_text()
                out = join(out, self.pile(it, ctx))
            elif isinstance(it, Matrix):
                flush_text()
                out = join(out, self.matrix(it, ctx))
            elif isinstance(it, Line):
                flush_text()
                out = join(out, self.line(it, ctx))
            i += 1
        flush_text()
        return out

    def func_name(self, name):
        if name.lower() in FUNCS and name not in FUNCS and name[0].isupper() and name[1:].islower():
            name = name.lower()  # Cos, Sin, Log... gõ hoa
        if name in FUNCS:
            return '\\' + name
        if name in FUNC_ALIAS:
            return FUNC_ALIAS[name]
        if len(name) == 1:
            return r'\mathrm{%s}' % name
        # tên hàm dính liền (vd "sinx" hiếm) hoặc chữ đứng
        for f in sorted(FUNCS, key=len, reverse=True):
            if name.startswith(f) and len(name) > len(f):
                return '\\' + f + ' ' + name[len(f):]
        return r'\mathrm{%s}' % name

    # --- pile / matrix
    def pile(self, p, ctx='', in_fence=False):
        rows = [self.line(l, ctx) for l in p.lines]
        if in_fence:
            return r'\begin{aligned}' + r'\\'.join('&' + x for x in rows) + r'\end{aligned}'
        if len(rows) == 1:
            return rows[0]
        if p.halign == 2:
            return r'\begin{gathered}' + r'\\'.join(rows) + r'\end{gathered}'
        if p.halign == 4:
            al = []
            for x in rows:
                m = re.search(r'(=|\\Leftrightarrow|\\Rightarrow|\\leq|\\geq|<|>|\\approx|\\neq)', x)
                if m and m.start() > 0:
                    al.append(x[:m.start()] + '&' + x[m.start():])
                else:
                    al.append('&' + x)
            return r'\begin{aligned}' + r'\\'.join(al) + r'\end{aligned}'
        return r'\begin{aligned}' + r'\\'.join('&' + x for x in rows) + r'\end{aligned}'

    def matrix(self, m, ctx='', in_fence=False):
        cells = [self.line(c, ctx) for c in m.cells]
        rows = []
        for r in range(m.rows):
            rows.append(' & '.join(cells[r * m.cols:(r + 1) * m.cols]))
        body = r'\\'.join(rows)
        if in_fence or (self.fence and m.cols == 1):
            if m.cols == 1:
                return r'\begin{aligned}' + r'\\'.join('&' + c for c in cells) + r'\end{aligned}'
            return r'\begin{array}{%s}' % ('l' * m.cols) + body + r'\end{array}'
        return r'\begin{matrix}' + body + r'\end{matrix}'

    # --- template
    def split_subs(self, t):
        lines = [s for s in t.subs if isinstance(s, (Line, Pile, Matrix))]
        chars = [s for s in t.subs if isinstance(s, Char)]
        return lines, chars

    def tmpl(self, t, ctx=''):
        sel, var = t.sel, t.var
        lines, chars = self.split_subs(t)
        L = lambda k, c=ctx: self.line(lines[k], c) if k < len(lines) else ''
        if sel in FENCES or sel == TM['INTERVAL']:
            main = lines[0] if lines else None
            # hệ / tuyển: ngoặc nhọn hoặc vuông một bên chứa pile
            inner_obj = None
            if isinstance(main, Line) and not main.null:
                objs = [o for o in main.items if not isinstance(o, Ctrl)]
                if len(objs) == 1 and isinstance(objs[0], (Pile, Matrix)):
                    inner_obj = objs[0]
            elif isinstance(main, (Pile, Matrix)):
                inner_obj = main
            if sel == TM['INTERVAL']:
                lmap = {0: '(', 1: ')', 2: '[', 3: ']'}
                left = lmap.get(var & 0x0F, '(')
                right = lmap.get((var >> 4) & 0x0F, ')')
                hasL = hasR = True
            else:
                left, right = FENCES[sel]
                hasL = bool(var & 1) or var == 0
                hasR = bool(var & 2) or var == 0
                if var == 0:
                    hasL = hasR = True
            if inner_obj is not None and (not hasR or not hasL) and sel in (TM['BRACE'], TM['BRACK']):
                body = self.pile(inner_obj, ctx, True) if isinstance(inner_obj, Pile) else \
                    self.matrix(inner_obj, ctx, True)
                lf = (r'\left' + left) if hasL else r'\left.'
                rf = (r'\right' + right) if hasR else r'\right.'
                return lf + body + rf
            if inner_obj is not None:
                body = self.pile(inner_obj, ctx, True) if isinstance(inner_obj, Pile) else \
                    self.matrix(inner_obj, ctx, False)
            else:
                self.fence += 1
                body = L(0)
                self.fence -= 1
            if sel == TM['BAR'] and hasL and not hasR:
                return r'\mid ' + body
            tall = bool(TALL.search(body))
            if tall or not (hasL and hasR):
                lf = (r'\left' + left) if hasL else r'\left.'
                rf = (r'\right' + right) if hasR else r'\right.'
                if left == '|' and hasL:
                    lf = r'\left|'
                return lf + body + rf
            return left + body + right
        if sel == TM['ROOT']:
            if var == 1 or (len(lines) > 1 and not getattr(lines[1], 'null', True)):
                idx = L(1, 'script')
                if idx:
                    return r'\sqrt[%s]{%s}' % (idx, L(0))
            return r'\sqrt{%s}' % L(0)
        if sel == TM['FRACT']:
            num, den = L(0, ctx), L(1, ctx)
            if var & 2:
                return '%s/%s' % (braced(num) if len(num) > 1 else num, braced(den) if len(den) > 1 else den)
            cmd = r'\frac' if ctx == 'script' else r'\dfrac'
            return cmd + '{%s}{%s}' % (num, den)
        if sel == TM['UBAR']:
            return r'\underline{%s}' % L(0)
        if sel == TM['OBAR']:
            return r'\overline{%s}' % L(0)
        if sel == TM['ARROW']:
            top, bot = L(0, 'script'), L(1, 'script')
            cmd = r'\xleftarrow' if (var & 0x10) and not (var & 0x20) else r'\xrightarrow'
            if var & 1:
                cmd = r'\xleftrightarrow' if False else cmd
            return cmd + ('[%s]' % bot if bot else '') + '{%s}' % top
        if sel in (TM['INTEG'], TM['INTOP']):
            n = var & 3
            sym = {1: r'\int', 2: r'\iint', 3: r'\iiint'}.get(n, r'\int')
            if var & 0x0C:
                sym = r'\oint'
            for c in chars:
                if c.code in (0x222C,):
                    sym = r'\iint'
                elif c.code in (0x222D,):
                    sym = r'\iiint'
                elif c.code in (0x222E,):
                    sym = r'\oint'
            body = L(0)
            lo, up = L(1, 'script'), L(2, 'script')
            s = r'\displaystyle' + sym
            if lo or up:
                s += r'\limits'
                if lo:
                    s += '_' + braced(lo)
                if up:
                    s += '^' + braced(up)
            body = fix_dx(body)
            return join(s, body)
        if sel in (TM['SUM'], TM['PROD'], TM['COPROD'], TM['UNION'], TM['INTER'], TM['SUMOP']):
            sym = {TM['SUM']: r'\sum', TM['PROD']: r'\prod', TM['COPROD']: r'\coprod',
                   TM['UNION']: r'\bigcup', TM['INTER']: r'\bigcap', TM['SUMOP']: r'\sum'}[sel]
            if sel == TM['SUMOP'] and chars and chars[0].code in SYM:
                sym = SYM[chars[0].code]
            lo, up = L(1, 'script'), L(2, 'script')
            s = sym
            if lo or up:
                s += r'\limits'
                if lo:
                    s += '_' + braced(lo)
                if up:
                    s += '^' + braced(up)
            return join(s, L(0))
        if sel == TM['LIM']:
            main = L(0).strip()
            lo, up = L(1, 'script'), L(2, 'script')
            # "max", "Min", \text{Max} gõ bằng chữ thường -> toán tử
            word = re.sub(r'^\\(?:text|mathrm)\{(.*)\}$', r'\1', main).strip()
            if word.lower() in ('lim', 'max', 'min', 'sup', 'inf'):
                main = '\\' + word.lower()
            if up.strip() in (r'\frown', r'\smile') and not lo:
                return r'\overset{%s}{%s}' % (up.strip(), main)  # cung tròn AB
            if re.fullmatch(r'\\(lim|max|min|sup|inf|sum|prod|int|bigcup|bigcap|log|ln)', main):
                s = main
                if lo:
                    s += r'\limits_' + braced(lo)
                if up:
                    s += ('' if lo else r'\limits') + '^' + braced(up)
                return s
            s = main
            if lo:
                s = r'\underset{%s}{%s}' % (lo, s)
            if up:
                s = r'\overset{%s}{%s}' % (up, s)
            return s
        if sel in (TM['HBRACE'], TM['HBRACK']):
            main, lab = L(0), L(1, 'script')
            if var & 1:
                return r'\overbrace{%s}' % main + ('^{%s}' % lab if lab else '')
            return r'\underbrace{%s}' % main + ('_{%s}' % lab if lab else '')
        if sel == TM['LDIV']:
            return L(0)
        if sel in (TM['SUB'], TM['SUP'], TM['SUBSUP']):
            sub = L(0, 'script')
            sup = L(1, 'script')
            s = ''
            if sub:
                s += '_' + braced(sub)
            if sup:
                s += '^' + braced(sup)
            if not s:
                s = '{}'
            return s
        if sel == TM['DIRAC']:
            return r'\langle %s|%s\rangle' % (L(0), L(1))
        if sel == TM['VEC']:
            m = L(0)
            if var & 4:
                return r'\underrightarrow{%s}' % m
            if (var & 1) and (var & 2):
                return r'\overleftrightarrow{%s}' % m
            if var & 1:
                return r'\overleftarrow{%s}' % m
            return r'\overrightarrow{%s}' % m
        if sel == TM['TILDE']:
            m = L(0)
            return (r'\widetilde{%s}' if len(m) > 1 else r'\tilde{%s}') % m
        if sel == TM['HAT']:
            m = L(0)
            return (r'\widehat{%s}' if len(strip_cmd(m)) > 1 else r'\hat{%s}') % m
        if sel == TM['ARC']:
            return r'\overset{\frown}{%s}' % L(0)
        if sel == TM['JSTATUS']:
            return L(0)
        if sel == TM['STRIKE']:
            return L(0)
        if sel == TM['BOX']:
            return r'\boxed{%s}' % L(0)
        self.warn.append('mẫu công thức lạ %d' % sel)
        return ''.join(self.line(l, ctx) for l in lines)


def script_kinds(piece):
    """tập các loại chỉ số ('_', '^') ở mức ngoài cùng của một mảnh LaTeX"""
    k = set()
    depth = 0
    for c in piece:
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif depth == 0 and c in '_^':
            k.add(c)
    return k


def strip_cmd(s):
    return re.sub(r'\\[A-Za-z]+|[{}]', '', s)


def fix_dx(body):
    """... dx ở cuối biểu thức dưới dấu tích phân -> \\,\\mathrm{d}x"""
    b = body.rstrip().replace(r'\text{d}', r'\mathrm{d}')
    b = re.sub(r'(?<=[^\s{(,])\s*(\\,)?\\mathrm\{d\}', r'\\,\\mathrm{d}', b)
    if r'\mathrm{d}' in b:
        return b
    m = re.search(r'(\\,)?(\\mathrm\{d\}|(?<!\\[A-Za-z])(?<!\\[A-Za-z]{2})(?<!\\[A-Za-z]{3})d)\s*([a-zA-Z]|\\[a-z]+)$', b)
    if m:
        return b[:m.start()] + r'\,\mathrm{d}' + m.group(3)
    return body


def decimal_comma(s):
    """1,5 -> 1{,}5; giữ dãy liệt kê 1,2,3 / 1,2,...,12"""
    def rep(mm):
        tok = mm.group(0)
        a, b = mm.start(), mm.end()
        after = s[b:b + 8]
        before = s[max(0, a - 8):a]
        if tok.count(',') >= 2 or after.startswith((',\\ldots', ',\\cdots', ',...', ',\\dots')) \
                or before.endswith(('\\ldots,', '\\cdots,', '...,', '\\dots,', '\\{')):
            return tok
        return tok.replace(',', '{,}')
    return re.sub(r'(?<!\d)\d+(?:,\d+)+', rep, s)


def post(s):
    # số thập phân dấu phẩy: 1,5 -> 1{,}5
    s = decimal_comma(s)
    # chữ d đứng gõ bằng kiểu Text
    s = s.replace(r'\text{d}', r'\mathrm{d}')
    # dấu chấm nhân kiểu Việt Nam: 2.3, u_1.q, (...).5 -> \cdot (giữ S.ABCD)
    s = re.sub(r'(?<=[\d\)\}])\.(?=[\d\(a-z\\])(?!\\(?:right|end|\\|quad|qquad|text))', r'\\cdot ', s)
    s = re.sub(r'(?<=(?<![\\A-Za-z])[a-z])\.(?=[\d(])', r'\\cdot ', s)
    # tên hàm gõ kiểu Text: \text{sin}x -> \sin x
    s = re.sub(r'\\text\{\s*(sin|cos|tan|cot|log|ln|lim|max|min|exp)\s*\}\s*',
               lambda mm: '\\' + mm.group(1).lower() + ' ', s, flags=re.I)
    s = re.sub(r'\\cdot (?=[\d(])', r'\\cdot', s)
    # tích phân, tổng, giới hạn gõ bằng ký tự + chỉ số: theo quy chuẩn \displaystyle\int\limits_a^b
    s = re.sub(r'(?<!\\displaystyle)\\(i{0,3}nt|oint)(?![A-Za-z])', r'\\displaystyle\\\1', s)
    s = re.sub(r'\\(i{0,3}nt|oint|sum|prod|lim|max|min)(?=[_^])', r'\\\1\\limits', s)
    if r'\int' in s:
        s = re.sub(r'(?<=[^\s{(,=+\-])\s*(\\,)?\\mathrm\{d\}(?=[a-zA-Z\\])', r'\\,\\mathrm{d}', s)
    # \quad thừa sau dấu ; ,
    s = re.sub(r'([;,])\s*\\q?quad\s*', r'\1', s)
    # dấu cách thừa
    s = re.sub(r' {2,}', ' ', s)
    # khoảng trắng văn bản ở đầu/cuối công thức
    s = re.sub(r'(\\ \s*)+$', '', s)
    s = re.sub(r'^(\s*\\ )+', '', s)
    # \text{} rỗng
    s = s.replace(r'\text{}', '')
    # ^\circ sau ^: x^{\circ} gộp; tránh ^^\circ
    s = s.replace(r'^{^\circ}', r'^\circ')
    s = re.sub(r'\^\{\s*\\circ\s*\}', r'^\\circ', s)
    # lệnh dính chữ phía sau (\circC, \circN) -> chèn khoảng trắng
    s = re.sub(r'\\circ(?=[A-Za-z])', r'\\circ ', s)
    return s.strip()


def mtef_to_latex(mtef_bytes):
    p = Parser(mtef_bytes)
    objs = p.parse()
    em = Emitter()
    parts = []
    for o in objs:
        if isinstance(o, Line):
            parts.append(em.line(o))
        elif isinstance(o, Pile):
            parts.append(em.pile(o))
        elif isinstance(o, Matrix):
            parts.append(em.matrix(o))
    s = ''
    for x in parts:
        s = join(s, x)
    s = post(s)
    if not s:
        em.warn.append('công thức rỗng')
    return s, em.warn


def wmf_to_latex(data):
    """ảnh WMF do MathType tạo (công thức dán dạng ảnh) có chứa MTEF trong bản ghi chú thích AppsMFCC"""
    if b'AppsMFCC' not in data:
        return None, ['không phải ảnh MathType']
    pos = 0
    chunks = []
    while True:
        i = data.find(b'AppsMFCC', pos)
        if i < 0:
            break
        _ver, _tot, clen = struct.unpack_from('<HII', data, i + 8)
        chunks.append(data[i + 18:i + 18 + clen])
        pos = i + 18 + clen
    blob = b''.join(chunks)
    sig = b'Design Science, Inc.\x00'
    j = blob.find(sig)
    if j >= 0:
        blob = blob[j + len(sig):]
    err = ''
    for cand in (blob, data[data.find(b'DSMT') - 5:] if data.find(b'DSMT') > 5 else b''):
        if not cand:
            continue
        try:
            lt, w = mtef_to_latex(cand)
            if lt:
                return lt, w
            err = 'công thức rỗng'
        except Exception as e:  # noqa
            err = str(e)
    return None, ['lỗi giải mã ảnh WMF MathType: %s' % err]


def ole_to_latex(ole_bytes):
    """trả về (latex, danh_sách_cảnh_báo); latex=None nếu không đọc được"""
    try:
        o = olefile.OleFileIO(io.BytesIO(ole_bytes))
        if not o.exists('Equation Native'):
            return None, ['không có Equation Native']
        d = o.openstream('Equation Native').read()
        hdr = struct.unpack_from('<H', d, 0)[0]
        return mtef_to_latex(d[hdr:])
    except Exception as e:  # noqa
        return None, ['lỗi giải mã: %s' % e]


if __name__ == '__main__':
    import sys
    import zipfile
    z = zipfile.ZipFile(sys.argv[1])
    names = sorted([n for n in z.namelist() if 'embeddings/oleObject' in n],
                   key=lambda x: int(re.search(r'(\d+)', x.split('/')[-1]).group(1)))
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    for n in names[:lim]:
        lt, w = ole_to_latex(z.read(n))
        print(n.split('/')[-1], '|', lt, '|', w if w else '')
