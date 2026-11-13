# Kiểm chứng đáp án – VatLi2026-GiaLai-SoGD

Nguồn: `kho/goc/Gia Lai - So GDDT.docx` (mã đề 0227, có bảng đáp án + lời giải sau dòng "Chọn X").
Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | A C C A **B** C D B A C A B B B A B D D | A C C A **D** C D B A C A B B B A B D D | I.1: A = 1,5·10⁵·1,2·10⁻³ = 180 J, ΔU = 180 − 40 = 140 J; I.3: B = 0,06/(4,5·0,1) = 0,133 T; I.8: t = 3T = 16 710 năm; I.9: 1,505·10²³·3,27·1,6·10⁻¹³ = 7,87·10¹⁰ J; I.13: 596/298 = 2,0; I.16: E_lkr(Au) < E_lkr(Te) < E_lkr(Y); I.18: F = 0,06 N, hướng lên |
| **I.5** | **B (Hình 4)** | **D (Hình 1)** | **Lệch.** Dòng điện hướng ra: đường sức là đường tròn đồng tâm, ngược chiều kim đồng hồ, càng xa dây càng thưa. Hình 1 đúng cả chiều lẫn phân bố (khoảng cách các đường tròn tăng dần ra ngoài, có vẽ tiết diện dây). Hình 4 cùng chiều nhưng hai đường ngoài sát nhau, cách xa hai đường trong (mật độ đường sức không giảm dần), không vẽ dây; Hình 3 chiều không nhất quán (đa số cùng chiều kim đồng hồ). Lời giải gốc chỉ xét chiều nên không phân biệt được Hình 1 và Hình 4. File gõ theo D, có `% KIỂM TRA` — thầy xem lại. |
| II.1 | Đ S Đ Đ | trùng | L = 4·0,04 = 0,16 m; B = 0,0689/(4,48·0,16) = 96,1 mT; F' = 68,9·cos30° = 59,7 mN |
| II.2 | Đ S S Đ | trùng | Q tỏa = 3,03·4200·5 = 63 630 J; λ = (63 630 − 3150 − 10 080)/0,15 = 336 000 J/kg; m₁λ = 50 400 J ≠ 3150 J |
| II.3 | Đ Đ S Đ | trùng | n = 1,24·10⁵·3·10⁻⁶/(8,31·296,5) = 1,510·10⁻⁴ mol |
| II.4 | Đ S Đ S | trùng | H(60 h) = 36·2^(−60/192) = 28,99 mCi < 30 mCi (đạt 30 mCi sau 50,5 h); m₀ = 0,289 μg, m(48 h) = 0,243 μg ≠ 0,43 μg |
| III.1–III.6 | 124 / 58 / 31 / 11 / 1,08 / 240 | trùng | III.1: N = 7,04·10¹⁸, H = 123,85 Bq (năm 365 ngày; 365,25 ngày cho 123,76) → 124; III.3: T = 303,86 K → 30,86 °C → 31; III.4: ΔS = 5,36·10⁻³ m², I = 10,72 mA → 11; III.5: Q = −1020 + 2100 = 1080 J; III.6: V₂ = 3V₁, V₁ + V₂ = 320 → 240 mL |

## Sửa lời đề (lỗi chữ bản gốc)
- In đậm từ phủ định: I.2 "**sai**", I.6 "**không**", I.10 "**sai**", I.12 "**không**", I.14 "**không**".
- I.1, II.3 (câu dẫn và hình): "pít-tông" → "pit-tông" (thuật ngữ SGK, thống nhất với III.5).
- I.3: phương án "0,47.10⁻²T" → $0{,}47\cdot 10^{-2}$ T (gõ lại kí hiệu).
- I.4, I.8, I.9, II.4, III.1, III.2: kí hiệu hạt nhân bản gốc vỡ ("47^107 Ag", "6^14 C", "53^131 I"...) gõ lại dạng ${}^{A}_{Z}\text{X}$.
- I.11: "Φ = BScosα" → $\Phi=BS\cos\alpha$.
- II.1 b): "B = F.L/I" gõ $B=\dfrac{F\cdot L}{I}$ (giữ nội dung mệnh đề sai).
- III.1: "becơren" → "becquerel" (thuật ngữ SGK 2018).
- Khối "Cho biết": thêm chữ "tính" vào dòng "Không làm tròn kết quả các phép (tính) trung gian".

## Hình
- 8 hình vẽ lại bằng TikZ: I.1 (đồ thị p–V), I.3 (dây AB treo hai lực kế giữa hai cực nam châm, `% giuhinh`), I.5 (4 hình đường sức), I.16 (đồ thị E_lkr theo A), II.1 (bộ đo lực từ bằng cảm biến lực, `% giuhinh`), II.2 (sơ đồ nhiệt lượng kế, đặt cạnh bảng số liệu), II.3 (xilanh – áp kế – cảm biến nhiệt độ – tay quay, `% giuhinh`), III.4 (khung vuông → hình thoi).
- I.3, II.1: nam châm tô N đỏ, S xanh theo quy ước (ảnh gốc màu xám).
- II.1: màn hình nguồn điện ảnh gốc ghi "11.5 V / 5.88 A" (không khớp đề, đề cho I = 4,48 A) → vẽ lại chỉ ghi "4.48 A"; màn hình lực kế ghi "68.9" mN.
- II.2: màn hình biến áp nguồn ảnh gốc ghi "2.148" (không có trong đề) → để trống; giữ "16.0 °C" của nhiệt kế (khớp t = 16 °C). Hình gốc là bộ thí nghiệm có dây điện trở đốt nóng (không khớp hẳn với các bước thí nghiệm trong đề) — giữ như gốc.
- I.5: bỏ nét đứt mờ nằm ngang trong Hình 4 của ảnh gốc (vết dựng hình).
- III.4: nhãn "θ°" gốc ghi thành $\theta$, thêm cung góc ở đỉnh.

## Dàn trang
- II.2: hình và bảng số liệu đặt ngang hàng (hai `minipage`) để Phần II gọn trang.
- II.1 gắn `% tachDS` (câu đầu Phần II được tách câu dẫn / bảng) để dùng chỗ trống trang 4.
