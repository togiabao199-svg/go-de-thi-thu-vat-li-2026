# Kiểm chứng đáp án – VatLi2026-HaNoi-YenVien-Lan1

Đề gốc (Word thuvienhoclieu, "Trường THPT Yên Viên – Bài kiểm tra khảo sát lớp 12 lần 1, năm học 2025 – 2026", mã đề 248) chỉ có bảng đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python. Phạm vi chủ yếu C1–C2; có ba câu ngoài chương trình 12: I.5 (dao động, mã `VL11-C1`), I.10 (gia tốc, lớp 10, mã `VL10-C2`), I.13 (sóng cơ, mã `VL11-C2`).

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | B B C A B D C A C D D C C C C A B C | trùng, trừ I.13 (xem dòng dưới) | I.4: đồ thị V–T qua gốc O, V giảm ⇒ nén đẳng áp ⇒ Hình 2; I.5: f = 4 Hz, 2 s ⇒ 8 dao động; I.9: Hình c là đẳng tích; I.14: 6/1,5 = 4 lít; I.15: 3,34·10⁵·0,5 = 167 kJ; I.16: 50m = 30(120 − m) ⇒ m = 45 g; I.17: 30/100 = 3/10 |
| **I.13** | **C** ($v_r>v_k>v_l$) | **D** ($v_r>v_l>v_k$) | **Đáp án gốc sai**: tốc độ sóng cơ giảm dần rắn → lỏng → khí. File gõ theo D, có `% KIỂM TRA` — thầy xem lại. |
| II.1 | S Đ Đ S | trùng | n = 10⁵·10⁻³/(8,31·301) = 0,040 mol; p/T: 332,2; 332,3; 332,3; 332,4; 330,5 ⇒ TB 331,9 ≈ 332; T₃/T₁ = 331/301 = 1,10 |
| II.2 | S Đ S Đ | trùng | T₁ = 276 K; p₂ = 3,41·10⁵·315/276 = 3,892·10⁵ Pa; n = 3,41·10⁵·1,5/(8,31·276) = 223,0 mol |
| II.3 | S Đ S Đ | trùng | P = 4200 W; 2 giờ: E = 30,24 MJ, Q = 25 % E = 7,56·10⁶ J; 1 giờ: Δt = 0,25·4200·3600/(30·4200) = 30 °C |
| II.4 | Đ S Đ S | trùng | Đọc lưới (1 phút × 10 °C): rắn −20 → −10 °C trong 1 phút; nóng chảy ở −10 °C từ phút 1 đến 13 (12 phút); lỏng −10 → 30 °C trong 11 phút; sôi ở 30 °C. c_ℓ/c_r = (11/40)/(1/10) = 2,75 |
| III.1–III.6 | 328 / 10 / 2,5 / 1,13 / 12,4 / 1,5 | trùng | III.2: 1,3·4,85/0,63 = 10,01; III.3: n = 0,02006 mol, N_O₂ = 0,21·n·N_A = 2,535·10²¹; III.4: 0,5·2,26·10⁶ = 1,13·10⁶ J; III.5: 1,5·1,38·10⁻²³·6·10⁵ = 12,42·10⁻¹⁸ J; III.6: (10⁵ + 10³·10·5)/10⁵ = 1,5 |

## Điểm cần thầy xem

