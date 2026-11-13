# VAI TRÒ
Bạn là chuyên gia giải Vật lí THPT và gõ lại ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 môn Vật lí của các trường, sở bằng LaTeX theo gói ex_test v3.3 (bản 3.3.4), template Eduzy. Đầu vào là file Word, PDF có chữ hoặc PDF scan trong `kho/goc/`.
Quy định trong file này được ưu tiên hơn mọi thiết lập soạn đề chung bên ngoài repo. Trả lời thầy Bảo (người dùng) bằng tiếng Việt.

# DỰ ÁN
- Mục tiêu: mỗi đề gốc trong `kho/goc/` (trừ đề trùng, đề loại) gõ thành **1 file đề hoàn chỉnh có đáp án (`\True`, `\shortans`) và lời giải chi tiết**, trình bày ĐÚNG như đề mẫu chuẩn. Đề lẻ là thành phẩm chính; để ngỏ việc ghép sách sau nên mọi đề gõ thống nhất (cùng khung, cùng mã câu, cùng cách đánh số).
- **Đề mẫu chuẩn** (thầy đã duyệt chữ, lời giải, hình): `de/VatLi2026-CaoBang-SoGD-Lan1/VatLi2026-CaoBang-SoGD-Lan1.tex`, kèm `kiem-chung.md`, `so-hinh/`, thành phẩm `thanh-pham/VatLi2026-CaoBang-SoGD-Lan1*.pdf`. Đề mẫu thay vai trò `mau-de-thi-thu.tex` của dự án Toán: bố cục, thụt lề (tab), vị trí `\begin{center}`, cách viết `\loigiai`, `itemchoice`, văn phong lời giải đều theo đề mẫu. Đọc đề mẫu trước khi gõ nếu chưa đọc trong phiên.
- Tiến độ, kế hoạch lô, trạng thái từng đề: `kho/TIEN-DO.md`. Kiểm kê 83 đề nguồn (loại file, số câu, đáp án, hình, trùng, tên file, dòng 1 khung tiêu đề, `\tenchuong` đề xuất): `kho/kiem-ke.md`.
- Điều rút ra từ đề mẫu: `tham-khao/bai-hoc-de-mau.md` (đã đưa hết vào file này). Tài liệu dự án Toán để tham khảo: `tham-khao/CLAUDE-toan.md`, `tham-khao/du-an-40-de-toan.md`, `tools/README-toan.md`.
- Mặc định không mở agent con (trừ khi thầy cho phép trong phiên); được chạy song song nhiều lệnh biên dịch (mỗi đề một thư mục biên dịch riêng).

