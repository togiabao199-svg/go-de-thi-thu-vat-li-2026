# Kiểm chứng đáp án – VatLi2026-HaNoi-ChuyenKHTN-Lan3

Đề gốc (PDF SieuGioi, THPT chuyên KHTN Hà Nội, "Đợt 3", mã 0302) không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python. Đề gốc không có khối "Cho biết"; lời giải dùng $N_A=6{,}02\cdot 10^{23}$ mol⁻¹, $k=9\cdot 10^9$ N·m²/C², $R=8{,}31$ J/(mol.K) (đề cho ở I.15).

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | D D C C A B A C B C D C A B B B A D | I.7: e = 500·0,01·0,3 = 1,5 V; R = 2·10⁻⁸·200/0,4·10⁻⁶ = 10 Ω; P = 0,225 W; I.8: 62 000/54 500 = 1,14 °C; I.9: 36,7 − 20,2 = 16,5 K (đọc màn hình); I.10: 2874/0,9 = 3193 W; I.15: √(3·8,31·295/0,004) = 1356 m/s; I.16: y² + 75y − 8415 = 0 ⇒ y = 61,60 cm, cột Hg 50,60 cm; I.17: ΔN = 7,854·10⁸, λ = 2,174·10⁻¹¹ s⁻¹, T = 1010,8 năm; I.18: V₀ = (283·13 − 293·2)/10 = 309,3 cm³ |
| II.1 | không có | Đ Đ S S | F = 8,20·10⁻⁸ N; v = 2,186·10⁶ m/s; I = 1,05·10⁻³ A (đề ghi 1 A); B = 2π·10⁻⁷·I/r = 12,45 T (đề ghi 4,0 T) |
| II.2 | không có | Đ Đ Đ Đ | x = 8, y = 6; t = 4,47·log₂1,2 = 1,176 tỉ năm; N_Pb/N_U = 238/1030 = 0,2311 ⇒ t = 1,341 tỉ năm |
| II.3 | không có | Đ Đ S S | phút đầu m_đá tăng 1 g/phút ⇒ lưu lượng 1 g/phút = 1/60 g/s; sau đó tan 11 g trong 10 phút (1,1 g/phút): t₀₁ = 1,1·320/4,2 = 83,81 °C; nước đá ban đầu dưới 0 °C; m_đá ban đầu 10 g |
| II.4 | không có | S Đ S Đ | x = 2r = √(8mU/(qB²)); m = qB²x²/(8U) = 3,38·10⁻²⁵ kg |
| III.1–III.6 | không có | 433 / 581 / 200 / 0,09 / −12 / 0,77 | III.1: (3) là giao của đường đẳng áp qua O, (1) với đoạn (2)(4): 9T₃ = 3900 ⇒ T₃ = 433,3 K; III.2: √(3·8,31·433,3/0,032) = 581,0 m/s; III.3: 50(t₀ − 44) = 14m₀, 150(t₀ − 60) = 30m₀ ⇒ t₀ = 100 °C, m₀ = 200 g; III.4: (1 − e^(−18λ))/(1 − e^(−2λ)) = 5 ⇒ e^(−2λ) = 0,8430, λ = 0,0854 s⁻¹ ≈ 0,09; III.5: p = 2,4·10¹³·1,38·10⁻²³·302 = 1,0002·10⁻⁷ Pa ⇒ x = −12; III.6: F = BIℓ = 0,03 N = mg ⇒ α = 45°, v = √(2·10·0,1·(1 − cos45°)) = 0,765 m/s |

## Điểm cần thầy xem

