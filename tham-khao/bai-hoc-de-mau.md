# Đề mẫu Vật lí đã duyệt và các điều rút ra (06/11/2026)

Đề mẫu chuẩn: `de/VatLi2026-CaoBang-SoGD-Lan1/VatLi2026-CaoBang-SoGD-Lan1.tex`. Nguồn là `kho/goc/Cao Bang - So GDDT - Lan 1.docx`. Thầy đã duyệt cả phần chữ, lời giải và hình. Thành phẩm nằm trong `thanh-pham/`. Ảnh so hình gốc với hình TikZ nằm ở `de/VatLi2026-CaoBang-SoGD-Lan1/so-hinh/`. Kết quả đối chiếu đáp án ở `de/VatLi2026-CaoBang-SoGD-Lan1/kiem-chung.md`.

Mọi đề sau theo đúng cách trình bày của đề mẫu. Khi viết CLAUDE.md, đưa các điều dưới đây vào.

## Đầu file
- Khai báo trước `\input{preamble-eduzy-v2}`: `\def\CheDo{solcolor}`, `\def\tenchuong{<Đơn vị> -- Lần n}`, `\def\thuonghieu{VẬT LÍ 12 -- Eduzy.com.vn}` (nếu không khai thì chân trang in nhầm "TOÁN 12"), `\def\TachCauDS{1}`, `\def\TachCauLG{1}`.
- Dòng 1 khung tiêu đề viết theo mẫu `ĐỀ THI THỬ THPT SỞ GD\&ĐT CAO BẰNG -- LẦN 1`.
- Sau khung tiêu đề là khối `\noindent\textbf{Cho biết:} ...` chép từ đề gốc.
- Bộ macro hình Vật lí (`\VLdienke`, `\VLcoc`, `\VLphich`, `\VLnamcham`, `\VLcham`, `\VLnhan`, `\VLthanhngang`, `\VLthanhdung`, các màu `VLdo`, `VLxanh`, `VLdong`, `VLgo`, `VLla`, các style `VLmui`, `VLgiua`) đang nằm trong file đề mẫu, ngay sau `\input`. Nên chuyển sang file dùng chung `preamble-vatli-hinh.tex`, gọi bằng `\input{preamble-vatli-hinh}`. Tên file bắt đầu bằng "preamble" thì `dong-goi.sh` tự chép vào zip.
  - Đã làm (06/11/2026, phiên 1a): macro nằm trong `preamble-vatli-hinh.tex` (thêm circuitikz `[european]`), đề gọi `\input{preamble-vatli-hinh}` ngay sau `\input{preamble-eduzy-v2}`; `tools/so_hinh.py` đọc macro từ file này. Quy chuẩn đầy đủ nay ở `CLAUDE.md`.

## ex_test tự in sẵn, không viết lại
- Phần I: ex_test tự in dòng "Chọn đáp án X", nên lời giải KHÔNG ghi "Chọn B.".
- Phần III: ex_test tự in ô "Đáp án", nên lời giải KHÔNG ghi "Đáp án: ...".
- Phần II: `itemchoice` tự in "a) Đ/S", sau đó viết `\itemch \textbf{Đúng.}` hoặc `\textbf{Sai.}` kèm lý do hay phép tính một dòng (giống mẫu Toán).

## Văn phong lời giải (thầy đã duyệt)
- Câu trắc nghiệm viết 1–2 dòng: công thức, thế số, kết quả. Câu lý thuyết chỉ một câu nêu lý do.
- Câu Đúng/Sai: nếu nhiều ý dùng chung một dữ kiện thì viết một dòng chung trước `itemchoice`. Ví dụ "Bảo toàn số khối và điện tích: ... X là He-4".
- Câu trả lời ngắn chỉ ghi các bước chính. Biểu thức dài dùng `\[...\]`.
- Không chép lại đề, không viết "Bước 1", không gạch đầu dòng, không giảng lại lý thuyết.

## Cách gõ
- Số và đơn vị: `$1784$~MeV`, `$25~\text{cm}^2$`, `$0{,}15$~T`, `$100\,^\circ\text{C}$`. Dấu thập phân viết `{,}`. Dấu nhân viết `\cdot`.
- Vectơ dùng `\vv{B}`. Kí hiệu hạt nhân viết `$^{235}_{\phantom{2}92}\text{U}$` hoặc `{}^{27}_{13}\text{Al}$`.
- Mỗi câu có comment mã ngay sau `\begin{ex}`: `%[VL12-C<n>-<NB|TH|VD>]`. Mã chủ đề Vật lí 12: C1 là vật lí nhiệt, C2 là khí lí tưởng, C3 là từ trường (gồm cảm ứng điện từ, dòng điện xoay chiều, máy biến áp, sóng điện từ), C4 là vật lí hạt nhân. Lớp 11 dùng `VL11-C<n>`, ví dụ `VL11-C2` cho chương sóng.
- Lỗi chữ của đề gốc (kí hiệu sai, chữ rác, mất chữ) thì sửa trong file đề và ghi vào `kiem-chung.md` của đề đó.

## Hình
- Hình ảnh chụp và hình thực tiễn vẽ lại chi tiết: có khối, tô chuyển màu nhạt, in trắng đen vẫn rõ (xem câu I.9 và II.4 của đề mẫu). Thêm comment `% giuhinh` để `thu-hinh` không thu nhỏ hình.
- Khi đặt hình giữa trang làm trang trước trống nhiều, có thể đặt hình bên phải các phương án bằng hai `minipage` (0,64 và 0,34 `\linewidth`), như câu I.5. Khi đó sửa lời đề "Hình dưới" thành "Hình bên".
- TikZ: KHÔNG dùng `smooth` cho `plot` hàm (hyperbol `12/\x` báo lỗi "Dimension too large"), thay bằng `samples=60`. Lưới vẽ trong hệ trục đã co giãn phải ghi `grid[step=1]`, vì `grid` trần dùng bước 1 cm. Mũi tên giữa đường dùng style `VLgiua`.
- Sau khi vẽ, chạy `python3 tools/so_hinh.py <file.tex> <thư mục ảnh gốc> "<câu>=<ảnh>,..."` để ra ảnh so `so-hinh/NN-cau-*.png` rồi tự soát từng hình. Ảnh gốc trong file Word lấy bằng `unzip -j <file.docx> 'word/media/*' -d <thư mục>`. Hình trong file Word thường neo lệch câu (Word đặt hình ở câu sau), phải đối chiếu với ảnh trang đề.

## Công cụ
- `tools/docx_doc.py <file.docx>` đọc đề Word của thuvienhoclieu tốt: giải mã đủ 244 công thức MathType, lấy cả bảng đáp án và lời giải.
- `tools/dan_trang/dan_trang.py tat-ca <file.tex>` rồi `xuat <file.tex>` chạy được với đường dẫn file đề. Phải có sẵn thư mục `thanh-pham/` thì `xuat` mới chạy, nếu không sẽ báo FileNotFoundError.
- Kết quả đề mẫu: bản đề 7 trang (ĐẠT), bản lời giải 10 trang. Đề mẫu tốn khoảng 1% hạn mức tuần (Opus 5.5).
