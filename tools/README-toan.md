# Công cụ trích xuất ngân hàng câu hỏi (dự án 40 đề)

Chạy từ gốc repo. Cần Python 3 với `lxml`, `olefile`, `pillow`, `numpy`, `pymupdf` (`pip install lxml olefile pillow numpy pymupdf`), LibreOffice (dựng ảnh hình vẽ bằng shape Word, đổi ảnh WMF/EMF sang PNG), poppler-utils (`pdftoppm`, `pdftotext`) và TeX Live (biên dịch xem thử).

| File | Việc |
|---|---|
| `mtef.py` | Giải mã công thức MathType (OLE `Equation.DSMT4`, định dạng MTEF v5) ra LaTeX theo quy chuẩn ký hiệu của CLAUDE.md. Cũng đọc được công thức MathType bị dán dạng ảnh WMF (MTEF nằm trong bản ghi `AppsMFCC` của ảnh). |
| `docx_doc.py` | Đọc file Word theo đúng thứ tự: đoạn văn, bảng, công thức, hình, đánh số tự động ("Câu 1:"), định dạng chữ (gạch chân, đậm...). Bỏ tem bảo mật ẩn và text box rỗng. |
| `tach_cau.py` | Tách từng câu hỏi, ghi `kho/ngan-hang/<tu-soan\|truong-so>/<MÃ>.json`. |
| `hinh_word.py` | Dựng ảnh đối chiếu cho hình vẽ bằng shape/drawing của Word (không có file ảnh sẵn): LibreOffice xuất PDF bản gốc và bản làm tàng hình riêng hình đó (giữ khung nên bố cục không đổi), so hai trang tìm trang và vùng hình, cắt ra `kho/ngan-hang/hinh-word/<MÃ>-hinh<id>-trang<n>.png` (kèm ảnh cả trang `<MÃ>-trang<n>.png`). `tach_cau.py` tự gọi. |
| `pdf_dap_an.py` | Đọc PDF đáp án khi không có file Word đáp án (TT32): đáp án Phần I theo nét gạch chân trong PDF, Phần II theo kết luận lời giải, Phần III theo ô "Trả lời"; lời giải lấy dạng văn bản thô. |
| `xem_thu.py` | Xuất file `.tex` xem thử từ JSON (ảnh gốc chèn để đối chiếu; `--thu-muc` để ghi ra chỗ khác). |

## Lệnh

```bash
python3 tools/tach_cau.py TT01 NC05 TS039
```

```bash
python3 tools/xem_thu.py TT01 NC05 TS039 --ten XemThu-TrichXuat
```

```bash
bash bien-dich.sh de/XemThu-TrichXuat/XemThu-TrichXuat.tex
```

Chạy toàn bộ kho (khoảng 2–3 phút; thêm `--khong-dung-hinh` để bỏ bước dựng ảnh shape bằng LibreOffice):

```bash
python3 tools/tach_cau.py --tat-ca
```

Thử riêng bộ giải mã MathType trên một file Word (in 50 công thức đầu):

```bash
python3 tools/mtef.py kho/de-tu-soan/thi-thu/TT01-dap-an.docx 50
```

## Cách nhận diện trong file nguồn

- Phần: đoạn bắt đầu bằng `PHẦN I/II/III/IV` hoặc `Phần 1/2/3/4` kèm tên phần; loại phần xác định theo tên ("Trắc nghiệm", "Đúng Sai", "Trả lời ngắn", "Tự luận"), không theo số. Câu như "Phần 1 (từ x=0 …)" trong lời giải không bị nhận nhầm.
- Câu: `Câu N` (chữ gõ tay hoặc đánh số tự động của Word).
- Lời giải: đoạn `Lời giải` / `Hướng dẫn giải`.
- Đáp án Phần I: chữ cái phương án được gạch chân (cả kho tự soạn và kho trường sở); dự phòng dòng `Chọn X`; nếu bản gốc không gạch chân thì suy từ lời giải (phương án duy nhất xuất hiện ở kết luận) và ghi cảnh báo. Nhãn phương án gõ lẫn trong công thức (`A.4.`) vẫn tách được.
- Đáp án Phần II: bảng mệnh đề đánh dấu X ở cột Đúng/Sai (kho trường sở); hoặc kết luận trong lời giải (`mệnh đề a) đúng`, `a) Đúng.`). Có cả hai thì đối chiếu, lệch nhau ghi cảnh báo.
- Đáp án Phần III: bảng ô trả lời (1 hàng, mỗi ô 1 ký tự) sau đề; dự phòng dòng `Trả lời: ...`.
- Bảng dữ liệu trong đề → `tabular`; bảng bố cục (chữ + hình, phương án xếp trong bảng) được trải phẳng.

## Chuẩn hóa tự động khi giải mã công thức

