# KIỂM ĐÁP ÁN V2 — 35 ĐỀ PDF (lô P01–P09), PHIÊN FABLE PHẦN B

Phiên 14/11/2026, nhánh `claude/great-knuth-6gcmjx`. Mỗi đề một agent con: giải lại độc lập 28 câu từ ảnh trang đề gốc và ghi đáp án ra nháp **trước khi** mở file `.tex`; tìm đáp án của chính đề trên mạng; soát câu lý thuyết theo SGK; rồi so với `\True`, `\shortans` trong file đề và giải lại lần hai các câu lệch, câu đang `% KIỂM TRA`, các điểm "thầy xem" / "Chờ thầy quyết" của `kho/TIEN-DO.md`. Kết quả từng đề: `de/<tên đề>/kiem-chung-v2.md` (bảng đáp án Fable đủ 28 câu, bảng câu lệch / câu `% KIỂM TRA`, căn cứ lý thuyết, nguồn trên mạng). Phiên này **không sửa** file `.tex`, `kiem-chung.md`, `kho/TIEN-DO.md` (phiên vẽ hình chạy song song trên nhánh khác): mọi thay đổi đáp án, lời đề, hình đều chờ thầy quyết.

## Kết quả

- **35/35 đề đã kiểm.** 32 đề không có câu / ý lệch: 29 đề trùng 28/28 ngay từ lượt giải độc lập đầu; 3 đề khác ở lượt đầu chỉ vì đề gốc lỗi, kết luận cuối là file không sai — Lương Thế Vinh II.2a (file đã sửa Z của I-131 từ 51 thành 53), Phan Đăng Lưu I.16 (A và C cùng đúng), Quảng Ninh SGD I.16 (không phương án nào đúng, mỗi bên chữa một phương án).
- **3 câu / ý lệch** (file khác kết luận cuối của Fable), cả ba đều do đề mơ hồ — Fable nghiêng về đáp án khác nhưng không khẳng định file sai: Cụm liên trường Hà Tĩnh II.2a, Kinh Môn II II.1a, Ngô Gia Tự I.11 (mục A).
- Không thấy câu nào file sai do tính toán. Phần còn lại là lỗi / chỗ mơ hồ của đề gốc cần thầy quyết (mục B–D), lỗi hình vẽ lại (mục G), sai sót nhỏ (mục H).
- Đối chiếu đáp án trên mạng (lượt bổ sung 14/11/2026, sau khi mở tên miền): 33/35 đề tìm được trang đúng đề trên VietJack có đáp án công khai; 17 đề khớp file hoàn toàn; 25 câu / ý mạng khác file ở 16 đề — 7 do nguồn nhầm hoặc không có lời giải, 10 trùng điểm đã nêu ở mục A–E, 8 điểm mới. Ở mục A: nguồn trùng file ở Hà Tĩnh II.2a, Kinh Môn II II.1a; trùng Fable (D) ở Ngô Gia Tự I.11. Xem mục "Đối chiếu mạng bổ sung".

Cách đếm "lệch": Phần I, III theo câu; Phần II theo ý. Thứ tự làm: đề có `% KIỂM TRA` trong `.tex` (21 đề, STT 1–21) → đề có điểm "Chờ thầy quyết" (8 đề, STT 22–29) → đề chỉ có điểm "thầy xem" (6 đề, STT 30–35).

## Đối chiếu mạng bổ sung (14/11/2026)

Lượt bổ sung sau khi thầy mở tên miền: 8 agent (mỗi agent 4–5 đề, đề có điểm mục A–D làm trước), chỉ tìm trang đăng đúng đề, ghi đáp án từng câu kèm link vào cột "Mạng" và mục "Đối chiếu mạng bổ sung (14/11/2026)" cuối `kiem-chung-v2.md` của từng đề; không giải lại đề, không sửa `.tex`, `kiem-chung.md`. Dòng tổng của lượt này ghi thêm vào mục "Tóm tắt" đầu mỗi `kiem-chung-v2.md`.

- **Nguồn**: khoahoc.vietjack.com, đọc bằng `curl`, tải lần lượt cách 1,5 s. Trang cả đề chỉ công khai đáp án câu 1–8 (các câu sau ghi "Bạn cần đăng ký gói VIP"). Đáp án các câu còn lại đọc ở trang từng câu (`/question/<id>`), nơi VietJack hiện công khai "Trả lời: Giải bởi Vietjack — Chọn đáp án X", không cần đăng nhập. Không đăng nhập, không mở phần VIP. Đề đúng phần lớn tìm qua trang danh mục https://khoahoc.vietjack.com/trac-nghiem/tot-nghiep-thpt/mon-Vat-ly/de-thi-tot-nghiep-thpt-vat-ly-2026?type=test (WebSearch hầu như không ra). Mỗi nguồn đã so lời câu, số liệu, thứ tự phương án / ý của đủ 28 câu với file `.tex`. Đáp án VietJack là lời giải của trang, không phải đáp án chính thức của trường / sở.
- **Kết quả**: 33/35 đề tìm được trang đúng đề có đáp án công khai (30 đề đủ 28/28 câu; Cụm liên trường Hà Tĩnh, Chuyên KHTN Lần 1, Cẩm Phả 27/28). Bắc Ninh SGD (scan): chỉ có bản đề trên chuvanbien, không có đáp án. Nguyễn Khuyến LTT Lần 10: không tìm thấy.
- **17 đề khớp file hoàn toàn**: Yên Hòa, Kinh Môn II, Nguyễn Khuyến LTT Lần 2, Nguyễn Khuyến LTT Lần 3, Chuyên ĐH Vinh, Thái Nguyên SGD, Hàm Rồng, Bắc Ninh SGD Lần 1, Cụm CM10, Lào Cai SGD, Ninh Bình SGD Lần 1, Ninh Bình SGD Lần 2, Chuyên Hạ Long, Hà Nội SGD, Phú Thọ SGD, Quảng Ninh SGD (I.16 cùng nội dung, khác chữ cái — xem dưới), Liên trường Nghệ An Lần 1 (VietJack khớp 28/28; bảng đáp án chuvanbien khác 2 câu).
- **25 câu / ý mạng khác file ở 16 đề** (23 theo VietJack, 2 theo bảng đáp án chuvanbien): 7 do nguồn nhầm hoặc không có lời giải, 10 trùng điểm đã nêu ở mục A–E (nguồn chọn cách hiểu / cách xử lí lỗi đề khác file), 8 điểm mới.

### M1. Nguồn nhầm nhãn, tính nhầm hoặc không có lời giải — file đúng hoặc chưa rõ (7)

