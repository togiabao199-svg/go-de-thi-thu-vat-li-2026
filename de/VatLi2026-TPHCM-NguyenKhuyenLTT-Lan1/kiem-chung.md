# Kiểm chứng đáp án – VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1

Đề gốc: PDF SieuGioi "SỞ GD&ĐT TP HCM – NGUYỄN KHUYẾN - LTT – Lần 1, năm 2025 - 2026", 6 trang, không có đáp án, không có lời giải. Mọi câu tự giải, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | C A D C C A A D D C C C A D A B B C | I.3: Hình 1 đẳng tích, ba hình còn lại đẳng áp; I.4: chiều dương quy ước (nhìn từ trên) cùng chiều kim đồng hồ ⇒ nam châm ở trên: dòng ngược chiều dương, ở dưới: theo chiều dương; I.10: mỗi ô dọc 2 mT, ô ngang 0,125 s (nhãn 0,5 ở ô thứ 4), B = (2 + 8t) mT, Φ(0,2 s) = 10 · 3,6·10⁻³ · 25·10⁻⁴ = 9·10⁻⁵ Wb = 90 μWb; I.11: e = 10 · 25·10⁻⁴ · 4·10⁻³/0,5 = 2·10⁻⁴ V; I.12: E × B cùng chiều v chỉ ở Hình 3; I.13: 1,5 · (8,31/6,02·10²³) · 300 = 6,21·10⁻²¹ J; I.14: 1,5 · pV = 2279,8 J; I.16: 0,03/(0,75 · 0,05) = 0,8 T; I.18: A đi lên nhanh dần, lực đỡ đĩa trái tăng ⇒ nghiêng trái |
| II.1 | không có | Đ Đ S S | R = 1,7·10⁻⁸ · 0,72/3,5·10⁻⁹ = 3,497 Ω; I = 12/(3,497 + 0,5) = 3,002 A; B = 0,004 · 9,8/(3 · 0,1) = 0,1306 T = 131 mT (98 mT là số bẫy khi bỏ r: I = 4 A); c) bản dài (+) của nguồn ở phía A ⇒ dòng điện trong đoạn ngang đi từ trước ra sau, B từ N sang S ⇒ lực từ hướng xuống |
| II.2 | không có | Đ Đ S S | a) theo hình: bản dài (+) ở dưới, dòng điện vào cuộn dây nhánh Q ở đầu phải, sang nhánh P, ra ở đầu phải nhánh P; vòng dây vẽ nghiêng "\" (sợi phía trước đi từ trên-trái xuống dưới-phải) ⇒ đường sức trong lõi ra ở P: P bắc, Q nam |
| II.3 | không có | Đ S Đ Đ | p(8 lít nước) = 120 · 10/2 = 600 kPa; rơle đóng ở 120 · 10/5 = 240 kPa; sau xả khí: 240 · 4/(120 · 10) = 0,8 ⇒ thoát 20% |
| **II.4** | **không có** | **Đ S S S** | **Ý c), d) phụ thuộc cách hiểu, thầy xem.** A = 1850 · 240 = 4,44·10⁵ J; Q nước = 1,2 · 4200 · 75 = 3,78·10⁵ J (đề ghi 3,87·10⁵); Q vỏ = 0,8 · 500 · 75 = 3·10⁴ J. c) "hiệu suất làm nóng nước" = Q nước/A = 85,1%; nếu tính cả vỏ ấm (Q nước + Q vỏ)/A = 91,9% ≈ 92%. d) nhiệt tỏa ra môi trường = A − Q nước − Q vỏ = 3,6·10⁴ J (8,1%) ⇒ khi sôi t = 1,2 · 2,3·10⁶/(0,919 · 500) = 6007 s = 1,67 giờ; số 1,8 giờ của đề chỉ ra khi coi cả nhiệt lượng vỏ ấm là hao phí (tỉ lệ 14,9%): 1,80 giờ. File gõ theo cách tính chặt (c Sai, d Sai). Hai cách hiểu khác: c Đ – d S (tính hiệu suất gồm vỏ ấm) hoặc c S – d Đ (coi nhiệt vỏ ấm là hao phí). |
| III.1–III.6 | không có | 121 / 0,85 / 46,7 / 281 / 1,9 / 0,3 | III.1: 0,2 · 4190 · 90 + 0,02 · 2,26·10⁶ = 120 620 J; III.2: 0,6 · 3,14 · (1 − 0,64)/(4 · 0,2) = 0,8478 V; III.3: p = (2/3) · 70·10⁻⁶ = 46,67·10⁻⁶; III.4: B²l²v/R = 0,49 · 0,04 · 4,3/0,3 = 0,2809 N; III.5: p chung, V_A : V_B = 2 : 5 → 3 : 4, B đẳng nhiệt p' = 1,25p, T'/T = 1,25 · 1,5 = 1,875; III.6: e = 0,576 V, R ngoài lớn nhất 3 ∥ 3 = 1,5 Ω, I_min = 0,576/2 = 0,288 A ≈ 0,3 A |