`\dfrac` (trong chỉ số trên/dưới dùng `\frac`), `\overrightarrow`, `\leq \geq \neq`, `\varnothing`, `\mathbb{R}`; số thập phân `1{,}5` (giữ dãy liệt kê `1,2,\ldots`, tập `\{1,2\}`); dấu chấm nhân kiểu Việt Nam `2.3`, `u_1.q` → `\cdot` (giữ `S.ABCD`); tích phân `\displaystyle\int\limits_a^b f(x)\,\mathrm{d}x`; `\sum\limits`, `\lim\limits`; hệ/tuyển `\left\{\begin{aligned}&...\end{aligned}\right.`; ngoặc chỉ dùng `\left(\right)` khi bên trong có phân số, tích phân...; tên hàm gõ hoa (`Cos`) hoặc gõ kiểu Text → `\cos`; bỏ khoảng trắng MathType thừa.

## Giai đoạn 4 — kiểm chứng đáp án (`tools/kiem_chung/`)

| File | Việc |
|---|---|
| `kiem_chung/xuat.py` | Xuất câu đã chọn (`kho/phan-bo.csv`, `kho/du-phong.csv`) ra văn bản để kiểm: `--de 01 02`, `--du-phong`, `--id <mã>...`, `--uu-tien`; `--loi-giai 0|1|2`, `--anh <thư mục>` tách ảnh gốc của câu có hình, `--ra <file>`. |
| `kiem_chung/ghi.py` | Gộp file kết quả lô (TSV 8 cột: id, vi_tri, loai, ket_qua, dap_an_goc, dap_an_moi, sua_de, ghi_chu) vào `kho/kiem-chung.tsv` và áp vào JSON ngân hàng (trường `kiem_chung`, đổi `dap_an` khi sửa). `--thong-ke` tiến độ, `--ap` áp lại từ TSV, `--ghi-de` ghi đè câu đã có. |

## Giai đoạn 5 — soạn đề (`tools/soan_de/`)

| File | Việc |
|---|---|
| `soan_de/khung.py` | Sinh KHUNG đề `de/LuyenDe-TN2027-DeXX/LuyenDe-TN2027-DeXX.tex` theo `kho/phan-bo.csv`: bố cục đúng `mau-de-thi-thu.tex` (preamble v2, 3 phần, `ans/<tên>-k`, bảng đáp án comment), mỗi câu có dòng `% <mã câu>` (giữ trong thành phẩm), nội dung và `\True`/`\shortans` theo đáp án sau kiểm chứng, lời giải gốc trong `\loigiai`, ghi chú soạn `%@` (vị trí, ghi chú chấm, kết quả kiểm chứng, chỗ sửa lời văn đã duyệt, mô tả hình theo `kho/danh-gia/hinh.tsv` kèm đường dẫn ảnh gốc). `--anh <thư mục>` tách ảnh gốc (ngoài repo), `--ghi-de` ghi đè khung đã có, `--thu-muc <thư mục>` ghi khung ra chỗ khác (lấy khối câu thay thế cho đề đã soạn). |
| `soan_de/kiem_tra.py` | Soát file đề đã soạn: hết `%@`, không `\includegraphics`/`\immini`/tkz-euclide/`$$`/`cases`, đủ 12–4–6 câu đúng mã và thứ tự phân bổ, `\True`/`\shortans` khớp ngân hàng (câu có `% KIỂM TRA` chỉ cảnh báo), lời giải Đúng/Sai `itemchoice` khớp `\True`, trả lời ngắn ≤ 4 ký tự; cảnh báo thiếu "Vậy", `\int` thiếu `\displaystyle`, thiếu `\Needspace`... Mã thoát 1 nếu còn LỖI. |

```bash
python3 tools/soan_de/khung.py 01 02 03 --anh /tmp/anh-goc
```

```bash
python3 tools/soan_de/kiem_tra.py de/LuyenDe-TN2027-De01/LuyenDe-TN2027-De01.tex
```

## Dàn trang (`tools/dan_trang/`)

