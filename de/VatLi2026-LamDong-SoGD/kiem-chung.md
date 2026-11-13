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
- III.5 (TMS): ảnh gốc ghi "B_max = 1,3 T" mâu thuẫn với lời đề (1,8 T) → chỉ ghi "B_max", không ghi số; nhãn dịch máy khó hiểu "Yếu tố từ trường có điện thế thời gian (xung TMS)", "Xung từ trường có điện thế ngược nhanh" → gộp thành "Xung từ trường (xung TMS)"; trục "B (Tesla)" → "B (T)".
