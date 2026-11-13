# Kiểm chứng đáp án – VatLi2026-HaiPhong-CumCM5

Nguồn: `kho/goc/Hai Phong - Cum chuyen mon so 5.docx` (Sở GD&ĐT Hải Phòng, Cụm chuyên môn 05, "Đề khảo sát kỳ thi tốt nghiệp THPT năm học 2025 – 2026", mã đề 0301, không ghi lần), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | C A B B A B A B C D A A D C C B D A | trùng | I.2: 762,7 tấn (1 MeV = 1,6·10⁻¹³ J) → 763; I.5: M = 0,628 N.m; I.9: v = 216,3 m/s; I.10: Δm = 0,20027 amu → 186,55 MeV; I.16: ΔU = 30 J |
| II.1 | Đ S S S | trùng | Q₁ = 3360 J, Q₂ = 68 000 J, Q₃ = 4200 J; m = 75 560/(4200·30) = 0,5997 kg; d) đến τ₂ nước tỏa Q₁ + Q₂ = 71,36 kJ ≠ 761,3 kJ |
| **II.2** | **S Đ Đ S** | **S Đ (Đ) S** | **% KIỂM TRA ý c):** chiều nam châm bị hút hay đẩy phụ thuộc chiều quấn cuộn dây, nhưng hình gốc vẽ các vòng dây nằm ngang, không thể hiện chiều quấn. Gõ theo đáp án gốc (Đúng: đầu trên cuộn dây là cực Bắc, hút cực S). Ý d) Sai theo lời giải gốc vì A, B để hở (chỉ có suất điện động cảm ứng, không có dòng điện) — cách hiểu chặt, thầy xem. |
| **II.3** | **S S Đ Đ** | **S S Đ Đ** | **% KIỂM TRA: dữ kiện mâu thuẫn** (lời giải gốc cũng ghi chú). V₁ = 14,13 m³, m_H₂ = 1,148 kg (a Sai). Định luật khí: p₂ = 1,013·10⁵·218/(27·300) = 2726 Pa (b: 2691 Pa → Sai). Điều kiện lơ lửng: ρ_kk = 5,148/381,5 = 0,01349 kg/m³ → p_kk = 843 Pa (d Đúng). Bỏ qua áp suất phụ thì áp suất trong bóng phải bằng áp suất khí quyển, nên 2726 Pa và 843 Pa không thể cùng đúng. b) Sai theo cả hai cách; d) Đúng chỉ theo điều kiện lơ lửng. Gõ theo đáp án gốc. |
| II.4 | Đ S Đ S | trùng | λ = 1,531·10⁻⁶ s⁻¹; N = 2,077·10¹⁴; m = 4,589·10⁻⁸ g = 0,0459 µg; d) H = 0,85·3,18·10⁸·2^(−1/5,24) = 2,37·10⁸ Bq ≠ 2,79·10⁸ |
| III.1–III.6 | 392 / 76 / 312 / 63 / 40 / 60 | trùng | xem phép tính dưới |

## Phép tính chính (Python)
- III.1: sin α = d/L = 0,02; BIL·L/2 = mg·(L/2) sin α → B = 0,01·9,8·0,02/(5·1) = 3,92·10⁻⁴ T → X = 392 (coi d là cung hay dây cung đều ra 392).
- III.2: E = (3,50/235)·6,02·10²³·200·1,6·10⁻¹³ = 2,869·10¹¹ J; t = E/120 = 2,391·10⁹ s = 75,8 năm → 76.
- III.3: p = 101 325 + (0,3·10 + 3)/(4·3,14·10⁻⁴) = 106 102 Pa; T = 298·106 102/101 325 = 312,05 K → 312.
- III.4: N = 10,5/23·6,02·10²³·23 = 63,21·10²³ → 63.
- III.5: L = 0,05/(0,5·0,5·0,5) = 0,4 m = 40 cm (đề không yêu cầu làm tròn, kết quả nguyên).
- III.6: ΔT = Δt = 60 K.