| Đề | Câu | File | Mạng | Ghi chú |
|---|---|---|---|---|
| Cụm liên trường Hà Tĩnh | I.9 | B | D | Lời giải của chính nguồn: thăng hoa là rắn → hơi, tức B; nguồn nhầm chữ cái. |
| Cẩm Phả – Lần 1 | I.6 | C | D | Lời giải ngay dưới của nguồn lại chọn C; nguồn tự mâu thuẫn. |
| Tĩnh Gia I | I.2 | A | D | Lời giải của nguồn kết luận nhiệt độ lưỡi dao và cán "xấp xỉ bằng nhau", tức A. |
| Chuyên Phan Bội Châu – Lần 1 | I.3 | B | C | Nguồn chọn (2/3)kT, lời giải bỏ trống công thức; SGK: E_đ = (3/2)kT (B). |
| Chuyên KHTN – Lần 1 | II.3a | Đ | S | Nguồn viết "= 0,00004 mol" trong khi chính biểu thức của nguồn cho 0,00401 mol (nhầm bậc 10). |
| Chuyên KHTN – Lần 3 | III.5 | −12 | −24 | Nguồn đổi cm⁻³ sang m⁻³ bằng cách nhân 10⁻⁶ (đúng là 10⁶), lệch đúng 12 bậc. |
| Chuyên KHTN – Lần 1 | III.5 | 8 | 1 | Nguồn chỉ ghi "Đáp án: 1", không lời giải; lời câu, số liệu trùng file. Chưa rõ lí do. |

### M2. Trùng điểm đã nêu ở mục A–E: nguồn chọn cách hiểu / cách xử lí lỗi đề khác file (10)

| Đề | Câu | File | Mạng | Ghi chú |
|---|---|---|---|---|
| Ngô Gia Tự – Lần 1 | I.11 (mục A) | C | **D** | Nguồn đúng đề ghi D (trang câu không kèm lời giải); câu cùng nội dung ở loigiaihay, tuyensinh247 (hai bản) cũng D; không nguồn nào ghi C. Fable cũng D. |
| Lương Thế Vinh – Lần 1 | II.2a (mục B) | S | Đ | Nguồn giữ nguyên ¹³¹₅₁I như đề gốc (Xe-131 có Z = 52, 79 neutron); file đã sửa Z = 53. Đáp án đang lưu hành theo nguyên văn đề là Đúng. |
| Nguyễn Khuyến LTT – Lần 1 | II.1b (`% KIỂM TRA`) | Đ | S | Nguồn giữ chữ "3 V" của đề gốc, chấm Sai vì sai đơn vị; file sửa thành 3 A. Tuyển tập trên chuvanbien (cùng câu) in "3 A". |
| Phan Đăng Lưu – Lần 1 | I.16 (mục D) | C | A | Đề có hai phương án đúng theo SGK; nguồn coi C sai (cho rằng chỉ phân tử khí mới chuyển động hỗn loạn không ngừng). |
| Phan Đăng Lưu – Lần 1 | II.2a (mục C) | S | Đ | Nguồn tính 0,178 mol rồi coi "xấp xỉ 0,17" là đúng (chấm lỏng). |
| Liên trường Nghệ An – Lần 2 | II.2d (mục C) | S | Đ | Nguồn in "8,9 °C" như đề, tính ra 9,84 °C nhưng vẫn chấm Đúng (nghi đề gõ đảo 9,8 thành 8,9). |
| Hưng Yên SGD – Lần 1 | II.1d (mục D) | Đ | S | Nguồn cho số chỉ của cân gồm cả khối lượng cốc. |
| Lương Đắc Bằng – Lần 1 | II.1d (mục D) | Đ | S | Nguồn: "chỉ kiểm chứng chứ không chứng minh được định luật" (cách hiểu chặt). |
| Cẩm Phả – Lần 1 | II.3c | S | Đ | Nguồn theo cách hiểu thứ hai đã ghi trong `kiem-chung-v2.md` ("không có quỹ đạo xác định"). |
| Cẩm Xuyên – Lần 2 | II.2c ("thầy xem", đọc hình) | Đ | S | Nguồn đồng ý chiều dòng điện như mũi tên i trên hình nhưng coi cạnh đó là nửa vòng phía trước nên gọi "ngược chiều kim đồng hồ" — khác cách đọc phối cảnh. |

### M3. Điểm mới, chưa có trong mục A–D (8) — thầy quyết

| Đề | Câu | File | Mạng | Ghi chú |
|---|---|---|---|---|
| Nguyễn Thị Minh Khai – Lần 1 | II.2c | S | Đ | Lời ý c trên trang in mômen 4·10⁻⁴ N·m như đề gốc và file, nhưng lời giải nguồn dùng 4,8·10⁻⁴ N·m → B = 0,08 T nên chấm Đúng. Nghi đề gốc in thiếu ",8": giữ S theo số in hay sửa mômen thành 4,8·10⁻⁴ (ý c thành Đ). |
| Lương Thế Vinh – Lần 1 | II.3d | S | Đ | Mệnh đề "Nội năng … bằng tổng công A và nhiệt lượng Q": file chấm Sai vì định luật I nói về *độ biến thiên* nội năng; nguồn ghi Đúng, không lời giải. |
| Cụm 13 trường – Lần 2 | II.2c | S | Đ | Nguồn: khí bị nén ⇒ A > 0 ⇒ ΔU = A > 0 (bỏ qua Q), trái câu "coi nhiệt độ của khí trong xilanh không đổi" của chính lời đề (file: đẳng nhiệt ⇒ ΔU = 0). |
| Ngô Gia Tự – Lần 1 | III.4 | 150 | 200 | Nguồn lấy 40 kW (nhiệt nồi hơi nhận mỗi giây) chia 20 %; file lấy 30 kW (công suất động cơ) chia 20 %. Hai cách hiểu "hiệu suất động cơ hơi nước"; `kiem-chung-v2.md` đã ghi cách hiểu 200. |
| Ngô Gia Tự – Lần 1 | III.5 | 32 | 34 | Cùng nhiệt lượng (≈ 1,055·10⁶ J), cùng thể tích đá tan (≈ 3,391·10⁻³ m³); khác mô hình phần đá tan: nguồn V = (4/3)πR³ + πR²(h − 2R), file V = πR²(h − R) + (2/3)πR³ (chênh (1/3)πR³). |
| Cẩm Phả – Lần 1 | II.3b | S | Đ | Nguồn hiểu "phân tử khói" là hạt khói. |
| Liên trường Nghệ An – Lần 1 | II.2d | S | Đ (chuvanbien) | Bảng đáp án trong PDF chuvanbien (đề "Sở GD&ĐT Nghệ An – Liên trường THPT", mã 3114), không lời giải; VietJack ghi S như file. Bản chuvanbien in công thức giống file. |
| Liên trường Nghệ An – Lần 1 | III.6 | 640 | 427 (chuvanbien) | 427 trùng 0,32·0,8/0,6 (coi cả trọng lượng đặt ở đoạn NP); không lời giải; VietJack ghi 640 như file. |

### M4. Các điểm mục A–E mà nguồn trùng file

