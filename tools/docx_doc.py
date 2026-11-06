# -*- coding: utf-8 -*-
"""
Đọc file Word (.docx) thành danh sách khối theo đúng thứ tự trong văn bản.

Mỗi khối:
  {'kind': 'p', 'items': [...], 'num': (numId, ilvl) | None, 'numlabel': 'Câu 3.' | '',
   'style': tên style, 'jc': căn lề}
  {'kind': 'tbl', 'rows': [[ [khối...], [khối...] ], ...]}   (mỗi ô là danh sách khối)

Mỗi phần tử trong 'items':
  {'t': 'text', 's': chuỗi, 'b': đậm, 'i': nghiêng, 'u': gạch chân, 'color': 'FF0000' | None,
   'hl': tô sáng | None}
  {'t': 'math', 's': mã LaTeX (None nếu không đọc được), 'warn': [...], 'ole': tên file OLE}
  {'t': 'img', 'name': 'image3.png', 'w': rộng (cm), 'h': cao (cm)}
  {'t': 'shape', 'desc': 'nhóm hình vẽ Word' ...}  (hình vẽ bằng shape/canvas của Word)
  {'t': 'textbox', 's': chữ trong text box}
  {'t': 'tab'} | {'t': 'br'}
"""
import re
import zipfile

from lxml import etree

from mtef import ole_to_latex, wmf_to_latex

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'v': 'urn:schemas-microsoft-com:vml',
    'o': 'urn:schemas-microsoft-com:office:office',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'wps': 'http://schemas.microsoft.com/office/word/2010/wordprocessingShape',
    'wpg': 'http://schemas.microsoft.com/office/word/2010/wordprocessingGroup',
    'wpc': 'http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'rel': 'http://schemas.openxmlformats.org/package/2006/relationships',
}
W = NS['w']


def q(tag):
    p, t = tag.split(':')
    return '{%s}%s' % (NS[p], t)


def ln(el):
    return etree.QName(el).localname


def wval(el, attr='val'):
    if el is None:
        return None
    return el.get(q('w:' + attr))


EMU_CM = 360000.0