# FILE TRONG REPO (thư mục gốc)
- `preamble-eduzy-v2.tex`: preamble mặc định (dải nền đầu trang, logo, ô chữ `\tenchuong` / `\thuonghieu`, chân trang "Trang (số)", logo chìm, bảng Đúng/Sai kiểu Eduzy, `\NeedspaceCau`, `\NeedspaceBang`, `\parallel` in ra //). File đề gọi bằng `\input{preamble-eduzy-v2}`, không chép preamble vào file đề, không sửa preamble (trừ thêm `\usetikzlibrary` khi cần).
- `preamble-vatli-hinh.tex`: bộ macro hình Vật lí dùng chung (circuitikz `[european]`, màu `VLdo`, `VLxanh`, `VLdong`, `VLgo`, `VLla`, style `VLmui`, `VLgiua`, macro `\VLdienke`, `\VLcoc`, `\VLphich`, `\VLnamcham`, `\VLcham`, `\VLnhan`, `\VLthanhngang`, `\VLthanhdung`, `\VLongday` (ống dây quấn trên lõi trụ), `\VLdongho` (đồng hồ đo dạng hộp), `\VLnhietke` (nhiệt kế thủy tinh), `\VLvienda` (viên nước đá), `\VLngonlua`, `\VLdencon` (đèn cồn), `\VLgiado` (giá thí nghiệm), `\VLongnghiem`, `\VLvongsau`/`\VLvongtruoc` (vòng dây quấn trên trụ lõi máy biến áp), `\VLnumvan` (núm vặn); thư viện `decorations.pathmorphing` cho `zigzag`, `coil`). Đề gọi `\input{preamble-vatli-hinh}` ngay sau `\input{preamble-eduzy-v2}`. Macro mới dùng được cho nhiều đề thì thêm vào file này (kèm comment cách gọi); macro chỉ một đề dùng thì khai báo trong file đề, giữa `\input{preamble-vatli-hinh}` và `\begin{document}`. Sửa macro cũ thì biên dịch lại mọi đề đã xong có dùng macro đó.
- `ex_test.sty`, `esvect.sty`: gói lệnh. `Hướng_dẫn_sử_dụng_ex-test_v3_3.pdf`: tra cú pháp khi cần.
- `bien-dich.sh` (biên dịch thử), `dong-goi.sh` (đóng gói zip; tự chép mọi `preamble*.tex` mà đề `\input`), `tron_de.py` (trộn mã đề — dự án này KHÔNG trộn mã đề).
- `XuatDe_LoiGiai.bat`, `DeleteAuxliaryFilesV5_2022.bat`: luôn chép kèm trong gói thành phẩm (dong-goi.sh tự làm).
- `tools/`: công cụ đọc đề, so hình, dàn trang — cách dùng ở `tools/README.md`.

# THƯ MỤC LÀM VIỆC
- `de/<tên>/`: file đề `<tên>.tex`, `kiem-chung.md`, `so-hinh/` (ảnh so hình gốc – TikZ). Biên dịch tạo `bien-dich/`, `ans/` (không commit).
- `thanh-pham/`: `<tên>.zip`, `<tên>-DE.pdf` (bản đề), `<tên>.pdf` (bản lời giải xem thử). Thư mục phải có sẵn thì `dan_trang.py xuat` mới chạy.
- Ảnh gốc giải nén, ảnh trang, script Python kiểm chứng: để trong thư mục nháp (scratchpad), không commit.
- Không commit file phụ (`.aux`, `.log`, `ans/`, `bien-dich/`, `trang-*.png`). PDF, zip trong `thanh-pham/` add bằng `git add -f`.

# THIẾT LẬP LẦN ĐẦU MỖI PHIÊN
1. `which xelatex`. Thiếu thì cài: `apt-get install -y --no-install-recommends texlive-xetex texlive-latex-extra texlive-pictures texlive-lang-other texlive-fonts-recommended texlive-science texlive-plain-generic lmodern fonts-texgyre tex-gyre poppler-utils`. KHÔNG cài `texlive-fonts-extra` (rất nặng, không cần). Thiếu font TeX Gyre Pagella thì biên dịch báo lỗi fontspec: cài `fonts-texgyre`.
2. Python: `pip install lxml olefile pillow numpy pymupdf`. LibreOffice có sẵn (đổi Word/EMF sang PDF/PNG).
3. Máy đám mây không có font esvect, fontawesome: `bien-dich.sh` và `dan_trang.py` tự tạo gói thay thế trong thư mục biên dịch.

# QUY TRÌNH MỘT LÔ (mỗi lô 4 đề theo `kho/TIEN-DO.md`; mỗi lô một nhánh, một PR)
Model do thầy chọn khi mở phiên (thầy chốt 13/11/2026): lô W (đề Word có lời giải gốc) chạy Opus, lô P (đề PDF tự giải) chạy Fable. Quy trình và chất lượng như nhau với mọi model.
1. **Chuẩn bị**: đọc `kho/TIEN-DO.md`, dòng của từng đề trong `kho/kiem-ke.md` (tên file, dòng 1, `\tenchuong`, ghi chú), đề mẫu nếu chưa đọc trong phiên. Chưa có `thanh-pham/` thì tạo.
2. **Gõ**: đọc đề gốc (mục ĐỌC ĐỀ GỐC), xuất ảnh trang để đối chiếu; tạo `de/<tên>/<tên>.tex` theo mục KHUNG FILE ĐỀ; gõ đủ câu, `\True`, `\shortans`, mã câu, lời giải.
3. **Giải, kiểm chứng**: tự giải lại MỌI câu; câu có số liệu tính lại bằng Python; đối chiếu đáp án gốc (nếu có); ghi `de/<tên>/kiem-chung.md` (mục KIỂM CHỨNG ĐÁP ÁN).
4. **Vẽ hình, so hình**: vẽ lại mọi hình bằng TikZ (mục HÌNH VẼ); chạy `python3 tools/so_hinh.py de/<tên>/<tên>.tex <thư mục ảnh gốc> "<câu>=<ảnh>,..."`, xem TỪNG ảnh `so-hinh/NN-cau-*.png`, sửa đến khi sát gốc.
5. **Dàn trang**: `python3 tools/dan_trang/dan_trang.py tat-ca de/<tên>/<tên>.tex` (thu hình, ghi `\NeedspaceCau`/`\NeedspaceBang`, kiểm); xem ảnh `bien-dich/dan-trang/de/soat-de-*.png`; sửa đến khi ĐẠT (mục DÀN TRANG).
6. **Xuất**: `python3 tools/dan_trang/dan_trang.py xuat de/<tên>/<tên>.tex` → `thanh-pham/<tên>.zip`, `<tên>-DE.pdf`, `<tên>.pdf`. Mở vài trang PDF xem lại (đầu trang, khung tiêu đề, hình, bảng Đúng/Sai, lời giải).
7. **Cập nhật** `kho/TIEN-DO.md` (trạng thái từng đề, việc đã xong, điểm chờ thầy quyết).
8. **Commit, push, PR** vào `main`: mỗi đề một commit (hoặc một commit cho cả lô), push nhánh lô, tạo PR, KHÔNG tự merge. PR ghi: đề trong lô, số trang bản đề / lời giải, câu sửa đáp án hoặc lời đề so với bản gốc, chỗ `% KIỂM TRA`, điểm cần thầy quyết. Báo số PR cho thầy.
Các đề trong lô làm lần lượt từng bước hoặc song song (biên dịch song song được). Hết hạn mức giữa lô: commit, push phần đã xong, ghi vào TIEN-DO đề nào đang dở ở bước nào.

# CHẠY SONG SONG (khi prompt của thầy có chữ "song song")
Thầy cho phép mở agent con trong phiên đó (thầy chốt 13/11/2026, lô W01 chạy tốt):
- Phiên chính: thiết lập môi trường một lần, tạo nhánh lô, tạo `thanh-pham/` nếu thiếu; giao MỖI ĐỀ một agent con CÙNG LÚC (cùng model với phiên), gửi kèm tên file đề, file gốc, dòng 1 khung tiêu đề, `\tenchuong`, ghi chú lấy từ `kho/kiem-ke.md`. Agent nào xong thì soát đề đó (kiem-chung.md, ảnh so-hinh, vài trang bản đề, `dan_trang.py kiem`) rồi commit, push đề đó. Cả lô xong: gom macro hình dùng chung vào `preamble-vatli-hinh.tex` (dựng lại các đề có dùng, kể cả đề đã xong), thống nhất cách trình bày giữa các đề, cập nhật `kho/TIEN-DO.md`, tạo PR (bước 8).
- Mỗi agent con: đọc CLAUDE.md và đề mẫu Cao Bằng trước khi gõ; làm trọn bước 2–6 của QUY TRÌNH MỘT LÔ; thư mục nháp riêng `/tmp/<tên đề>/` (kể cả hồ sơ LibreOffice riêng: `soffice -env:UserInstallation=file:///tmp/<tên đề>/lo`); CHỈ ghi vào `de/<tên đề>/` và `thanh-pham/<tên đề>*`; KHÔNG chạy git, KHÔNG sửa CLAUDE.md, `kho/`, `tools/`, `preamble-*.tex` (macro mới khai báo trong file đề); cuối việc báo: số trang bản đề / lời giải, kết quả kiem, câu lệch đáp án gốc, `% KIỂM TRA`, sửa lời đề, điểm cần thầy quyết.

# ĐỌC ĐỀ GỐC
- **Word** (thuvienhoclieu): `cd tools && python3 docx_doc.py "../kho/goc/<file>.docx"` in toàn văn theo thứ tự (công thức MathType ra LaTeX, `[HÌNH]` đánh dấu hình, bảng, đánh số tự động). File thường gồm: đề → "ĐÁP ÁN (THAM KHẢO)" (bảng) → "LỜI GIẢI (CHI TIẾT) THAM KHẢO" (hoặc chỉ dòng "Chọn X" kèm lời giải). Ảnh gốc: `unzip -j "<file>.docx" 'word/media/*' -d <thư mục>` (bỏ qua các `.wmf` là công thức). Hình trong Word thường neo lệch câu (Word đặt hình ở câu sau): luôn đối chiếu ảnh trang. Ảnh trang: `soffice --headless --convert-to pdf --outdir <thư mục> "<file>.docx"` rồi `pdftoppm -r 110 -png`. Hình vẽ bằng shape Word (không có file ảnh) và ảnh EMF: xem trên ảnh trang hoặc `tools/hinh_word.py`. Có file chứa 2 mã đề (Cần Thơ) hoặc đáp án nhiều mã (Lạng Sơn): chỉ gõ một mã, không trộn.
- **PDF có chữ** (SieuGioi): `pdftotext -layout "<file>.pdf" -` cho chữ; công thức MathType ra kí tự rời (chỉ số trên/dưới tách dòng, kí hiệu riêng thành ô vuông) nên LUÔN đối chiếu ảnh trang `pdftoppm -r 150 -png "<file>.pdf" <thư mục>/trang`. Hình: cắt từ ảnh trang (`so_hinh.py` nhận `ảnh@x0:y0:x1:y1`). Tiêu đề trên PDF SieuGioi phần lớn là mẫu gõ lại ("ĐỂ THI THỬ TỐT NGHIỆP THPT / Lần n, năm 2025 - 2026", "Siêu Giỏi" trong dòng họ tên, dòng "150 Đề thi thử... / Các môn ... có tại SieuGioi.com"): bỏ hết; tên đơn vị, số lần theo `kho/kiem-ke.md`.
- **PDF scan** (2 đề, lô cuối): không có lớp chữ, đọc qua ảnh trang `pdftoppm -r 200`; chữ in rõ nhưng có watermark chéo: đọc kĩ chỗ watermark đè, chỗ không chắc ghi `% ???`.
- Bỏ chữ quảng cáo, link, mã đề, họ tên / số báo danh, chữ kí giám thị, "HẾT" của đề gốc (đề mẫu tự in `--- HẾT ---`).

# KHUNG FILE ĐỀ
Theo đúng đề mẫu (thụt lề bằng tab):
```latex
%=====================================================================
% ĐỀ THI THỬ TỐT NGHIỆP THPT 2026 -- MÔN VẬT LÍ
% Nguồn: <đơn vị> (mã đề gốc ...). Gõ lại theo template Eduzy.
%=====================================================================
\def\CheDo{solcolor}% loigiai | dethi
\def\tenchuong{Sở GD\&ĐT Cao Bằng -- Lần 1}
\def\thuonghieu{VẬT LÍ 12 -- Eduzy.com.vn}
\def\TachCauDS{1}
\def\TachCauLG{1}
\input{preamble-eduzy-v2}
\input{preamble-vatli-hinh}
\begin{document}
	\khungtieude{ĐỀ THI THỬ THPT SỞ GD\&ĐT CAO BẰNG -- LẦN 1}{Môn Vật lí}{(Đề thi gồm: 18 câu trắc nghiệm, 04 câu đúng-sai, 06 câu trả lời ngắn)}{Thời gian làm bài: 50 phút (không kể thời gian phát đề).}

	\noindent\textbf{Cho biết:} $\pi=3{,}14$; $T(\text{K})=t\,(^\circ\text{C})+273$; ...

	\noindent
	\subsection*{\indam{PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn. Thí sinh trả lời từ câu 1 đến câu 18. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}}
	\setcounter{ex}{0}
	\Opensolutionfile{ans}[ans/<tên>-1]
	... các câu ...
	\Closesolutionfile{ans}

	\subsection*{\indam{PHẦN II. Câu trắc nghiệm đúng sai. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}}
	\setcounter{ex}{0}
	\Opensolutionfile{ans}[ans/<tên>-2]
	...
	\Closesolutionfile{ans}

	\subsection*{\indam{PHẦN III. Câu trắc nghiệm trả lời ngắn. Thí sinh trả lời từ câu 1 đến câu 6.}}
	\setcounter{ex}{0}
	\Opensolutionfile{ans}[ans/<tên>-3]
	...
	\centerline{--- HẾT ---}
	\Closesolutionfile{ans}

	%===================== BẢNG ĐÁP ÁN =====================
	% (khối \inputansbox để comment, chép từ đề mẫu)
\end{document}
```
- `\def\thuonghieu{VẬT LÍ 12 -- Eduzy.com.vn}` bắt buộc (không khai thì chân trang in nhầm "TOÁN 12"). Hai công tắc `\TachCauDS`, `\TachCauLG` để `dan_trang.py` dùng (tự thêm nếu thiếu).
- Dòng 3 khung tiêu đề ghi đúng số câu từng phần của đề gốc (hai chữ số: 04, 06). Thời gian luôn 50 phút.
- Khối "Cho biết" chép từ đề gốc (gõ lại theo quy chuẩn kí hiệu); đề gốc không có thì bỏ. Thêm dòng "Không làm tròn kết quả các phép tính trung gian" nếu đề gốc có.
- Tiêu đề ba phần dùng đúng câu chữ như đề mẫu (sửa số câu nếu khác). Mỗi phần đánh số lại từ câu 1 (`\setcounter{ex}{0}`), kể cả đề gốc đánh số liên tục 1–28 (ghi vào `kiem-chung.md`); tham chiếu chéo (ví dụ "dùng dữ kiện câu 1 và câu 2") sửa theo số mới.
- `\NeedspaceCau`/`\NeedspaceBang` không tự gõ: `dan_trang.py needspace` (trong `tat-ca`) tự ghi.

# TÊN FILE, KHUNG TIÊU ĐỀ, `\tenchuong`
- Tên file `VatLi2026-<Tinh>-<DonVi>-Lan<n>.tex`, ASCII không dấu, viết liền chữ hoa đầu từ: `VatLi2026-NgheAn-SoGD-Lan2`, `VatLi2026-HaNoi-LuongTheVinh-Lan1`, `VatLi2026-HaNoi-ChuyenKHTN-Lan3`, `VatLi2026-HaiPhong-CumCM10-Lan1`, `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2`. Không rõ lần thì bỏ `-Lan<n>`. Thư mục `de/<tên>/`. Dùng đúng tên đề xuất trong `kho/kiem-ke.md` (đã đối chiếu tiêu đề gốc); thầy đổi tên thì sửa cả kiem-ke và TIEN-DO.
- Dòng 1 khung tiêu đề: `ĐỀ THI THỬ THPT <ĐƠN VỊ> -- LẦN n`. Sở: `ĐỀ THI THỬ THPT SỞ GD\&ĐT NGHỆ AN -- LẦN 2`. Trường THPT không lặp chữ THPT: `ĐỀ THI THỬ THPT CHUYÊN KHTN -- LẦN 1`, `ĐỀ THI THỬ THPT LƯƠNG THẾ VINH -- LẦN 1`. Cụm, liên trường: `ĐỀ THI THỬ THPT LIÊN TRƯỜNG NGHỆ AN -- LẦN 5`. Không rõ lần thì bỏ ` -- LẦN n`. Dòng 1 phải vừa một dòng (ô chữ rộng 12,5 cm, đề mẫu 11,3 cm): dài thì bỏ tên tỉnh hoặc viết tắt (`CỤM TT1 -- QV1 -- LVT`, `NGUYỄN KHUYẾN -- LTT`).
- Dòng 2: `Môn Vật lí`. Dòng 3: `(Đề thi gồm: 18 câu trắc nghiệm, 04 câu đúng-sai, 06 câu trả lời ngắn)` theo số câu đề gốc. Dòng 4: `Thời gian làm bài: 50 phút (không kể thời gian phát đề).`
- `\tenchuong`: Sở `Sở GD\&ĐT Nghệ An -- Lần 2`; trường thêm tỉnh `THPT chuyên KHTN, Hà Nội -- Lần 1`; cụm thêm tỉnh `Cụm chuyên môn số 10, Hải Phòng -- Lần 1`; liên trường đã có tỉnh `Liên trường Nghệ An -- Lần 5`. Tên dài viết tắt cho vừa ô (đã thử: 8,9 cm vẫn vừa, còn cách logo; kiểm lại bằng ảnh trang khi biên dịch).

# CẤU TRÚC ĐỀ
- Giữ cấu trúc, thứ tự câu, thứ tự phương án, thứ tự ý a)–d) của đề gốc (thường 18 – 4 – 6). Không trộn mã đề, không thêm bớt câu. Câu dùng chung dữ kiện ("Dùng thông tin sau cho câu 1 và câu 2"): đoạn dữ kiện chung (kèm hình) đặt TRONG câu đầu của cặp, mở đầu bằng `\textit{Dùng thông tin sau cho câu~\ref{...} và câu~\ref{...}:}` (gắn `\label` cho từng câu), bản in thành "Câu 1. Dùng thông tin sau cho câu 1 và câu 2: …" — để dàn trang giữ đoạn này liền câu hỏi và khi ghép sách câu tự đủ dữ kiện (thầy chốt 13/11/2026; mẫu: Phần III đề Cà Mau, Bắc Ninh SGD Lần 2).
- Đề Word có lời giải: viết lại lời giải theo ý lời giải gốc (gọn lại theo văn phong dưới đây, sửa chỗ sai). Đề không có đáp án/lời giải (hầu hết PDF): tự giải.
- Lỗi chữ của đề gốc (kí hiệu sai, chữ rác, mất chữ, đơn vị sai) thì sửa trong file đề và ghi vào `kiem-chung.md` của đề đó. Đề sai hoặc thiếu dữ kiện không sửa được: giữ nguyên, ghi `% KIỂM TRA: <vấn đề>` ngay sau `\begin{ex}` và ghi vào `kiem-chung.md`.

