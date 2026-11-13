# Kiểm chứng đáp án – VatLi2026-SonLa-SoGD-Lan2

Nguồn: `kho/goc/Son La - So GDDT - Lan 2.docx` (Sở GD&ĐT Sơn La, thi thử lần 2, mã đề 0209), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | A C D B A C B B B A B B A A A C B A | trùng | I.4: ΔU = 2000 − 1200 = 800 J; I.5: V₂ = 100·250/(0,5·300) = 166,7 → 167 cm³; I.6: 220·120/2200 = 12 V; I.10: 2⁻⁴ = 6,25%; I.15: Φ = 0,05·2·10⁻³·cos 60° = 5·10⁻⁵ Wb |
| II.1 | Đ Đ S S | trùng | p(30 m) = 1,013·10⁵ + 1000·9,8·30 = 3,953·10⁵ Pa ≈ 395 kPa (không phải 294 kPa); V₀/V = 3,953/1,013 = 3,90 (không phải 2,9) |
| II.2 | S Đ S S | trùng | d) Δt₁ = 11 °C, Δt₂ = 17,7 °C; ΔU₁ = 2·4200·11 = 92 400 J < ΔU₂ = 148 680 J nên chậu 2 giảm nội năng nhiều hơn |
| II.3 | Đ Đ S Đ | trùng | **a) bảng đáp án gốc Đúng, nhưng lời giải gốc ghi Sai** với cách đọc hình "(1) biến trở, (6) nam châm điện". Đối chiếu ảnh: (1) cuộn dây có lõi sắt nối với nguồn (5) qua biến trở (6) và khóa K (4) — là nam châm điện; (2) nối với điện kế (3) — cuộn dây dẫn; (6) là biến trở con chạy trên đế cam, (4) khóa K dạng cầu dao. Thứ tự ở mệnh đề a) đúng → gõ Đúng (theo bảng đáp án); lời giải viết lại theo hình. |
| II.4 | S S S S | trùng | a) 203 MeV = 3,248·10⁻¹¹ J = 324,8·10⁻¹³ J (đề ghi 10⁻¹⁹); b) m = 175·10⁶·86 400/3,248·10⁻¹¹/6,02·10²³·235 = 181,7 g ≈ 0,182 kg; c) E(1 kg) = 8,320·10¹³ J ↔ 3,08·10⁶ kg ≈ 3080 tấn than; d) m = 0,25·8,320·10¹³/(2100·10 + 334 000) = 5,86·10⁷ kg |
| III.1–III.6 | 843 / 6067 / 0,05 / 3,3 / 6,3 / 200 | trùng | xem phép tính dưới |

## Phép tính chính (Python)
- III.1: V₀ = 10⁻³/1,29 = 7,752·10⁻⁴ m³; V = V₀·(1,013·10⁵·293)/(10⁵·273) = 8,428·10⁻⁴ m³ = 842,8 ml → 843.
- III.2: t = 5730·log₂(0,25/0,12) = 6067,46 năm → 6067.
- III.3: cạnh 1 m; e = Blv = 0,1 V; I = 0,1/2 = 0,05 A (kết quả chính xác, đề không cần làm tròn).
- III.4: λ = 3·10⁸/(90·10⁶) = 3,333 m → 3,3.
- III.5: Δm = 4·1,0073 + 6·1,0087 − 10,0135 = 0,0679 amu; W_lk = 63,249 MeV; W_lkr = 6,325 → 6,3.
- III.6: mỗi vòi chảy V = 0,25t lít; V(90 − 40) = V(40 − 10) + 50(40 − 20) ⇒ V = 50 lít ⇒ t = 200 s (lời giải gốc dùng nhiệt độ trung bình hai vòi 50 °C, thêm 100 lít, cùng kết quả). Kết quả nguyên, đề không cần làm tròn.
- II.4 dùng N_A = 6,02·10²³ mol⁻¹, 1 MeV = 1,6·10⁻¹³ J như lời giải gốc (đề gốc không có khối "Cho biết"; lấy e = 1,602·10⁻¹⁹ C cũng không đổi Đ/S).