class DocxReader:
    def __init__(self, path):
        self.path = path
        self.z = zipfile.ZipFile(path)
        self.rels = self._rels('word/_rels/document.xml.rels')
        self.numfmt = self._numbering()
        self.counters = {}
        self.math_cache = {}
        self.stats = {'math': 0, 'math_fail': 0, 'img': 0, 'shape': 0}
        self.warnings = []

    # ------------------------------------------------------------ phụ trợ
    def _rels(self, name):
        out = {}
        if name not in self.z.namelist():
            return out
        x = etree.fromstring(self.z.read(name))
        for r in x:
            out[r.get('Id')] = r.get('Target')
        return out

    def _numbering(self):
        """numId -> {'abs': abstractNumId, 'lv': {ilvl: (fmt, lvlText, start)}, 'override': {ilvl: start}}"""
        res = {}
        if 'word/numbering.xml' not in self.z.namelist():
            return res
        x = etree.fromstring(self.z.read('word/numbering.xml'))
        absd = {}
        for a in x.findall(q('w:abstractNum')):
            aid = wval(a, 'abstractNumId')
            lv = {}
            for l in a.findall(q('w:lvl')):
                il = int(wval(l, 'ilvl'))
                fmt = wval(l.find(q('w:numFmt'))) or 'decimal'
                txt = wval(l.find(q('w:lvlText'))) or ''
                st = wval(l.find(q('w:start')))
                lv[il] = (fmt, txt, int(st) if st else 1)
            absd[aid] = lv
        for n in x.findall(q('w:num')):
            nid = wval(n, 'numId')
            aid = wval(n.find(q('w:abstractNumId')))
            ov = {}
            for o in n.findall(q('w:lvlOverride')):
                il = int(wval(o, 'ilvl'))
                so = o.find(q('w:startOverride'))
                if so is not None:
                    ov[il] = int(wval(so))
            res[nid] = {'abs': aid, 'lv': absd.get(aid, {}), 'override': ov}
        return res

    def numlabel(self, numId, ilvl):
        info = self.numfmt.get(numId)
        if not info or numId == '0':
            return ''
        lv = info['lv'].get(ilvl)
        if not lv:
            return ''
        fmt, txt, start = lv
        key = numId  # bộ đếm theo từng danh sách (numId)
        cnt = self.counters.setdefault(key, {})
        if ilvl not in cnt:
            cnt[ilvl] = info['override'].get(ilvl, start)
        else:
            cnt[ilvl] += 1
        for deeper in [k for k in cnt if k > ilvl]:
            del cnt[deeper]

        def fmtnum(v, f):
            if f == 'decimal':
                return str(v)
            if f == 'upperLetter':
                return chr(ord('A') + v - 1)
            if f == 'lowerLetter':
                return chr(ord('a') + v - 1)
            if f == 'upperRoman':
                return ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'][v - 1] if v <= 10 else str(v)
            if f == 'lowerRoman':
                return ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x'][v - 1] if v <= 10 else str(v)
            if f == 'bullet':
                return ''
            return str(v)

        def rep(m):
            k = int(m.group(1)) - 1
            v = cnt.get(k, lv[2] if k == ilvl else 1)
            f = info['lv'].get(k, (fmt,))[0]
            return fmtnum(v, f)
        if fmt == 'bullet':
            return ''
        return re.sub(r'%(\d)', rep, txt)

    def math(self, rid):
        target = self.rels.get(rid)
        if not target:
            return None, ['không thấy OLE %s' % rid], ''
        name = 'word/' + target if not target.startswith('/') else target[1:]
        if name in self.math_cache:
            return self.math_cache[name] + (target,)
        try:
            data = self.z.read(name)
        except KeyError:
            return None, ['thiếu %s' % name], target
        lt, w = ole_to_latex(data)
        self.math_cache[name] = (lt, w)
        return lt, w, target

    # ------------------------------------------------------------ đọc run
    def run_props(self, r):
        rp = r.find(q('w:rPr'))
        d = {'b': False, 'i': False, 'u': False, 'color': None, 'hl': None, 'vert': None}
        if rp is None:
            return d
        b = rp.find(q('w:b'))
        if b is not None and wval(b) not in ('0', 'false'):
            d['b'] = True
        i = rp.find(q('w:i'))
        if i is not None and wval(i) not in ('0', 'false'):
            d['i'] = True
        u = rp.find(q('w:u'))
        if u is not None and wval(u) not in ('none', None, '0'):
            d['u'] = True
        c = rp.find(q('w:color'))
        if c is not None and wval(c) not in ('auto', '000000'):
            d['color'] = wval(c)
        h = rp.find(q('w:highlight'))
        if h is not None and wval(h) != 'none':
            d['hl'] = wval(h)
        sh = rp.find(q('w:shd'))
        if sh is not None and wval(sh, 'fill') not in (None, 'auto', 'FFFFFF'):
            d['hl'] = d['hl'] or wval(sh, 'fill')
        rf = rp.find(q('w:rFonts'))
        if rf is not None:
            d['font'] = rf.get(q('w:ascii')) or rf.get(q('w:hAnsi')) or ''
        va = rp.find(q('w:vertAlign'))
        if va is not None:
            d['vert'] = wval(va)
        if rp.find(q('w:vanish')) is not None:
            d['hidden'] = True
        return d

    def drawing_item(self, dr):
        """w:drawing -> img / shape / textbox / None(bỏ)"""
        docpr = dr.find('.//' + q('wp:docPr'))
        name = docpr.get('name', '') if docpr is not None else ''
        if name.startswith('TemBaoMat'):
            return None
        ext = dr.find('.//' + q('wp:extent'))
        w = h = None
        if ext is not None:
            w = round(int(ext.get('cx', 0)) / EMU_CM, 2)
            h = round(int(ext.get('cy', 0)) / EMU_CM, 2)
        blips = dr.findall('.//' + q('a:blip'))
        did = docpr.get('id') if docpr is not None else None
        if dr.find('.//' + q('wpg:wgp')) is not None or dr.find('.//' + q('wpc:wpc')) is not None:
            txt = self.textbox_text(dr)
            self.stats['shape'] += 1
            return {'t': 'shape', 'desc': 'hình vẽ bằng shape Word', 'w': w, 'h': h,
                    'nimg': len(blips), 'label': txt[:200], 'docpr': did}
        gd = dr.find('.//' + q('a:graphicData'))
        if gd is not None and gd.get('uri', '').endswith('wordprocessingInk'):
            if (w or 0) < 0.3 and (h or 0) < 0.3:
                return None  # nét mực lạc (chấm nhỏ), không phải hình
            self.stats['shape'] += 1
            return {'t': 'shape', 'desc': 'hình vẽ tay (Ink) trong Word', 'w': w, 'h': h,
                    'nimg': 0, 'label': '', 'docpr': did}
        if blips:
            rid = blips[0].get(q('r:embed')) or blips[0].get(q('r:link'))
            name = (self.rels.get(rid) or '').split('/')[-1]
            m = self.wmf_math(name)
            if m:
                return m
            self.stats['img'] += 1
            return {'t': 'img', 'name': name, 'w': w, 'h': h}
        tb = dr.find('.//' + q('wps:txbx'))
        if tb is not None:
            txt = self.textbox_text(dr)
            if not txt.strip() or STAMP.match(txt):
                return None
            return {'t': 'textbox', 's': txt, 'w': w, 'h': h}
        # một shape đơn lẻ không chữ, không ảnh (khung trang trí, text box rỗng): bỏ
        return None

    def wmf_math(self, name):
        """ảnh .wmf là công thức MathType dán dạng ảnh -> phần tử công thức"""
        if not name.lower().endswith('.wmf'):
            return None
        try:
            data = self.z.read('word/media/' + name)
        except KeyError:
            return None
        if b'AppsMFCC' not in data:
            return None
        lt, w = wmf_to_latex(data)
        if not lt:
            return None  # không giải mã được: giữ làm ảnh
        self.stats['math'] += 1
        return {'t': 'math', 's': lt, 'warn': w, 'ole': 'wmf:' + name}

    def textbox_text(self, el):
        parts = []
        for t in el.iter(q('w:t')):
            parts.append(t.text or '')
        for o in el.iter(q('o:OLEObject')):
            pass
        return ' '.join(p for p in parts if p.strip())

    def pict_item(self, pict):
        im = pict.find('.//' + q('v:imagedata'))
        if im is not None:
            rid = im.get(q('r:id'))
            name = (self.rels.get(rid) or '').split('/')[-1]
            m = self.wmf_math(name)
            if m:
                return m
            self.stats['img'] += 1
            return {'t': 'img', 'name': name, 'w': None, 'h': None}
        if pict.find('.//' + q('v:textbox')) is not None:
            txt = self.textbox_text(pict)
            if txt.strip() and not STAMP.match(txt):
                return {'t': 'textbox', 's': txt}
            return None
        self.stats['shape'] += 1
        return {'t': 'shape', 'desc': 'hình VML', 'w': None, 'h': None, 'nimg': 0, 'label': ''}

    def run_items(self, r, out):
        props = self.run_props(r)
        if props.get('hidden'):
            return
        for c in r:
            tag = ln(c)
            if tag == 't':
                s = clean_text(c.text or '', props.get('font', ''))
                if s:
                    it = {'t': 'text', 's': s}
                    it.update({k: v for k, v in props.items() if k not in ('hidden', 'font')})
                    out.append(it)
            elif tag == 'tab':
                out.append({'t': 'tab'})
            elif tag in ('br', 'cr'):
                if c.get(q('w:type')) == 'page':
                    continue
                out.append({'t': 'br'})
            elif tag == 'noBreakHyphen':
                out.append(dict({k: v for k, v in props.items() if k not in ('hidden', 'font')}, t='text', s='-'))
            elif tag == 'sym':
                ch = c.get(q('w:char'))
                font = c.get(q('w:font')) or ''
                sc = sym_char(font, ch)
                if sc:
                    out.append(dict({k: v for k, v in props.items() if k not in ('hidden', 'font')}, t='text', s=sc))
            elif tag == 'object':
                ole = c.find('.//' + q('o:OLEObject'))
                if ole is not None and (ole.get('ProgID') or '').startswith('Equation'):
                    lt, w, tgt = self.math(ole.get(q('r:id')))
                    self.stats['math'] += 1
                    if lt is None:
                        self.stats['math_fail'] += 1
                    out.append({'t': 'math', 's': lt, 'warn': w, 'ole': tgt.split('/')[-1]})
                else:
                    im = c.find('.//' + q('v:imagedata'))
                    rid = im.get(q('r:id')) if im is not None else None
                    name = (self.rels.get(rid) or '').split('/')[-1]
                    m = self.wmf_math(name)
                    if m:
                        out.append(m)
                        continue
                    self.stats['img'] += 1
                    out.append({'t': 'img', 'name': name,
                                'w': None, 'h': None,
                                'prog': ole.get('ProgID') if ole is not None else ''})
            elif tag == 'drawing':
                it = self.drawing_item(c)
                if it:
                    out.append(it)
            elif tag == 'pict':
                it = self.pict_item(c)
                if it:
                    out.append(it)
            elif tag == 'AlternateContent':
                ch = c.find(q('mc:Choice'))
                if ch is None:
                    ch = c.find(q('mc:Fallback'))
                if ch is not None:
                    fake = etree.Element(q('w:r'))
                    for x in ch:
                        fake.append(x)
                    self.run_items(fake, out)

    def para_items(self, p, out):
        for c in p:
            tag = ln(c)
            if tag == 'r':
                self.run_items(c, out)
            elif tag in ('hyperlink', 'ins', 'smartTag', 'fldSimple', 'customXml', 'sdtContent', 'sdt',
                         'moveTo', 'dir', 'bdo'):
                self.para_items(c, out)
            elif tag == 'oMathPara':
                self.para_items(c, out)
            elif tag == 'oMath':
                self.stats['math'] += 1
                lt = omml(c)
                out.append({'t': 'math', 's': lt, 'warn': ['công thức OMML (Word Equation)'], 'ole': 'OMML'})

    def paragraph(self, p):
        items = []
        self.para_items(p, items)
        ppr = p.find(q('w:pPr'))
        num = None
        lab = ''
        style = ''
        jc = ''
        if ppr is not None:
            npr = ppr.find(q('w:numPr'))
            if npr is not None:
                nid = wval(npr.find(q('w:numId')))
                il = wval(npr.find(q('w:ilvl')))
                if nid and nid != '0':
                    num = (nid, int(il or 0))
                    lab = self.numlabel(nid, int(il or 0))
            st = ppr.find(q('w:pStyle'))
            style = wval(st) or ''
            j = ppr.find(q('w:jc'))
            jc = wval(j) or ''
        if num is None and style:
            num = self.style_num(style)
            if num:
                lab = self.numlabel(*num)
        return {'kind': 'p', 'items': items, 'num': num, 'numlabel': lab, 'style': style, 'jc': jc}

    _style_cache = None

    def style_num(self, style):
        """style có gắn đánh số (vd style 'Câu hỏi' tự đánh 'Câu 1.')"""
        if self._style_cache is None:
            self._style_cache = {}
            if 'word/styles.xml' in self.z.namelist():
                x = etree.fromstring(self.z.read('word/styles.xml'))
                for s in x.findall(q('w:style')):
                    npr = s.find(q('w:pPr') + '/' + q('w:numPr'))
                    if npr is not None:
                        nid = wval(npr.find(q('w:numId')))
                        il = wval(npr.find(q('w:ilvl')))
                        if nid and nid != '0':
                            self._style_cache[wval(s, 'styleId')] = (nid, int(il or 0))
        return self._style_cache.get(style)

    def table(self, t):
        rows = []
        for tr in t.findall(q('w:tr')):
            row = []
            for tc in tr.findall(q('w:tc')):
                row.append(self.blocks(tc))
            # ô bị gộp trong w:sdt
            rows.append(row)
        return {'kind': 'tbl', 'rows': rows}

    def blocks(self, parent):
        out = []
        for el in parent:
            tag = ln(el)
            if tag == 'p':
                out.append(self.paragraph(el))
            elif tag == 'tbl':
                out.append(self.table(el))
            elif tag in ('sdt',):
                c = el.find(q('w:sdtContent'))
                if c is not None:
                    out.extend(self.blocks(c))
            elif tag in ('customXml', 'sdtContent'):
                out.extend(self.blocks(el))
        return out

    def read(self):
        doc = etree.fromstring(self.z.read('word/document.xml'))
        body = doc.find(q('w:body'))
        return self.blocks(body)