| File | Việc |
|---|---|
| `dan_trang/dan_trang.py` | Dàn trang đề (bản đề ưu tiên): `do-hinh` đo kích thước mọi hình và xuất ảnh soát hình; `thu-hinh` thu hình theo quy tắc CLAUDE.md (đồ thị, hình phẳng ≤ 4,5 cm; hình không gian ≤ 4 cm; tkz-tab gọn); `needspace` đo độ cao từng khối câu ở bản đề và ghi `\Needspace` vừa đúng (câu đầu phần đặt trên tiêu đề phần); `kiem` biên dịch bản đề + bản lời giải, soát câu bị ngắt và trang trống quá 1/4 (bản lời giải 1/3), xuất ảnh ghép trang bản đề; `xuat` = `kiem` + chép `thanh-pham/<tên>.pdf`, `<tên>-DE.pdf` + đóng gói zip. Nhận số đề (`01`) hoặc đường dẫn file `.tex`. Từ 05/11/2026: ghi `\NeedspaceCau[..]{..}` / `\NeedspaceBang{..}` (lệnh thêm trong preamble-eduzy-v2, bật bằng `\def\TachCauDS{1}`, `\def\TachCauLG{1}`), tự chọn câu Đúng/Sai cần tách câu dẫn / bảng, miễn trang trước tiêu đề phần, bản lời giải tách phần đề câu cao hơn 1/3 trang. Comment trong câu (thêm 05/11/2026, `kho/sua-hinh.md`): `% giuhinh` — `thu-hinh` không thu hình của câu, `do-hinh` và `kiem` không báo lệch cỡ (`kiem` ghi LƯU Ý cho hình cao hơn trần quy định ở các câu khác); `% tachDS` — `needspace` cho tách câu dẫn / bảng của câu Đúng/Sai kể cả câu đầu Phần II (tiêu đề phần + câu dẫn + hình ở cuối trang trước). |
| `dan_trang/do_khoi.tex` | Bộ đo chèn vào bản biên dịch tạm (zref-savepos): vị trí đầu/cuối khối câu, cuối câu dẫn và đầu bảng Đúng/Sai, tiêu đề phần, vị trí và kích thước hình. Không dùng trong thành phẩm. |

```bash
python3 tools/dan_trang/dan_trang.py thu-hinh 01
```

```bash
python3 tools/dan_trang/dan_trang.py needspace 01
```

```bash
python3 tools/dan_trang/dan_trang.py xuat 01
```

## Giai đoạn 6 — ghép 40 đề thành 2 quyển sách (`sach/`, `tools/sach/`)

| File | Việc |
|---|---|
| `sach/Sach-LuyenDe-TN2027-QuyenDe.tex`, `sach/Sach-LuyenDe-TN2027-QuyenLoiGiai.tex` | Hai file chính (XeLaTeX, chạy trong `sach/`). Preamble, `ex_test.sty`, `esvect.sty` tìm ở thư mục cha qua `\input@path`; file đề `\input` thẳng từ `../de/`. |
| `sach/sach-chung.tex` | `\ChenDe` (bỏ `\input{preamble-eduzy-v2}` và biến `\begin{document}`…`\end{document}` của file đề thành nhóm thường, đề bắt đầu trang lẻ), `\SangTrangLe` / `\SangTrangChan` (trang trắng hoàn toàn: mặt sau bìa trước, trang trước bìa sau), `\SangTrangLeCoDau` (trang trống có đầu trang, chân trang, logo chìm; sau một đề mang đầu trang của đề đó — dùng trong `\ChenDe`, `\BangDapAn`; quy tắc 06/11/2026), `\ChenBia` (pdfpages, cắt 3 mm lề xén), `\MucLuc`, `\BangDapAn` (đọc `ans/` do ex_test sinh ra). |
| `sach/phan-dau/*.tex` | Lời nói đầu, trang cấu trúc đề và hướng dẫn chấm (Quyển Đề). |
| `sach/bia/*.pdf` | Bìa dựng sẵn (216 × 303 mm): `bia-07.pdf`, `bia-07-loigiai.pdf` (dòng "LỜI GIẢI", công tắc `\QuyenLoiGiai` trong `bia/bia-07.tex`), `bia-07-sau.pdf`. |
| `sach/bien-dich-sach.sh` | `bia` dựng 3 PDF bìa (`bia bia-07-loigiai` chỉ dựng lại bìa có tên); `de`, `loigiai` biên dịch một quyển vào `sach/bien-dich/<quyển>/` (thư mục ra riêng nên chạy song song được, tự chạy lại khi log còn đòi); `tat-ca` = bìa + 2 quyển song song. |
| `sach/dong-goi-sach.sh` | Đóng gói `thanh-pham/Sach-LuyenDe-TN2027-NguonSach.zip`, chép 2 PDF sách vào `thanh-pham/`. |
| `sach/BienDich-Sach.bat` | Biên dịch cả 2 quyển trên Windows (MiKTeX, XeLaTeX, 2–4 lượt); trong zip đặt ở thư mục gốc. |
| `tools/sach/kiem_sach.py` | Kiểm tra 2 quyển: A4, tổng trang chẵn, bìa trước/sau, mỗi đề bắt đầu trang lẻ, số trang = bản lẻ, văn bản (pdftotext, bỏ số trang), vị trí chữ và ảnh từng trang khớp bản lẻ trong `thanh-pham/`, trang 2 và trang trước bìa sau trắng hoàn toàn, trang trống chèn thêm khác có đầu trang (đề trước / dòng chung), chân trang, logo chìm, đầu trang, mục lục, bảng đáp án khớp `\True`/`\shortans`. |

```bash
bash sach/bien-dich-sach.sh tat-ca
```

```bash
python3 tools/sach/kiem_sach.py
```

```bash
bash sach/dong-goi-sach.sh
```
