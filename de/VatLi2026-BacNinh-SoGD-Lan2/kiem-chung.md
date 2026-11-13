# Kiểm chứng đáp án – VatLi2026-BacNinh-SoGD-Lan2

Nguồn: `kho/goc/Bac Ninh - So GDDT - Lan 2.docx` (Sở GD&ĐT Bắc Ninh, mã đề 0207), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 (trừ I.9) | D A A D A B C C · A D C C D D B A B | trùng | I.4: \|e\| = độ dốc đồ thị Φ(t), tăng dần A → B → C; I.5: 26 p + 26 e = 52 |
| **I.9** | **C** | **B** | **Lệch.** Theo hình, mạch ngoài nối vào đầu M và con chạy (không nối M, N như lời giải gốc viết). Dịch con chạy từ M sang N: điện trở đoạn M–con chạy tăng, dòng điện qua nam châm điện giảm, từ thông qua khung giảm → dòng cảm ứng chống lại sự giảm → khung bị **hút lại gần** (B). D sai vì từ thông giảm. File gõ theo B, có `% KIỂM TRA`. Thầy xem lại. |
| II.1 | Đ Đ Đ S | trùng | ý c) "(III) là đủ để đưa ra kết luận (IV)" — giữ Đ theo đáp án gốc (thí nghiệm làm theo nhiều cách: dịch nam châm, đổi tốc độ, dịch cuộn dây) |
| II.2 | S Đ Đ Đ | trùng | L = P(t₂ − t₁)/(m₁ − m₂); dây hở làm m₁ − m₂ nhỏ đi nên L tính được lớn hơn |
| II.3 | Đ Đ S S | trùng | |
| II.4 | Đ S Đ Đ | trùng | |
| III.1–III.6 | 242 / 8103 / 30,2 / 0,44 / 1198 / 9,15 | trùng | xem phép tính dưới |

## Phép tính chính (Python)
- III.1: V₀ = pVT₀/(2Tp₀) = 80·200·223/(2·295·25) = 241,90 m³ → 242.
- III.2: n = pV/(RT) = 101 000·200/(8,31·300) = 8102,69 mol → 8103.
- III.3: đồ thị: U₀₁ = 320 V (lưới 80 V/ô, 15 ms/ô, cực đại tại 75 ms, chu kì 90 ms). U₂ = (320/√2)·100/750 = 30,17 V → 30,2.
- III.4: Δt = T/2 = 2,5·10⁻⁵ s; |ΔΦ| = 2NB₀S, S = 3,14·0,03² = 2,826·10⁻³ m²; B₀ ≤ 0,01·1·2,5·10⁻⁵/(2·100·2,826·10⁻³) = 4,423·10⁻⁷ T → 0,44 µT (π thật: 0,4421 µT, cùng kết quả).
- III.5: N₀ = 192·0,17/60·6,02·10²³ = 3,2749·10²³; λ = ln2/(5,27·365·86 400) = 4,1707·10⁻⁹ s⁻¹; H(1 năm) = λN₀·2^(−1/5,27) = 1,19752·10¹⁵ Bq → x = 1197,52 → 1198.
- III.6: công suất liều tối thiểu 24/40 = 0,6 Gy/phút; t = 5,27·log₂(2/0,6) = 9,1538 năm → 9,15.

## Sửa lời đề (lỗi chữ bản gốc)
- I.8: in đậm "sai" ("Chọn câu **sai**"), gộp dòng "Chọn câu sai." với câu dẫn.
- I.17: in đậm "**không**".
- I.4: bỏ dấu chấm thừa cuối câu dẫn ("…theo thứ tự tăng dần là."); "(hình a)", "(hình b)" viết "(Hình a)", "Hình b" khớp chú thích hình.
- I.10: phương án B, C "Q.m", "1/(m.Q)" gõ dấu nhân "Q·m", "1/(m·Q)".
- II.2: công thức ý b) "P.(t₂ − t₁)" bỏ dấu chấm; "hoá hơi" → "hóa hơi".
- II.4: "CO₂" gõ CO$_2$.
- III.4: "điều hoà" → "điều hòa"; bỏ gạch chân thừa ở "10 mA."
- Thông tin chung câu 1–2: bỏ thẻ chữ thừa "<u>…</u>" quanh "khối lượng mol giống nhau" (bản gốc in nguyên văn thẻ HTML).
- Thông tin chung câu 5–6: kí hiệu hạt nhân bản gốc vỡ ("27⁶⁰Co") → ${}^{60}_{27}\text{Co}$; bỏ chữ nghiêng lẫn trong đoạn ("giống nhau có chu kì bán rã… khối lượng").
- Cho biết: "N_A = 6,02·10²³ mol⁻¹" giữ đơn vị mol⁻¹ theo gốc.

## Trình bày
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại). Hai khối "Dùng thông tin sau cho câu 1 và câu 2", "…câu 5 và câu 6" đặt trong câu đầu của cặp (câu 1, câu 5), mở đầu bằng chữ nghiêng "Dùng thông tin sau cho câu~\ref{..} và câu~\ref{..}:" như đề Cà Mau – Lần 1 cùng lô, để `dan_trang.py` đo, giữ trọn khối với câu hỏi (phiên chính thống nhất). Khối câu 5–6 đặt hình bên cạnh chữ để gọn trang.
- Hình: 9 hình gốc vẽ lại bằng TikZ (I.4 khung dây quay + đồ thị Φ(t); I.9 khung ABCD, nam châm điện, biến trở; II.1 điện kế – cuộn dây – nam châm; II.2 bộ dụng cụ đo nhiệt hóa hơi; II.3 khinh khí cầu; III.1 khoang máy bay; III.3 máy biến áp + đồ thị u₁(t); III.4 khung dây trên giá; III.5 máy Gamma Knife). Ảnh so ở `so-hinh/`.
- Hình Gamma Knife bỏ dòng chữ quảng cáo tiếng Anh "Treatment without an incision" của ảnh gốc.
- Tô màu lại hình theo bảng màu 13/11/2026 (I.4 cực N đỏ, S xanh, đường sức và $\vv{B}$ xanh, khung dây và vành khuyên màu đồng, đường $\Phi(t)$ xanh very thick, điểm A, B, C chấm tròn viền đen; I.9 khung ABCD đồng, biến trở nền đồng nhạt, giá treo gỗ; II.1 thanh nam châm đế nửa S xanh, nửa N đỏ, kim điện kế đỏ; II.2 màn hiển thị xanh lá nhạt, cọc và dây đỏ của nguồn, nước trong bình xanh; III.1 ghế xanh, thảm lối đi, đèn trần vàng nhạt; III.3 đầu dây đồng, đồ thị $u_1$ đỏ very thick; III.4 cuộn dây đồng, tấm nhựa xanh nhạt; III.5 vỏ máy xám xanh, chùm tia vàng nhạt, tâm hội tụ cam; II.3 giữ màu sẵn có).
