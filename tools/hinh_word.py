# -*- coding: utf-8 -*-
"""
Dựng ảnh đối chiếu cho HÌNH VẼ BẰNG SHAPE/DRAWING CỦA WORD (nhóm shape, canvas, Ink) — loại hình
không có sẵn file ảnh trong word/media/.

Cách làm (LibreOffice -> PDF -> cắt vùng hình):
  1. Xuất nguyên file Word ra PDF, kết xuất từng trang thành ảnh.
  2. Tạo bản sao file Word trong đó RIÊNG hình cần lấy bị làm tàng hình (không viền, không tô, chữ trắng,
     ảnh con thay bằng ảnh trong suốt; khung giữ nguyên nên bố cục trang không đổi), xuất PDF lần nữa.
  3. So hai bản theo từng trang: trang khác nhau là trang chứa hình, vùng điểm ảnh khác nhau là vùng hình.
  4. Cắt vùng đó (nới lề) từ trang gốc -> kho/ngan-hang/hinh-word/<MÃ>-hinh<docPr id>-trang<số trang>.png;
     lưu kèm ảnh cả trang -> <MÃ>-trang<số trang>.png để xem ngữ cảnh.

Dùng trong tools/tach_cau.py (tự gọi khi có hình loại 'hinh-ve-word'); chạy riêng:
    python3 tools/hinh_word.py kho/de-tu-soan/minh-hoa-nang-cao/NC05-dap-an.docx NC05 <docPr id> ...
"""
import glob
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

import numpy as np
from lxml import etree
from PIL import Image

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(GOC, 'kho', 'ngan-hang', 'hinh-word')
DPI = 150
NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'wpg': 'http://schemas.microsoft.com/office/word/2010/wordprocessingGroup',
    'wpc': 'http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas',
}


def soffice_pdf(docx, workdir):
    prof = os.path.join(workdir, 'lo-profile')
    subprocess.run(['soffice', '-env:UserInstallation=file://' + prof, '--headless', '--convert-to', 'pdf',
                    '--outdir', workdir, docx], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   timeout=600)
    pdf = os.path.join(workdir, os.path.splitext(os.path.basename(docx))[0] + '.pdf')
    return pdf if os.path.exists(pdf) else None


def pdf_pages(pdf, workdir, tag):
    pre = os.path.join(workdir, tag)
    subprocess.run(['pdftoppm', '-r', str(DPI), '-png', pdf, pre], check=True)
    files = sorted(f for f in os.listdir(workdir) if f.startswith(tag + '-') and f.endswith('.png'))
    return [os.path.join(workdir, f) for f in files]


def _blank_png():
    import io
    buf = io.BytesIO()
    Image.new('RGBA', (8, 8), (255, 255, 255, 0)).save(buf, 'PNG')
    return buf.getvalue()


BLANK_PNG = _blank_png()
A = '{%s}' % NS['a']
W = '{%s}' % NS['w']
FILLS = ('solidFill', 'gradFill', 'pattFill', 'blipFill', 'noFill', 'grpFill')


def make_invisible(gd, blank_rid):
    """làm tàng hình mọi thứ trong hình (không viền, không tô, chữ trắng, ảnh trong suốt), giữ khung"""
    for el in list(gd.iter()):
        if not isinstance(el.tag, str):
            continue
        ln = etree.QName(el).localname
        if ln in ('spPr', 'grpSpPr'):
            geom = None
            for c in list(el):
                cl = etree.QName(c).localname
                if cl in FILLS or cl in ('ln', 'effectLst', 'effectDag', 'scene3d', 'sp3d'):
                    el.remove(c)
                elif cl in ('prstGeom', 'custGeom'):
                    geom = c
            pos = (list(el).index(geom) + 1) if geom is not None else len(el)
            if ln == 'spPr':
                nf = etree.Element(A + 'noFill')
                lnel = etree.Element(A + 'ln')
                etree.SubElement(lnel, A + 'noFill')
                el.insert(pos, lnel)
                el.insert(pos, nf)
        elif ln == 'style' and etree.QName(el).namespace.endswith(('wordprocessingShape', 'picture')):
            el.getparent().remove(el)
        elif ln == 'blip':
            for k in list(el.attrib):
                if k.endswith('}embed') or k.endswith('}link'):
                    el.set(k, blank_rid)
        elif ln == 'imagedata':
            for k in list(el.attrib):
                if k.endswith('}id'):
                    el.set(k, blank_rid)
        elif ln == 'r' and etree.QName(el).namespace == NS['w']:
            rpr = el.find(W + 'rPr')
            if rpr is None:
                rpr = etree.Element(W + 'rPr')
                el.insert(0, rpr)
            for c in rpr.findall(W + 'color') + rpr.findall(W + 'highlight') + rpr.findall(W + 'shd'):
                rpr.remove(c)
            col = etree.SubElement(rpr, W + 'color')
            col.set(W + 'val', 'FFFFFF')
        elif ln in ('shd', 'pBdr') and etree.QName(el).namespace == NS['w'] and \
                etree.QName(el.getparent()).localname == 'pPr':
            el.getparent().remove(el)


