# Kiểm chứng đáp án – VatLi2026-HaNoi-LuongTheVinh-Lan2

Đề gốc (PDF SieuGioi, THPT Lương Thế Vinh – Hà Nội, lần 1 năm học 2025 – 2026, không có mã đề) không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | D C A B D A D B C D D B A B A C D A | I.5: E × B cùng hướng truyền sóng; E lên, truyền sang Tây ⇒ B hướng Bắc; I.7: công (atm·l) 12 / 7,5 / 12 / 3; I.8: Hình 2 có 2 p, 3 e (Hình 1, 4 trung hòa, Hình 3 ion dương); I.12: n = p/(kT) tỉ lệ hệ số góc; I.14: Np(93; 237) → α → (91; 233) → β⁻ → (92; 233) = S; I.15: E₀ = 100π·0,04/π = 4 V; I.16: 100 vạch phải vừa 90 khoảng cũ ⇒ co bớt 10%; I.17: B = 0,01/(5·0,2) = 10 mT; I.18: r = mv/(qB) = 5,850 m và 5,925 m, d = 2Δr = 150 mm |
| **II.1** | không có | S Đ S Đ | f = 1000·3/60 = 50 Hz; 6 cuộn nối tiếp N = 1200: E = 2π·50·1200·0,5·10⁻³/√2 = 133,3 V |
| **II.2** | không có | **S** Đ S S | **Ý a) phụ thuộc chỗ sửa lời đề (xem dưới).** λ = ln2/(8·86400) = 1,003·10⁻⁶ s⁻¹; H(24 h) = 36·2^(−1/8) = 33,0 mCi > 30 (cần 50,5 h); đã phân rã 1 − 30/36 = 16,7% |
| II.3 | không có | Đ Đ Đ S | d): định luật I cho ΔU = A + Q (độ biến thiên nội năng), không phải nội năng |
| II.4 | không có | Đ S Đ S | p₁·1 = 1,25·1,2 ⇒ p₁ = 1,5 bar; lần 2: V = 1,5·1,2/1,25 = 1,44 l ⇒ phun 0,24 l (đề ghi 0,3 l) |
| III.1–III.6 | không có | 2,42 / 200 / 752 / 2,7 / 20 / 5 | III.1: 110·log₂(0,45/0,18)/60 = 2,4235 h; III.2: φ = π/3, P = (200/√2)(4/√2)·0,5 = 200 W; III.3: L = 755 + 45 = 800 mm, p₂ = 5·45/52 = 4,327 mmHg ⇒ 752,33; III.4: B₀ = 2π·10⁻⁷·100·0,025/0,1 = 1,571·10⁻⁵ T, B_đ = B₀·tan 60° = 2,72·10⁻⁵ T; III.5: 5/4 = (40 − tₓ)/(36 − tₓ) ⇒ tₓ = 20 °C, C_nước = 4C_chai; III.6: tₙ = 20 + 25·0,8ⁿ: t₄ = 30,24, t₅ = 28,19 ⇒ chai thứ 5 |

## Điểm cần thầy xem

