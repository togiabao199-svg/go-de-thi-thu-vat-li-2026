# Kiểm chứng đáp án – VatLi2026-LamDong-SoGD

Nguồn: `kho/goc/Lam Dong - So GDDT.docx` (Sở GD&ĐT Lâm Đồng, mã đề 0201, đề gốc 6 trang, có đáp án + lời giải tham khảo). Đề gốc đánh số mỗi phần từ câu 1 nên giữ nguyên số câu.

Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | D A A B D D C C B D A D B D C A B B | trùng | I.5: m·c của sắt 0,92m, nhôm 0,88m, đồng 0,76m; I.14: 2,3·10⁶·0,05 = 1,15·10⁵ J; I.16: V ∝ T, V giảm: nén đẳng áp; I.17: A = 1, Z = 1 (proton) |
| II.1 | Đ S Đ S | trùng | t' = 50·2^(365/1945,5) ≈ 56,94 phút (tăng thêm 6,94 phút); λ = ln2/(1945,5·86 400) ≈ 4,12·10⁻⁹ s⁻¹ |
| II.2 | S Đ Đ S | trùng | e = 800·5·10⁻³·0,1·2 = 0,8 V; I = 0,2 A; dòng cảm ứng ngược chiều kim đồng hồ ABCDA |
| II.3 | S S Đ Đ | trùng | Δt = 55 K; Q = 15·4180·55 = 3 448 500 J; τ = Q/(0,95·2500) = 1452 s ≈ 24,2 phút |
| II.4 | Đ S Đ S | trùng | Lưới: (1) = (3;1), (2) = (3;3), (3) = (1;1) (p; V theo ô); n = 2,4·10⁵·1,8·10⁻³/(8,31·297) ≈ 0,175 mol, m ≈ 0,35 g |
| **III.1** | **1067** | **521** | **Lệch.** Lời giải gốc đọc đồ thị: nóng chảy 9 → 24 phút, đun lỏng 24 → 56 phút, 100 → 200 °C — không khớp hình trong đề. Đo lưới ảnh gốc (image19.png): cột 3 phút/ô (vạch 6 và 12 cách 2 ô), hàng 20 °C/ô (260 °C ở hàng thứ 13); nóng chảy từ 9 đến 21 phút ở 140 °C, chất lỏng nóng lên từ 21 đến 36 phút, từ 140 °C đến 260 °C. c = λΔt₂/(Δt₁ΔT) = 50 000·15/(12·120) ≈ 520,8 → **521**. File gõ 521, ghi `% KIỂM TRA` — thầy xem lại. |
| III.2 | −6,8 | −6,8 (`% KIỂM TRA`) | T = 2·5,51·10⁻²¹/(3k). Đề không cho k: k = 1,38·10⁻²³ → T = 266,18 K, x = −6,8 (đáp án gốc); k = 1,381·10⁻²³ → x = −7,0; k = 1,380649·10⁻²³ → x = −6,9. Gõ −6,8 theo gốc; thầy cân nhắc thêm "Cho biết k = 1,38·10⁻²³ J/K". |
| III.3–III.6 | 36,9 / 139 / 9 / 3,6 | trùng | N₀ = 0,29·10⁻⁶/241·6,02·10²³ ≈ 7,244·10¹⁴; λ ≈ 5,088·10⁻¹¹ s⁻¹; H₀ ≈ 36,86 kBq; t = 432·ln0,8/ln0,5 ≈ 139,07 năm; e = 18 V, I = 2,5 mA, F = 1,8·2,5·10⁻³·2·10⁻³ = 9 μN; Φ = 1,8·20·10⁻⁴ = 3,6 mWb |

Ghi chú: III.5, III.6 đề gốc không ghi yêu cầu làm tròn; đáp số 9 và 3,6 là số đúng, không cần làm tròn.

## Sửa lời đề (lỗi chữ bản gốc)
- I.12, I.15: in đậm từ phủ định "**không**".
- I.17: kí hiệu hạt nhân gốc vỡ ("9^19 F", "8^16 O") → ${}^{19}_{\phantom{1}9}$F, ${}^{16}_{\phantom{1}8}$O.
- I.18: "cylinder", "piston" → "xilanh", "pit-tông" (thuật ngữ SGK 2018).
- II.1: kí hiệu ⁶⁰₂₇Co vỡ ("27^60 Co") gõ lại; ý a) "+-1^0e" → ${}^{\phantom{-}0}_{-1}$e; "Chu kỳ" → "Chu kì".
- II.2: "theo phương vuông góc A'D'" → "theo phương vuông góc với A'D'".
- II.3c: "cung cấp cho nước trong máy tăng từ nhiệt độ từ 15 °C lên 70 °C" → "cung cấp để nước trong máy tăng nhiệt độ từ 15 °C lên 70 °C"; 3448500 J → 3 448 500 J.
- III.3: kí hiệu ²⁴¹₉₅Am vỡ gõ lại; "kilobecơren" → "kilobecquerel"; "Nguyên lý" → "Nguyên lí".
- III.5: "bệnh lý" → "bệnh lí".

