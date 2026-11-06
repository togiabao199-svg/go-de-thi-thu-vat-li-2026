# DỰ ÁN 40 ĐỀ LUYỆN THI TN THPT 2027

Đọc file này cùng CLAUDE.md trước khi làm bất kỳ việc gì thuộc dự án. Mọi quy chuẩn soạn đề, ký hiệu, hình vẽ, biên dịch, đóng gói vẫn theo CLAUDE.md. Tiến độ ghi trong kho/TIEN-DO.md.

## Mục tiêu
- 40 đề lẻ, đánh số Đề 01 → Đề 40. Mỗi đề là một file .tex hoàn chỉnh (preamble v2), tên file LuyenDe-TN2027-De01.tex … LuyenDe-TN2027-De40.tex, thư mục de/LuyenDe-TN2027-DeXX/.
- 40 đề lẻ là thành phẩm chính. Giai đoạn 6 (quyết định người dùng 05/11/2026) ghép 40 đề thành 2 quyển sách (Quyển Đề, Quyển Lời giải); file đề lẻ không đổi.
- Cấu trúc mỗi đề theo CLAUDE.md: 12 trắc nghiệm, 4 Đúng/Sai, 6 trả lời ngắn, 90 phút.
- \khungtieude ghi "ĐỀ LUYỆN THI TỐT NGHIỆP THPT NĂM 2027 -- ĐỀ SỐ XX".

## Nguồn câu hỏi
- kho/de-tu-soan/ : 43 đề người dùng tự soạn, ƯU TIÊN DÙNG TRƯỚC. Các file đã nằm sẵn trong kho/de-tu-soan/; danh sách và tên file gốc ở kho/de-tu-soan/DANH-SACH.md.
  - thi-thu/TT01 → TT33 (33 đề thi thử) và TT30plus (bản nâng cao của Đề 30, dùng như nguồn bổ sung).
  - minh-hoa-nang-cao/NC01 → NC10 (10 đề minh họa nâng cao).
  - Mỗi file *-dap-an.docx chứa đủ đề + đáp án + lời giải, công thức là đối tượng MathType (có nhúng mã LaTeX).
  - Riêng TT32: file Word đáp án gốc bị trùng với Đề 31, nên có TT32-de.docx (đề) + TT32-dap-an.pdf (lời giải).
  - Đây là các file "đáp án" lấy từ máy; nếu cần bản đề không lời giải hay PDF để đối chiếu thì hỏi người dùng.
- kho/de-truong-so/ : 180 file đề thi thử, khảo sát của các trường, sở năm học 2025-2026 (TS001 → TS180; Word, công thức MathType có nhúng mã LaTeX). Các file đã nằm sẵn trong kho/de-truong-so/; tên gốc ở kho/de-truong-so/DANH-SACH.md. Chỉ dùng để bổ sung khi kho tự soạn thiếu câu, có câu dở hoặc câu không đúng chuẩn đề TN THPT hiện hành. Lưu ý: một số file là đề kiểm tra tháng/đầu năm (phạm vi hẹp), đề Cần Thơ chia 2 file; đề cũ chưa đúng cấu trúc 2025+ thì bỏ.
- Nguồn đã được người dùng xác nhận được phép sử dụng.

## Nguyên tắc phân bổ câu (QUAN TRỌNG)
- Độ khó xét theo TỪNG CÂU, không theo nguồn đề. Đề nào (TT, NC hay TS) cũng có câu dễ lẫn câu khó.
- Đọc hết mọi câu của mọi đề, gắn mức độ cho từng câu, rồi rã toàn bộ đề gốc ra: câu dễ của mọi nguồn gom vào nhóm đề 01 → 20, câu khó vào nhóm đề 21 → 40.
- Không giữ nguyên đề gốc nào; mỗi đề mới là câu trộn từ nhiều đề gốc khác nhau.
- Nguồn chỉ quyết định thứ tự ưu tiên khi có nhiều câu cùng loại, cùng mức: ưu tiên kho tự soạn (TT, NC) trước, kho trường sở (TS) sau.

## Hai mức đề

### Đề 01 → 20: mức cơ bản
- Phần I (12 câu): nhận biết, thông hiểu thông thường; không có bẫy, đọc là thấy hướng làm.
- Phần II: Câu 1 LUÔN là toán thuần, rất dễ (xem quy định Phần II ở mục Chung). Câu 2 → 4 là toán thực tiễn, mức vừa phải (tối đa 1 ý VD).
- Phần III (6 câu): toán thực tiễn, chỉ câu TH hoặc VD dễ (một hai bước, số liệu gọn, câu hỏi trực tiếp).