- **II.2 (`% KIỂM TRA`)**: bản gốc ghi iodine-131 là ¹³¹₅₁I (cả 4 chỗ). Iodine có Z = 53 nên đã sửa thành ¹³¹₅₃I. Khi đó Xe (Z = 54) có 131 − 54 = **77** neutron ⇒ ý a) "Xe có 79 neutron" **Sai**. Nếu giữ Z = 51 như bản gốc thì Xe có Z = 52, N = 79 ⇒ ý a) Đúng. Có thể người ra đề dùng Z = 51 và định a) Đúng; file gõ theo số liệu thật (a Sai).
- **III.2**: hai trục thời gian của đồ thị gốc không có số và chu kì vẽ khác nhau (đồ thị u vẽ 1 chu kì, đồ thị i vẽ 4/3 chu kì trên cùng độ dài trục). Lời giải chỉ dùng giá trị ban đầu: u = U₀ (φ_u = 0), i = I₀/2 đang giảm (φ_i = π/3) ⇒ φ = π/3; hình vẽ lại giữ nguyên dạng hình gốc.
- **III.4**: hiểu α = 60° là góc giữa kim và hướng Đông – Tây (đúng lời đề, khớp hình gốc): tan α = B_đ/B₀ ⇒ X = 2,7. Nếu hiểu là góc lệch so với hướng Bắc – Nam thì X = 0,9.
- **II.1 d)**: coi 6 cuộn dây mắc nối tiếp (hình gốc nối tiếp các cuộn), E = 133 V khớp lời đề.
- I.12: hình gốc không ghi tên trục chung; các đường là đường đẳng tích qua gốc O, bình cùng dung tích.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi, dòng họ tên / số báo danh, "Đề thi gồm 05 trang", dòng quảng cáo, "HẾT". Tên đơn vị, lần thi theo kiểm kê.
- Cho biết: "R = 8,31 J. mol⁻¹" thiếu K⁻¹ → `J·mol⁻¹·K⁻¹`; "6,02.10²³" → `6,02·10²³`.
- I.1: "Mặt trời" → "Mặt Trời". I.2: "Lithium" → "lithium". I.4: "súng bắn tốc độ Rađa" → "súng bắn tốc độ radar". I.5: "véc tơ" → "vectơ". I.9: "Irene Joliot-Curie và Frédéric Joliot - Curie" → "Irène Joliot-Curie và Frédéric Joliot-Curie"; "phốt pho" → "phosphorus" (IUPAC). I.13: "giải trí,..." → "giải trí,…". I.14: "Ký hiệu" → "Kí hiệu"; phương án bị vỡ dòng ("B. / S. C. P.") gõ lại thành R / S / P / Q. I.17: bỏ dấu ":" cuối câu dẫn. I.18 (hình): "Nguồn ion CUl₄" → "Nguồn ion UCl₄".
- II.1: "f = n.p/60" → `f = np/60`. II.2: ¹³¹₅₁I → ¹³¹₅₃I (xem trên); "Iodine - 131" → "iodine-131"; "Xenon" → "xenon"; "Y học" → "y học"; "10⁻⁶ (s⁻¹)" → `10⁻⁶ s⁻¹`. II.3: "pít - tông" → "pit-tông". II.4: "nguyên lý" → "nguyên lí"; hình: "Pít-tông" → "Pit-tông".
- III.1: "chu kỳ" → "chu kì"; "Làm tròn quả đến hàng phần trăm" → "(kết quả làm tròn đến chữ số hàng phần trăm)"; dấu phẩy "tiêm một liều lượng FDG giống nhau, tại thời điểm chẩn đoán" cho rõ nghĩa.
- III.2: "P = U.I.cosφ (W)" → `P = UI cos φ (W)`; bỏ dấu cách trước "?".
- III.3: "thuỷ" → "thủy"; "(làm tròn kết quả đến hàng đơn vị)" đưa vào trước dấu "?" → "(làm tròn kết quả đến chữ số hàng đơn vị)?".
- III.4: "Vật lý" → "Vật lí"; "được tỉnh theo công thức" → "được tính theo công thức"; "Đông- Tây" → "Đông -- Tây"; "B₀ = 2π.10⁻⁷.N.I/R" → `B₀ = 2π·10⁻⁷·NI/R`; "(làm tròn kết quả và lấy 1 chữ số sau dấu phẩy thập phân)" → "(làm tròn kết quả đến chữ số hàng phần mười)".
- III.5: "Xác định giá trị của tₓ theo đơn vị °C ?" → "… theo đơn vị °C."
- Câu dùng chung dữ kiện: I.4–I.5 và III.5–III.6 đặt đoạn dữ kiện trong câu đầu của cặp (`\label`/`\ref`).

## Đánh số lại câu

Đề gốc đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6), giữ nguyên.

## Hình