- **I.13** (`% KIỂM TRA` trong file): bảng đáp án gốc C, giải lại D.
- Đề gốc không có khối "Cho biết": II.1, II.2, III.3 cần R, N_A; lời giải dùng R = 8,31 J/(mol.K), N_A = 6,02·10²³ (đáp số khớp đáp án gốc). File không thêm khối "Cho biết" (theo quy định: đề gốc không có thì bỏ).
- III.4 (1,13), III.6 (1,5) đáp số không nguyên nhưng là giá trị đúng, không cần làm tròn; đề gốc không ghi yêu cầu làm tròn, giữ nguyên.
- III.3: dữ kiện "khối lượng mol của không khí là 29 g/mol" thừa (không dùng), giữ nguyên.
- I.5, I.10, I.13 thuộc lớp 10/11 (dao động, động học, sóng cơ) — giữ nguyên như đề gốc.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề trường, dòng họ tên, số báo danh, mã đề, chữ quảng cáo thuvienhoclieu, dòng "HẾT" và bảng đáp án cuối file.
- Tiêu đề Phần I gốc ghi "Thí sinh trả lời từ câu 1 đến câu 12" (sai, đề có 18 câu) → dùng tiêu đề chuẩn "từ câu 1 đến câu 18".
- Kí hiệu "⁰C", "0C", "⁰F" → "°C", "°F" (I.1, I.16, II.2, II.4, III.1, III.3, III.4); "3,41.10⁵", "x.10²¹"… → dấu nhân "·".
- I.5: "phương trình: … Trong 2s vật thực hiện được số dao động là:" → bỏ dấu hai chấm; "(cm)" đặt ngoài công thức.
- I.6, I.9: in đậm "không".
- I.11: "$v^2$ là trung bình của các bình phương tốc độ" → "$\overline{v^2}$" (khớp các phương án).
- I.12: kí hiệu A, Q, ΔU gõ thành công thức; phương án B thiếu dấu chấm (bỏ dấu chấm cuối phương án theo quy chuẩn).
- I.13: kí hiệu $v_r$, $v_l$, $v_k$ → $v_\text{r}$, $v_\ell$, $v_\text{k}$.
- I.14, II.3: "50%", "25%" → "50 %", "25 %".
- I.15: phương án "Q=167J", "Q=167.10⁶J", "Q=7.10⁷ J" → "$Q=167$~J", "$Q=167\cdot 10^6$~J", "$Q=7\cdot 10^7$~J".
- I.16: bỏ dấu phẩy thừa "ở 20 °C, và nước nóng".
- I.17: "khối lượng m1" → "$m_1$"; "$c_1,c_2$" → "$c_1$, $c_2$".
- II.1: "nhiệt độ t oC" → "nhiệt độ $t$ (°C)"; bảng số liệu (ảnh trong file gốc) gõ lại thành `tabular`.
- II.3: "4200 J/kg.K" → "4200 J/(kg.K)"; ý c) "năng lượng mặt trời" → "năng lượng Mặt Trời".
- II.4: "t (⁰C)", "τ(phút)" → "$t$ (°C)", "$\tau$ (phút)"; ý b) "cr và cℓ, thì cℓ = 11cr" → "$c_\text{r}$ và $c_\ell$ thì $c_\ell=11c_\text{r}$"; ý d) "-10⁰C" → "$-10$ °C".
- III.2, III.3: đặt dấu "?" sau ngoặc "(kết quả làm tròn …)".
- III.5: "Vành nhật hoa của mặt trời" → "Mặt Trời"; đơn vị hằng số Boltzmann "J/mol.K" → "J/K" (sai đơn vị); "nguyên tử heli" → "helium" (thuật ngữ SGK 2018); "(kết quả…)" đặt trước dấu "?".

## Đánh số lại câu

Đề gốc đã đánh số Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6 (như file gõ). Không có tham chiếu chéo.

## Hình

6 hình gốc (`word/media/`: `image1.png`, `image2.png`, `image7.png`, `image42.jpeg`, `image48.jpeg`, `image52.emf`) → 6 `tikzpicture`, ảnh so ở `so-hinh/`:

- I.4: đồ thị V–T (`image1.png`, đặt bên phải lời đề như gốc) và bốn đồ thị phương án Hình 1–4 (`image2.png`; ảnh so 01 ghép hai ảnh gốc). Ảnh gốc Hình 3, 4 bị cắt mất chỉ số và ngoặc: "(1", "(2" → "(1)", "(2)"; Hình 3 hai nhãn "p" → $p_1$, $p_2$; Hình 4 nhãn "p" → $p_1$.
- I.9: bốn đồ thị Hình a–d (`image7.png`).
- II.1: bộ thí nghiệm bình cầu – áp kế – nhiệt kế (`image42.jpeg`, `% giuhinh`), đặt cạnh bảng số liệu; ngọn lửa đổi sang màu `\VLngonlua` theo bảng màu (gốc lửa xanh).
- II.3: máy nước nóng năng lượng Mặt Trời (`image48.jpeg`, `% giuhinh`).
- II.4: đồ thị t–τ (`image52.emf`, đổi PNG qua ảnh trang 400 dpi); giữ lưới 1 phút × 10 °C, các mốc theo lưới gốc: (0; −20), (1; −10), (13; −10), (24; 30), (28; 30); lưới đổi sang xám nhạt, đường đồ thị `VLdo`.