## Sửa lời đề (lỗi chữ bản gốc)
- Cho biết: "J.mol⁻¹.K⁻¹", "6,02.10²³" viết lại theo quy chuẩn (J·mol⁻¹·K⁻¹, 6,02·10²³).
- I.1: bỏ dấu chấm thừa sau "Thứ tự đúng là".
- I.2: "Helium" → "helium"; "mLi, mH, mHe" → m_Li, m_H, m_He; "toả" → "tỏa"; "4,19 kJ/kg.K" → "4,19 kJ/(kg.K)".
- I.3: hình gốc là một ảnh 4 đồ thị không ghi số hình; thêm nhãn "Hình 1 … Hình 4" dưới từng đồ thị (thứ tự trái → phải, khớp lời giải gốc "Hình 2"); nhãn trục tung "v²" → $\overline{v^2}$ (trung bình bình phương tốc độ).
- I.5: "Tính mômen ngẫu lực từ tác dụng lên khung?" → "Độ lớn moment ngẫu lực từ tác dụng lên khung là" (thuật ngữ SGK "moment"). Giữ đơn vị "N/m" ở phương án B, D như bản gốc (có vẻ là phương án nhiễu cố ý sai đơn vị) — thầy xem có đổi thành N.m không.
- I.6: "véc tơ" → "vectơ"; phương án B ảnh gốc vẽ kí hiệu ⊕ (vòng tròn có dấu cộng) — vẽ lại bằng ⊗ (từ trường hướng vào) theo quy ước.
- I.7: "J/kg.K", "kg/J.K" → "J/(kg.K)", "kg/(J.K)"; I.9, II.1 thống nhất "J/(kg.K)".
- I.9: tốc độ "V" → $v$.
- I.10: "khối lượng của proton, neutron, hạt nhân Na lần lượt là …" → "khối lượng của proton là …, của neutron là …, của hạt nhân Na là …" (tránh tràn lề bản lời giải, giữ nội dung).
- I.11, I.12, I.18: in đậm "không"; I.17: in đậm "sai".
- I.12: "máy biến thế" → "máy biến áp" (thống nhất với I.11).
- I.14: "Clayperon p.V = n.R.T" → "Clapeyron $pV=nRT$".
- II.1 b), III.3: "toả", "thuỷ" → "tỏa", "thủy".
- II.2 c): "lo xo" → "lò xo".
- II.4 a): thêm dấu cách thiếu trước "phóng ra"; b) giữ nguyên biểu thức λ = ln2/T (s⁻¹) (ý Sai).
- III.1: "X.10⁻⁶" → $X\cdot 10^{-6}$.
- III.3: "101325 Pa" → "101 325 Pa"; "Fms" → $F_{\text{ms}}$; "đơn vị Kelvin" → "đơn vị kelvin".
- III.6: "bao nhiêu độ Kelvin" → "bao nhiêu kelvin" (kelvin không có "độ").
- Bỏ "Mã đề 0301", họ tên / số báo danh, điểm từng phần trong tiêu đề phần, dòng "Hết".

## Trình bày
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại).
- Hình: 7 hình vẽ lại bằng TikZ (I.6 có 4 phương án hình):
  - I.3 bốn đồ thị $\overline{v^2}$ – T (đường VLdo; Hình 2 có đoạn nét đứt gần gốc như gốc).
  - I.6 bốn phương án: dây đen, mũi tên dòng điện và $I$ màu VLdo; $\vv{B}$, ⊗, ⊙ màu VLxanh.
  - II.1 đồ thị nhiệt độ – thời gian: nước VLdo, nước đá VLxanh, đoạn cân bằng VLluc, nét gióng xám.
  - II.2 bộ thí nghiệm giá – lò xo – nam châm – thước – cuộn dây (`% giuhinh`); nam châm N đỏ / S xanh (đề có ghi cực), cuộn dây màu đồng, thước gỗ nhạt. Cuộn dây vẽ các vòng nằm ngang như gốc (không thêm chiều quấn — xem % KIỂM TRA II.2).
  - II.3 bóng thám không (ảnh chụp, `% giuhinh`): trời xanh chuyển màu, mây, bóng trắng `\shade`, dây treo, thiết bị đo; đặt bên phải câu dẫn (khớp chữ "hình bên" của gốc).
  - III.1 thanh OM, góc α, $I$ (VLdo), ⊙ $\vv{B}$ (VLxanh), cung $d$ nét đứt hai đầu mũi tên.
  - III.3 chai thủy tinh nút bần trong nồi nước trên bếp ga (ảnh chụp, `% giuhinh`): ngọn lửa ga giữ màu xanh thật.
- Không khai báo macro riêng trong file đề.
- Ảnh so ở `so-hinh/`. Lưu ý kĩ thuật: `tools/so_hinh.py` gọi `xelatex hinh.tex` với `TEXINPUTS=<gốc repo>//` nên khi nhiều agent chạy song song có thể biên dịch nhầm `so-hinh/hinh.tex` của đề khác (lần đầu ra 4 trang hình của đề khác); đã chạy bản chép trong thư mục nháp, sửa thành `xelatex ./hinh.tex`.
