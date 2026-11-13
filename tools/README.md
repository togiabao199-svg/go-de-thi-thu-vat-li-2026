# Công cụ (dự án Vật lí)

Chạy từ gốc repo. Cần TeX Live có XeLaTeX và font TeX Gyre (xem `CLAUDE.md`, mục THIẾT LẬP), `poppler-utils` (`pdftotext`, `pdftoppm`, `pdfinfo`, `pdfimages`), LibreOffice (`soffice`), Python 3 với `lxml`, `olefile`, `pillow`, `numpy`, `pymupdf` (`pip install lxml olefile pillow numpy pymupdf`). Các công cụ chép từ dự án Toán; mô tả gốc ở `tools/README-toan.md`.

| Công cụ | Việc | Dùng cho Vật lí |
|---|---|---|
| `docx_doc.py` (+ `mtef.py`) | Đọc file Word theo đúng thứ tự: đoạn, bảng, công thức MathType giải mã ra LaTeX, hình (`[HÌNH]`, tên ảnh trong `word/media/`), hình vẽ bằng shape Word (kèm `docpr`, chữ trong hình), đánh số tự động. | **Dùng.** Đọc tốt đề Word thuvienhoclieu: cả 42 đề Word của kho giải mã hết công thức (0 lỗi) (đề mẫu Cao Bằng 244 công thức), lấy được cả bảng đáp án và lời giải. |
| `so_hinh.py` | Tách mọi `tikzpicture` (cả `circuitikz`) của file đề thành ảnh, ghép cạnh ảnh gốc → `de/<tên>/so-hinh/NN-cau-<câu>.png`. Macro đọc từ `preamble-vatli-hinh.tex` + khai báo riêng của đề. | **Dùng, bắt buộc mỗi đề.** |
| `dan_trang/dan_trang.py` (+ `do_khoi.tex`) | Dàn trang: `do-hinh`, `thu-hinh`, `needspace`, `kiem`, `xuat`, `tat-ca`. Nhận đường dẫn file `.tex`. | **Dùng** (`tat-ca` rồi `xuat`). |
| `hinh_word.py` | Dựng ảnh gốc cho hình vẽ bằng shape Word (không có file ảnh): LibreOffice xuất PDF bản gốc và bản làm tàng hình riêng hình đó, so hai bản để cắt vùng hình. | Dùng khi đề Word có shape (Cà Mau, Lạng Sơn, Cụm HH-NSL-TD1, Ninh Bình Cụm 9). |
| `tach_cau.py`, `xem_thu.py`, `pdf_dap_an.py`, `soan_de/khung.py`, `soan_de/kiem_tra.py` | Ngân hàng câu, phân bổ, soát đề của dự án 40 đề Toán (đường dẫn `kho/de-tu-soan`, `kho/ngan-hang`, mã TT/NC/TS, cấu trúc 12–4–6). | Chưa dùng; sửa lại nếu sau này cần. |

## Đọc đề gốc

**Word** (in toàn văn; chạy trong `tools/` để import được `mtef.py`):

```bash
cd tools && python3 docx_doc.py "../kho/goc/Cao Bang - So GDDT - Lan 1.docx" > /tmp/de.txt
```

Ảnh gốc của hình (bỏ qua các `.wmf` là công thức; `.emf` đổi sang PNG bằng `soffice --headless --convert-to png`):

```bash
unzip -o -j "kho/goc/Cao Bang - So GDDT - Lan 1.docx" 'word/media/*' -d <thư mục ảnh>
```

Ảnh trang để đối chiếu (hình trong Word hay neo lệch sang câu sau, nên luôn đối chiếu):

```bash
soffice --headless --convert-to pdf --outdir <thư mục> "kho/goc/Cao Bang - So GDDT - Lan 1.docx"
```

```bash
pdftoppm -r 110 -png "<thư mục>/Cao Bang - So GDDT - Lan 1.pdf" <thư mục>/trang
```

Thứ tự ảnh theo văn bản (để ghép đúng ảnh với câu khi chạy `so_hinh.py`):

```bash
cd tools && python3 -c "
from docx_doc import DocxReader
def walk(bl):
    for b in bl:
        if b['kind'] == 'p':
            for it in b['items']:
                if it['t'] in ('img', 'shape'): print(it.get('name') or 'shape docpr=%s' % it.get('docpr'))
        else:
            for r in b['rows']:
                for c in r: walk(c)
walk(DocxReader('../kho/goc/Cao Bang - So GDDT - Lan 1.docx').read())"
```

Hình vẽ bằng shape Word: lấy `docpr` từ lệnh trên rồi (LibreOffice có thể đặt lệch chữ trong shape; đối chiếu ảnh trang):

```bash
cd tools && python3 -c "from hinh_word import render; print(render('../kho/goc/Ca Mau - So GDDT - Lan 1.docx', 'CaMau', ['562103436'], outdir='<thư mục ảnh>', force=True))"
```