STAMP = re.compile(r'^\s*\[ID:\s*\d+')  # tem bảo mật ẩn chèn trong đề


def omml(el):
    """chuyển công thức OMML (Word Equation) đơn giản sang LaTeX"""
    def kids(e, name):
        x = e.find(q('m:' + name))
        return conv(x) if x is not None else ''

    def conv(e):
        out = ''
        for c in e:
            t = ln(c)
            if t == 'r':
                out += ''.join(x.text or '' for x in c.iter(q('m:t')))
            elif t == 'f':
                out += '\\dfrac{%s}{%s}' % (kids(c, 'num'), kids(c, 'den'))
            elif t == 'sSup':
                out += '{%s}^{%s}' % (kids(c, 'e'), kids(c, 'sup'))
            elif t == 'sSub':
                out += '{%s}_{%s}' % (kids(c, 'e'), kids(c, 'sub'))
            elif t == 'sSubSup':
                out += '{%s}_{%s}^{%s}' % (kids(c, 'e'), kids(c, 'sub'), kids(c, 'sup'))
            elif t == 'rad':
                d = kids(c, 'deg')
                out += ('\\sqrt[%s]{%s}' % (d, kids(c, 'e'))) if d else '\\sqrt{%s}' % kids(c, 'e')
            elif t == 'd':
                out += '\\left(' + ','.join(conv(x) for x in c.findall(q('m:e'))) + '\\right)'
            elif t in ('e', 'num', 'den', 'oMath', 'box', 'borderBox'):
                out += conv(c)
            elif t in ('rPr', 'ctrlPr', 'fPr', 'sSupPr', 'sSubPr', 'radPr', 'dPr'):
                continue
            else:
                out += conv(c)
        return out
    return conv(el)