14 hình (13 vị trí hình theo kiểm kê; câu III.4 gồm ảnh bộ thí nghiệm và sơ đồ la bàn vẽ chung một `tikzpicture`), ảnh so ở `so-hinh/`. Vùng cắt ảnh trang 300 dpi (`pdftoppm -r 300`, tỉ lệ khổ trang): I.4 tr.1 `0.69:0.515:0.935:0.635`; I.7 tr.2 `0.08:0.065:0.92:0.20`; I.8 tr.2 `0.08:0.24:0.93:0.37`; I.10 tr.2 `0.76:0.55:0.92:0.64`; I.12 tr.2 `0.68:0.70:0.93:0.835`; I.13 tr.2 `0.70:0.825:0.94:0.955`; I.14 tr.3 `0.55:0.11:0.96:0.27`; I.18 tr.3 `0.65:0.645:0.94:0.80`; II.1 tr.4 `0.75:0.115:0.94:0.265`; II.3 tr.4 `0.75:0.725:0.93:0.875`; II.4 tr.5 `0.58:0.12:0.94:0.29`; III.2 tr.5 `0.17:0.83:0.86:0.93`; III.3 tr.6 `0.64:0.12:0.94:0.315`; III.4 tr.6 `0.45:0.475:0.94:0.62`.

- Hình thực tiễn (I.4 cảnh sát bắn tốc độ, I.10 nồi áp suất, I.13 đá khô, II.3 bình khí – đèn cồn – tay ấn, II.4 ảnh bình phun, III.3 phong vũ biểu, III.4 ảnh bộ thí nghiệm) vẽ có khối, `\shade`, gắn `% giuhinh`; chờ phiên vẽ lại chi tiết. II.3 dùng `\VLdencon`, `\VLtayan`; III.4 dùng `\VLkimnc`.
- I.7, I.8 thêm nhãn "Hình 1" … "Hình 4" dưới từng hình (hình gốc chỉ xếp theo thứ tự). I.8: proton đỏ, neutron xám đen, electron xanh.
- II.1: nam châm rotato tô N đỏ, S xanh; dây quấn trên cực stato đỏ; hình đặt cạnh lời dẫn để dàn trang ĐẠT.
- III.4: ⊗ I / ⊙ I tô màu dòng điện (đỏ); kim la bàn lệch 60° so với hướng Tây như hình gốc.

## Vẽ lại hình thực tiễn (PHIÊN FABLE 14/11/2026)

Vẽ lại cả 7 hình thực tiễn (các câu `% giuhinh`), dò theo ảnh gốc cắt ở 300 dpi (tọa độ TikZ lấy theo điểm ảnh của ảnh gốc, trục y hướng xuống). Sơ đồ, đồ thị (I.7, I.8, I.12, I.14, I.18, II.1, III.2) giữ nguyên. Không đổi lời đề, đáp án, lời giải; `dan_trang.py` ghi lại `\NeedspaceCau` của 6 câu. Bản đề 8 trang (ĐẠT), bản lời giải 11 trang.

