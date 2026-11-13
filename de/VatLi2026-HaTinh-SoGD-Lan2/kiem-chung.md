# Kiểm chứng đáp án – VatLi2026-HaTinh-SoGD-Lan2

Nguồn: `kho/goc/Ha Tinh - So GDDT - Lan 2.docx` (Sở GD&ĐT Hà Tĩnh, mã đề 0306), có bảng đáp án và lời giải tham khảo đủ ba phần. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | A D D A B A C B D C A B D C B A C C | trùng | I.3: c = 8400/22,5 = 373,3 J/(kg.K) (C bình = 1148 J/K); I.8: 100·(2,20/2,31)⁸ = 67,68 kPa; I.14: Δm = 0,2009 amu → 187,14 MeV; I.17: e = 0,15 mV, i = 0,5 mA, ngược chiều kim đồng hồ A→D→C→B |
| **I.4** | **A (Hình 3)** | **A, sau khi sửa hình** | **Ảnh gốc Hình 3 vẽ I hướng LÊN, B hướng ra, F sang phải: theo quy tắc bàn tay trái hình này ĐÚNG, khi đó cả 4 hình đều đúng (câu không có đáp án).** Lời giải gốc ghi "Hình 3: I hướng xuống … F phải sang trái, nhưng hình vẽ cho sang phải: sai". Vẽ lại Hình 3 với I hướng xuống để khớp lời giải và đáp án gốc; ghi `% KIỂM TRA`. Thầy xem. |
| **I.5** | **B (N – S – N)** | **B, sau khi sửa hình** | **Ảnh gốc ghi bên phải: ray trên S, tàu N, ray dưới "S"** — mâu thuẫn với mũi tên lực đẩy ở dưới và lời giải gốc ("cực dưới là N"); nếu giữ S thì không có phương án đối xứng. Vẽ lại cực dưới bên phải là N; ghi `% KIỂM TRA`. Thầy xem. |
| II.1 | Đ S Đ Đ | trùng | q_n/q_l = 28/32 = 0,875; lưu lượng cực đại 0,7 + 0,6125 = 1,3125 lít/s ≠ 1,4 |
| II.2 | Đ S Đ Đ | trùng | lý thuyết (định luật Lenz) |
| II.3 | S Đ S Đ | trùng | n = 10⁵·75·10⁻⁶/(8,31·318) = 2,84·10⁻³ mol; V/T = 0,2358; 0,2357; 0,2355; 0,2361; 0,2359. Đề không cho R: dùng 8,31 (ý a sai với mọi R hợp lí) |
| II.4 | Đ Đ S Đ | trùng | 2^(−2026/5730) = 0,7826 → giảm 21,7 % ≠ 25 % |
| III.1–III.6 | 727 / 7,11 / 0,84 / 4,05 / 12,6 / 27 | trùng | xem phép tính dưới; **III.1 có `% KIỂM TRA`** |

## Phép tính chính (Python)
- III.1: E = Pt/H = 175·10⁶·86 400/0,25 = 6,048·10¹³ J; N = E/(203·1,6·10⁻¹³) = 1,862·10²⁴; m = N/N_A·235 = 726,9 g → 727. **KIỂM TRA:** đề ghi "công suất nhiệt 175 MW" lại cho "hiệu suất 25%" — nếu 175 MW là công suất nhiệt phân hạch thì không chia hiệu suất, m ≈ 182 g (lời giải gốc cũng ghi chú điều này). Đề không cho N_A và đổi MeV → J: dùng 6,02·10²³, 1,6·10⁻¹³ J (lấy 6,022·10²³ và 1,602·10⁻¹³ J thì ra 726). Gõ theo đáp án gốc 727.
- III.2: C(13V₀; p₀); trên BC p/p₀ = (16 − x)/3, pV/(p₀V₀) = x(16 − x)/3 lớn nhất 64/3 tại x = 8; nhỏ nhất tại A: 3 → 64/9 = 7,11.
- III.3: e = π·(10⁻³)²·0,02/0,075 = 8,378·10⁻⁷ V = 0,84 μV.
- III.4: p = ρv²/3 = 0,06·450²/3 = 4050 Pa = 4,05 kPa.
- III.5: B = 4π·10⁻⁷·(100/0,02)·2 = 12,57 mT → 12,6.
- III.6: x = (210/131)·(1 − 2^(−1/8,02))/(1 − 2^(−1/138,4)) = 26,57 → 27.