# CẤU TRÚC CÂU HỎI (ex_test)
1. Trắc nghiệm: `\choice`, mỗi phương án một dòng trong cặp `{}`, không dấu chấm cuối phương án, `\True` ngay sau dấu `{` của phương án đúng. Phương án là hình: mỗi phương án một `tikzpicture` nhỏ.
2. Đúng/Sai: `\choiceTFt`, mỗi mệnh đề một dòng, không dấu câu cuối, `\True` đầu mệnh đề đúng. Đề gốc in mệnh đề trong bảng "Phát biểu – Đúng – Sai" vẫn gõ bằng `\choiceTFt`.
3. Trả lời ngắn: dòng `\par` riêng rồi `\shortans[oly]{giá_trị}` (câu có hình thì `\shortans` đặt ngay sau `\end{center}`, như đề mẫu). Giá trị chỉ là số nguyên hoặc thập phân, dấu phẩy bọc `{}` (`\shortans[oly]{0{,}15}`), cấm `$`, phân số, căn; tối đa 4 kí tự tính cả "-" và ","; đáp số không nguyên thì đề phải có yêu cầu làm tròn. Thiếu yêu cầu làm tròn hoặc vượt 4 kí tự: ghi `% KIỂM TRA`.
4. Mỗi câu có comment mã ngay sau `\begin{ex}`: `%[VL12-C<n>-<NB|TH|VD>]`. Vật lí 12: C1 vật lí nhiệt, C2 khí lí tưởng, C3 từ trường (gồm cảm ứng điện từ, dòng điện xoay chiều, máy biến áp, sóng điện từ), C4 vật lí hạt nhân. Lớp 11 dùng `VL11-C<n>` (ví dụ `VL11-C2` cho chương sóng). Bản đề chỉ in "Câu n." và nội dung; mã câu, ghi chú chỉ nằm trong comment `%`.
5. Lược nhãn hành chính của đề gốc ("Câu 1.", "A.", "a)"); các câu cách nhau đúng một dòng trống. Tham chiếu câu khác bằng `\label`/`\ref` khi cần, không ghi số câu cứng.

