# Kiểm chứng đáp án – VatLi2026-HaiPhong-SoGD-Lan1

Nguồn: `kho/goc/Hai Phong - So GDDT - Lan 1.docx` (Sở GD&ĐT Hải Phòng, đề khảo sát kỳ thi tốt nghiệp THPT năm học 2025 – 2026, mã đề 0201), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | C B D B B C A C C B C D B D D B C B | trùng | I.4: 16·6,02·10²³/30,974 = 3,11·10²³; I.12: T = N/(A·m) = kg·A⁻¹·s⁻²; I.15: cực S lại gần, từ thông (hướng −Oy) tăng, B cảm ứng hướng +Oy ⇒ A→D→C→B→A; I.17: H = 1,7427·10⁸/4,25·10⁸ = 41,0 % |
| II.1 | S Đ Đ Đ | trùng | V/T = 0,2358; 0,2357; 0,2355; 0,2361 ml/K; đường V(t) khớp kéo dài cắt trục t ở ≈ −278 °C |
| II.2 | Đ Đ S S | trùng | λ = ln2/(8·86400) = 1,003·10⁻⁶ s⁻¹; t = 8·log₂125 = 55,7 ngày ≠ 31,6 |
| II.3 | Đ S S Đ | trùng | c) sau 6 phút nhiệt độ cốc nhôm giảm 36,5 → 33,5 °C |
| II.4 | Đ S Đ Đ | trùng | |
| III.1, III.2 | 1,69 / 1,56 | trùng | xem dưới |
| **III.3** | **4,70** | **4,71** | **Lệch.** H = 14,8·10⁴·2^(−1/8,06) = 135 804 Bq; V = 135 804/28,86 = 4705,6 ml = 4,7056 lít → làm tròn hàng phần trăm **4,71**. Lời giải gốc làm tròn trung gian (1,36·10⁵/28,86 ≈ 4700) dù đề ghi "không làm tròn kết quả trung gian". File gõ 4,71, có `% KIỂM TRA`. Thầy xem. |
| III.4–III.6 | 2,3 / 2,5 / 4 | trùng | |

## Phép tính chính (Python)
- III.1: E = Pt/H = 4·10⁸·86400/0,25 = 1,3824·10¹⁴ J; N = E/(200·1,6·10⁻¹³ J) = 4,32·10²⁴; m = N/N_A·235 = 1686,4 g ≈ 1,69 kg (dùng e = 1,602·10⁻¹⁹ C ra 1,684 kg, vẫn 1,68–1,69; đề quen dùng 1,6·10⁻¹⁹).
- III.2: (25 + x)/340 = (25 − x)/300 ⇒ x = 1000/640 = 1,5625 ≈ 1,56 cm.
- III.4: F = mg sin30° − ma = 0,25 − 0,02 = 0,23 N (lực từ hướng lên dốc vì a < g sinα); I = F/(Bl) = 0,23/(0,5·0,2) = 2,3 A.
- III.5: e = 50·0,5·0,01/0,1 = 2,5 V.
- III.6: nén đẳng nhiệt nên p₂ = 2,5 atm; V₂ = 2·5/2,5 = 4 lít.

## Điểm cần thầy xem
- **I.4** (`% KIỂM TRA`): đề gốc viết "³¹₁₅P là một đồng vị phóng xạ của nguyên tố phosphorus", nhưng ³¹P là đồng vị bền duy nhất của phosphorus (³²P mới phóng xạ). Giữ nguyên lời đề (không ảnh hưởng phép tính); thầy có thể sửa thành "là một đồng vị của nguyên tố phosphorus".
- **III.3** (`% KIỂM TRA`): đáp án gốc 4,70, tính lại 4,71 (xem bảng).