SYMBOL_FONT = {'F0B3': '≥', 'F0A3': '≤', 'F0B9': '≠', 'F0DE': '⇒', 'F0DB': '⇔', 'F0AE': '→', 'F0B4': '×',
               'F0B1': '±', 'F0A5': '∞', 'F070': 'π', 'F061': 'α', 'F062': 'β', 'F0D0': '∠', 'F05E': '⊥',
               'F0CE': '∈', 'F0CF': '∉', 'F0C6': '∅', 'F0B0': '°', 'F0D6': '√', 'F02D': '−', 'F0A2': '′',
               'F0FC': '✓', 'F0FB': '✗', 'F0E0': '⟨', 'F0F1': '⟩'}


def sym_char(font, ch):
    """ký tự w:sym / chữ font Symbol -> Unicode; ký tự Webdings, Wingdings (ô đánh dấu...) bỏ"""
    ch = (ch or '').upper()
    if len(ch) == 2:
        ch = 'F0' + ch
    if font.lower().startswith('symbol') and ch in SYMBOL_FONT:
        return SYMBOL_FONT[ch]
    try:
        v = int(ch, 16)
        if v >= 0xF000:
            v -= 0xF000
        return chr(v) if font.lower().startswith(('times', 'arial', 'calibri', 'cambria')) else ''
    except ValueError:
        return ''


