# Kiểm chứng đáp án – VatLi2026-QuangTri-SoGD-Lan1

Nguồn: `kho/goc/Quang Tri - So GDDT - Lan 1.docx` (mã đề 0204, có đáp án và lời giải tham khảo). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | D B C A B A B C A A B D A B C B C D | trùng | I.6: V₂ = V₁/2; I.16: dòng điện Đông → Tây, B Nam → Bắc, lực từ hướng xuống; I.18: p, V cùng tăng thì T = pV/(nR) phải tăng |
| II.1 | Đ S Đ S | trùng | Φ = αa²(x + a/2) tăng; dòng cảm ứng ngược chiều kim đồng hồ (MQPNM), lực từ hướng lên; e/v = αa² ≠ αa |
| II.2 | S Đ S Đ | trùng | (1) trên hướng truyền thẳng, (2) góc lệch lớn |
| II.3 | S Đ Đ Đ | trùng | Đọc ô dọc: vật rắn 5, nước 1, T_cb: A 2, B 3, C 4. Q_B ∼ 2 < Q_C ∼ 3; c_A ∼ 1/3, c_C ∼ 3 → c_C/c_A = 9. Ý b) hiểu nhiệt độ đọc từ trục t (đáy khung) như lời giải gốc. |
| II.4 | S S Đ Đ | trùng | p₂/p₁ = 323/298 ≈ 1,084; v₂/v₁ = √(323/298) ≈ 1,041; khí tràn ra 1 − 298/311 ≈ 4,18% |
| III.1–III.6 | 300 / 0,99 / 31 / 0,4 / 1,03 / 15 | trùng | xem dưới |

## Phép tính Phần III
- III.1: f = 1/0,2 = 5 vòng/s = 300 vòng/phút.
- III.2: ω = 10π; S = 31,4/(0,1·10π) = 10 m² (π = 3,14), a = √10 ≈ 3,162 m; I₀ = 3,14 A; F = 0,1·3,14·3,162 ≈ 0,993 N → 0,99.
- III.3: Q = 5·10⁵·4200·220 = 4,62·10¹¹ J; N = Q/(0,9·3,2·10⁻¹¹) ≈ 1,604·10²² hạt; Δm = N/N_A·235 ≈ 6,262 g; m_U = Δm/0,005 ≈ 1252 g; M = m_U/0,04 ≈ 31,31 kg → 31.
- III.4: m = 168 000/(334 000 + 84 000) ≈ 0,402 kg → 0,4.
- III.5: n = 16·10⁵·4·10⁻⁴/(8,31·300) ≈ 0,2567 mol; m ≈ 1,027 g → 1,03.
- III.6: F = (16·10⁵ − 10⁵)·10⁻⁵ = 15 N.

## Sửa lời đề (lỗi chữ bản gốc)
- II.4: "Một người dùng xe ô tô bên đường" → "Một người dừng xe ô tô bên đường".
- I.18: in đậm từ phủ định "**không**".
- Tiêu đề ba phần theo câu chữ đề mẫu (bản gốc: "PHẦN I. Thí sinh trả lời từ câu 1 đến câu 18...").
- Kí hiệu hạt nhân gõ theo quy chuẩn (²³⁵₉₂U canh số, ¹⁴₆C); đơn vị R gõ J·mol⁻¹·K⁻¹.
- Phần III: đoạn "Dùng thông tin sau cho Câu 1 và Câu 2" (và Câu 5, Câu 6) đặt trong câu đầu của cặp, có `\label`/`\ref`.

## Hình
- II.1: đặt hình bên phải phần sau câu dẫn (hai `minipage`) để trang 3 bản đề không trống quá 1/4.
- III.1: hình gốc vẽ khung chữ nhật và kí hiệu ⊕; vẽ lại khung hình vuông (đúng lời đề "khung dây hình vuông ABCD") và kí hiệu ⊗ (đường sức hướng vào) theo SGK.
- II.3: đường liền nét (vật rắn) tô `VLdo`, đường nét đứt (nước) tô `VLxanh`, giữ kiểu nét đứt / chấm gạch / gạch dài như gốc.
- III.5: hình thực tiễn đơn giản (bình khí, ống, van), không cần `% giuhinh`.