Script kiểm chứng: `/tmp/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1/py/giai.py` (scratchpad, không commit).

## Điểm cần thầy xem

- **II.1 b)** (`% KIỂM TRA`): bản gốc ghi "cường độ dòng điện chạy trong mạch điện là 3 V" (sai đơn vị). Coi là lỗi chữ, sửa thành "3 A", chấm Đúng (I = 3,00 A). Nếu thầy muốn giữ "3 V" như một ý bẫy đơn vị thì ý b) thành Sai.
- **II.1 c)**: chiều dòng điện suy từ kí hiệu nguồn trên hình gốc (ảnh mờ, phóng 600 dpi): từ phía K sang B lần lượt bản dài – bản ngắn – bản dài – bản ngắn ⇒ cực dương ở phía chốt A. Lực từ hướng xuống ⇒ c) Sai. Hình vẽ lại giữ đúng thứ tự bản cực này.
- **II.2 a)**: kết luận dựa vào cực nguồn (bản ngắn đậm ở trên là cực âm) và chiều quấn dây vẽ trên hình gốc; nếu đọc ngược chiều quấn thì a) thành Sai. Hình vẽ lại giữ đúng nét quấn "\" của gốc.
- **II.4 c), d)** (`% KIỂM TRA`): xem dòng II.4 ở bảng trên.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi ("ĐỂ THI THỬ…", "Lần 1, năm 2025 - 2026"), dòng họ tên / số báo danh, "Đề thi gồm 06 trang", dòng quảng cáo chân trang.
- Cho biết: "R = 8,31 J. mol⁻¹" → "R = 8,31 J·mol⁻¹·K⁻¹" (bản gốc thiếu K⁻¹).
- I.1: in đậm "không".
- I.4: "như hình vẽ" → "như hình bên" (hình đặt bên phải phương án như bản gốc).
- I.6: bỏ dấu phẩy thừa "lên mặt trên của sạc, thì…".
- I.8: bỏ dấu ":" sau "chứng tỏ", phương án viết thường đầu dòng (nối tiếp câu dẫn).
- I.10–I.11, I.13–I.14: đoạn "Dùng các thông tin sau cho câu … và câu …" đặt trong câu đầu của cặp, tham chiếu bằng `\label`/`\ref`. I.10: "100μ Wb", "90μ Wb" → "100 μWb", "90 μWb". I.13: "101325 Pa" → "101 325 Pa".
- I.12 (hình): kí hiệu vectơ hướng vào mặt phẳng hình "⊕" của bản gốc vẽ thành "⊗" theo SGK 2018 (Hình 1, Hình 3); "⊙" giữ nguyên.
- I.18: "k hông" → "không".
- II.1: "trong do" → "trong đó"; "dòng diện" → "dòng điện"; "3 V" → "3 A" (xem trên); "hình vẽ bên" → "hình bên"; suất điện động viết $\mathscr{E}$.
- II.3 (hình): "Rơ le áp suất" → "Rơle áp suất" (thống nhất với lời đề).
- II.4: "220 V − 50 Hz" → "220 V – 50 Hz".
- III.3: "70 μ J/m³" → "70 μJ/m³"; thêm dấu chấm cuối câu.
- III.6: thêm dấu "?" cuối câu hỏi.

## Đánh số câu

Đề gốc đã đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6), giữ nguyên.

## Hình