## Sửa lời đề (lỗi chữ bản gốc)
- I.4: "Khối lượng mol nguyên tử của ³¹₁₅P bằng 30,974 g" → "… 30,974 g/mol" (sai đơn vị); kí hiệu "³¹15P" (MathType vỡ) → ³¹₁₅P.
- I.4: tiêu đề phần I, II, III bỏ "(4,5 điểm)", "(4,0 điểm)", "(1,5 điểm)", dùng câu chữ chuẩn của đề mẫu.
- I.7: phương án D "J/kg.K" → "J/(kg.K)" (thống nhất cách viết với I.17).
- I.12: các phương án "1, T = 1, s.kg⁻¹.A⁻¹" bỏ dấu phẩy rác, dấu nhân viết "·".
- I.16: "vectơ cảm ứng từ B", "vectơ pháp tuyến n" viết kí hiệu vectơ $\vv{B}$, $\vv{n}$.
- I.17: "380, (J/kg.K)", "1,8·10⁵, J/kg", "5·10⁶, J" bỏ dấu phẩy rác trước đơn vị.
- II.1: "(2) Đổ nước sôi vào hộp chứa cho ngập hoàn toàn xi lanh" → "xilanh"; ý c) "hệ tọa độ V − t (°C)" viết "$V$ -- $t$ (°C)".
- II.2, III.3: kí hiệu "¹³¹53I" (MathType vỡ) → ¹³¹₅₃I; II.2 "12500" viết tách nhóm 12 500; "(World Health Organization – WHO)" giữ nguyên.
- II.2 b), III.4, III.5: bỏ dấu phẩy rác trước đơn vị ("1,0·10⁻⁶, s⁻¹", "0,5, T", "0,4, m/s²", "10, m/s²").
- III.1: "²³⁵92U" → ²³⁵₉₂U; "25%" → "25 %".
- III.2: "cách đều 2 đầu xilanh" → "cách đều hai đầu xilanh".
- III.3: "1 (ml)" → "1 ml"; "(Đồng vị …" → "(đồng vị …".
- Không câu hỏi nào có từ phủ định cần in đậm.

## Trình bày
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại). Không có cặp câu dùng chung dữ kiện.
- Mã câu: I.5 (chụp CT, tia X) xếp `VL12-C3` (sóng điện từ) như câu chụp X-quang đề Cần Thơ.
- Hình: 11 hình vẽ lại bằng TikZ, tô màu theo bảng màu chung; 8 hình có `% giuhinh` (ảnh thực tiễn, mạch circuitikz):
  - I.4 ô nguyên tố P (giữ chữ tiếng Anh, "30.974" như hình gốc — số này có trong lời đề).
  - I.5 máy chụp CT (khung máy, bóng phát tia X, chùm tia quạt, bàn chụp, bệnh nhân, máy tính xử lí); đặt bên phải đoạn "Biết rằng … Nhận định nào …" để gọn trang.
  - I.10 bình gas mini đang xịt (ngón tay ấn nút xanh, vòi đóng băng, tia khí).
  - I.15 nam châm N đỏ, S xanh, khung dây ABCD màu đồng, hệ trục Oxyz, mũi tên chiều chuyển động màu VLluc.
  - I.17 xưởng đúc chuông (bình khí đốt, lò có lửa, chuông trên khuôn); bỏ người thợ (chi tiết trang trí). Lửa, kim loại nóng chảy tô VLdo.
  - II.1 bộ thí nghiệm áp kế – cảm biến nhiệt độ – xilanh – tay quay đặt cạnh bảng số liệu; màn hình cảm biến giữ "45.0 °C" (đúng số liệu lần đo 1 trong bảng).
  - II.3 cốc thủy tinh, cốc nhôm, hai nhiệt kế điện tử (màn hình "20.0" = số liệu t = 0 trong bảng); đặt bên phải đoạn "Thí nghiệm 2". Nước không tô phân biệt nóng/lạnh.
  - II.4 phanh điện từ: đĩa, trục quay, lõi thép có rãnh, cuộn dây đồng, mạch K – nguồn một chiều, dòng điện I đỏ, từ trường xanh, lực từ, chiều quay; giữ các chú thích của hình gốc.
  - III.1 tàu ngầm hạt nhân cắt dọc (lò phản ứng tô VLdo, các khoang).
  - III.2 xilanh hai ngăn A, B (p = 1 atm, T = 300 K, 25 cm); hình gốc không vẽ x, giữ nguyên.
  - III.4 hai ray nghiêng 30°, thanh MN, R, nguồn, các trục tham chiếu, $\vv{B}$ màu VLxanh; đặt bên phải phần cuối câu dẫn.