### Đề 21 → 40: mức đề thi thật
- Độ khó và phân bố mức độ ngang đề tham khảo/chính thức của Bộ GD&ĐT, có câu vận dụng, vận dụng cao ở Phần II và Phần III.
- Phần II: câu 1 là câu dễ toán thuần (xem mục Chung); câu 2 → 4 có ý c, d mức VD. Riêng câu xác suất được dùng câu "cần sửa" có ý c, d mức VD (miễn không cụt ý, không thiếu dữ kiện).

### Chung
- Mỗi câu hỏi chỉ xuất hiện một lần trong cả 40 đề. Không dùng hai câu gần như trùng nhau (cùng dạng, chỉ đổi số) trong cùng một đề.
- Trong mỗi phần, câu xếp từ dễ đến khó.
- Phủ đều chủ đề giữa các đề; đề sau không lặp lại y nguyên cơ cấu chủ đề của đề trước.
- Mọi hình vẽ lại bằng TikZ (theo mục HÌNH VẼ của CLAUDE.md), kể cả hình trong kho nguồn đang là ảnh.
- **Phần I (quy định cứng, cả 40 đề, 05/11/2026):** chỉ gồm câu toán thuần mức nhận biết, thông hiểu. Câu thực tiễn chỉ được giữ nếu là câu thống kê đọc bảng số liệu (2D3, 1D3, 0D5) hoặc câu chuyển động hỏi vận tốc (đạo hàm, 1D9 bài 1 dạng 2). Đã thay 4 câu: Đề 18 câu 12 TS004-I-09 → TS119-I-10, Đề 27 câu 9 TS004-I-11 → TS007-I-05, Đề 29 câu 12 TS009-I-08 → TS028-I-08, Đề 31 câu 7 TS003-I-12 → TS030-I-07 (câu cũ ghi vào `kho/danh-gia/khong-dung.tsv`; `tools/phan_bo/chon_cau.py` kiểm quy tắc này qua `phan_I_hop_le`).
- **Phần II (quy định cứng, cả 40 đề, 03/11/2026):** 4 câu Đúng/Sai gồm đúng 4 chuyên đề hàm số, Oxyz, tích phân, xác suất, mỗi chuyên đề một câu; không dùng chuyên đề khác (không thống kê, không vectơ không tọa độ, không mũ – lôgarit...). Câu 1 là câu hàm số dễ hoặc Oxyz dễ (toán thuần, mọi ý NB/TH), luân phiên giữa các đề; câu 1 là hàm số thì một câu sau là Oxyz và ngược lại. Oxyz gồm phương pháp tọa độ (2H5) và tọa độ điểm, vectơ trong hệ Oxyz (2H2 bài 2, 3).
- **Phần III (quy định cứng, cả 40 đề, 04/11/2026):** có ĐÚNG 1 câu hình học không gian (khoảng cách, góc, thể tích...). Đề 01–20 nếu thiếu câu hình không gian thực tiễn dễ thì dùng câu hình không gian toán thuần mức TH hoặc VD dễ. Đề có câu Oxyz ở Phần III vẫn giữ Oxyz; câu bị thay là câu không phải Oxyz (ưu tiên câu cùng chuyên đề bị lặp hoặc câu lớp 10–11). Đề 21–40: III.1 là câu hình không gian, không thêm câu hình không gian thứ hai. Chi tiết: `kho/ma-tran.md`.
- **Cấm câu ép đáp số** kiểu "tính 7220a", "a + b + c", "x + yz", "100p" ở cả 40 đề (cờ `ep` trong `kho/danh-gia/do-kho-tln.tsv`).
- Không dùng câu cụt ý, thiếu dữ kiện, đề sai (`kho/danh-gia/khong-dung.tsv`); không dùng câu "cần sửa" khi cùng ô còn câu "tốt" (trừ ô xác suất Phần II đề 21 → 40 nói trên).

## Các giai đoạn (mỗi giai đoạn một hoặc nhiều phiên; xong mỗi giai đoạn cập nhật kho/TIEN-DO.md, push và chờ người dùng duyệt)

Thứ tự đã đổi theo quyết định người dùng (03/11/2026): sau giai đoạn 2 làm MA TRẬN VÀ PHÂN BỔ trước, rồi mới KIỂM CHỨNG ĐÁP ÁN (chỉ các câu đã chọn và câu dự phòng).