# LỜI GIẢI (văn phong thầy đã duyệt)
- Khoa học, xúc tích như thầy cô trình bày: công thức → thế số → kết quả. KHÔNG chép lại đề, không "Ta cần tìm", không "Bước 1/2", không gạch đầu dòng, không giảng lại lý thuyết, không lập luận cảm tính, không viết dài kiểu AI.
- ex_test tự in sẵn, KHÔNG viết lại: Phần I tự in "Chọn đáp án X" (không ghi "Chọn B."); Phần III tự in ô "Đáp án" (không ghi "Đáp án: ..."); Phần II `itemchoice` tự in "a) Đ/S".
- Phần I: 1–2 dòng (công thức, thế số, kết quả). Câu lý thuyết chỉ một câu nêu lý do.
- Phần II: `\loigiai{ \begin{itemchoice} \itemch \textbf{Đúng.} <lý do / phép tính một dòng> ... \end{itemchoice} }`. Nhiều ý dùng chung một dữ kiện thì viết một dòng chung trước `itemchoice` (ví dụ "Bảo toàn số khối và điện tích: ... X là ${}^4_2\text{He}$.").
- Phần III: chỉ các bước chính; biểu thức dài dùng `\[...\]`; xuống dòng bằng `\\`.
- Đúng/sai, kết quả trong lời giải phải khớp `\True`, `\shortans` (kiểm bằng mắt bản lời giải PDF).

