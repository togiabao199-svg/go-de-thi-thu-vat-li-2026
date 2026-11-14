# Kiểm chứng đáp án – VatLi2026-DaNang-SoGD-Lan1

Nguồn: `kho/goc/Da Nang - So GDDT - Lan 1.docx` (mã đề 0201, có đáp án và lời giải tham khảo). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | C C D C C A C C A B A A B B D B A B | trùng | I.1: 9/4 = 2,25; I.6: 9t/5 + 32 = 2t ⇒ t = 160; I.7: 0,5·1800·60 = 54 kJ; I.13: R³ = 0,03·1000·310/223 = 41,70 ⇒ R = 3,47 m. **I.3: phương án B \|−ΔΦ/Δt\| cũng bằng D về giá trị (đề có hai phương án tương đương); giữ D theo bản gốc, ghi `% KIỂM TRA`.** |
| II.1 | Đ Đ S Đ | trùng | p = 77 cmHg; V = π(0,3 mm)²·150 mm = 4,24·10⁻⁸ m³; n = 1,758·10⁻⁶ mol; h/t giảm 6,0 → 2,3 (không tỉ lệ), h/T ≈ 0,50; V/T lần lượt 0,1423; 0,1438; 0,1416; 0,1438; 0,1435; 0,1411, trung bình 0,14267 |
| II.2 | Đ S Đ Đ | trùng | A = 3,7·4·3600/0,9 = 59 200 J |
| II.3 | Đ Đ S S | trùng | cổ góp hai nửa vành khuyên: dòng qua đèn một chiều |
| II.4 | S Đ S Đ | trùng | d) theo định luật bảo toàn năng lượng (hệ gồm tay, mặt) |
| III.1, III.2 | 8,9 / 1,1 | trùng | N₀ = H₀T/ln2 = 5·10⁵·1 235 520/0,6931 = 8,91·10¹¹; N = (0,1 + 0,12)N₀ ⇒ H = 1,1·10⁵ Bq (hiểu như lời giải gốc: số nguyên tử cây tích lũy tính ở cuối mỗi chu kì) |
| **III.3** | **4** | **3** | **Lời giải gốc tính I = E/(R_thanh + R_ray) = 80 A, bỏ điện trở trong r = 0,05 Ω mà đề cho (và chính câu III.4 lại dùng R = 0,2 Ω có r). Đúng: I = 12/(0,1 + 0,05 + 0,05) = 60 A ⇒ F = 0,5·60·0,1 = 3 N. File gõ đáp án 3, ghi `% KIỂM TRA` — thầy xem lại.** |
| III.4–III.6 | 57 / 11,4 / 5,1 | trùng | III.4: e_c = 0,6 V, I = 11,4/0,2 = 57 A; III.5: n₁ = 203,17, n₂ = 193,36, Δm = 274,6 g, /24 = 11,44 g; III.6: 94,5 + 5010 = 5104,5 J |

## Sửa lời đề (lỗi chữ bản gốc)
- "lý tưởng" → "lí tưởng", "chu kỳ" → "chu kì", "vector" → "vectơ", "sự hoá hơi" → "sự hóa hơi" (thuật ngữ SGK).
- I.3: phương án C "|ΔΦΔt|" gõ thành $|\Delta\Phi\cdot\Delta t|$.
- I.11: kí hiệu hạt nhân ³₁T, ⁴₂He gõ lại (bản gốc chữ "và" nằm trong công thức).
- I.13: phần chú thích "thiết bị sử dụng để thu thập thông tin…" đặt trong ngoặc đơn cho rõ câu.
- I.14: "trên hình vẽ" → "trên hình bên" (hình đặt bên phải các phương án).
- I.15: giữ nguyên các phương án nhiễu (A có "¹₀H" như bản gốc).
- II.2: "thiết bị sạc pin điện thoại, bộ sạc" → "(bộ sạc)".
- III.1/III.2: "Sử dụng các thông tin sau cho Câu 1 và Câu 2" → `Dùng thông tin sau cho câu 1 và câu 2:` đặt trong câu 1 (tương tự câu 3, 4); "Phosphorus-32, ³²P," → "Phosphorus-32 (³²P)"; câu hỏi "Tìm m làm tròn kết quả đến chữ số hàng phần mười?" → "Tìm m (làm tròn kết quả đến chữ số hàng phần mười)."
- III.5: "Nitrogen, N₂," → "Nitrogen (N₂)"; "gram" → "gam"; câu hỏi gộp yêu cầu làm tròn vào ngoặc.
- III.6: "Một viên nước có khối lượng" → "Một viên nước đá có khối lượng" (bản gốc mất chữ "đá").
- Không có câu hỏi chứa từ phủ định cần in đậm.

## Hình
- 8 hình vẽ lại bằng TikZ (I.16 gồm 4 biển cảnh báo ở 4 phương án): I.2 máy dò cá, I.10 dynamo xe đạp, I.14 bàn tay trái, I.16 biển cảnh báo, II.1 thí nghiệm ống thủy tinh – giọt thủy ngân, II.2 bộ sạc điện thoại, II.3 máy phát điện, III.3 súng điện từ.
- I.14: ba mũi tên (1), (2), (3) vẽ cùng màu đen (bản gốc tô (2) đỏ, (3) xanh lá — trùng màu quy ước dòng điện/từ trường, lộ đáp án).
- I.2: chùm sóng vẽ nét đứt xám như gốc (không tô màu sóng để khỏi gợi ý loại sóng).
- II.3: cực S xanh, N đỏ (đề ghi tên cực).