1. TRÍCH XUẤT
   - Viết script trong tools/ để đọc file Word, lấy mã LaTeX từ công thức MathType, tách từng câu hỏi.
   - Mỗi đề nguồn ra một file kho/ngan-hang/<nguon>/<ten-de>.json; mỗi câu gồm: id, nguồn (tu-soan / truong-so), tên đề gốc, số câu gốc, loại (TN / DS / TLN), nội dung LaTeX, phương án hoặc mệnh đề, đáp án, lời giải gốc nếu có, mô tả hình (có hình hay không, hình gì).
   - Chạy thử trước trên 3 đề mỗi kho, xuất file .tex xem thử, dừng chờ duyệt rồi mới chạy toàn bộ.

2. ĐÁNH GIÁ VÀ PHÂN LOẠI (đọc hết mọi câu, không lấy mẫu)
   - Gắn cho từng câu: chủ đề, mã dạng (kiểu %[2H5N2-2]), mức độ (NB / TH / VD / VDC), kiểu (toán thuần / thực tiễn), chất lượng (tốt / cần sửa / loại) kèm lý do ngắn, đánh dấu câu trùng hoặc gần trùng.
   - Câu "loại": sai kiến thức, ngoài chương trình GDPT 2018, sai chuẩn định dạng đề TN THPT mới (ví dụ đáp án trả lời ngắn không ghi được trong 4 ký tự mà không sửa được), lời văn tối nghĩa.
   - Xuất kho/thong-ke.md: số câu theo chủ đề × mức độ × loại câu, tách riêng hai kho, chỉ ra chỗ thiếu.
   - (Đã xong, đã duyệt 03/11/2026.) Quy ước đã chốt: câu kiểu Bernoulli giải được bằng đếm cổ điển/quy tắc nhân → cần sửa (viết lại lời giải), không loại; "trùng" = cùng đề bài (kể cả khác phương án nhiễu, đổi tên người) → câu đứng sau (TT < NC < TS) bị loại; "gần trùng" = đổi số liệu hoặc cùng bảng số liệu hỏi khác → không xếp chung một đề.

3. MA TRẬN VÀ PHÂN BỔ (làm trước kiểm chứng — theo quyết định người dùng 03/11/2026) — **ĐÃ XONG, đã duyệt 03/11/2026**: `kho/ma-tran.md`, `kho/phan-bo.csv` (880 câu), `kho/du-phong.csv` (87 câu), `kho/phan-bo.md`; script `tools/phan_bo/` (`ma_tran.py`, `chon_cau.py`, `xuat_nhap.py`, `ep_dap_so.py`).
   - Đề xuất ma trận chủ đề × mức độ cho đề cơ bản và đề mức thi thật, ghi vào kho/ma-tran.md, dừng chờ duyệt.
   - Sau khi duyệt: chọn câu cho 40 đề, lập kho/phan-bo.csv (đề số, phần, vị trí, id câu, nguồn). Ưu tiên kho tự soạn; chỉ lấy kho trường sở khi thiếu. Chỉ chọn câu chất lượng tốt hoặc cần sửa; không chọn câu loại.
   - Kèm khoảng 10% câu dự phòng (kho/du-phong.csv, cùng cột, ghi ô ma trận mà câu dự phòng thay được), để thay ngay khi giai đoạn kiểm chứng phát hiện câu sai không sửa được.
   - Không xếp hai câu trùng hoặc gần trùng (kho/danh-gia/trung.tsv) vào cùng một đề; câu trùng chỉ dùng một lần trong cả 40 đề.
   - Đúng/Sai mức thi thật: độ khó lấy từ ý c, d mức VD (không đòi cả câu mức VDC, vì kho chỉ có 8 câu ĐS thực tiễn VDC).
   - Liệt kê các ô ma trận vẫn thiếu câu (nếu có) để người dùng quyết định soạn mới hay nới ma trận.
   - Quy tắc chọn câu bổ sung (quyết định 03/11/2026, sau khi xem nháp Đề 01, Đề 21):
     - Độ khó dùng mức đã chấm ở giai đoạn 2, không đoán theo độ dài lời giải. Đề 01–20, Phần III chỉ lấy câu TH hoặc VD dễ (một hai bước, số liệu gọn, câu hỏi trực tiếp); "VD dễ" lấy theo điểm con chấm thêm ở `kho/danh-gia/do-kho-tln.tsv`. Cấm câu ép đáp số ở cả 40 đề.
     - Cả 40 đề: Phần III xếp từ dễ đến khó, câu khó nhất ở cuối.
     - Cả 40 đề: không dùng câu "cần sửa" nếu cùng ô còn câu "tốt"; tuyệt đối không dùng câu cụt ý, thiếu dữ kiện (danh sách `kho/danh-gia/khong-dung.tsv` và cờ `hong` trong `do-kho-tln.tsv`).