## Sửa lời đề (lỗi chữ bản gốc)
- I.4 (hình), I.5 (hình): xem bảng trên.
- I.7: kí hiệu hạt nhân "⁶³29Cu, ²³⁸92U" gõ đúng ⁶³₂₉Cu, ²³⁸₉₂U; "đơn giản hoá" → "đơn giản hóa"; "số khối A" → $A$. Nhãn trục hình gốc "E_binding/Mev/nucleon" → "$E_{\text{lkr}}$ (MeV/nucleon)" (khớp kí hiệu trong câu).
- I.14: "²³11Na" → ²³₁₁Na; "1 amu.c²" → 1 amu·c².
- I.16: "-110 kJ", "-90 kJ" gõ dấu trừ toán học.
- III.1, III.6: "²³⁵92U", "²¹⁰84Po", "¹³¹53I" gõ đúng chỉ số.
- III.2: "đồ thị p - V" → "đồ thị (p, V)"; "Tỷ số" → "Tỉ số".
- III.5: "4π.10⁻⁷nI" → 4π·10⁻⁷nI.
- III.6: "Geiger-Muller" → "Geiger – Müller"; "ion hoá" → "ion hóa".
- II.3: "pít-tông" → "pit-tông" (thuật ngữ SGK); danh sách chú thích hình gốc gạch đầu dòng gộp thành một đoạn, đặt cạnh bảng số liệu; vạch chia thước trên xilanh gốc ghi "100 cm" → "cm³" (thể tích); màn hình cảm biến nhiệt độ gốc ghi "24 °C" để trống (không phải số liệu bài).
- II.4: "Vonfram" → "vonfram"; chú thích hình (ảnh gốc): "Silicon", "Carbon-14" viết thường; "Vật liệu chắn màng" đọc là "Vật liệu chắn mỏng" (chữ ảnh gốc mờ — thầy xem).
- I.4 in đậm "không đúng" như gốc. Không câu nào khác có từ phủ định cần in đậm.

## Trình bày
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại).
- Khối "Sử dụng các thông tin sau cho Câu 17 và Câu 18" đặt trong câu I.17, mở đầu `\textit{Dùng thông tin sau cho câu~\ref{..} và câu~\ref{..}:}`.
- Hình: 9 hình vẽ lại bằng TikZ, có `% giuhinh` ở 4 hình thực tiễn (II.2, II.3, II.4, III.6):
  - I.4 bốn hình lực từ (nền vùng từ trường `VLxanh!8`, ⊗/⊙ có vòng tròn, I đỏ, F xanh lá).
  - I.5 mặt cắt tàu đệm từ, đặt bên phải phương án; nam châm bên trái (cực cần suy luận) để xám, bên phải N đỏ / S xanh; mũi tên lực xanh lá.
  - I.7 đồ thị E_lkr – A (lưới 40 × 2, 19 điểm đọc từ ảnh gốc).
  - I.17 khung dây ABCD + đồ thị B(t).
  - II.2 sơ đồ phanh tái sinh hai giai đoạn (đủ chữ trong khung, chữ cỡ 5,5–6 pt), rộng 16,5 cm.
  - II.3 bộ thí nghiệm xilanh – áp kế – cảm biến – hộp nước.
  - II.4 pin hạt nhân C-14 nhiều lớp, đủ 6 chú thích (ý a dựa vào chú thích lớp 5).
  - III.2 chu trình hình bình hành (mỗi quá trình một màu, vùng chu trình tô `VLla!35`).
  - III.6 máy đếm Geiger cầm tay + ống đếm, bộ đếm, loa (màn hình để trống; bỏ chữ hiệu "S.E.A.P.", "PM-141A Radiation Detector").
- Macro riêng khai báo trong file đề: `\VLchamtron` (⊙ có vòng, cặp với `\VLnhantron`), `\VLtiaset`, `\VLpindung`, `\VLbanhrang`, `\VLoto`, `\VLbanhxe`, `\VLrotor`.
- Ảnh so ở `so-hinh/`.

## Dàn trang
- Bản đề 7 trang (ĐẠT), bản lời giải 11 trang (trang 2 trống 6,7 cm, trang 5 trống 7,0 cm: trong giới hạn 1/3).
- II.3: chú thích (1)–(6) đặt cạnh bảng số liệu; II.4 tách câu dẫn (trang 5) / bảng Phát biểu (trang 6).
- Đã soát bản xám (trang 4–5 bản đề): các đối tượng phân biệt được; cực N/S có chữ.