## Sửa lời đề (lỗi chữ bản gốc)
- I.1: "220V" → "220 V"; phương án viết thường, bỏ dấu chấm cuối (câu dẫn kết thúc bằng "là").
- I.3: kí hiệu E_d → $\overline{E}_{\text{đ}}$ (động năng tịnh tiến trung bình).
- I.4: "xi lanh" → "xilanh", "pít-tông" → "pit-tông".
- I.7: "thuật chụp hình PET" → "kĩ thuật chụp hình PET"; "các đồng vị phóng xạ" → "đồng vị phóng xạ"; kí hiệu hạt nhân vỡ "^{18}9F", "^{18}8O" → ${}^{18}_{9}\text{F}$, ${}^{18}_{8}\text{O}$; "Fluorine-18", "Oxygen-18" viết thường (fluorine-18, oxygen-18).
- I.8: "Boron", "Cadmium", "Uranium-235" viết thường (boron, cadmium, uranium-235).
- I.9: "khí ôxi" → "khí oxygen" (tên IUPAC).
- I.11: "Trạm điều khiển" → "trạm điều khiển"; "lớp điện li" → "tầng điện li" (khớp các phương án).
- I.12: "Chọn phát biểu sai?" → "Chọn phát biểu **sai**." (in đậm từ phủ định, bỏ dấu hỏi); đơn vị "J/kg.K" → "J/(kg.K)" thống nhất với II.4.
- I.16, I.18: in đậm "**không**".
- I.17: "Cobalt-60" → "cobalt-60"; "Chọn phát biểu đúng?" → "Chọn phát biểu đúng."
- II.2: "ghi lại bảng bên dưới" → "ghi lại ở bảng bên dưới".
- II.4: kí hiệu hạt nhân vỡ "^{235}92U" → ${}^{235}_{92}\text{U}$; bỏ dấu "}" rác trước ${}^{235}_{92}\text{U}$ ở ý c), d); bỏ chữ nghiêng lẫn trong câu dẫn.
- III.1: "(Kết quả làm tròn…)" → "(kết quả làm tròn…)".
- III.2: thêm "theo đơn vị năm" (đề gốc không nêu đơn vị của đáp số; chu kì bán rã cho theo năm, đáp án gốc 6067 năm).
- III.3: "2Ω" → "2 Ω".
- III.4, III.5: "(Kết quả…)" viết thường, đưa vào trong câu hỏi; III.5 "MeV/nucleon? (Kết quả…)." → "MeV/nucleon (kết quả…)?".

## Trình bày, hình
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại). Không có cặp câu dùng chung dữ kiện.
- 3 hình gốc vẽ lại bằng TikZ (ảnh so ở `so-hinh/`):
  - II.2: ảnh minh họa (hai học sinh trong phòng thí nghiệm, bảng trắng, tờ đồ thị, bình tam giác, ống đong, giá thí nghiệm, chậu cây, cửa sổ) — không dùng để giải; vẽ đơn giản, đặt bên trái bảng số liệu (hai `minipage`) để gọn trang. `% giuhinh`. Chờ phiên vẽ lại.
  - II.3: ảnh chụp bộ thí nghiệm cảm ứng điện từ: điện kế (3) dùng `\VLdienke{1}`, cuộn dây (2) và nam châm điện (1) dùng macro riêng `\SLcuonde`, biến trở (6) và khóa K (4) trên đế cam, nguồn (5) có tay xách, núm vặn `\VLnumvan`; dây nối đỏ/xanh như ảnh. Không tô khác màu (1) và (2) (ý a) yêu cầu nhận biết). `% giuhinh`. Chờ phiên vẽ lại.
  - III.3: vùng từ trường giới hạn (chấm, nền `VLxanh!8`), khung dây màu đồng nằm một nửa trong vùng, $\vv{v}$ màu `VLluc`.
- Bảng số liệu II.2: `tabular` cỡ `\footnotesize`.