- **I.10** (`% KIỂM TRA`): P = (2,5/60)·4180·16,5/0,9 = 3193 W ≈ 3,2 kW, không có phương án 3,2 kW; chọn phương án gần nhất 3,0 kW (C). Nếu bỏ qua hiệu suất được 2,87 kW (gần 2,9 kW – D), nhưng đề cho H = 90% và hỏi công suất tiêu thụ điện.
- **I.9**: số "36,7 °C" trên màn hình máy là dữ kiện bắt buộc của câu (nhiệt độ nước ra), nên giữ trên hình vẽ lại.
- **I.17**: đề không cho N_A; lời giải dùng 6,02·10²³ mol⁻¹ (với 6,022·10²³ vẫn ra ≈ 1011 năm).
- **II.1 d)**: cảm ứng từ tại tâm dòng điện tròn B = 2π·10⁻⁷ I/r (không có trong SGK 2018 bộ KNTT); kết quả 12,4 T khác xa 4,0 T nên kết luận Sai chắc chắn.
- **II.3 c)**: đề không cho nhiệt dung riêng của nước đá nên không tính được t₀₂; kết luận Sai dựa vào việc khối lượng nước đá tăng trong phút đầu (nước đá phải dưới 0 °C).
- **III.2**: đề hỏi tốc độ căn quân phương của phân tử oxygen; dùng M(O₂) = 32 g/mol (đề cho khối lượng mol nguyên tử 16 g/mol). R = 8,31 J/(mol.K) lấy theo I.15.
- **III.3**: hình gốc vẽ phác đường N(t) lồi lên và trục t không đều (30, 44, 60). Đường thật theo dữ kiện là N = 200(t − 30)/(100 − t) (cong lõm lên); hình vẽ lại theo đúng hàm này, trục chia đều, giữ các mốc 30, 44, 60 và 50, 150.
- **III.4**: λ = 0,0854 s⁻¹, làm tròn hàng phần trăm được 0,09 (nhạy với cách đọc đồ thị; hai điểm (2; 3) và (18; 15) đề đánh dấu rõ trên lưới).

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi, dòng "Siêu Giỏi", mã đề, dòng quảng cáo. Tiêu đề gốc ghi "Đợt 3" → "Lần 3" theo kiểm kê.
- Chính tả, thuật ngữ: "nguyên lý" → "nguyên lí", "lý tưởng" → "lí tưởng", "Vật lý" → "Vật lí", "toạ độ" → "tọa độ", "Tỷ số" → "Tỉ số", "vector" → "vectơ"; "Helium", "Hydrogen", "Oxygen", "Uranium" → viết thường "helium", "hydrogen", "oxygen", "uranium"; "Geiger - Muller" → "Geiger – Müller".
- I.2, I.4: phương án viết thường chữ đầu (nối tiếp câu dẫn "thì", "cho"). I.3, I.18: bỏ dấu "?" sau "là" (câu nối tiếp phương án).
- I.7: "2.10⁻⁸ Ω.m" → "2·10⁻⁸ Ω·m". I.8, I.15: đơn vị "J/kgK", "J/mol.K" → "J/(kg.K)", "J/(mol.K)". I.17: "1μmol" → "1 μmol".
- I.9–I.10: dòng "Sử dụng các thông tin sau cho Câu 9 và Câu 10" đưa vào đầu câu I.9 ("Dùng thông tin sau cho câu 9 và câu 10:", `\label`/`\ref`); hình máy làm nóng nước đặt trong câu I.9.
- II.3: "nhiệt dung riêng của nước là 4,2 kJ/kg" → "4,2 kJ/(kg.K)"; ý a) "Khối lượng nước đổ vào cốc là 1/60 (g/s)" → "Khối lượng nước đổ vào cốc trong mỗi giây là 1/60 g".
- II.4: "đế n" → "đến"; "B = 80mT" → "B = 80 mT".
- III.1–III.2: "Sử dụng các thông tin sau cho Câu 1 và Câu 2" đưa vào đầu câu III.1; "biến đối" → "biến đổi"; "0,2l", "1,0l" → "0,2 lít", "1,0 lít"; nhãn trục "V (l)" → "V (lít)"; "Kelvin (K)" → "kelvin (K)".
- III.3: thêm "gam" vào câu hỏi ("là bao nhiêu gam?") vì đề cho m₀ (g).
- III.4–III.6: sắp lại "(làm tròn kết quả đến chữ số hàng …)" thống nhất; III.4 "(s⁻¹ và làm tròn…)" → "theo đơn vị s⁻¹ (làm tròn…)"; III.6: "chuyê̂n" → "chuyển", "I = 2A" → "I = 2 A", "(Làm tròn đến 2 chữ số sau dấu phẩy)" → "(làm tròn kết quả đến chữ số hàng phần trăm)".

## Đánh số lại câu

Đề gốc đã đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6), giữ nguyên. Tham chiếu chéo I.9–I.10, III.1–III.2 dùng `\label`/`\ref`.

## Hình