14 hình gốc → 15 `tikzpicture` (II.4 gồm ấm điện và đồ thị; bảng thông số Hình 1 gõ bằng `tabular`), ảnh so ở `so-hinh/`. Vùng cắt ảnh trang (150 dpi, tỉ lệ khổ trang): I.3 tr.1 `0.12:0.445:0.90:0.58`; I.4 tr.1 `0.81:0.64:0.94:0.79`; I.6 tr.2 `0.74:0.065:0.935:0.155`; I.10 tr.2 `0.72:0.40:0.93:0.53`; I.12 tr.2 `0.13:0.675:0.88:0.81`; I.15 tr.3 `0.52:0.125:0.95:0.30`; I.18 tr.3 `0.55:0.53:0.95:0.63`; II.1 tr.3 `0.65:0.76:0.94:0.93`; II.2 tr.4 `0.57:0.30:0.94:0.49`; II.3 tr.4 `0.62:0.54:0.94:0.80`; II.4 tr.5 `0.08:0.185:0.92:0.315`; III.4 tr.5 `0.64:0.69:0.95:0.79`; III.5 tr.6 `0.71:0.075:0.95:0.15`; III.6 tr.6 `0.82:0.24:0.95:0.36`.

- Hình thực tiễn (`% giuhinh`), vẽ ở mức các lô trước, chờ phiên vẽ lại: I.6 (sạc không dây, hộp tai nghe, điện thoại có biểu tượng pin), I.15 (dây chuyền phân loại rác, lon rơi ở vị trí 1, 2; lược bớt rác hữu cơ chi tiết), II.1 (nam châm chữ U trên cân, khung dây, công tắc, nguồn), II.4 (ấm điện inox).
- Màu: nam châm N đỏ / S xanh (I.4, II.1); đường sức, B xanh; E đỏ, v và F xanh lá; dây dẫn, cuộn dây màu đồng; cạnh khung dây trong từ trường (III.4) giữ màu đỏ như gốc.
- Macro riêng của đề: `\NKlon` (lon kim loại nằm nghiêng, dùng ở I.15).

## Vẽ lại hình thực tiễn (PHIÊN FABLE 14/11/2026)

Vẽ theo toạ độ điểm ảnh của ảnh gốc (ảnh nhúng trong PDF, phóng to có lưới), không đổi nội dung vật lí, lời đề, đáp án.

- **I.6** (`so-hinh/03-cau-I-6.png`): vẽ lại đế sạc đôi hình ô van (mặt trên, thành bên, vành bóng), dây cáp và đầu cắm, hộp tai nghe trắng, điện thoại đặt chếch (viền máy, mặt kính, đĩa sạc nhìn xuyên qua máy, biểu tượng pin xanh, các dòng chữ nhỏ), bóng đổ. Không vẽ mảng nền xám mờ ở góc trái trên của ảnh (không thuộc thiết bị).
- **I.15** (`so-hinh/06-cau-I-15.png`): vẽ lại dây chuyền đúng bố cục gốc: hai con lăn, tay đỡ xanh, dây băng tải vòng qua con lăn phải; rác trên băng (hộp nhựa, kem ốc quế, chai nhựa, vỏ tôm, vỏ chuối, ớt chuông xanh / cam, cà rốt, rau), các lon bị bóp méo thấy đáy và miệng lon; lon cam và lon đỏ bám theo con lăn, lon xanh rơi ở vị trí 1, lon đỏ ở vị trí 2 (giữ như gốc). Macro mới `\NKlon` (5 tham số), `\NKotchuong`.
- **II.1** (`so-hinh/08-cau-II-1.png`): nam châm vẽ lại đúng dạng chữ C của gốc (hai má cực N, S hướng vào nhau, khe hở phía trên, lòng khe thấy đáy và thành trái), tô khối N đỏ / S xanh, cân là tấm phẳng có bóng đổ; khung dây màu đồng đi xuống từ A, đoạn ngang chạy trong khe từ trước ra sau, đi lên B. Khóa K và nguồn hai pin vẽ bản cực thẳng đứng như gốc; **thứ tự bản cực giữ nguyên: từ phía K sang B là dài – ngắn (đậm) – dài – ngắn (đậm)**.
- **II.4** (`so-hinh/11-cau-II-4.png`): vẽ lại ấm điện inox: thân bóng gương (dải phản chiếu tối giữa thân, hai mép tối, dải đáy), nắp vòm, núm nhựa đen, quai xách (hai tay kim loại, tay cầm đen), vòi, đầu cắm nguồn bên phải, dây điện cuộn và phích cắm. Bảng Hình 1, đồ thị Hình 2 giữ nguyên.
- **II.3** (`so-hinh/10-cau-II-3.png`, sơ đồ cắt dọc, không phải ảnh chụp): hình cũ vẽ cụm ống thành chữ T (hai ống cùng đi lên), khác gốc; vẽ lại theo gốc: cổ bình, ống nước ra đi thẳng lên, nhánh ngang qua rơle (hộp đen) tới ống nước vào; vỏ bình hai lớp, bóng chứa nước, bóng chứa khí có hai gân nối với vỏ. Đáy bình (ảnh gốc bị cắt) vẽ khép kín; cụm ống vẽ to hơn tỉ lệ gốc để nhãn không đè.
- **II.2** (`so-hinh/09-cau-II-2.png`, sơ đồ): chỉ THÊM đoạn dây nối hai cuộn dây (từ mép dưới nhánh P xuống mép dưới nhánh Q, sát chỗ uốn của lõi) có trên hình gốc mà hình cũ thiếu (thiếu thì mạch hở). Cực nguồn, chiều quấn "\", chỗ nối dây vào cuộn giữ nguyên.

