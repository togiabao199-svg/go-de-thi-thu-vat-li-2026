# Kiểm chứng đáp án – VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10

Đề gốc: PDF scan (sách "250+ đề thi thử THPTQG Vật lý 2026", có watermark chéo), "Trường Nguyễn Khuyến – Lê Thánh Tông Hồ Chí Minh, đề thi thử tốt nghiệp THPT, lần 10, năm học 2025 – 2026", mã đề 100, 5 trang. Không có đáp án, không có lời giải (cuối đề chỉ có dòng quảng cáo "Đáp án + lời giải chi tiết xem tại website…"): mọi câu tự giải, các câu có số liệu tính lại bằng Python (script ở thư mục nháp `/tmp/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10/py/giai.py`). Đọc đề qua ảnh trang `pdftoppm -r 200`; watermark đè không làm mất chữ nào (đã phóng to các chỗ bị đè: I.13 "720 J", I.14 "0,25p₀", I.17 "0,1 kg", III.4 "180·10³"), không có chỗ `% ???`.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | A C C A D C A B B C D C B C A A D A | I.3: T₁ > T₂ nên đường đẳng nhiệt T₁ ở xa gốc hơn ⇒ Hình 3 (Hình 1 ghi T₁ < T₂ trên trục, Hình 4 không phải hyperbol); I.5: nén đoạn nhiệt ⇒ nhận công, nội năng tăng; I.9: nội năng phụ thuộc T và V; I.13: 1750 − 720 = 1030 J; I.14: p₀·1,25V = pV; I.15: Q = 1,5·4200·73 = 459 900 J, A = 1000·720 J ⇒ H = 63,875 %; I.16: (9,9 − 2)/20·100 = 39,5 °C; I.17: c = (38 + 840)·4/(0,1·76) = 462,1 J/(kg.K); I.18: ΔU = mgl·sin30° − ½mv² = 30 − 15 = 15 J |
| II.1 | không có | Đ Đ S Đ | p·l = 4500 cm·kPa ở cả bốn lần đo; pV = 10⁵·0,45·7,5·10⁻⁵ = 3,375 Pa·m³ (đề ghi 45·10³); l = 20 cm ⇒ p = 225 kPa |
| II.2 | không có | S S Đ Đ | m_nước = 0,5 g/s·600 s = 0,3 kg; bay hơi thu nhiệt; m_kk = 1,2·36 = 43,2 kg; Δt = 0,3·2,25·10⁶/(43,2·1005) = 15,547 ≈ 15,55 °C |
| II.3 | không có | S Đ Đ Đ | xem mục "Điểm cần thầy xem"; d) p_k1 = 760 − 746 = 14 mmHg, l₁ = 54 mm, l₂ = 54 − 6 = 48 mm ⇒ p_k2 = 15,75 mmHg ⇒ p₀ = 767,75 mmHg |
| II.4 | không có | Đ S S Đ | trong t phút: môi trường làm tan m, dây nung làm tan M − m; 2t phút: 2(M − m) (đề ghi 2(M − 2m)); λ = 24·120/(8·10⁻³) = 3,6·10⁵ J/kg |
| III.1–III.6 | không có | 0,88 / 60 / 0,12 / 2,4 / 0,77 / 0,82 | III.1: 2,2/2,5 = 0,88 lít; III.2: 200 − 140 = 60 J; III.3: 0,2·4190·90 + 0,02·2,26·10⁶ = 120 620 J = 0,12 MJ; III.4: 2,5·380·1054 + 2,5·180·10³ = 1 451 300 J, t = 1 451 300/10 000 = 145,1 s = 2,42 phút; III.5: cân bằng ở 6 °C (đọc đồ thị), Q_thu = 4200 + 68 000 + 5040 = 77 240 J = m·4200·24 ⇒ m = 0,766 kg; III.6: p₂ = 10⁵ + 100/0,01 = 1,1·10⁵ Pa ⇒ V₂ = 900/1,1 = 818,2 cm³ ⇒ x = 0,82 |

## Điểm cần thầy xem