4. KIỂM CHỨNG ĐÁP ÁN (chỉ các câu đã chọn và câu dự phòng)
   - Tự giải, câu tính toán kiểm bằng Python, đếm/xác suất kiểm bằng liệt kê; ghi kết quả (đã kiểm / đã sửa đáp án / nghi vấn). Ưu tiên các câu đã ghi "nghi đáp án" ở giai đoạn 2.
   - Câu sai không sửa được thì thay bằng câu dự phòng cùng ô ma trận, cập nhật phan-bo.csv (thêm câu vào `kho/danh-gia/khong-dung.tsv` rồi chạy `python3 tools/phan_bo/chon_cau.py --giu`: giữ nguyên các câu khác, chỉ chọn lại vị trí đó).
   - Kiểm trước tiên các câu có `uu_tien_kiem` = x trong `kho/phan-bo.csv` (câu nghi đáp án được duyệt cho dùng: TT14-II-01 sửa ý d; NC05-II-04; TS091-II-04), rồi các câu "cần sửa".

5. SOẠN ĐỀ
   - Soạn theo lô (ví dụ 5 đề mỗi phiên): gõ theo CLAUDE.md, vẽ lại hình TikZ, biên dịch, đóng gói thanh-pham/LuyenDe-TN2027-DeXX.zip kèm PDF xem thử.
   - Mặc định có lời giải và gắn \True theo CLAUDE.md, trừ khi người dùng yêu cầu khác.
   - Đề thành phẩm chỉ có "Câu n." (ex_test tự đánh số) và nội dung câu; KHÔNG in mã câu, ô ma trận, mức hay ghi chú chấm. Các thông tin đó chỉ có trong bản nháp phân bổ (`thanh-pham/XemThu-PhanBo-DeXX.pdf`). Mã câu nguồn chỉ được giữ ở dòng comment `%` ngay sau `\begin{ex}` để tra cứu, không in ra (quyết định 03/11/2026).

