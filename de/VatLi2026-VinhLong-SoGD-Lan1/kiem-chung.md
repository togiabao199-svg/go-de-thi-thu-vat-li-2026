# Kiểm chứng đáp án – VatLi2026-VinhLong-SoGD-Lan1

Nguồn: `kho/goc/Vinh Long - So GDDT - Lan 1.docx` (mã đề 0201, có đáp án và lời giải tham khảo). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | B D B B D A D B D C D A A C A D B C | trùng | I.14: đẳng nhiệt ΔU = 0, nén A > 0 ⇒ Q < 0; I.18: vận tốc trung bình (vectơ) bằng 0, chỉ C đúng |
| II.1 | Đ S Đ S | trùng | B hướng vào, v sang phải, lệch lên ⇒ q > 0; sinθ = L/r = \|q\|BL/(mv) |
| II.2 | Đ S Đ Đ | trùng | |
| II.3 | Đ Đ S S | trùng | pV: P = 1, Q = 3, R = 6, S = 2 (đơn vị p₀V₀); chu trình ngược chiều kim đồng hồ ⇒ khí nhận công 2p₀V₀ |
| II.4 | S S Đ Đ | trùng | (P₂ − P₁)t = L(Δm₂ − Δm₁) |
| III.1–III.6 | bảng đáp án: 800 / 0,8 / 6,0 mWb / 30 μT / 2 / 16,3 | 800 / 0,8 / 30 / 6 / 2 / 16,3 | **Bảng đáp án và lời giải gốc đảo thứ tự câu 3, câu 4** (lời giải gốc "Câu 3" tính ΔΦ, "Câu 4" tính B), trong khi lời đề: câu 3 hỏi B (μT), câu 4 hỏi ΔΦ (mWb). Gõ theo lời đề: III.3 = 30, III.4 = 6. |

## Phép tính chính
- III.1: n = pV/(RT) = 66 480 · 29 / (8,31 · 290) = 800 mol.
- III.2: ρ = nM/V = 800 · 0,029 / 29 = 0,8 kg/m³.
- III.3: q = |ΔΦ|/R, |ΔΦ| = 2NBS ⇒ B = qR/(2NS) = 10⁻³ · 6 / (2 · 1000 · 0,1) = 3·10⁻⁵ T = 30 μT.
- III.4: |ΔΦ| = qR = 6·10⁻³ Wb = 6 mWb.
- III.5: N = 3 − 1 = 2.
- III.6: N_He/N_H = 2^(t/T) − 1 = 1,5 ⇒ t = 12,3 · log₂2,5 = 16,26 ≈ 16,3 năm.

## Sửa lời đề (lỗi chữ bản gốc)
- I.2 phương án A: "hypebol" → "hyperbol" (thuật ngữ SGK).
- I.9: in đậm "**không**" (không thấy mát).
- I.10, I.15, I.16: "hoá" → "hóa" (thống nhất chính tả).
- I.11, I.18: kí hiệu W_d → W_đ.
- II.3: hình gốc ghi nhãn điểm P là "F"; vẽ lại ghi đúng P như lời đề.
- III (câu 1, 2): "Một buồng nghỉ nhỏ trên đỉnh Fansipan." (câu thiếu vị ngữ) → "Xét một buồng nghỉ nhỏ trên đỉnh Fansipan."
- III.6: in đậm "**không**" (không tiếp xúc với khí quyển).
- Đoạn "Dùng thông tin sau cho câu …" của ba cặp III.1–2, III.3–4, III.5–6 đặt trong câu đầu của mỗi cặp (có `\label`/`\ref`).

## Hình
- 4 hình vẽ lại bằng TikZ (so-hinh/): I.2 đồ thị N(t); II.1 hạt bay qua vùng từ trường (vùng từ trường tô nền VLxanh!8, dấu × xanh, v xanh lá); II.2 sơ đồ thí nghiệm Rutherford (`% giuhinh`); II.3 chu trình p–V (bốn quá trình bốn màu, vùng chu trình tô VLla!35).