Đối chiếu ảnh gốc phóng to (400 dpi và ảnh nhúng gốc) cho ba câu có đáp án phụ thuộc hình:

- **I.10**: lưới 5 × 4 ô; số 4 ở vạch ngang thứ 2, số 0,5 ở vạch dọc thứ 4; đường thẳng xuất phát từ (0; 1 ô), đi qua các nút lưới (2 ô; 2 ô) và (4 ô; 3 ô). Cách đọc B = (2 + 8t) mT của file khớp ảnh gốc.
- **II.1 c)**: kí hiệu nguồn trên ảnh gốc, từ phía khóa K sang chốt B: vạch dài mảnh – vạch ngắn đậm – vạch dài mảnh – vạch ngắn đậm; chốt A ở phía trước, chốt B ở phía sau (đoạn dây chéo song song với cạnh chiều sâu của nam châm). Cách đọc của file (cực dương phía A, dòng điện trong đoạn ngang đi từ trước ra sau) khớp ảnh gốc.
- **II.2 a)**: nguồn trên ảnh gốc từ trên xuống: vạch ngắn đậm – vạch dài – vạch ngắn đậm – vạch dài (cực âm ở trên, cực dương ở dưới, phía công tắc S); các vòng dây mặt trước của cả hai nhánh nghiêng "\" (đầu trên lệch trái); dây trên nối vào mép trên đầu phải cuộn P, dây dưới nối vào mép dưới đầu phải cuộn Q, hai cuộn nối với nhau bằng đoạn dây thẳng đứng ở đầu trái. Cách đọc của file khớp ảnh gốc.

Bố cục: I.15 hai cột 0,49 / 0,41 `\linewidth`; II.1 hai cột 0,6 / 0,3 `\linewidth` (hình rộng 5,0 cm; thử 5,5 cm thì trang 5 bản đề trống 8,5 cm nên giữ 5,0 cm). Dàn trang: bản đề 7 trang ĐẠT, bản lời giải 11 trang (lưu ý trang 5 trống 7,5 cm).

Hình chưa ưng: I.6 — ảnh gốc mờ, phân giải thấp (329 × 190 điểm ảnh) nên các dòng chữ trên màn hình điện thoại chỉ vẽ thành nét gạch; hộp tai nghe vẽ dạng khối bo tròn, không có chi tiết bản lề / đèn báo (ảnh gốc không thấy rõ). I.15 — rác hữu cơ vẽ giản lược hơn ảnh gốc (ảnh gốc là tranh minh họa nhiều chi tiết nhỏ).

## Sửa hình theo báo cáo phiên kiểm đáp án (14/11/2026)

- II.4 (Hình 2, đồ thị): bản trước chia trục hoành 10 khoảng 48 s (4 điểm trung gian trên đoạn đun); hình gốc chia 8 khoảng 60 s (3 điểm trung gian ở 60, 120, 180 s). Đã vẽ lại theo gốc; các mốc 25 °C, 100 °C, 240 s, 480 s không đổi nên đáp án không đổi.
- II.2: nét dây nối hai cuộn dây ở đầu trái lõi sắt (thiếu ở bản trên `main`) đã được thêm trong lúc vẽ lại hình (PHIÊN FABLE), đúng gốc.