## Hình vẽ (vẽ lại TikZ, chỗ khác ảnh gốc)
- I.9: bốn biển vẽ lại; biển tam giác dùng `\VLbienbao` (vàng viền đen), biển cấm (Hình 4) tô đỏ như biển thật.
- I.13 (ảnh "Quy trình làm muối truyền thống"): bỏ chú thích "(Bay Hơi Tự Nhiên)" dưới ô 2 vì lộ đáp án B (bay hơi); giữ "2. Phơi nước". Thầy xem có muốn giữ nguyên chú thích gốc.
- I.18: ảnh chụp ống tiêm – lọ thuốc vẽ lại, đặt bên phải các phương án (dàn trang).
- II.2: hai đoạn nối từ C, B tới A'D' (có trong hình gốc) vẽ nét mảnh đen; khung ABCD vẽ màu đồng, nét đậm.
- II.3: nhãn gốc "Dường dẫn điện vào" → "Đường dẫn điện vào"; "Ống dẫn nước nóng vào" → "Ống dẫn nước nóng ra" (nước nóng đi ra; bản gốc ghi "vào" ở cả hai ống). Số 70 °C trên màn hình giữ vì là dữ kiện đề.
- II.4: lưới gốc giãn không đều theo trục p (hai hàng trên hẹp hơn); vẽ lưới đều, giữ (1), (2), (3) và đường (2)–(3) kéo dài qua O (đúng quan hệ của lời giải gốc V₂ = 3V₁, p₁ = 3p₃).
- III.1: nhãn trục gốc "τ(⁰C)" → "T (°C)" cho khớp lời đề (đề gọi nhiệt độ là T); giữ các chấm trên trục như gốc (t = 6, 12, 21, 30, 36 phút; T ≈ 48, 140, 260 °C).
- III.3 (bộ báo cháy ion hóa): ảnh gốc là ảnh minh họa có nhiều nhãn sai/khó hiểu, vẽ lại gọn: bỏ tiêu đề; nhãn "HẠT α" trong đám khói → "Khói"; hộp dưới gốc ghi nhầm "NGUỒN PHÓNG XẠ" → "Mạch điện tử"; bỏ nhãn "ĐÈN ĐIỆN TỬ", "ÂM THANH CƯỜNG"; "Còi báo (tắt)" / "Còi báo (kêu)" giữ.
- III.5 (TMS): ảnh gốc ghi "B_max = 1,3 T" mâu thuẫn với lời đề (1,8 T) → chỉ ghi "B_max", không ghi số. (Bản cũ gộp nhãn thành "Xung từ trường (xung TMS)", trục "B (T)"; bản vẽ lại 14/11/2026 trả lại đủ nhãn, trục như gốc — xem mục cuối.)

