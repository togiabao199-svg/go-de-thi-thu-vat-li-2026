# Kiểm chứng đáp án – VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2

Đề gốc (PDF SieuGioi, "THPT Lê Thánh Tông – Đợt 2", mã 0302) không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | A D B B A B B C A B A B C A D D D C | I.4: BC nằm ngang ở 80 °C ⇒ băng phiến nóng chảy; I.5: ΔU = 100 − 20 = 80 J; I.8: đường T₂ xa gốc hơn ⇒ T₁ < T₂; I.9: 2,5·330/300 = 2,75 bar; I.11: 0,5·2·0,2·sin30° = 0,1 N; I.12: f = 2·1800/60 = 60 Hz; I.16: dòng Foucault trong thước nhôm hãm hộp chứa nam châm; I.17: X = ¹⁷₈O có 9 neutron; I.18: Δm = 18,0007 − 18,0020 = −0,0013 amu ⇒ thu 1,211 MeV |
| II.1 | không có | Đ S S S | b): dòng điện ra từ cực dương (vạch dài, bên trái) qua khóa S vào đầu trái cuộn dây; nét liền (nửa vòng trước) đi từ trên xuống ⇒ quy tắc nắm tay phải: B trong lòng ống hướng sang phải ⇒ đầu trái cực Nam, đầu phải cực Bắc |
| II.2 | không có | S Đ Đ Đ | μ = ρL = 1050·2·10⁻³/60 = 0,035 kg/s; ΔT = 250/(0,035·3800) = 1,880 °C; lưu lượng giảm 4 lần ⇒ 7,519 °C |
| II.3 | không có | Đ Đ Đ S | kΔℓ₀ = 28 N; p mở = 10⁵ + 28/(2·10⁻⁴) = 2,4·10⁵ Pa; n = 1,2·10⁵·0,05/(8,31·300) = 2,407 mol; T₂ = 300·2,4/1,2 = 600 K = 327 °C (đề ghi 600 °C) |
| II.4 | không có | Đ Đ Đ S | E = 10¹⁰·230·1,6·10⁻¹³ = 0,368 J; D = 73,6 Gy; H = 147,2 Sv (đề ghi 147,2 mSv) |
| III.1–III.6 | không có | 30 / 2 / 3 / 9,6 / 2,55 / 5,6 | III.1: (86 − 32)/1,8 = 30; III.2: m·v_rms = √(3mkT) = 2,404·10⁻²³ (nếu dùng tốc độ trung bình √(8RT/πM): 2,21·10⁻²³, vẫn a = 2); III.3: e = ½Bωr² tăng theo ω, B, r; số nan hoa, vật liệu nan hoa không đổi e ⇒ 3; III.4: ½·5·10⁻³·2π·5·0,35² = 9,621 mV; III.5: E = 6,02·10²³/235·200·1,6·10⁻¹³ = 8,197·10¹⁰ J ⇒ 1782 kg xăng ⇒ 2,546 m³ (N_A = 6,022·10²³ cho 2,547, vẫn 2,55); III.6: đọc lưới (1) = (V₀; 4 ô), (2) = (4V₀; 1 ô) ⇒ T₁ = T₂, Q = công: Qa = 12, Qb = 7,5, Qc = 3 ⇒ x + y = 1,6 + 4 = 5,6 |

## Điểm cần thầy xem