- **II.3 a)** "Áp suất khí quyển bằng áp suất ở miệng ống thủy tinh trong chậu": gõ **Sai** (miệng ống nằm sâu dưới mặt thoáng thủy ngân trong chậu nên áp suất tại miệng ống lớn hơn p₀; p₀ bằng áp suất tại điểm ngang mặt thoáng). Nếu người ra đề hiểu "miệng ống" là mức mặt thoáng thì ý này Đúng.
- **II.4 b)** "Ở bước 2, nước đá tan … do nhận nhiệt lượng từ dây nung": gõ **Sai** vì ở bước 2 nước đá nhận nhiệt từ cả dây nung và môi trường (chính là ý đồ trừ m ở bước 1). Nếu hiểu lỏng thì có thể chấm Đúng.
- **I.12**: chọn C "ngưng tụ" (hơi → lỏng); B "ngưng kết" là hơi → rắn, không đúng.
- **III.1**: đề không yêu cầu làm tròn nhưng đáp số chính xác 0,88 (4 kí tự), không cần ghi KIỂM TRA.
- **III.6**: đề vừa nói "xilanh và pit-tông cách nhiệt" vừa cho "nhiệt độ của khối khí không đổi"; lời giải theo dữ kiện đẳng nhiệt (đề gốc giữ nguyên).

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ dòng sách "250+ đề thi thử THPTQG Vật lý 2026", watermark, chân trang (tên, số Zalo), "Đề chính thức", "Đề thi gồm 05 trang", họ tên / số báo danh, mã đề 100, "HẾT", câu "Thí sinh không sử dụng tài liệu…", dòng quảng cáo đáp án cuối đề.
- Cho biết: "R = 8,31 J.mol⁻¹" (thiếu K⁻¹) → "8,31 J·mol⁻¹·K⁻¹"; "t(⁰C)" → "t (°C)".
- Tiêu đề Phần II gốc bị cụt ("…ở mỗi câu, thí sinh") → dùng tiêu đề chuẩn.
- Chính tả thống nhất: "hoá" → "hóa", "thuỷ" → "thủy", "toả" → "tỏa"; "pít-tông", "pittông" → "pit-tông"; "J/(kg. K)" → "J/(kg.K)"; "⁰C", "24∘C", "30∘" → "°C", "°"; "1,2 kg/m3" → "1,2 kg/m³"; "2,0 Lít" → "2,0 lít"; "200 gam" → "200 g"; "38, 5⁰C", "7, 5.10⁻⁵", "2, 25.10⁶", "3, 4.10⁵", "3, 6.10⁵" (dấu cách thừa sau dấu phẩy) → viết liền.
- I.11: in đậm "không" (bản gốc không in đậm). I.1, I.3 giữ in đậm "đúng" như gốc.
- I.15: bảng thông số gốc có cột thứ ba lặp lại nhãn cột thứ nhất ("Điện áp định mức / Công suất định mức / Dung tích") mà không có số liệu → bỏ cột thừa, gõ bảng 2 cột.
- II.1 c): "45.10³ Pam³" → "45·10³ Pa·m³". II.1: "7, 5.10⁻⁵ m²" → "7,5·10⁻⁵ m²".
- II.3: "80 cm − 90 cm" → "80 cm – 90 cm" (gạch nối khoảng); d) "Áp suất" viết hoa giữa câu → "áp suất", "767,75mmHg" → "767,75 mmHg".
- II.4: "bật biến áp nguồn" giữ nguyên; "Bước 1:", "Bước 2:" in đậm nghiêng như gốc.
- III.6: "S = 100 cm" (thiếu mũ 2) → "S = 100 cm²"; "x.10⁻³ m³" → "x·10⁻³ m³".

## Đánh số lại câu

Đề gốc đã đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6), giữ nguyên. Đề không có tham chiếu chéo giữa các câu.

## Hình

8 hình gốc → 8 `tikzpicture` (ảnh so ở `so-hinh/`); hai bảng (I.15, II.1) gõ bằng `tabular`. Vùng cắt ảnh trang (200 dpi, tỉ lệ khổ trang): I.3 tr.1 `0.09:0.426:0.93:0.567`; I.5 tr.1 `0.76:0.629:0.945:0.763`; II.1 tr.3 `0.765:0.184:0.945:0.291`; II.2 tr.3 `0.70:0.445:0.945:0.555`; II.3 tr.3 `0.695:0.711:0.925:0.904`; II.4 tr.4 `0.74:0.239:0.945:0.394`; III.5 tr.5 `0.685:0.07:0.935:0.212`; III.6 tr.5 `0.81:0.237:0.93:0.362`.

- Hình gốc nền xám, trục xanh lá / đỏ sẫm, chữ watermark "thukhoadaihoc.vn" trên hình: bỏ nền, bỏ watermark, trục đen theo quy chuẩn.
- I.3: bốn đồ thị giữ nguyên dạng, nhãn T₁, T₂ đúng vị trí gốc.
- I.5 (ghế văn phòng + ống A, B phóng to), II.1 (bộ thí nghiệm Boyle với bơm đạp chân), II.2 (quạt hơi nước), II.4 (bộ thí nghiệm nhiệt nóng chảy) là hình thực tiễn: vẽ có khối, gắn `% giuhinh`; chờ phiên vẽ lại chi tiết.
- II.3: thủy ngân tô xám bạc (màu thật) thay cho xanh cyan của gốc; nhãn giữ nguyên chữ gốc ("Màng ngăn thủy ngân bay hơi").
- III.5: đường nước (từ 30 °C) màu `VLdo`, đường nước đá (từ −10 °C) màu `VLxanh`; nhiệt độ cân bằng 6 °C là dữ kiện có trên đồ thị gốc.
- III.6: gia trọng tô màu đồng, pit-tông xám, khí `VLxanh!10`.
- Dàn trang: hình II.3, II.4, III.5, III.6 đặt bên phải câu dẫn (như bản gốc) để bản đề ĐẠT.