- **Mục A**: Cụm liên trường Hà Tĩnh II.2a (nguồn S; lần đo 7 có pV không xấp xỉ không đổi); Kinh Môn II II.1a (nguồn S, lí do hao phí nhiệt). Ngô Gia Tự I.11: nguồn D (M2).
- **Mục B**:
  - Chuyên KHTN Lần 3 I.10: bản VietJack cũng in H = 90 %, tính ra 3193 W, vẫn chọn C.
  - Hưng Yên SGD II.2: bản VietJack in "12 kW" nhưng lời giải thế 1200 W, ra Đ Đ S S — ủng hộ cách file sửa 1,2 kW.
  - Liên trường Nghệ An Lần 2 I.8: bản VietJack in "(2/2)kT" mà vẫn chấm A — ủng hộ cách file sửa (3/2)kT.
  - Thái Nguyên SGD I.17: bản VietJack cũng có C trùng B, chọn A.
  - Yên Hòa I.7: nguồn giữ λ = 34·10⁵ J/kg, chọn B; III.4: đề trên nguồn in N_A = 6,2·10²³ nhưng lời giải dùng 6,02·10²³, ra 2,97 như file.
  - Tĩnh Gia I II.3: nguồn đúng đề có cùng lỗi in và ghi **S S S S** như file. Đáp án S Đ Đ Đ mà phiên trước dẫn là của bản lời khác (đề V-SAT, ý b, c, d khác lời). II.3d nguồn S. III.2: trang nguồn cũng không có hình mạch, tính theo mạch nối tiếp ra 0,66.
  - Cẩm Phả III.6: trang nguồn cũng thiếu hình ("Đề bài thiếu hình, thiếu V"), không có đáp số — kích thước phòng 8 × 5 × 4 m vẫn chưa xác minh được.
  - **Quảng Ninh SGD I.16**: nguồn chọn **B**, và bản VietJack in B = (N₂/N₁)·U₁ (dấu nhân), C = (N₁/N₂)·U₁ → đáp án gốc nhiều khả năng là B, dấu "+" ở B trên bản PDF là lỗi gõ. File chữa phương án C (cùng nội dung đáp án). Thầy quyết: chữa B (đáp án B, khớp nguồn) hay giữ.
- **Mục C** — nguồn in cùng số và cũng chấm Sai như file, nên các số này có trong đề gốc, không phải lỗi gõ lại: Cẩm Xuyên II.3d (1282 kg); Ngô Gia Tự II.4d (in 4160); Nguyễn Khuyến LTT Lần 3 II.1b, II.1d (in 2,64·10⁶; 41 kJ); Nguyễn Khuyến LTT Lần 1 II.4c (85,1 %), II.4d (1,67 h); Phú Thọ SGD II.2b, II.2c (bản mã 0203 của Sở cũng in 75 kJ, 10,8 J); Kinh Môn II II.3d (3,33 W); Chuyên KHTN Lần 3 II.1d (12,45 T); Quảng Ninh SGD II.3d (in 2,65·10⁻⁴); Tĩnh Gia I II.3d; Cụm CM10 I.6 (in "Mười độ chia", A); Bắc Ninh SGD (scan) II.4d (đề của Sở in cùng 0,185 kg, 11,60 W, 3995 J/kg.K; không có đáp án). Khác file: Phan Đăng Lưu II.2a, Liên trường Nghệ An Lần 2 II.2d (M2).
- **Mục D** — nguồn chọn cùng cách hiểu với file: Chuyên KHTN Lần 1 III.4 (16); Yên Hòa III.3 (78,6), II.1b (S); Cụm 13 trường I.17 (B; nguồn cũng ghi chú đề mơ hồ); Cụm liên trường Hà Tĩnh III.3 (4,65); Phan Đăng Lưu III.1 (20), III.2 (10); Kinh Môn II III.6 (2,3); Hàm Rồng II.4c (S), III.6 (2108); Hà Nội SGD II.2b (S); Hưng Yên SGD II.1c; Bắc Ninh SGD Lần 1 II.2c (Đ), III.6 (0,6); Liên trường Nghệ An Lần 1 II.1c (S), II.4d (Đ); Phú Thọ SGD II.1a (S, lí do khác); Chuyên Phan Bội Châu II.2b, II.4b (Đ); Nguyễn Thị Minh Khai II.4c (S, 99 kJ); Ninh Bình SGD Lần 2 III.5 (6,23), III.6 (1,98); Lương Đắc Bằng II.4c (S), II.3c (Đ). Khác file: Phan Đăng Lưu I.16, Hưng Yên SGD II.1d, Lương Đắc Bằng II.1d (M2). Nguyễn Khuyến LTT Lần 10 (II.3a, II.4b, III.6): không có nguồn.
- **Mục E** (đọc hình) — nguồn trùng file: Nguyễn Thị Minh Khai I.3 (D); Cụm CM10 II.3b, c, II.4a, b; Lào Cai SGD I.6, II.1c; Chuyên ĐH Vinh I.17, II.3; Chuyên Hạ Long II.1b; Thái Nguyên SGD II.1c; Nguyễn Khuyến LTT Lần 2 II.1b; Ninh Bình SGD Lần 2 II.4a; Lương Đắc Bằng II.2d. Khác file: Cẩm Xuyên II.2c (M2).

### M5. Tên đề, lần thi (bổ sung mục I)

- **Bắc Ninh SGD (scan)**: **đã xác nhận** là đề kiểm tra cuối học kì I năm học 2025–2026, Vật lí 12, Sở GD&ĐT Bắc Ninh, 45 phút, mã đề 0203 (PDF trên chuvanbien, cùng mã đề, khớp 28 câu); bản trong kho đã bị đổi tiêu đề thành "khảo sát chất lượng tốt nghiệp THPT, 50 phút". Thầy quyết có giữ đề này trong bộ thi thử không.
- **Lương Thế Vinh**: VietJack đăng đề này với tên "THCS&THPT Lương Thế Vinh – Hà Nội **lần 2**" (khớp ghi chú `kiem-ke.md`: file "Lần 2" của SieuGioi trùng nội dung file Lần 1). Thầy xem lại tên / lần của file.
- **Nguyễn Khuyến LTT Lần 1**: tuyển tập trên chuvanbien ghi câu II.1, II.2 lấy từ "Đề kiểm tra thường xuyên 2025–2026 trường Nguyễn Khuyến – Lê Thánh Tông"; đề "Lần 1" có thể là đề kiểm tra này.
- **Ninh Bình SGD Lần 1**: danh mục VietJack có trang riêng cho lần 2, lần 3 của Sở Ninh Bình; trang không ghi lần khớp file → ủng hộ "Lần 1".
- Tên trên VietJack (để tra lại): Cụm liên trường Hà Tĩnh = "Sở Hà Tĩnh"; Liên trường Nghệ An Lần 2 = "Liên trường Anh Sơn – Đô Lương – Thanh Chương – Yên Thành" (không ghi lần); Liên trường Nghệ An Lần 1 = "Liên trường THPT Nghệ An mã đề 3114"; Nguyễn Khuyến LTT Lần 2 = "THPT Lê Thánh Tông (HCM)"; Nguyễn Khuyến LTT Lần 3 = "Nguyễn Khuyến (HCM)"; Hưng Yên SGD = mã đề 0209; Bắc Ninh SGD Lần 1 = mã đề 0204; Phú Thọ SGD = mã đề 0203, "khảo sát chất lượng lớp 12 (đợt 1)".