**PDF có chữ** (SieuGioi): chữ đọc tốt bằng `pdftotext`; công thức MathType ra kí tự rời (chỉ số tách dòng, kí hiệu thành ô vuông) nên luôn đối chiếu ảnh trang:

```bash
pdftotext -layout "kho/goc/Ha Noi - So GDDT - Lan 1.pdf" /tmp/de.txt
```

```bash
pdftoppm -r 150 -png "kho/goc/Ha Noi - So GDDT - Lan 1.pdf" <thư mục ảnh>/trang
```

**PDF scan** (2 đề: `Bac Ninh - So GDDT - chua ro lan.pdf`, `TP HCM - Nguyen Khuyen - Le Thanh Tong - Lan 10.pdf`): không có lớp chữ (`pdftotext` ra rỗng), máy không có OCR; đọc thẳng ảnh trang `pdftoppm -r 200 -png`, chữ in rõ, có watermark chéo.

## So hình (`so_hinh.py`)

```bash
python3 tools/so_hinh.py de/VatLi2026-CaoBang-SoGD-Lan1/VatLi2026-CaoBang-SoGD-Lan1.tex <thư mục ảnh> "I.2=image2.png,I.5=image10.jpeg,I.9=image15.jpeg,I.11=image17.jpeg,I.15=image18.jpeg,I.16=image24.jpeg,I.18=image36.jpeg,II.1=image37.jpeg,II.3=image47.jpeg,II.4=image54.jpeg,III.2=image59.jpeg,III.5=image63.jpeg"
```

- Câu đánh `I.2`, `II.4`, `III.5` theo thứ tự `\begin{ex}` trong từng PHẦN (câu có nhiều hình thì có nhiều ảnh cùng số câu, đánh số thứ tự `NN` khác nhau; ghép ảnh gốc theo câu nên hai hình cùng câu dùng chung một ảnh gốc).
- Đề PDF: ảnh gốc là ảnh trang kèm vùng cắt sau `@`, `x0:y0:x1:y1` (giá trị ≤ 1 là tỉ lệ khổ ảnh, > 1 là pixel): `"I.5=trang-2.png@0.08:0.31:0.55:0.52"`. Câu không ghi ảnh gốc thì ô gốc để trắng.
- Hình dựng ở cỡ chữ 12pt như file đề (`\footnotesize` = 10pt), nên nhãn trong ảnh so đúng cỡ so với nét vẽ.
- Màu `blue`, `cyan`, `teal` được đổi sang tông vàng như preamble-eduzy-v2, nên ảnh so khớp màu bản in. Biên dịch lỗi thì in dòng lỗi và giữ `so-hinh/hinh.tex`, `hinh.log` để xem.
- Xem từng ảnh `so-hinh/NN-cau-*.png`, sửa TikZ, chạy lại đến khi sát gốc; commit thư mục `so-hinh/`.

## Dàn trang (`dan_trang/dan_trang.py`)

```bash
python3 tools/dan_trang/dan_trang.py tat-ca de/VatLi2026-CaoBang-SoGD-Lan1/VatLi2026-CaoBang-SoGD-Lan1.tex
```

```bash
python3 tools/dan_trang/dan_trang.py xuat de/VatLi2026-CaoBang-SoGD-Lan1/VatLi2026-CaoBang-SoGD-Lan1.tex
```

- `tat-ca` = `thu-hinh` (thu hình quá 4,5 cm, trừ câu có `% giuhinh`) → `needspace` (đo khối câu ở bản đề, ghi `\NeedspaceCau`/`\NeedspaceBang`, tự chọn câu Đúng/Sai cần tách câu dẫn / bảng) → `kiem` (biên dịch bản đề + bản lời giải, soát ngắt câu, trang trống; ảnh `de/<tên>/bien-dich/dan-trang/de/soat-de-*.png`). `xuat` = `kiem` + chép `thanh-pham/<tên>.pdf`, `<tên>-DE.pdf` + `dong-goi.sh` (zip). Phải có sẵn thư mục `thanh-pham/`.
- Luôn truyền đường dẫn file `.tex` (cách gọi bằng số đề `01` là của dự án Toán).
- Mọi `preamble*.tex` ở gốc repo được chép vào thư mục biên dịch; zip có `preamble-eduzy-v2.tex` và `preamble-vatli-hinh.tex`.
- Chỉ đo, thu hình trong `\begin{tikzpicture}`: mạch điện vẽ bằng lệnh circuitikz trong `tikzpicture`. Linh kiện circuitikz không co theo `scale`, nên câu có mạch gắn `% giuhinh` (đặt cỡ bằng `\ctikzset{bipoles/length=...}`).
- Đề mẫu dựng lại 06/11/2026: bản đề 7 trang (ĐẠT), bản lời giải 10 trang (trang 4 trống 8,6 cm, trong giới hạn 1/3).

## Biên dịch thử nhanh

```bash
bash bien-dich.sh de/<tên>/<tên>.tex
```

Ra `de/<tên>/bien-dich/<tên>.pdf` và ảnh `trang-*.png`, in lỗi, tràn lề, kí tự thiếu.