6. GHÉP 40 ĐỀ THÀNH 2 QUYỂN SÁCH (yêu cầu người dùng 05/11/2026; in 2 mặt, khổ A4) — nguồn ở `sach/`
   - **Quyển Đề** `sach/Sach-LuyenDe-TN2027-QuyenDe.tex`: bìa trước `bia/bia-07.tex` giữ nguyên (trang 1, mặt sau trắng); lời nói đầu ngắn (khoảng nửa trang, văn phong trung tính: không quảng cáo, không câu động viên, không con số thống kê trong tiêu đề); trang cấu trúc đề và hướng dẫn chấm theo thang 2025 (90 phút; Phần I 12 câu × 0,25; Phần II 4 câu, mỗi câu đúng 1 ý 0,1 – 2 ý 0,25 – 3 ý 0,5 – 4 ý 1; Phần III 6 câu × 0,5); mục lục Đề số 01 … 40, Bảng đáp án kèm số trang; 40 đề chế độ `dethi`; bảng đáp án cuối sách (mỗi đề một khối Phần I, II, III, nhiều đề một trang, đọc từ `ans/` do ex_test sinh ra, không gõ tay); bìa sau `bia/bia-07-sau.tex`.
   - **Quyển Lời giải** `sach/Sach-LuyenDe-TN2027-QuyenLoiGiai.tex`: bìa trước bia-07 có thêm dòng nhỏ "LỜI GIẢI" dưới chữ MÔN TOÁN (cùng font, tông màu, hai vạch ngang hai bên, căn giữa, không đè hình; bản đầu ghi "QUYỂN LỜI GIẢI", đổi 05/11/2026) — công tắc `\QuyenLoiGiai` trong `bia/bia-07.tex`, mặc định tắt nên bìa Quyển Đề không đổi; mục lục Lời giải Đề số 01 … 40; 40 đề chế độ `solcolor` như bản lời giải lẻ; bìa sau bia-07-sau.
   - **Quy cách chung:** bìa dựng riêng bằng XeLaTeX (font Montserrat ở `bia/fonts`), chèn bằng pdfpages, cắt 3 mm lề xén mỗi cạnh về A4 210 × 297 mm; bìa trước là trang 1, bìa sau là trang cuối và là trang chẵn. Mỗi đề, mỗi lời giải bắt đầu ở trang lẻ; trang trống chèn thêm để đề bắt đầu trang lẻ có đầu trang, chân trang và logo chìm như trang thường (trang trống ngay sau một đề mang đầu trang của đề đó "... -- Đề số XX", trang trống ở phần đầu sách mang dòng chung "Luyện thi tốt nghiệp THPT năm 2027"); riêng mặt sau bìa trước và trang ngay trước bìa sau để trắng hoàn toàn (quyết định 06/11/2026, `kho/sua-hinh.md` mục 60; bản đầu để mọi trang chèn thêm trắng). File đề `\input` thẳng từ `de/` (không chép, không sửa); `\TachCauDS`, `\TachCauLG` bật cho cả sách. Đầu trang mỗi đề giữ như bản lẻ ("... -- Đề số XX"); phần đầu sách và bảng đáp án ghi "Luyện thi tốt nghiệp THPT năm 2027"; số trang chạy liên tục cả quyển (bìa trước là trang 1). Mỗi đề trong sách giữ nguyên dàn trang bản lẻ (cùng số trang, câu nằm cùng trang).
   - **Cách làm:** `sach/sach-chung.tex` có `\ChenDe{XX}{../de/...}`: trong một nhóm, đổi `\input` để bỏ qua `\input{preamble-eduzy-v2}` của file đề, biến `\begin{document}`…`\end{document}` của file đề thành nhóm thường; các dòng `\def\tenchuong`, `\def\TachCau..` đầu file đề vẫn chạy cục bộ nên đầu trang đúng như bản lẻ; trang cuối của đề được đẩy ra trong nhóm. Không dùng docmute vì file đề gọi `\documentclass` gián tiếp qua `\input{preamble-eduzy-v2}` (docmute đọc lố hết file preamble và báo lỗi). Số trang cho mục lục ghi thẳng vào `.aux` (`\immediate\write`, không chèn mốc vào trang) để không đổi dàn trang. Preamble, ex_test.sty, esvect.sty tìm ở thư mục cha qua `\input@path`.
   - **Xuất:** `thanh-pham/Sach-LuyenDe-TN2027-QuyenDe.pdf`, `thanh-pham/Sach-LuyenDe-TN2027-QuyenLoiGiai.pdf`, `thanh-pham/Sach-LuyenDe-TN2027-NguonSach.zip` (2 file chính, phần đầu sách, PDF bìa dựng sẵn, các thư mục đề cần `\input`, preamble, ex_test.sty, esvect.sty, `BienDich-Sach.bat` biên dịch cả 2 quyển trên Windows bằng MiKTeX XeLaTeX, đủ lượt cho mục lục và bảng đáp án; giải nén ra biên dịch được ngay).
   - **Kiểm tra** (`python3 tools/sach/kiem_sach.py`): mỗi đề bắt đầu trang lẻ; số trang từng đề bằng bản lẻ; văn bản từng trang khớp bản lẻ (pdftotext, bỏ số trang; thêm cả vị trí từng chữ); mục lục đúng số trang; bảng đáp án khớp `\True`/`\shortans` trong file đề; tổng số trang chẵn, bìa sau ở trang cuối; mặt sau bìa trước và trang trước bìa sau trắng hoàn toàn, các trang trống chèn thêm khác có đầu trang (đúng đề trước hoặc dòng chung), chân trang đúng số trang, logo chìm, thân trang trống. Xem ảnh vài trang trống ở cả 2 quyển. Xem ảnh bìa trước 2 quyển, bìa sau, lời nói đầu, trang cấu trúc đề, mục lục, các trang bảng đáp án, trang đầu Đề 01 và Đề 40 của mỗi quyển.
   - Lệnh: `bash sach/bien-dich-sach.sh tat-ca` (bìa + 2 quyển) → `python3 tools/sach/kiem_sach.py` → `bash sach/dong-goi-sach.sh`. Sửa file đề nào thì biên dịch lại bản lẻ (thanh-pham/) và sách rồi chạy lại kiểm tra.

## Ghi chú kỹ thuật
- Thư mục kho/ có thể lớn: không commit file trung gian không cần thiết (ảnh tạm, file giải nén trùng với zip gốc nếu quá nặng — hỏi người dùng nếu repo vượt khoảng 500 MB).
- kho/TIEN-DO.md luôn ghi: giai đoạn hiện tại, việc đã xong, việc đang chờ duyệt, quyết định người dùng đã đưa ra.