### M6. Link phiên trước ghi nhầm đề, truy cập

- Link phiên trước hóa ra là đề khác (đã ghi trong từng file): VietJack "Lương Thế Vinh lần 1" (/164073, đề 40 câu năm trước), "Chuyên KHTN" không hậu tố (đề đúng là trang có hậu tố `-61`), "Chuyên Hạ Long", "Chuyên ĐH Vinh" (đề năm trước), câu Thái Nguyên `question/2061691` (đề ĐGNL ĐHSP Hà Nội), câu Tĩnh Gia II.3 (bản lời khác của đề V-SAT).
- Đọc được: khoahoc.vietjack.com (`curl`); chuvanbien.vn (WebFetch, có lúc trả 503); loigiaihay.com, tuyensinh247.com (WebFetch).
- Bị chặn: hoatieu.vn (WebFetch 403; `curl` bị chế độ cấp quyền của phiên chặn); docs.google.com, news.laodong.vn, vietnamnet.vn, image.plo.vn, video.vietjack.com, vietjack.com (WebFetch không phân giải được tên miền). Không thử cách khác.
- Phiên chính kiểm bằng script: 35 file `kiem-chung-v2.md` đủ 28 dòng bảng đáp án, các cột Câu / Fable / File / Khớp giữ nguyên, chỉ điền cột Mạng; mỗi file có đúng một mục "Đối chiếu mạng bổ sung". 6 agent tự báo có chạy lệnh git chỉ đọc (`git status`, `git diff`), không thay đổi repo.

## Bảng 35 đề