def clean_text(s, font):
    """chữ thường trong run: đổi ký tự vùng riêng (font Symbol) sang Unicode, bỏ ký tự riêng khác"""
    if not any('\ue000' <= c <= '\uf8ff' for c in s):
        return s
    out = []
    for c in s:
        if '\ue000' <= c <= '\uf8ff':
            if font.lower().startswith('symbol'):
                out.append(SYMBOL_FONT.get('%04X' % ord(c), ''))
            continue
        out.append(c)
    return ''.join(out)


# ---------------------------------------------------------------- chữ thuần (để dò mẫu)
def plain(items, math_mark=True):
    s = []
    for it in items:
        t = it['t']
        if t == 'text':
            s.append(it['s'])
        elif t == 'math':
            s.append('$%s$' % (it['s'] if it['s'] is not None else '???') if math_mark else '§')
        elif t == 'tab':
            s.append('\t')
        elif t == 'br':
            s.append('\n')
        elif t == 'img':
            s.append('[HÌNH]')
        elif t == 'shape':
            s.append('[HÌNH VẼ WORD]')
        elif t == 'textbox':
            s.append('[TEXTBOX: %s]' % it['s'])
    return ''.join(s)


def dump(blocks, indent=''):
    lines = []
    for b in blocks:
        if b['kind'] == 'p':
            lab = ('{%s} ' % b['numlabel']) if b['numlabel'] else ''
            lines.append(indent + lab + plain(b['items']).replace('\n', '⏎'))
        else:
            lines.append(indent + '[BẢNG %dx%d]' % (len(b['rows']), max((len(r) for r in b['rows']), default=0)))
            for r in b['rows']:
                cells = [' / '.join(plain(x['items']) if x['kind'] == 'p' else '[bảng con]' for x in c) for c in r]
                lines.append(indent + '  | ' + ' | '.join(cells))
    return '\n'.join(lines)


if __name__ == '__main__':
    import sys
    rd = DocxReader(sys.argv[1])
    bl = rd.read()
    print(dump(bl))
    print(rd.stats, file=sys.stderr)