- **I.4** (`01-cau-I-4.png`): vẽ lại toàn cảnh đúng bố cục ảnh — cảnh sát nhìn từ phía sau (mũ bảo hiểm vàng có chữ CSGT, lỗ thoáng, vành và quai mũ, khẩu trang, cổ áo, áo kaki, cầu vai, phù hiệu tay áo, cẳng tay), bàn tay nắm báng súng (bốn ngón ôm báng, ngón cái), súng bắn tốc độ (hộp ống kính, thân máy, khối ngắm phía trên, báng có vân), mặt đường có bóng cây và vạch sơn, bó vỉa sơn trắng – xanh, dải phân cách sọc đỏ trắng, hàng cây, nhà mái trắng, xe buýt và hai xe máy phía xa, tán cây góc trái, mây. Rộng 6,4 cm (hình cũ 4,6 cm).
- **I.10** (`04-cau-I-10.png`): nồi áp suất nhìn chếch từ trên như ảnh — thân bầu inox có vệt phản chiếu đen, vành nồi, nắp vồng có gờ tròn, núm nắp nhựa đen cổ kim loại, van báo áp suất, quai trái ốp kim loại có đai đen, tay cầm phải hai tầng có nút gạt và ke màu đồng.
- **I.13** (`06-cau-I-13.png`): ly cocktail miệng rộng đáy nón (hình cũ là ly bầu tròn), khói cuộn trên miệng ly, tràn xuống bên trái và phủ mặt bàn, làn khói mỏng bên phải; nền đen. Macro `\LTVkhoi`.
- **II.3** (`10-cau-II-3.png`): bàn tay ấn vẽ theo dáng ảnh gốc (thay `\VLtayan`), đĩa ấn, cán, pit-tông đen, bình thủy tinh thành dày có gờ miệng, kiềng mặt lưới hai chân choãi, đèn đốt có ống đốt, đế, núm van và ống dẫn như ảnh gốc (thay `\VLdencon`).
- **II.4** (`11-cau-II-4.png`): ảnh bình phun — tay cầm cong có rãnh ngón tay và cò bóp, núm tay bơm, cần bơm, cổ bơm có khía, nắp đen, vòi có núm vặn khía, van xả bên vai, thân nhựa trong (xilanh bơm, gioăng pit-tông, ống hút mềm bên trong), đế đen có gân. Sơ đồ cắt vẽ lại sát gốc: vòm bình, thành bình nét đôi, mặt nước gợn sóng, thành ống gạch chéo ở nửa trên, hai chốt bản lề, van k₁ (cuối ống trong) và k₂ (đáy xilanh), cán và tay cầm bơm, áp kế có vạch và cung đỏ, ống dẫn nước nét đôi, khóa k, tia phun. Nhãn cỡ `\footnotesize` (trước là `\scriptsize`).
- **III.3** (`13-cau-III-3.png`): chậu thủy tinh thành dày có vành miệng, khối thủy ngân có vệt sáng – tối, mặt thoáng elip, ống thủy tinh đầu tròn với cột thủy ngân và phần trống phía trên, mũi tên áp suất khí quyển tô chuyển màu, kích thước h, bốn nhãn như hình gốc.
- **III.4** (`14-cau-III-4.png`): ảnh bộ thí nghiệm — hộp đế nhựa trắng bo góc, vòng nhựa trong và cuộn dây đồng, la bàn (thân đen, mặt số có vạch chia, kim đỏ – xanh như hình cũ), giá đỡ đen, hai núm kim loại có khía (macro `\LTVnumkl`), hai phích cắm đen dây đen bên phải, hai phích cắm đen dây xám bên trái. Sơ đồ la bàn bên phải giữ nguyên (chỉ dời sang phải 0,3 cm).

Lưu ý:

- II.3: lời đề ghi "ngọn lửa đèn cồn" nhưng hình gốc vẽ đèn đốt có ống dẫn (kiểu đèn khí); hình vẽ lại theo hình gốc. Không ảnh hưởng đáp án.
- II.4: trong sơ đồ gốc, mũi tên "Pit-tông" chỉ vào đoạn ống thành gạch chéo (nửa trên), mũi tên "Xilanh" chỉ vào đoạn ống dưới; hình vẽ lại giữ đúng như vậy (hình cũ vẽ pit-tông là một cán có đầu nằm trong ống gạch chéo suốt chiều dài). Không ảnh hưởng đáp án.
- Hình chưa thật ưng: I.10 (thân và nắp inox tô chuyển màu còn phẳng hơn ảnh chụp, nắp trông vồng hơn ảnh); I.4 (hậu cảnh cây, mây, nhà ở mức cách điệu vì ảnh gốc mờ).

## Chốt đáp án (thầy duyệt 14/11/2026)

- **II.2 a): giữ Z = 53 đã sửa (đề gốc in ¹³¹₅₁I ở 6 chỗ), sửa lời ý a "79 neutron" thành "77 neutron"; Sai → Đúng** (¹³¹₅₃I → e⁻ + ¹³¹₅₄Xe, Xe có 131 − 54 = 77 neutron). Câu II.2 thành Đ Đ S S. Viết lại lời giải ý a, bỏ `% KIỂM TRA` của câu.
- **Đổi tên đề: `VatLi2026-HaNoi-LuongTheVinh-Lan1` → `VatLi2026-HaNoi-LuongTheVinh-Lan2`** (VietJack đăng đề này với tên "Lương Thế Vinh – Hà Nội lần 2"; file "Lần 2" của SieuGioi trùng nội dung). Đổi thư mục, file, dòng 1 khung tiêu đề (`… LƯƠNG THẾ VINH -- LẦN 2`), `\tenchuong` (`THPT Lương Thế Vinh, Hà Nội -- Lần 2`), mọi `\label`/`\ref`, thành phẩm (xóa bản Lan1).
- Các điểm còn lại ở `kho/KIEM-DAP-AN-V2.md` — II.3d (S), III.2 (200), III.4 (2,7): giữ như file, thầy chốt 14/11/2026. Các `% KIỂM TRA` khác giữ nguyên.