| STT | Lô | Đề (mở `kiem-chung-v2.md`) | Trạng thái | Số lệch | Câu lệch (file / Fable) | Kết luận của Fable | Đáp án trên mạng (đối chiếu bổ sung 14/11/2026) |
|---|---|---|---|---|---|---|---|
| 1 | P01 | [`VatLi2026-HaNoi-ChuyenKHTN-Lan3`](../de/VatLi2026-HaNoi-ChuyenKHTN-Lan3/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. I.10 giữ C (tính ra 3,19 kW, không có phương án; nhiều khả năng đề chép sai H = 90 % thay cho 95 %). II.1d Sai chắc (12,4 T). III.4 = 0,09 sát ngưỡng làm tròn. | VietJack (trang hậu tố `-61`) 28/28; khác III.5 (−24, nguồn đổi đơn vị nhầm) |
| 2 | P01 | [`VatLi2026-HaNoi-LuongTheVinh-Lan1`](../de/VatLi2026-HaNoi-LuongTheVinh-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp theo đề đã sửa. II.2a: Sai với Z = 53 (file đã sửa), Đúng với nguyên văn Z = 51 — thầy quyết. III.2 = 200 W, III.4 = 2,7 đúng. | VietJack (tên "Lương Thế Vinh lần 2") 28/28; khác II.2a (Đ, giữ Z = 51), II.3d (Đ) |
| 3 | P02 | [`VatLi2026-HaNoi-YenHoa-Lan1`](../de/VatLi2026-HaNoi-YenHoa-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. I.7 giữ B (theo λ = 34·10⁵ J/kg in trên đề). Hai cách hiểu: II.1b (hướng nhìn), III.3 (78,6 / 78,1). **Hình I.13 đảo cực nguồn.** | VietJack 28/28, khớp |
| 4 | P02 | [`VatLi2026-HaTinh-CamXuyen-Lan2`](../de/VatLi2026-HaTinh-CamXuyen-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.3d Sai (1282 kg / đề "khoảng 1250 kg") — thầy quyết. III.4 = 3,46, không còn mơ hồ. | VietJack 28/28; khác II.2c (S, đọc phối cảnh); II.3d S như file |
| 5 | P03 | [`VatLi2026-HaTinh-CumLienTruong`](../de/VatLi2026-HaTinh-CumLienTruong/kiem-chung-v2.md) | xong | 1 | II.2a: S / Đ | Đề mơ hồ (lần đo 7 bất thường); Fable nghiêng Đ, không khẳng định file sai. III.3 = 4,65 (4,68 cũng có cơ sở). II.3c, d định tính giữ Đ. | VietJack ("Sở Hà Tĩnh") 27/28; II.2a S như file; khác I.9 (D, nguồn nhầm nhãn) |
| 6 | P03 | [`VatLi2026-HaiPhong-Cum13Truong-Lan2`](../de/VatLi2026-HaiPhong-Cum13Truong-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. I.17 giữ B (0,7 N mỗi dây; D nếu hiểu tổng hai dây 1,4 N) — thầy quyết. | VietJack 28/28; I.17 B như file; khác II.2c (Đ) |
| 7 | P03 | [`VatLi2026-HaiPhong-KinhMonII-Lan2`](../de/VatLi2026-HaiPhong-KinhMonII-Lan2/kiem-chung-v2.md) | xong | 1 | II.1a: S / Đ | Đề mơ hồ (nguyên tắc phép đo → Đ; xét hao phí → S). II.2b, III.6 giữ như file. Điểm mới: II.3d (2,5 W của đề đúng bằng kết quả khi bỏ sót cos α). | VietJack 28/28, khớp (II.1a S như file) |
| 8 | P04 | [`VatLi2026-Hue-PhanDangLuu-Lan1`](../de/VatLi2026-Hue-PhanDangLuu-Lan1/kiem-chung-v2.md) | xong | 0 | — (I.16: đề có hai phương án đúng) | I.16 A và C cùng đúng theo SGK, file gõ C — thầy quyết. II.2a Sai (0,1787 mol / "xấp xỉ 0,17"). III.2 = 10, III.1 = 20. | VietJack 28/28; khác I.16 (A), II.2a (Đ) |
| 9 | P04 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1b Đ (đã sửa "3 V" → 3 A). II.4c mơ hồ (85 % / 92 %), II.4d Sai. Hình II.4, II.2 lệch nhỏ. | VietJack 28/28; khác II.1b (S, giữ chữ "3 V") |
| 10 | P04 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan3`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan3/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1b, II.1d Sai theo chữ in (II.1d: tính ra 34,1 kJ, đề in "41 kJ" — nghi mất kí tự) — thầy quyết. | VietJack 28/28, khớp (II.1b, d S như file) |
| 11 | P05 | [`VatLi2026-HungYen-SoGD-Lan1`](../de/VatLi2026-HungYen-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28 theo đề đã sửa P = 1,2 kW (giữ 12 kW thì II.2a Sai). II.1c S, II.1d Đ mơ hồ nhẹ. | VietJack (mã 0209) 28/28; khác II.1d (S); II.2 ủng hộ sửa 1,2 kW |
| 12 | P05 | [`VatLi2026-NgheAn-ChuyenDHVinh-Lan1`](../de/VatLi2026-NgheAn-ChuyenDHVinh-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; I.17, II.3 đọc hình độc lập khớp; không câu mơ hồ. **Hình III.3 vẽ sai chiều vòng từ trường quanh một thanh ray.** | VietJack 28/28, khớp |
| 13 | P06 | [`VatLi2026-NgheAn-LienTruong-Lan2`](../de/VatLi2026-NgheAn-LienTruong-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. Đồng ý sửa I.8 thành (3/2)kT. II.4c Đ. II.2d Sai (9,84 °C / đề ghi 8,9). | VietJack 28/28; khác II.2d (Đ); I.8 ủng hộ sửa (3/2)kT |
| 14 | P07 | [`VatLi2026-PhuTho-NgoGiaTu-Lan1`](../de/VatLi2026-PhuTho-NgoGiaTu-Lan1/kiem-chung-v2.md) | xong | 1 | I.11: C / D | Fable nghiêng D (đoạn trích loigiaihay, tuyensinh247 cũng D); cần đối chiếu SBT KNTT bài 8. II.4d Sai (4461 / đề in 4160 — nghi 4460). | VietJack 28/28; khác I.11 (D), III.4 (200), III.5 (34) |
| 15 | P07 | [`VatLi2026-QuangNinh-CamPha-Lan1`](../de/VatLi2026-QuangNinh-CamPha-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. III.6 = 14 chỉ đúng với hình phòng tự dựng 8 × 5 × 4 m (đề gốc mất hình) — thầy quyết. | VietJack 27/28; khác I.6 (D, nguồn tự mâu thuẫn), II.3b, c (Đ Đ); III.6 nguồn cũng thiếu hình |
| 16 | P08 | [`VatLi2026-QuangNinh-SoGD-Lan1`](../de/VatLi2026-QuangNinh-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — (I.16: đề gốc không có phương án đúng) | I.16: file chữa C, đoạn trích VietJack ghi B — thầy quyết chữa phương án nào. Điểm mới: II.3d (2,56·10⁻⁴ W / đề in 2,65·10⁻⁴). III.2, III.3, III.6 đúng. | VietJack 28/28, khớp nội dung; I.16 nguồn chọn B (chữa B) |
| 17 | P08 | [`VatLi2026-ThaiNguyen-SoGD-Lan1`](../de/VatLi2026-ThaiNguyen-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.1c đo điểm ảnh cực nguồn khớp; không câu mơ hồ. | VietJack 28/28, khớp |
| 18 | P08 | [`VatLi2026-ThanhHoa-HamRong-Lan1`](../de/VatLi2026-ThanhHoa-HamRong-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.4c Sai, mơ hồ (MN không thuộc mạch kín; trường có thể Đ). III.6 = 2108 theo hằng số SGK. | VietJack 28/28, khớp |
| 19 | P09 | [`VatLi2026-ThanhHoa-TinhGia1`](../de/VatLi2026-ThanhHoa-TinhGia1/kiem-chung-v2.md) | xong | 0 | — | II.3 S S S S theo chữ in; sửa lỗi in thì S Đ Đ Đ (bản lời khác trên VietJack cũng S Đ Đ Đ) — thầy quyết. III.2 = 0,66 với mạch tự dựng. | VietJack 28/28; II.3 S S S S như file; khác I.2 (D, nguồn nhầm nhãn) |
| 20 | P01 | [`VatLi2026-BacNinh-SoGD-Lan1`](../de/VatLi2026-BacNinh-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.2c Đ mơ hồ nhẹ; III.5 = 8,01, III.6 = 0,6 đúng. | VietJack (mã 0204) 28/28, khớp |
| 21 | P09 | [`VatLi2026-BacNinh-SoGD`](../de/VatLi2026-BacNinh-SoGD/kiem-chung-v2.md) (scan) | xong | 0 | — | Khớp 28/28. II.4d Sai (3888 / 3995; 3995 ứng với m = 0,18 kg) — thầy quyết. Có thể là đề cuối học kì I (mục I). | chuvanbien: bản đề cuối học kì I (mã 0203), không có đáp án |
| 22 | P01 | [`VatLi2026-HaNoi-ChuyenKHTN-Lan1`](../de/VatLi2026-HaNoi-ChuyenKHTN-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. III.4 = 16 (18 nếu không trừ khí còn lại) — thầy quyết. III.6 = 0,05 theo cả lời đề lẫn hình gốc. | VietJack 27/28; khác II.3a (S, nguồn tính nhầm), III.5 (1, không lời giải) |
| 23 | P02 | [`VatLi2026-HaNoi-NguyenThiMinhKhai-Lan1`](../de/VatLi2026-HaNoi-NguyenThiMinhKhai-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.4c mơ hồ nhẹ (99 / 100 kJ). **Hình II.2 (Hình a) đảo cực nguồn.** | VietJack 28/28; khác II.2c (Đ, lời giải nguồn dùng 4,8·10⁻⁴ N·m) |
| 24 | P03 | [`VatLi2026-HaiPhong-CumCM10-Lan1`](../de/VatLi2026-HaiPhong-CumCM10-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.3b, c, II.4a, b đọc hình khớp. I.6 = A theo lời đề "Mười độ chia" (C nếu là "Một độ chia"). | VietJack 28/28, khớp |
| 25 | P04 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.1b đọc chiều quấn, cực nguồn khớp. | VietJack ("Lê Thánh Tông (HCM)") 28/28, khớp |
| 26 | P05 | [`VatLi2026-LaoCai-SoGD-Lan1`](../de/VatLi2026-LaoCai-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; I.6, II.1c đọc hình khớp; không câu mơ hồ. | VietJack 28/28, khớp |
| 27 | P06 | [`VatLi2026-NgheAn-LienTruong-Lan1`](../de/VatLi2026-NgheAn-LienTruong-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; I.8 = B. II.1c, II.4d mơ hồ nhẹ. | VietJack (mã 3114) 28/28, khớp; bảng đáp án chuvanbien khác II.2d (Đ), III.6 (427) |
| 28 | P06 | [`VatLi2026-NinhBinh-SoGD-Lan2`](../de/VatLi2026-NinhBinh-SoGD-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. III.5 = 6,23 (6,24 nếu R = 8,314 — đề không cho R). III.6 = 1,98. | VietJack 28/28, khớp |
| 29 | P07 | [`VatLi2026-QuangNinh-ChuyenHaLong-Lan1`](../de/VatLi2026-QuangNinh-ChuyenHaLong-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.1b đọc cực nguồn khớp. | VietJack 28/28, khớp |
| 30 | P02 | [`VatLi2026-HaNoi-SoGD-Lan1`](../de/VatLi2026-HaNoi-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.2b mơ hồ ("cùng chuyển động"). | VietJack 28/28, khớp |
| 31 | P05 | [`VatLi2026-NgheAn-ChuyenPhanBoiChau-Lan1`](../de/VatLi2026-NgheAn-ChuyenPhanBoiChau-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.2b, II.4b mơ hồ nhẹ. **Hình I.6 vẽ electron thành nhãn dòng điện I.** | VietJack 28/28; khác I.3 (C, nguồn nhầm chữ cái) |
| 32 | P06 | [`VatLi2026-NinhBinh-SoGD-Lan1`](../de/VatLi2026-NinhBinh-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; không câu mơ hồ. | VietJack 28/28, khớp |
| 33 | P07 | [`VatLi2026-PhuTho-SoGD-Lan1`](../de/VatLi2026-PhuTho-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1a Sai, mơ hồ (lượng khí thay đổi) — thầy quyết. II.2b, II.2c Sai theo số in (75 kJ; "10,8 J"). | VietJack 28/28, khớp |
| 34 | P08 | [`VatLi2026-ThanhHoa-LuongDacBang-Lan1`](../de/VatLi2026-ThanhHoa-LuongDacBang-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1d Đ, II.4c S — mơ hồ, thầy quyết. II.2d S, II.3c Đ (tính cả N vòng). | VietJack 28/28; khác II.1d (S) |
| 35 | P09 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10/kiem-chung-v2.md) (scan) | xong | 0 | — | Khớp 28/28. II.3a S (Đ nếu coi miệng ống ngang mặt thoáng), II.4b S — thầy quyết. III.6 = 0,82 (đẳng nhiệt theo lời đề). | không tìm thấy |

## Các điểm chờ thầy quyết (gom từ báo cáo 35 agent)

Độ tin cậy: mỗi đề có một lượt giải lại độc lập, không có đáp án chính thức để chốt. "Khớp" nghĩa là hai lượt giải (lô P và Fable) ra cùng đáp án. Với các ý phụ thuộc đọc hình mờ, hai lượt cùng đọc một ảnh gốc nên có thể cùng sai theo một hướng. Phiên chính soát bằng script: mỗi `kiem-chung-v2.md` đủ 28 dòng, cột "File" trùng `\True` / `\shortans` trong `.tex`. Phiên chính không giải lại từng câu.

### A. Câu / ý lệch (file khác kết luận cuối của Fable) — 3

| Đề | Câu | File | Fable | Mạng (14/11) | Ghi chú |
|---|---|---|---|---|---|
| Cụm liên trường Hà Tĩnh | II.2a | S | Đ (nghiêng, khoảng 2/3) | S (VietJack, như file) | pV sáu lần đầu lệch dưới 0,7 %, riêng lần 7 lệch +12,9 %; ý d đã tách lần 7 thành số liệu nghi ngờ. Không khẳng định file sai; chọn Đ thì phải viết lại lời giải ý a. |
| Kinh Môn II – Lần 2 | II.1a | S | Đ (nghiêng, khoảng 60 %) | S (VietJack, lí do hao phí) | "Nhiệt lượng nước thu vào bằng điện năng cung cấp": theo nguyên tắc phép đo (ý c tính đúng bằng đẳng thức này) → Đ; xét hao phí → S. Chọn Đ thì II.1 thành Đ S Đ Đ. |
| Ngô Gia Tự – Lần 1 | I.11 | C | D | **D** (VietJack đúng đề; loigiaihay, tuyensinh247 cũng D) | Đoạn trích tìm kiếm của loigiaihay, tuyensinh247 cũng ghi D (chưa mở được trang). `kiem-chung.md` cũ ghi chọn C "theo SBT Vật lí 12" — cần thầy đối chiếu bản in SBT KNTT bài 8. |

### B. Hai lượt giải khớp nhau, nhưng đáp án phụ thuộc cách xử lí lỗi đề gốc

- **Lương Thế Vinh II.2a**: file sửa Z của I-131 từ 51 thành 53 nên a Sai; theo nguyên văn đề gốc (Z = 51, in ở 6 chỗ) thì a Đúng.
- **Chuyên KHTN Lần 3 I.10**: giữ C (3,0 kW). Cùng bài ở đề Liên trường Nghệ An Lần 2 dùng H = 95 % với cùng bộ phương án → nhiều khả năng đề KHTN chép sai H = 90 %; thầy quyết giữ 90 % kèm ghi chú hay sửa 95 %.
- **Hưng Yên SGD Lần 1 II.2**: đồng ý sửa P = 12 kW → 1,2 kW (cho m₂ = 2,53 kg, khớp ý a); giữ 12 kW thì a Sai.
- **Liên trường Nghệ An Lần 2 I.8**: đồng ý sửa (2/2)kT → (3/2)kT.
- **Thái Nguyên SGD Lần 1 I.17**: phương án C trùng B ở đề gốc; đáp án A không đổi dù sửa hay không.
- **Quảng Ninh SGD I.16**: đề gốc không có phương án đúng; file chữa C. Đoạn trích VietJack ghi đáp án **B** (tức trường chữa dấu "+" ở B thành "·"). Thầy quyết chữa C hay chữa B.
- **Yên Hòa I.7**: giữ B theo λ = 34·10⁵ J/kg in trên đề (bốn phương án đều tính theo số này). III.4: file sửa N_A 6,2 → 6,02·10²³ (đáp số 2,97); theo nguyên văn có thể ra 3,06 tùy cách tính.
- **Tĩnh Gia I II.3**: theo chữ in là S S S S (như file); nếu sửa lỗi in ("20 °C", "J/(kg.K)", ý d "nhiệt lượng cần cung cấp cho chảo") thì S Đ Đ Đ — bản lời khác của câu này trên VietJack cũng ghi S Đ Đ Đ.
- **Cẩm Phả III.6**: đề gốc mất hình kích thước phòng; 14 kg chỉ đúng với phòng tự dựng 8 × 5 × 4 m (Δm = 0,0884·V). Chưa xác minh được kích thước gốc.
- **Tĩnh Gia I III.2**: 0,66 đúng với mạch nối tiếp tự dựng (đề gốc thiếu hình).

### C. Mệnh đề lệch số liệu — tính chặt là Sai như file, nhưng đề có dấu hiệu gõ nhầm (đáp án của trường có thể là Đúng)

- Cẩm Xuyên II.3d (1282 kg / đề "khoảng 1250 kg"); Phan Đăng Lưu II.2a (0,1787 mol / "xấp xỉ 0,17"); Ngô Gia Tự II.4d (4461 / đề in 4160 — nghi 4460); Nguyễn Khuyến Lần 3 II.1d (34,1 kJ / đề in "41 kJ" — nghi mất kí tự), II.1b (2,50·10⁶ / 2,64·10⁶); Nguyễn Khuyến LTT Lần 1 II.4c (85 % nếu chỉ tính nước / 92 % nếu tính cả vỏ ấm), II.4d (1,67 h / 1,8 h); Bắc Ninh SGD (scan) II.4d (3888 / 3995 — 3995 đúng với m = 0,18 kg); Liên trường Nghệ An Lần 2 II.2d (9,84 °C / đề ghi 8,9); Phú Thọ SGD Lần 1 II.2b (75,6 kJ / 75 kJ), II.2c (10 080 J / đề in "10,8 J").
- **Điểm mới (chưa có trong TIEN-DO)**: Kinh Môn II II.3d (3,33 W; 2,5 W của đề đúng bằng kết quả khi bỏ sót cos α); Chuyên KHTN Lần 3 II.1d (12,4 T; 4,0 T của đề đúng bằng kết quả khi áp nhầm công thức dây thẳng); Quảng Ninh SGD II.3d (2,56·10⁻⁴ W / đề in 2,65·10⁻⁴ — nghi đảo chữ số); Tĩnh Gia I II.3d ("nhiệt lượng mà nhôm thu vào" / số của đề là nhiệt lượng cả chảo thu); Cụm CM10 I.6 (đề ghi "Mười độ chia (10 °C)" → A như file; câu quen thuộc là "Một độ chia" → C).

### D. Hai cách hiểu — Fable chọn cùng cách với file

Chuyên KHTN Lần 1 III.4 (16; không trừ khí còn lại thì 18); Yên Hòa III.3 (78,6; trừ khí còn lại thì 78,1), II.1b (hướng nhìn hình); Cụm 13 trường I.17 (B mỗi dây 0,7 N; D tổng 1,4 N); Cụm liên trường Hà Tĩnh III.3 (4,65; 4,68); Phan Đăng Lưu I.16 (A và C cùng đúng theo SGK — KNTT / CTST, Cánh diều; file gõ C), III.2 (10 J; đoạn trích VietJack cũng 10), III.1 (20; đoạn trích VietJack cũng 20); Kinh Môn II III.6 (2,25 A → 2,3; gợi ý đổi yêu cầu làm tròn sang hàng phần trăm); Hàm Rồng II.4c (S; đáp án trường có thể Đ), III.6 (2108 theo hằng số SGK; 2105–2107 với hằng số khác); Hà Nội SGD II.2b; Hưng Yên SGD II.1c, d; Bắc Ninh SGD Lần 1 II.2c; Liên trường Nghệ An Lần 1 II.1c, II.4d; Phú Thọ SGD Lần 1 II.1a; Chuyên Phan Bội Châu II.2b, II.4b; Nguyễn Thị Minh Khai II.4c (99 kJ / 100 kJ); Ninh Bình SGD Lần 2 III.5 (6,23 với R = 8,31; 6,24 với 8,314), III.6 (1,98); Lương Đắc Bằng II.1d (Đ; Sai nếu hiểu chặt chữ "chứng minh được định luật"), II.4c (S; Đ nếu hiểu "do hao phí nên giá trị đo lớn hơn"), II.3c (Đ khi tính cả N = 1000 vòng; một vòng thì S); Nguyễn Khuyến LTT Lần 10 II.3a (S vì miệng ống sâu dưới mặt thoáng; Đ nếu coi ngang mặt thoáng), II.4b (S; chấm lỏng có thể Đ), III.6 (0,82 đẳng nhiệt theo lời đề, dù đề cũng ghi "cách nhiệt").

### E. Ý phụ thuộc đọc hình (chiều quấn dây, cực nguồn, phối cảnh, vị trí điểm) — Fable đọc độc lập trên ảnh gốc phóng to, đều khớp file

Nguyễn Thị Minh Khai I.3 (đoạn trích VietJack cũng D); Cụm CM10 II.4a, b, II.3b, c; Kinh Môn II II.2b; Nguyễn Khuyến LTT Lần 1 II.1c, II.2a, I.10; Nguyễn Khuyến LTT Lần 2 II.1b; Lào Cai SGD I.6, II.1c; Chuyên ĐH Vinh I.17, II.3; Liên trường Nghệ An Lần 1 I.8 (ghi chú "không phân biệt trước / sau" trong `kiem-chung.md` cũ chưa chính xác: mỗi vòng chỉ có một nét vắt qua mặt trước lõi); Chuyên Hạ Long II.1b; Thái Nguyên SGD Lần 1 II.1c (đo điểm ảnh bốn vạch cực); Ninh Bình SGD Lần 2 II.4a; Hà Nội SGD II.3; Lương Đắc Bằng II.2d (điểm (4) là giao của đường qua O với đường đẳng nhiệt → S).

### F. Đáp số Phần III đề không yêu cầu làm tròn / thiếu hằng số — đều khớp file

Bắc Ninh SGD Lần 1 III.6 (0,6 là giá trị đúng, không cần làm tròn); Quảng Ninh SGD III.2 (608), III.3 (0,44), III.6 (2,15; lấy 1 eV = 1,602·10⁻¹⁹ J thì 2,14); Chuyên ĐH Vinh II.4d, III.2 (14; không đổi với c = 4180 hay 4200); Nguyễn Khuyến LTT Lần 10 III.1 (0,88 chính xác); các đề không có "Cho biết" (Chuyên KHTN Lần 3, Nguyễn Khuyến LTT Lần 2, Hàm Rồng, Ninh Bình SGD Lần 2): đổi N_A, R, k không làm đổi đáp số, trừ Ninh Bình SGD Lần 2 III.5 và Hàm Rồng III.6 nêu ở mục D.

### G. Lỗi HÌNH vẽ lại sai quan hệ so với hình gốc (chuyển phiên vẽ hình; phiên này không sửa)

- **Yên Hòa I.13**: kí hiệu nguồn bị đảo cực (gốc: vạch dài ở trên / phía xa; TikZ: vạch ngắn ở trên) → cực nguồn mâu thuẫn với mũi tên I.
- **Nguyễn Thị Minh Khai II.2 (Hình a)**: đảo cực nguồn và chỉ vẽ 1 pin (gốc 2 pin, bản dài bên phải nối biến trở) → theo hình vẽ lại, lực từ lên X hướng lên, mâu thuẫn Hình b và đáp án ý a.
- **Chuyên Phan Bội Châu I.6**: hai electron ⊖ ở dây trái, phải của hình gốc bị vẽ thành nhãn "I" đỏ nhưng giữ chiều mũi tên của electron → đọc thành dòng điện chạy vào cực dương ở mạch ngoài.
- **Chuyên ĐH Vinh III.3**: vòng mũi tên từ trường quanh hai thanh ray vẽ cùng chiều (gốc ngược chiều nhau); thiếu dấu "−" ở đầu ray phía sau.
- Lệch nhỏ, không ảnh hưởng đáp án: Nguyễn Khuyến LTT Lần 1 II.4 (trục chia 5 khoảng tới 240 s, gốc 4 khoảng), II.2 (thiếu nét dây nối hai cuộn); Cẩm Phả II.1 (lưới 9 hàng, gốc 8); Cẩm Xuyên II.2 (nét đứt đường sức); Lào Cai SGD I.6, Liên trường Nghệ An Lần 1 I.8 (móc thừa ở vòng dây cuối); Chuyên KHTN Lần 1 III.6 (đầu pin hở với dây nối); Chuyên Phan Bội Châu II.3 (chấm xanh thiếu dấu "−"); Cụm CM10 II.4 (chi tiết móc dưới của cuộn dây).

### H. Lời đề, lời giải, ghi chú — sai sót nhỏ agent thấy (không đổi đáp án)

Cẩm Xuyên II.4d (lời giải ghi 18 070 s, đúng là 18 059 s); Phan Đăng Lưu II.2d (lời giải ghi "(2) → (5) đẳng áp" trong khi chu trình không có đoạn này); Chuyên Phan Bội Châu II.2c (14,14 → 14,13 m/s); Yên Hòa II.2b (lời giải thêm giả thiết "hai cánh tay đòn bằng nhau"). Sửa chữ chưa ghi ở mục "Sửa lời đề" của `kiem-chung.md`: Cụm liên trường Hà Tĩnh I.13 ("nhiệt T₁" → "nhiệt độ T₁"), Hưng Yên SGD I.18 (bỏ chữ "đó"), Bắc Ninh SGD (scan) I.16 (thêm "trạng thái"), Ninh Bình SGD Lần 2 III.3 ("phần chục" → "phần mười"). Lương Thế Vinh: `kiem-chung.md` ghi sửa ¹³¹₅₁I "cả 4 chỗ", thực tế 6 chỗ (file đã sửa đủ). Kinh Môn II: `kiem-chung.md` ghi bỏ dòng "…" ở bảng II.1 nhưng file vẫn giữ.

### I. Tên, lần thi

- Liên trường Nghệ An Lần 1: trang hoatieu (theo đoạn trích tìm kiếm) gọi là "Sở Nghệ An Lần 1", 24 mã đề 3101–3124 → ủng hộ cách đặt "Lần 1".
- **Bắc Ninh SGD (scan)**: theo đoạn trích tìm kiếm của chuvanbien.vn (file `LOP12_DEKTCUOIKI1_SOBACNINH_SOCANTHO.pdf`), đây có thể là đề **kiểm tra cuối học kì I** Vật lí 12 của Sở Bắc Ninh (45 phút), bên sưu tầm đổi tiêu đề thành "khảo sát chất lượng tốt nghiệp THPT, 50 phút". Chưa xác nhận được (trang bị chặn) — thầy xem có giữ đề này trong bộ thi thử không.

### J. Đối chiếu trên mạng ở lượt đầu (đã làm bổ sung — xem mục "Đối chiếu mạng bổ sung (14/11/2026)")

Ghi lại tình trạng lượt đầu:

Mạng của phiên (môi trường Default, mức Limited, danh sách tên miền cho phép trống) chặn các trang đăng đề: `khoahoc.vietjack.com`, `hoatieu.vn`, `chuvanbien.vn`, `loigiaihay.com`, `tuyensinh247.com`, `docs.google.com`, `vietnamnet.vn`, `image.plo.vn`, `news.laodong.vn`. Agent chỉ đọc được đoạn trích của công cụ tìm kiếm (một phần ở 5 đề: Phan Đăng Lưu, Quảng Ninh SGD, Nguyễn Thị Minh Khai, Cụm CM10, câu I.11 Ngô Gia Tự). Link đã ghi ở mục "Nguồn trên mạng" của từng `kiem-chung-v2.md`:

- VietJack có trang cả đề cho 10 đề (Lương Thế Vinh, Cẩm Xuyên, Chuyên KHTN Lần 3, Phan Đăng Lưu, Quảng Ninh SGD, Nguyễn Thị Minh Khai, Cụm CM10, Liên trường Nghệ An Lần 1, Chuyên Hạ Long, Chuyên Phan Bội Châu) và trang câu lẻ cho 7 đề (Cụm liên trường Hà Tĩnh, Thái Nguyên SGD Lần 1, Liên trường Nghệ An Lần 2, Chuyên KHTN Lần 1, Tĩnh Gia I, Nguyễn Khuyến LTT Lần 1, Nguyễn Khuyến LTT Lần 10). Đáp án cả đề trên VietJack có khi nằm sau gói VIP.
- hoatieu.vn có trang cho ít nhất 8 đề (Hưng Yên SGD, Bắc Ninh SGD Lần 1, Hàm Rồng, Chuyên Hạ Long, Phú Thọ SGD, Cụm CM10, Liên trường Nghệ An Lần 1, Ninh Bình SGD), nhiều trang kèm file đáp án.
- Cuối phiên (14/11/2026) thầy đã duyệt thêm 5 tên miền `khoahoc.vietjack.com`, `hoatieu.vn`, `chuvanbien.vn`, `loigiaihay.com`, `tuyensinh247.com` vào danh sách cho phép của môi trường Default. Tuy vậy, trong phiên này lệnh đọc các trang đó (cả `curl` lẫn WebFetch) vẫn bị chế độ cấp quyền tự động của Claude Code chặn (lí do "Unauthorized Access"), nên chưa chạy bổ sung. Muốn chạy: thêm luật cho phép đọc các tên miền này (ví dụ `WebFetch(domain:khoahoc.vietjack.com)`) vào `permissions.allow` của `.claude/settings.json` trong repo, rồi chạy bổ sung riêng bước đối chiếu mạng cho các điểm ở mục A–D (rẻ, không phải giải lại); chỉ đọc phần công khai, không vượt nội dung trả phí (VIP).

### K. Quy trình

- Phiên chính kiểm bằng dấu thời gian truy cập tệp: với cả 35 đề, `fable.md` (nháp đáp án độc lập) được ghi **trước** lần đầu `kiem-chung.md` của đề đó được mở (cách nhau từ khoảng 45 giây đến 2 phút). Không kiểm được theo cách này với file `.tex` (phiên chính đã đọc các file `.tex` từ đầu phiên để dựng công cụ trích đáp án).
- 4 agent tự báo có chạy `git status --short` (chỉ đọc) — trái quy định "không chạy git" nhưng không thay đổi repo. Thay đổi của nhánh so với `main` chỉ gồm 35 file `kiem-chung-v2.md` mới và file này; không file nào có sẵn bị sửa.
- Nháp của từng agent (`fable.md`, `mang.md`, script tính) ở `/tmp/<tên đề>/` của máy phiên, không commit.

### L. Việc tiếp theo đề xuất

1. Thầy quyết các điểm mục A–D (nhất là 3 ý lệch mục A, các câu sửa lời đề mục B, các mệnh đề nghi gõ nhầm mục C), rồi một phiên sửa `.tex`, `kiem-chung.md`, `TIEN-DO.md` theo quyết định.
2. Chuyển 4 lỗi hình mục G (Yên Hòa I.13, Nguyễn Thị Minh Khai II.2, Chuyên Phan Bội Châu I.6, Chuyên ĐH Vinh III.3) cho phiên vẽ hình (phần A).
3. ~~Chạy bổ sung đối chiếu mạng~~ — đã làm ngày 14/11/2026 (mục "Đối chiếu mạng bổ sung"). Thầy quyết thêm các câu mạng khác file ở M2, M3 (nhất là Ngô Gia Tự I.11, III.4, III.5; Nguyễn Thị Minh Khai II.2c; Lương Thế Vinh II.2a, II.3d; Quảng Ninh SGD I.16) và tên / lần đề ở M5 (Bắc Ninh SGD scan, Lương Thế Vinh).
4. Sửa các sai sót nhỏ mục H cùng lúc với việc 1.