## Vẽ lại hình thực tiễn (PHIÊN FABLE 14/11/2026)
Ảnh gốc: `word/media/` của file Word (I.2 = image5, I.10 = image45, I.14 = image59, I.16 = image64–67 ghép ngang, II.1 = image68, II.2 = image82, II.3 = image92, III.3 = image113). Các hình vẽ theo tọa độ điểm ảnh của ảnh gốc (`x=...cm, y=-...cm`). Nội dung vật lí (chiều mũi tên, cực nam châm, nhãn, số liệu) giữ như bản trước.
- I.2 (máy dò cá): vẽ lại tàu (thân cong có bóng, ca bin, cột ăng ten, người điều khiển, màn hình có vệt cá và đáy biển), đầu dò, chùm sóng nét đứt, đàn cá 9 con có đuôi, mắt, mang; mặt nước gợn sóng, đáy biển có chấm cát.
- I.10 (dynamo xe đạp): vẽ lại bánh xe (lốp, vành, nan hoa đan chéo), càng xe đỏ có đai kẹp, đèn xe, dây điện quấn theo càng, dynamo dạng chai (núm khía tì vào lốp, thân xám, đáy cam); hình cắt: vỏ chai trong, núm xoay khía, trục, nam châm trụ hai nửa, lõi chữ U, cuộn dây, bóng đèn có đui, hai dây nối, mũi tên chiều quay. Bốn đường gióng không có chữ của ảnh gốc (nhãn bị cắt mất) không vẽ.
- I.14 (bàn tay trái): vẽ lại bàn tay ngửa bằng đường cong (ngón cái choãi, bốn ngón duỗi, kẽ ngón, đốt ngón, chỉ tay) — macro mới `\VLbantaytrai`; ba mũi tên (1), (2), (3) vẫn cùng màu đen.
- I.16 (4 biển cảnh báo): kí hiệu vẽ bằng bộ macro `\VLkh...` mới (bề mặt nóng, phóng xạ, chất nổ, sóng tắt dần có mũi tên), khung bằng `\VLbiencanhbao` cỡ 1,2.
- II.1 (thí nghiệm ống thủy tinh – giọt thủy ngân): vẽ lại cốc thủy tinh có vành, nước có elip mặt thoáng; ống thủy tinh có vạch chia và giọt thủy ngân; đũa khuấy; nhiệt kế; giá đỡ (đế, trụ, hai thanh ngang, khớp nối có vít, kẹp); kiềng bốn chân có mặt lưới; đèn khí (đế, cổ đồng, van) và ngọn lửa.
- II.2 (bộ sạc điện thoại): vẽ lại điện thoại nằm nghiêng (thân, màn hình, nút bên, loa), bộ sạc mở vỏ (chân cắm, thân, bảng mạch, ba cuộn cảm, máy biến áp nhỏ, tụ, chip, cổng USB), đầu cắm và dây cáp; kính lúp phóng to máy biến áp (lõi, hai cuộn dây quấn, đế, dây ra, chân hàn), mũi tên hai chiều.
- II.3 (máy phát điện): vẽ lại theo đúng bố cục ảnh gốc: nam châm S (mặt trên, mặt cực lõm có gạch bóng) và N, khung dây ABCD có hai đầu dây bẻ bậc về cổ góp, cổ góp hai nửa vành khuyên có bề dày, hai chổi quét, trục OO′ (chỉ vẽ phần ngoài khung như gốc), dây nối, bóng đèn trên đế chóp; chiều quay giữ như bản trước.
- III.3 (súng điện từ): vẽ lại bệ hai tầng (khối đế có rãnh, tấm đế có hốc chữ nhật, miếng đệm), hai thanh ray tròn trên gờ, đầu kẹp dây, thanh kim loại màu đồng có bề dày và mũi tên dòng điện, nguồn điện (màn hình, hai núm, hai lỗ cắm), hai dây nối cong, mũi tên $I$, 8 đường sức từ đúng vị trí ảnh gốc.

Macro mới khai báo trong file đề (đề xuất chuyển vào `preamble-vatli-hinh.tex`): `\VLbiencanhbao{x}{y}{cỡ}{\VLkh...}`, `\VLkhphongxa`, `\VLkhtiaset`, `\VLkhsinhhoc`, `\VLkhchamthan`, `\VLkhdaulau`, `\VLkhbematnong`, `\VLkhchatno`, `\VLkhsongtatdan`, `\VLkhraochan`, `\VLkhlyvo`, `\VLkhanmon`, `\VLkhbinhchuachay`, `\VLkhnguoichay`, `\VLkhphongxaiso` (đều `{x}{y}{cỡ}`), `\VLbantaytrai{x}{y}{tỉ lệ}`.

Hình chưa ưng: II.2 các linh kiện nhỏ trên bảng mạch vẽ giản lược (ảnh gốc là nét vẽ dày đặc chi tiết); II.3 chỗ đầu dây khung nối vào cổ góp và hai chổi quét vẽ gọn hơn ảnh gốc. Bản đề 7 trang (ĐẠT), bản lời giải 10 trang.