- I.17, III.1 là ảnh EMF: so hình bằng vùng cắt ảnh trang bản LibreOffice (`hr-04.png`, `hr-07.png`, 200 dpi).
- Ảnh so ở `so-hinh/`.

## Vẽ lại hình thực tiễn (14/11/2026, Opus 5.5)
Vẽ lại hai hình thực tiễn I.5, III.1 theo toạ độ điểm ảnh của ảnh gốc (`x={\linewidth/632}`, `x={0.6\linewidth/239}`, trục y lật), soát từng vùng cắt cạnh ảnh gốc (ảnh chồng, so viền tối). Chỉ sửa `tikzpicture` hai câu này, màu riêng của đề và cách đặt hình; lời đề, `\True`, `\shortans`, `\loigiai`, các hình khác giữ nguyên. Hai dòng I.5, III.1 ở mục "Trình bày" phía trên nay thay bằng mô tả dưới đây.
- I.5 máy chụp CT (`so-hinh/02-cau-I-5.png`, gốc `image18.png` 632×422): nền tường xám nhạt chuyển màu có khe ghép, sàn lát gạch phối cảnh, bóng đổ dưới đế máy và bệ bàn, nền bo góc; khung máy (gantry) nhìn xiên trước – trái đúng tỉ lệ: vành ngoài viền đậm, mặt bên cong xám trắng, chân và vách dưới xanh xám, mặt trước elip trắng có gờ vát xám, đường ghép theo elip, hai gờ nổi, rãnh xanh xám trên nóc, tấm sáng bên hông, bảng điều khiển bên hông (màn hình, nút vàng, đèn); lòng máy elip (mặt trong xám tối dần, vành tối phía sau, ống sáng phía sau); bóng phát tia X hộp thang có ô tối, ống chuẩn trực, quầng cam; chùm tia quạt vàng – cam nhiều tia, chấm lấp lánh, vùng sáng trên ngực; vệt tia xanh nhạt trong lòng máy; hai bảng đầu thu bo góc (hai cột nút tròn cam có điểm sáng) và vòng tròn xanh phía trên; ba mũi tên vàng (bóng phát → bảng phải, ngực → bảng trái, dải vàng kép từ bảng phải xuống dải đầu thu cuối bàn); bệnh nhân nằm ngửa (tóc đen, mặt, tai, áo cộc tay xám xanh vén lên thấy bụng, hai tay xuôi có ngón, quần dài nhiều nếp, hai bàn chân trần có ngón, bóng người trên đệm); đệm xanh xám, mặt bàn trắng, rãnh tối dọc mép, mép bàn hai lớp, đầu bàn bo tròn có dải đầu thu vàng phát sáng (lưới ô) và thanh đầu thu tối có ô vàng; bệ bàn trắng ba tầng có rãnh tối trên đế xanh xám; khung máy tính góc trên phải viền đậm bo góc (tủ máy chủ hai tầng có khe ổ đĩa, đèn cam; màn hình lát cắt CT ổ bụng nền đen, cơ quan cam – nâu, cột sống trắng, cột chữ nhỏ vẽ thành vạch; chân đế, bàn phím có lưới phím, chuột, dây, mặt bàn, gầm bàn, chân bàn); hai mũi tên cong xanh nhạt về khung máy tính. Bỏ dấu sao watermark. Vẫn đặt bên phải đoạn "Biết rằng … Nhận định nào …" (hai `minipage` 0,42 | 0,56 `\linewidth`, hình 9,7 × 6,5 cm), thêm `\smallskip` để hình không sát dòng trên.
- III.1 tàu ngầm hạt nhân (`so-hinh/09-cau-III-1.png`, gốc `emf85.png` 239×143): thân tàu đen xám kim loại nhìn xiên (mũi tròn bên trái cao, thuôn dần về đuôi thấp bên phải), tô khối (dải sáng trên lưng, mũi được chiếu sáng), bóng đổ mềm dưới thân và dưới đuôi (bóng tỏa `HPmotbong`, pha trộn multiply); tháp chỉ huy, cánh lái ngang hai bên tháp, 4 ống tiềm vọng / cột ăng-ten, cọc nhỏ trên boong; đuôi có bánh lái đứng trên – dưới, cánh lái ngang (mép sáng, lỗ nhỏ), vành bao trục, chân vịt đồng 6 cánh có điểm sáng kim loại; mặt cắt bổ dọc có bề dày vỏ (dải đồng xỉn + viền sáng) và hàng đinh tán dọc dải vỏ dưới; nội thất theo đúng vị trí ảnh gốc: khoang mũi (thiết bị trụ vàng, ống đỏ – xanh), khoang ngư lôi (5 quả ngư lôi vàng trên giá), khoang máy (hộp thiết bị, đèn, nhiều ống dẫn đỏ / xanh, van, tua-bin vàng), lò phản ứng (bình trụ đầu vòm, lõi rực cam – vàng, đáy, ống dẫn hai bên), hai phòng điều khiển (vách màn hình xanh lam nhiều ô, bàn điều khiển có đèn, sàn) với 5 thủy thủ áo xanh đậm ngồi quay lưng (2 + 3 như gốc), boong dưới (giá ống vàng, thùng hàng), khoang đuôi (tủ thiết bị vàng, màn hình xanh, máy móc, thùng), vách ngăn, sàn các tầng. Không có chữ. Đặt lại như bản Word gốc: hình ở giữa ngay dưới câu dẫn, câu hỏi "Nếu công suất …" ở dưới hình (lời không đổi), rộng 0,6 `\linewidth` (10,4 × 6,3 cm); bản cũ đặt hình nhỏ bên phải câu hỏi.
- Màu riêng khai báo trong file đề (tiền tố `HPmot`): I.5 `HPmotvien`, `HPmott1`–`HPmott3` (tường), `HPmots1`, `HPmots2` (sàn), `HPmotxanhxam`, `HPmotxanhtoi`, `HPmotxam`, `HPmotdem`, `HPmotda`, `HPmotao`, `HPmotquan`, `HPmotvang`, `HPmotcam`, `HPmotxanhnhat`, `HPmotxanh`; III.1 `HPmotthan`, `HPmotthansang`, `HPmotkim`, `HPmotdongvang`, `HPmotman`, `HPmotaolinh`, `HPmotla`; bóng tỏa `\pgfdeclareradialshading{HPmotbong}`. Không thêm macro; không dùng `blue`, `cyan`, `teal`.
- Ảnh gốc: I.5 lấy `image18.png`; I.17 và III.1 nay lấy bitmap tách từ file EMF (`emf57.png` từ `image57.emf`, `emf85.png` từ `image85.emf`) thay cho vùng cắt ảnh trang LibreOffice.
- Điểm còn khác gốc: I.5 người, nếp áo quần, mặt vẽ ở mức minh họa (gọn hơn ảnh gốc), lát cắt CT trên màn hình vẽ giản lược thành các khối, chữ trên màn hình thay bằng vạch, ít chấm lấp lánh hơn; III.1 ảnh gốc rất nhỏ, nội thất dày đặc chi tiết mờ nên bản vẽ theo các mảng chính (không có khung đồng quanh bình lò, ít đồ vật nhỏ hơn), màu thân tàu đều hơn ảnh gốc. Bản xám (`pdftoppm -gray`) vẫn phân biệt rõ các mảng.
- Dàn trang sau khi vẽ lại: bản đề 9 trang ĐẠT (trống cuối trang 4,8 / 3,0 / 3,4 / 1,3 / 6,1 / 1,9 / 4,2 / 3,6 / 11,4 cm, trang cuối); bản lời giải 13 trang (trước 12: hai hình to hơn), lưu ý trang 3, 6, 9 bản lời giải trống 8,0 / 8,7 / 7,7 cm (trong khoảng 1/4–1/3 trang), không lỗi.