def blank_copy(docx, docpr_id, dest):
    """bản sao docx, hình có docPr id cho trước bị làm tàng hình (giữ nguyên khung, bố cục không đổi)"""
    zin = zipfile.ZipFile(docx)
    x = etree.fromstring(zin.read('word/document.xml'))
    rels = etree.fromstring(zin.read('word/_rels/document.xml.rels'))
    blank_rid = 'rIdEZblank'
    r = etree.SubElement(rels, '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship')
    r.set('Id', blank_rid)
    r.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
    r.set('Target', 'media/ezblank.png')
    found = None
    for dp in x.iter('{%s}docPr' % NS['wp']):
        if dp.get('id') != docpr_id:
            continue
        ext = dp.getparent().find('wp:extent', NS)
        found = (int(ext.get('cx')), int(ext.get('cy'))) if ext is not None else (0, 0)
        dr = dp.getparent().getparent()  # wp:inline/anchor -> w:drawing
        gd = dr.find('.//a:graphicData', NS)
        if gd is not None:
            make_invisible(gd, blank_rid)
        # bỏ phương án dự phòng VML của cùng hình (nếu có)
        alt = [a for a in dr.iterancestors() if etree.QName(a).localname == 'AlternateContent']
        if alt:
            for fb in alt[0].findall('mc:Fallback', NS):
                alt[0].remove(fb)
    if found is None:
        return None
    zout = zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED)
    for it in zin.infolist():
        data = zin.read(it.filename)
        if it.filename == 'word/document.xml':
            data = etree.tostring(x, xml_declaration=True, encoding='UTF-8', standalone=True)
        elif it.filename == 'word/_rels/document.xml.rels':
            data = etree.tostring(rels, xml_declaration=True, encoding='UTF-8', standalone=True)
        zout.writestr(it, data)
    zout.writestr('word/media/ezblank.png', BLANK_PNG)
    zout.close()
    return found


def diff_box(a_png, b_png):
    """khung bao vùng điểm ảnh khác nhau giữa trang gốc và trang đã làm tàng hình hình"""
    a = np.asarray(Image.open(a_png).convert('L'), dtype=np.int16)
    b = np.asarray(Image.open(b_png).convert('L'), dtype=np.int16)
    if a.shape != b.shape:
        return None
    m = np.abs(a - b) > 40
    if m.sum() < 20:
        return None
    ys, xs = np.where(m)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def render(docx, ma, docpr_ids, outdir=OUT, force=False):
    """-> {docpr_id: {'anh': đường dẫn ảnh cắt (tương đối gốc repo), 'trang': số trang, 'anh_trang': ...}}"""
    os.makedirs(outdir, exist_ok=True)
    res = {}
    todo = []
    for did in docpr_ids:
        old = glob.glob(os.path.join(outdir, '%s-hinh%s-trang*.png' % (ma, did)))
        if old and not force:
            crop = old[0]
            trang = int(crop.rsplit('trang', 1)[1].split('.')[0])
            res[did] = {'anh': os.path.relpath(crop, GOC), 'trang': trang,
                        'anh_trang': os.path.relpath(os.path.join(outdir, '%s-trang%d.png' % (ma, trang)), GOC)}
        else:
            for f in old:
                os.remove(f)
            todo.append(did)
    if not todo:
        return res
    work = tempfile.mkdtemp(prefix='hinhword-')
    try:
        src = os.path.join(work, 'goc.docx')
        shutil.copy(docx, src)
        pdf0 = soffice_pdf(src, work)
        if not pdf0:
            return res
        pages0 = pdf_pages(pdf0, work, 'goc')
        for did in todo:
            sub = os.path.join(work, 'b' + did)
            os.makedirs(sub)
            bdoc = os.path.join(sub, 'rong.docx')
            ext = blank_copy(src, did, bdoc)
            if ext is None:
                continue
            pdf1 = soffice_pdf(bdoc, sub)
            if not pdf1:
                continue
            pages1 = pdf_pages(pdf1, sub, 'rong')
            hit = None
            for k, (p0, p1) in enumerate(zip(pages0, pages1)):
                box = diff_box(p0, p1)
                if box:
                    hit = (k, box)
                    break
            if not hit:
                continue
            k, (x0, y0, x1, y1) = hit
            img = Image.open(pages0[k])
            pad = int(DPI * 0.05)
            W, H = img.size
            crop = img.crop((max(0, x0 - pad), max(0, y0 - pad), min(W, x1 + pad), min(H, y1 + pad)))
            cpath = os.path.join(outdir, '%s-hinh%s-trang%d.png' % (ma, did, k + 1))
            crop.save(cpath, optimize=True)
            ppath = os.path.join(outdir, '%s-trang%d.png' % (ma, k + 1))
            if not os.path.exists(ppath):
                pg = img.convert('RGB')
                pg = pg.resize((pg.width * 2 // 3, pg.height * 2 // 3))
                pg.save(ppath, optimize=True)
            res[did] = {'anh': os.path.relpath(cpath, GOC), 'trang': k + 1,
                        'anh_trang': os.path.relpath(ppath, GOC)}
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return res


if __name__ == '__main__':
    print(render(sys.argv[1], sys.argv[2], sys.argv[3:], force=True))