## Vẽ lại hình thực tiễn (14/11/2026, Opus 5.5)
Chỉ sửa `tikzpicture` câu III.5 và khai báo riêng của đề; lời đề, `\shortans`, `\loigiai` giữ nguyên. Ảnh so: `so-hinh/10-cau-III-5.png` (dựng lại cả 10 ảnh so).
- Cách vẽ: hệ toạ độ là điểm ảnh của ảnh gốc `image26.png` (597×396, `x=0.0245cm, y=-0.0245cm`, hình rộng 14,5 cm ≈ 0,83 `\linewidth`, cao 9,5 cm, `% giuhinh`). Các nét hữu cơ (viền mặt – cằm – cổ, vòm sọ, đường viền và nếp cuộn não, thùy thái dương, tiểu não có sọc, thân não, 5 vòng đường sức từ + vòng trong cùng, toàn bộ mạng neuron và sợi trục trong vòng phóng to) lấy toạ độ bằng cách dò khung xương nét trên ảnh gốc (làm mảnh Zhang–Suen, nối ngã ba, làm trơn), rồi vẽ bằng `plot[smooth]`; độ dày từng nét theo độ dày đo trên ảnh gốc; tua neuron sẫm vẽ thành nét thon dần (đa giác độ dày giảm dần từ thân ra ngọn). Vùng tô (da đầu, cổ, não, thân não, thân neuron) lấy từ biên miền kín của ảnh gốc. Chồng ảnh gốc lên hình vẽ: các nét trùng khít (lệch dưới 1 điểm ảnh).
- Bộ phận: đầu nhìn nghiêng mặt quay trái (trán, mũi, môi, cằm, hàm, cổ, gáy), da tô khối nhạt, cổ mờ dần; đường da đầu mảnh chạy dưới cuộn; não hồng nhạt tô khối (sáng giữa, đậm rìa), nếp cuộn đỏ sẫm đủ như gốc; tiểu não có sọc, thân não thả xuống tô khối; neuron nhỏ (thân sẫm, 5 tua) ở tâm vùng chịu tác động; đường sức từ `VLxanh` khép kín lồng nhau, ngọn hội tụ vào chỗ tiếp giáp hai vòng cuộn. Cuộn TMS hình số 8: hai vòng xuyến dày nhìn xiên (elip khớp ảnh gốc), mặt trên tô chuyển sáng – tối, thành bên có 5 vạch quấn, lỗ giữa thấy thành trong có vạch; tay cầm hình trụ chĩa lên trái (thân có rãnh, đầu tròn), khâu nối có gờ, dây cáp vòng xuống trước mặt. Hai đường thẳng từ tâm vùng chịu tác động tới vòng phóng to (elip đứng, viền đậm, nền nhạt); trong vòng: 5 neuron sẫm (thân tô khối, nhân trắng, tua thon dần), 8 neuron sáng (thân viền mảnh tô kem, nhân vòng), sợi trục cong dài đan khắp vòng.
- Nhãn như gốc (câu chữ, ngắt dòng, vị trí, mũi tên): "Thiết bị cuộn TMS"; "Các neuron thần kinh / được hoạt hóa / (hoạt động)" — **hai mũi tên chỉ vào hai neuron sáng** (thân viền mảnh có nhân vòng, ở trên – phải vòng phóng to), đúng như ảnh gốc; "Các neuron thần kinh / trong trạng thái nghỉ" — **một mũi tên chỉ vào neuron sẫm lớn** ở dưới – phải (hình cũ vẽ đảo: "hoạt hóa" chỉ neuron sẫm, "nghỉ" chỉ neuron sáng). Đồ thị: trục đứng "$B$ (Tesla)", trục ngang "$t$ (ms)", xung dương nhọn rồi nhịp âm nhỏ hơn rồi về 0 (đường `VLxanh` đậm); **nhãn "$B_{\max}$" không ghi số** (gốc in 1,3 T, lời đề cho 1,8 T); "Xung từ trường / có điện thế ngược nhanh" có mũi tên chỉ nhịp âm; "Yếu tố từ trường / có điện thế thời gian / (xung TMS)" bên phải đồ thị. Chữ `\footnotesize`, nhãn đồ thị `\scriptsize`.
- Màu, khai báo riêng (giữa `\input{preamble-vatli-hinh}` và `\begin{document}`): bỏ macro `\LDneuron` (chỉ hình cũ dùng); thêm màu `LDda`, `LDda2`, `LDvien`, `LDnao0`, `LDnao2`, `LDnep`, `LDtn`, `LDthan`, `LDmo`, `LDsoi`, `LDsoinhat`, `LDsoma1`, `LDsoma2`, `LDsang`, `LDcuon1`–`LDcuon4`, `LDcuonv`; lệnh `\LDd{(x,y)...}` (nét trơn qua các điểm), `\LDs{...}` (đoạn thẳng). Không dùng `blue`, `cyan`, `teal`. Bản xám (`pdftoppm -gray`) vẫn phân biệt rõ da, não, nếp, đường sức, cuộn, neuron sẫm / sáng.
- Còn khác gốc: chữ nhãn dùng font của đề (Pagella) nên trông nhỏ hơn chữ in đậm hẹp của ảnh gốc; nét vẽ mảnh hơn nét ảnh gốc (ảnh gốc độ phân giải thấp, nét dày 2–3 điểm ảnh); thân neuron sẫm tô chuyển màu thay cho nền gạch chéo của ảnh gốc. Mã hình lớn (khoảng 500 dòng, 45 KB) vì giữ đủ nét như gốc.
- Dàn trang sau khi vẽ lại: bản đề 7 trang ĐẠT (trang 7 trống 5,5 cm, trang cuối); bản lời giải 11 trang (lưu ý cũ: trang 7 trống 7,6 cm, trong khoảng 1/4–1/3 trang; câu III.5 bản lời giải: phần đề + hình hết trang 10, dòng "Lời giải." cuối trang 10, lời giải sang trang 11).