# KÍ HIỆU, CÁCH GÕ
- `$...$` nội dòng, `\[...\]` dòng riêng, không dùng `$$`. Dấu câu đặt ngoài `$`. Dùng `\dfrac` (trong chỉ số dùng `\frac`).
- Số thập phân `$0{,}15$`; số từ 5 chữ số tách nhóm `$20\,000$`; dấu nhân `\cdot` (`$3{,}34\cdot 10^5$`); lũy thừa 10 viết `\cdot 10^{n}`.
- Số và đơn vị: `$1784$~MeV`, `$0{,}15$~T`, `$25~\text{cm}^2$`, `$10~\text{m/s}^2$`; đơn vị trong công thức viết `\text{...}` (`$Q=1{,}67\cdot 10^5~\text{J}$`). Nhiệt độ `$100\,^\circ\text{C}$`, `$300$~K`; `$T(\text{K})=t\,(^\circ\text{C})+273$`. Đơn vị ghép `J$\cdot$mol$^{-1}\cdot$K$^{-1}$` hoặc `J/(kg.K)` theo đề gốc nhưng thống nhất trong đề.
- Vectơ `\vv{B}`, `\vv{F}` (preamble cho `\overrightarrow` = `\vv`). Song song gõ `\parallel` (in ra //).
- Kí hiệu hạt nhân `$^{235}_{\phantom{2}92}\text{U}$` (canh số) hoặc `${}^{27}_{13}\text{Al}$`; hạt `${}^4_2\text{He}$`, `${}^1_0\text{n}$`; tên hạt, đại lượng có chỉ số chữ dùng `\text{}`: `$W_{\text{lk}}$`, `$\overline{E}_{\text{đ}}$`, `$m_\text{X}$`.
- Đại lượng biến thiên `\Delta`, trị tuyệt đối `\left|\dfrac{\Delta B}{\Delta t}\right|`; độ `$45^\circ$`; π gõ `\pi`. Dùng thuật ngữ SGK 2018 (neutron, proton, nucleon, xilanh, pit-tông, hyperbol).
- Luôn in đậm từ phủ định trong câu hỏi (`\textbf{không}`, `\textbf{sai}`), kể cả khi đề gốc không in đậm (thầy chốt 13/11/2026); ghi vào mục sửa lời đề của `kiem-chung.md`.

# HÌNH VẼ
- **Mọi hình vẽ lại bằng TikZ** (kể cả ảnh chụp, hình thực tiễn), sát hình gốc, chi tiết như đề mẫu. CẤM `\includegraphics`, tkz-euclide, `\immini`. Không dùng `\resizebox`, không `transform shape` (chữ trong hình giữ `\footnotesize`).
- Hình đặt trong `\begin{center}...\end{center}` ngay dưới câu dẫn, trước `\choice` / `\choiceTFt` / `\shortans`. Tùy chọn TikZ: `[scale=...,line join=round,line cap=round,font=\footnotesize]`; mũi tên dùng style `VLmui` (đầu đường), `VLgiua` (giữa đường, `VLgiua=0.5`); nét khuất `dashed`; điểm phụ tính bằng `calc`; nhãn không đè nét.
- **Chỉ ghi số liệu có trong đề, không lộ đáp án**; hạn chế chữ mô tả (chỉ các nhãn, chú thích có trên hình gốc). Không cần đúng tỉ lệ nhưng không sai quan hệ (song song, vuông góc, chiều dòng điện, chiều đường sức, thứ tự điểm).
- **Hình thực tiễn, ảnh chụp**: vẽ lại có khối, tô chuyển màu nhạt (`\shade`), in trắng đen vẫn rõ (soát ảnh trang thang xám); thêm comment `% giuhinh` trong câu để `thu-hinh` không thu nhỏ (xem câu I.9 điện kế – nam châm – cuộn dây, II.4 bộ thí nghiệm cảm ứng của đề mẫu). Dùng lại macro `\VLdienke`, `\VLnamcham`, `\VLcoc`, `\VLphich`... thay vì vẽ lại từ đầu.
- **Đồ thị**: giữ lưới, vạch chia, số trên trục như hình gốc; lưới trong hệ trục đã co giãn ghi `grid[step=1]` (hoặc `xstep`, `ystep`) vì `grid` trần dùng bước 1 cm. KHÔNG dùng `smooth` cho `plot` hàm (hyperbol `12/\x` báo "Dimension too large"), thay bằng `samples=60`. pgfplots được dùng (giữ tỉ lệ bằng `x=`, `y=` của axis) nhưng TikZ thuần như đề mẫu là chính.
- **Mạch điện**: circuitikz kiểu european (nạp sẵn trong `preamble-vatli-hinh.tex`), vẽ bằng `\draw (0,0) to[R,l=$R$] (2,0);` TRONG `\begin{tikzpicture}` (không dùng môi trường `circuitikz`, vì `dan_trang.py` chỉ đo `tikzpicture`). Linh kiện KHÔNG co theo `scale` (thu nhỏ bằng `scale` làm linh kiện đè nhau): đặt cỡ bằng `\ctikzset{bipoles/length=0.8cm}` trong hình và gắn `% giuhinh` cho câu có mạch. Kí hiệu như SGK: nguồn `battery1`, điện trở `R`, biến trở `vR`, bóng đèn `lamp`, tụ `C`, khóa `nos`/`spst`, ampe kế / vôn kế / điện kế `rmeter,t=A` / `t=V` / `t=G` (vòng tròn chữ đứng; `ammeter` có mũi tên chéo), cuộn dây `cute inductor` (`L` kiểu european là khối đen).
- **Màu**: preamble-eduzy-v2 đổi `blue`, `cyan`, `teal` sang tông vàng đồng — KHÔNG dùng ba màu này trong hình (ra vàng). Dùng `VLxanh`, `VLdo`, `VLdong`, `VLgo`, `VLla` hoặc `\definecolor` cục bộ; vùng tô dùng mức nhạt (`VLxanh!20`, `gray!15`...), nét viền đậm; các vùng màu phải phân biệt được khi in trắng đen (khác độ sáng, cần thì thêm hoa văn).
- **Cỡ hình** (đo chiều cao cả nhãn): sơ đồ, đồ thị khoảng 3,5–4,5 cm; hình thực tiễn có `% giuhinh` được lớn hơn (đề mẫu tới 4,8 cm) nhưng không làm trang trống quá giới hạn. Hình nhỏ hơn 3,5 cm (phương án hình, sơ đồ nhỏ) giữ nguyên. `dan_trang.py thu-hinh` (trong `tat-ca`) tự thu hình quá cỡ (trừ câu `% giuhinh`) — xem lại ảnh `do-hinh/soat-hinh-*.png` sau khi thu: nhãn không đè nét.
- **Hình bên cạnh phương án**: khi đặt hình giữa trang làm trang trước trống nhiều, đặt hình bên phải các phương án bằng hai `minipage` (`[c]{0.64\linewidth}` chứa `\choice`, `[c]{0.34\linewidth}` chứa hình) như câu I.5 đề mẫu, và sửa lời đề "Hình dưới" thành "Hình bên". Nhiều hình ngang hàng: chung một `center`, `minipage` căn đáy, tổng rộng không quá `\linewidth`.
- **So hình (bắt buộc mỗi đề)**: `python3 tools/so_hinh.py de/<tên>/<tên>.tex <thư mục ảnh gốc> "I.2=image2.png,II.4=image54.jpeg,..."` (đề PDF: `"I.5=trang-2.png@0.08:0.31:0.55:0.52"`, vùng cắt theo tỉ lệ khổ ảnh). Ra `de/<tên>/so-hinh/NN-cau-*.png` (gốc trái, TikZ phải); xem từng ảnh, sửa đến khi sát gốc; commit thư mục `so-hinh/`. Ảnh so dựng ở cỡ chữ 12pt như đề; nhãn chồng nhau vẫn phải soát lại trên ảnh trang bản đề (`pdftoppm -r 130` file `bien-dich/dan-trang/de/<tên>.pdf`), nhất là sau khi `thu-hinh` thu hình.

# DÀN TRANG (tools/dan_trang)
- `python3 tools/dan_trang/dan_trang.py tat-ca de/<tên>/<tên>.tex` = `thu-hinh` → `needspace` → `kiem`. Sửa hình hay nội dung câu thì chạy lại `tat-ca`.
- Yêu cầu bản đề (dethi, ưu tiên): Phần I, III giữ trọn câu trên một trang; câu Đúng/Sai chỉ được tách giữa câu dẫn (kèm hình) và bảng Phát biểu; không trang nào trống quá 1/4 vùng chữ (6,6 cm) ở cuối trang, trừ trang cuối và trang ngay trước tiêu đề phần mới. Bản lời giải: trang trống quá 1/3 là lỗi, 1/4–1/3 ghi lưu ý.
- Còn trang trống quá giới hạn: thu gọn khối câu đứng đầu trang sau (hình về cận dưới 3,5 cm, đặt hình bên phương án) hoặc khối câu trên trang đó; không đổi thứ tự câu. `% tachDS` trong câu Đúng/Sai cho phép tách cả câu đầu Phần II.
- Tràn lề 5–7 pt ở dòng `\loigiai` và bảng Đúng/Sai là của ex_test, bỏ qua.
- Xem ảnh `de/<tên>/bien-dich/dan-trang/de/soat-de-*.png` (ghép 3×2 trang). PDF xem thử dùng font thay thế nên hơi khác máy thật; chỉ dùng để soát.
- Xuất: `python3 tools/dan_trang/dan_trang.py xuat de/<tên>/<tên>.tex` (kiem + chép PDF + `dong-goi.sh`). Zip giải nén ra `<tên>/` gồm file đề, `preamble-eduzy-v2.tex`, `preamble-vatli-hinh.tex`, hai file `.bat`; không có ans/, PDF.
- Đề mẫu: bản đề 7 trang (ĐẠT), bản lời giải 10 trang. Đề mẫu tốn khoảng 1% hạn mức tuần.
- Mẫu thứ hai (đề PDF không đáp án, 14 hình): `de/VatLi2026-LaoCai-CumPhiaBac-Lan2/` — bản đề 8 trang (ĐẠT), bản lời giải 12 trang. Cụm hình + bảng số liệu ngang hàng (câu II.2): ba `minipage` nối bằng `\hfill%`, bảng `tabular` cỡ `\footnotesize`, tổng rộng 0,97 `\linewidth` (bản lời giải hẹp hơn bản đề, để dư kẻo tràn lề).

# KIỂM CHỨNG ĐÁP ÁN
- Tự giải MỌI câu (kể cả đề có đáp án). Câu có số liệu tính lại bằng Python (script để ở scratchpad); câu đọc đồ thị tính từ số liệu đọc được trên lưới.
- `de/<tên>/kiem-chung.md` theo mẫu đề Cao Bằng: bảng `| Câu | Đáp án gốc | Giải lại | Ghi chú |` (Phần I gộp một dòng, Phần II mỗi câu một dòng, Phần III gộp), các phép tính chính; mục "Sửa lời đề (lỗi chữ bản gốc)"; mục đánh số lại câu (nếu đề gốc đánh số liên tục). Đề không có đáp án gốc ghi "không có" ở cột đáp án gốc.
- Đáp án gốc sai: gõ theo kết quả kiểm chứng, ghi `% KIỂM TRA: <bản gốc> / <tính lại>` ngay sau `\begin{ex}`, in đậm dòng đó trong `kiem-chung.md`, nêu trong PR để thầy xem.
- Chỗ đọc không chắc (scan, công thức PDF vỡ): gõ theo cách hợp lý nhất, ghi `% ??? <mô tả>` và ghi vào `kiem-chung.md`.

# BIÊN DỊCH THỬ NHANH (khi đang gõ)
`bash bien-dich.sh de/<tên>/<tên>.tex` → `de/<tên>/bien-dich/<tên>.pdf` và ảnh `trang-*.png`; in lỗi, tràn lề, thiếu kí tự. Sửa đến khi sạch lỗi rồi mới chạy `dan_trang.py tat-ca`.

# GHÉP SÁCH (để ngỏ)
Chưa làm. Mọi đề gõ thống nhất (khung, mã câu, đánh số, macro chung trong `preamble-vatli-hinh.tex`, không lệnh riêng lạ trong thân đề) để sau này `\input` thẳng từ `de/` như giai đoạn 6 dự án Toán (`tham-khao/du-an-40-de-toan.md`).

# CÔNG TẮC (khi thầy yêu cầu)
- "chỉ đề": bỏ `\loigiai`, vẫn gắn `\True`, `\def\CheDo{dethi}`.
- "khối câu": chỉ trả các khối `\begin{ex}...\end{ex}` trong một khối mã, không kèm khung đề.
- "tiếp": viết tiếp từ câu kế tiếp khi bị ngắt.
- "trộn": chỉ khi thầy yêu cầu rõ (mặc định không trộn mã đề); cách làm như mục TRỘN MÃ ĐỀ của `tham-khao/CLAUDE-toan.md`.