- **II.1 b)**: kết luận dựa vào chiều quấn vẽ trên hình gốc (nét liền là nửa vòng phía trước, nét đứt phía sau) và cực nguồn (vạch dài bên trái). Hình TikZ giữ đúng chiều quấn và cực nguồn đó. Đọc như vậy thì đầu trái là cực Nam ⇒ b) Sai. Nếu người ra đề không chủ ý chiều quấn thì ý này không xác định được; dù thế nào, b) vẫn khó là Đúng.
- **II.1 a)**: lò xo vẽ ở bên trái tấm chặn, nên phải là lò xo kéo (lực đàn hồi kéo chốt sang trái) để giữ khóa; lời đề nói "kéo chốt sắt sang trái", đã chọn Đúng.
- **I.7**: chọn B theo cách nói quen thuộc "ở 0 K các phân tử ngừng chuyển động (nhiệt)"; về mặt lượng tử vẫn có dao động điểm không, nhưng các phương án khác sai rõ.
- **III.2, III.5**: đề gốc không có khối "Cho biết" nên không cho R, N_A, k; lời giải dùng R = 8,31 J/(mol.K), N_A = 6,02·10²³ mol⁻¹. "Động lượng trung bình" hiểu là m·v_rms (vectơ động lượng trung bình bằng 0); hai cách hiểu tốc độ đều cho a = 2.
- **III.3**: đề ghi "(làm tròn kết quả đến chữ số hàng đơn vị)" cho câu đếm số biện pháp; giữ nguyên.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi ("ĐỀ THI THỬ TỐT NGHIỆP THPT - VẬT LÍ 12", "Siêu Giỏi", dòng quảng cáo, mã đề 0302). Dòng 1 khung tiêu đề, `\tenchuong` theo `kho/kiem-ke.md`.
- I.2: in đậm "không". I.4: "Đồ thị biểu diễn…" → "Đồ thị hình bên biểu diễn…" (hình đặt bên phải phương án).
- I.6, I.8: "hypebol" → "hyperbol"; I.6: "(p − T)" → "$(p,T)$".
- I.10: "Tesla (T)", "Weber (Wb)", "Henry (H)", "Vôn (V)" → viết thường tên đơn vị (tesla, weber, henry, vôn) vì phương án nối tiếp câu dẫn; "từ thông (Φ)" → "từ thông $\Phi$".
- I.15: "Huỷ" → "Hủy".
- I.17–I.18: "Nitơ" → "nitrogen"; thêm dấu cách giữa số và đơn vị amu, MeV. Đoạn dữ kiện chung đặt trong I.17 (`\label`/`\ref`).
- II.1 (hình): "khoá điều khiển" → "khóa điều khiển".
- II.2: "vi xử lý" → "vi xử lí"; "P = 250W" → "250 W".
- II.3: "nắp van (piston)" → "nắp van (pit-tông)", nhãn hình "Piston" → "Pit-tông"; "Cho biết: Áp suất" → "Cho biết: áp suất". Hình van an toàn trong bản gốc đặt cạnh câu II.4 (lệch câu) → chuyển về II.3.
- II.4: "Liều hấp thụ", "Liều tương đương" → viết thường; "Gray", "Sievert", "Cyclotron", "Hydrogen" → "gray", "sievert", "cyclotron", "hydrogen"; "1,6.10⁻¹³" → "1,6·10⁻¹³"; "D = E/m" → $D=\dfrac{E}{m}$.
- III.1: kí hiệu nhiệt độ Fahrenheit "t_r", Celsius "t_c" → $t_\text{F}$, $t_\text{C}$.
- III.2: "Nitrogen" → "nitrogen"; "a. 10⁻²³ kg. m/s" → "$a\cdot 10^{-23}$ kg.m/s".
- III.3: thêm dấu chấm cuối mục (2); "B = 5.10⁻³ T" → "$5\cdot 10^{-3}$ T". Đoạn dữ kiện chung đặt trong III.3 (`\label`/`\ref`).
- III.5: "46.10⁶ J/kg" → "$46\cdot 10^6$ J/kg".
- III.6: chữ "c" in đậm thừa trong "(a, b, c)" → chữ thường.

## Đánh số câu

Đề gốc đã đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6), giữ nguyên.

## Hình

7 hình gốc → 7 `tikzpicture`, ảnh so ở `so-hinh/`. Vùng cắt ảnh trang 300 dpi (tỉ lệ khổ trang): I.4 tr.1 `0.70:0.47:0.95:0.58`; I.8 tr.1 `0.76:0.79:0.95:0.885`; II.1 tr.2 `0.61:0.775:0.95:0.93`; II.2 tr.3 `0.68:0.09:0.95:0.21`; II.3 tr.3 `0.81:0.72:0.95:0.91`; III.3 tr.4 `0.68:0.30:0.95:0.415`; III.6 tr.4 `0.70:0.70:0.95:0.815`.

- I.4, I.8 đặt bên phải phương án; II.1, II.2, II.3, III.3, III.6 đặt bên phải câu dẫn (hai `minipage`, tổng rộng ≤ 0,93 `\linewidth` để bản lời giải không tràn lề) như bố cục đề gốc.
- II.2 (ảnh chụp tản nhiệt AIO), II.3 (mặt cắt van an toàn), III.3 (bánh xe): hình thực tiễn vẽ có khối, `% giuhinh`; bỏ nền tối của ảnh II.2. Chờ phiên vẽ lại chi tiết.
- I.8: hai đường đẳng nhiệt tô hai màu trung tính (xanh lá, tím), không dùng đỏ/xanh dương để khỏi gợi ý nóng/lạnh.