11 hình gốc + 1 bảng (I.11, gõ bằng `tabular`) → 11 `tikzpicture`, ảnh so ở `so-hinh/`. Vùng cắt ảnh trang (300 dpi, tỉ lệ khổ trang): I.6 tr.1 `0.64:0.52:0.96:0.64`; I.7 tr.1 `0.74:0.635:0.96:0.75`; I.9 tr.1 `0.72:0.855:0.96:0.96`; I.16 tr.2 `0.84:0.64:0.95:0.76`; I.18 tr.3 `0.72:0.035:0.96:0.12`; II.1 tr.3 `0.64:0.165:0.96:0.28`; II.3 tr.3 `0.62:0.605:0.96:0.76`; II.4 tr.3 `0.7:0.805:0.95:0.97`; III.1 tr.4 `0.72:0.24:0.96:0.36`; III.3 tr.4 `0.63:0.39:0.96:0.505`; III.4 tr.4 `0.62:0.545:0.95:0.66`.

- I.9 (máy làm nóng nước, hình thực tiễn, `% giuhinh`): dùng `\VLmanhinh`, `\VLnumvan`, `\VLongnoi`; ống nước nóng đỏ, nước lạnh xanh như ảnh (có chú thích chữ, không phải ý suy luận). Chờ phiên vẽ lại chi tiết.
- Dàn trang: I.16 hình đặt bên phải phương án; II.3, II.4 hình đặt bên phải câu dẫn (minipage `[t]`); II.4 tách câu dẫn / bảng Phát biểu.

## Vẽ lại hình thực tiễn (PHIÊN FABLE 14/11/2026)

- **I.9** (máy làm nóng nước, `% giuhinh`): vẽ lại bằng macro mới `\VLmaynuocnong{x}{y}{tỉ lệ}{nội dung màn hình}` — thân máy bo góc có vành, bóng đổ trên tường, bảng điều khiển gờ nổi có vệt phản quang, màn hình LCD hiện số bảy đoạn "36,7 °C" (macro `\VLsoled`, số đề dùng làm dữ kiện), núm điều chỉnh có vành khía và vạch chỉ, hai sợi dây điện phía trên, ống nước nóng (đỏ) / lạnh (xanh) có cổ nối; năm nhãn chữ có gạch chân và đường chỉ như hình gốc (vẽ ngoài macro, bám các điểm `(VLmnn-...)`). Hình 8,2 × 4,8 cm.
- **I.16** (ống thủy tinh ấn vào chậu thủy ngân): vẽ lại chậu và hai ống có bề dày thành thủy tinh, thủy ngân tô chuyển màu có vệt sáng mặt thoáng, phần thủy ngân vào ống (đoạn $l-h$) giữ nét đứt như hình gốc; nhãn $p_0$, $l=112{,}2$, $p_1$, $h$, $l-h$ giữ nguyên, tách khỏi nét ống.
- **I.18** (áp kế khí: bình cầu + ống nằm ngang): vẽ lại vỏ thủy tinh liền khối có bề dày, vệt sáng trên bình và ống, giọt thủy ngân có mặt khum hai đầu, đầu ống bên phải để hở như hình gốc; nhãn A giữ nguyên.
- Giữ nguyên (sơ đồ nguyên lí, đồ thị): I.6, I.7, II.1, II.3, II.4, III.1, III.3 (đồ thị theo hàm suy từ dữ kiện), III.4.
- Macro mới khai báo trong file đề (đề nghị chuyển vào `preamble-vatli-hinh.tex` để các đề Nghệ An Liên trường Lần 2, Hưng Yên SGD Lần 1, Lạng Sơn SGD Lần 1 dùng lại): `\VLmaynuocnong`, `\VLsoled` (kèm lệnh phụ `\VLledngang`, `\VLleddung`, `\VLledve`, bảng mã `VLledma0`…`VLledma9`, `VLledma-`).
- Ảnh so dựng lại cho cả 11 hình (ảnh trang 300 dpi); vùng cắt đổi nhẹ: I.9 tr.1 `0.72:0.862:0.96:0.96`; I.16 tr.2 `0.84:0.64:0.95:0.755`; I.18 tr.3 `0.72:0.035:0.96:0.117`.
- Hình chưa ưng: không có. Lưu ý: dấu thập phân trên màn hình vẽ thành dấu phẩy ("36,7") cho khớp cách ghi số của đề, ảnh gốc là dấu chấm ("36.7").

## Chốt đáp án (thầy duyệt 14/11/2026)

- Các điểm còn lại ở `kho/KIEM-DAP-AN-V2.md` — I.10 (C, H = 90 % như đề in), II.1d (S), III.4 (0,09), III.5 (−12): giữ như file, thầy chốt 14/11/2026. Các `% KIỂM TRA` khác giữ nguyên.
