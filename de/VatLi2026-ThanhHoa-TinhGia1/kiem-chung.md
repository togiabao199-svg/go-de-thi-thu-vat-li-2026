# Kiểm chứng đáp án – VatLi2026-ThanhHoa-TinhGia1

Đề gốc (PDF SieuGioi, Trường THPT Tĩnh Gia I – Sở GD&ĐT Thanh Hóa, mã 0223) không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python. Đề gốc không có khối "Cho biết"; lời giải dùng N_A = 6,02·10²³ mol⁻¹, 1 amu = 931,5 MeV/c², 1 MeV = 1,6·10⁻¹³ J.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | D A D A D A A D D D B A C D D A A A | I.1: J/(kg·K) = m²/(s²·K) ⇒ b: m²/(s²·K⁴); I.4: B từ N sang S, dòng điện đoạn giữa hai cực chạy từ sau ra trước (theo chiều I trên hai cạnh ngang) ⇒ F hướng lên (A); I.5: t_Y = 32 + 1,8 t_X ⇒ 20 °X; I.9: B hướng vào (dấu ×), hạt dương lệch trái ⇒ hạt 1 là β⁺, r₁ < r₂ ⇒ động năng β⁺ nhỏ hơn; I.11: E × B cùng hướng truyền (lên), B hướng Nam ⇒ E hướng Tây; I.12: 70·3480·5/334000 = 3,647 kg; I.18: ω = 5π, Φ₀ = √(16 + 9) = 5 Wb |
| II.1 | không có | S Đ Đ S | (1)→(2) trên đường qua O (đẳng tích) ⇒ T₂ = 290·1,8 = 522 K; hình bình hành ⇒ T₃ = 870 + 232 = 1102 K; V₃ = 400·1102/(1,8·290) = 844,4 cm³ (1200 cm³ là V₄); (3)→(4) song song (1)→(2) nên không qua O, không đẳng tích |
| II.2 | không có | Đ Đ S S | λ = 5,626·10⁻⁷ s⁻¹; N_lá = 6,061·10¹⁸; N₀ = 0,215/32·6,02·10²³ = 4,045·10²¹ ⇒ 0,1499 % ≈ 0,15 % (bỏ qua phân rã từ lúc tưới đến lúc đo, đề không cho khoảng thời gian này); H(1,5 ngày) = 3,17·10¹² Bq (đề ghi 2,17·10¹⁰); số electron phóng ra trong 1,5 ngày = 4,26·10¹⁷ (đề ghi 3,17·10¹²) |
| **II.3** | không có | **S S S S** | C = 1,26·896 + 0,18·385 = 1198,26 J/K. a) định nghĩa thiếu "1 kg". **b)** 30 → 100 °C: 83 878,2 J; con số 95 860,8 J của đề ứng với 20 → 100 °C. **c)** c = 1198,26/1,44 = 832,125 J/(kg.K), đề ghi đơn vị J/(g.K). d) nhôm: 1,26·896·640 + 1,26·390 000 = 1 213 934,4 J; 1 258 286,4 J là tính cả phần đồng nóng lên (thêm 0,18·385·640 = 44 352 J). **Bốn ý đều Sai; b) và c) có thể là lỗi gõ của đề gốc (nếu sửa "30 °C" thành "20 °C" thì b) Đúng, nếu đơn vị là J/(kg.K) thì c) Đúng). File gõ đúng chữ bản gốc, ghi `% KIỂM TRA` — thầy xem.** |
| II.4 | không có | S Đ S Đ | Δt = 0,1/1,5 = 0,067 s; e = 500·5·10⁻³·0,1·1,5 = 0,375 V; I = 0,125 A; từ thông hướng vào tăng ⇒ dòng ngược chiều kim đồng hồ: A → B → C → D → A (kiểm thêm: v × B trên cạnh CB hướng từ B lên C) |
| III.1–III.6 | không có | 1,7 / 0,66 / 16 / 1,9 / 8 / 420 | III.1: lưới 10/3 ms một ô, I₀ = 2 A, T = 20 ms, i(0) = −1 A đang tăng ⇒ đổi chiều lần đầu tại T/12 = 1,667 ms; III.2: I = 12/12 = 1 A, t = 0,2·10⁻³·130·299,5/11,75 = 0,6627 s; III.3: Δm = 0,2313 amu ⇒ 215,46 MeV/phân hạch; E = 550·10⁶·25·365·86400/0,3 = 1,445·10¹⁸ J; N = 4,19·10²⁸; m = 16 340 kg ≈ 16 tấn (dùng 235 g/mol cũng ra 16 345 kg); III.4: 8400 − 7440 = 960 J; t = 960/504 = 1,905 °C; III.5: T_H₂/T_O₂ = 1/2, (1/2)·(32/2) = 8; III.6: T₁ = 300/0,9 = 333,3 K; 50p = 0,9·10⁵·40·5/3 + 10⁶ ⇒ p = 1,4·10⁵ Pa; p/T₁ = 420 Pa/K |

## Điểm cần thầy xem

- **II.3 (b, c)**: như bảng trên; nếu thầy coi là lỗi gõ thì sửa lời đề ("20 °C", "J/(kg.K)") và đổi `\True` cho b), c).
- **II.1 d)**: đề gốc ghi "Quá trình (1) → (3) và quá trình (3) → (4)"; (1) → (3) không phải một quá trình của chu trình, sửa thành "(1) → (2)". Kết luận Sai không đổi (dù đọc theo cách nào).
- **II.2 b)**: đề không cho thời gian từ lúc tưới đến lúc đo; lời giải so trực tiếp số hạt trong lá với số hạt ban đầu (bỏ qua phân rã) ⇒ 0,15 %, Đúng.
- **III.2**: đề gốc ghi "mắc cầu chì vào một mạch điện như hình vẽ" nhưng bản PDF không có hình. Hình tự dựng: nguồn (E, r), khóa K, cầu chì mắc nối tiếp (đoản mạch: cầu chì là điện trở ngoài duy nhất, khớp số liệu R + r = 12 Ω).
- **I.9**: câu dùng lực Lorentz và bán kính quỹ đạo r = mv/(|q|B) (ngoài chương trình 2018); đã phóng to ảnh trang xác nhận dấu "×" và chiều cong hai vết.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi, dòng họ tên ("Siêu Giỏi"), số báo danh, mã đề, chân trang quảng cáo. Tên đơn vị theo tiêu đề gốc ("Sở GD&ĐT Thanh Hóa – Trường Tĩnh Gia I"), không ghi lần.
- Thứ tự ý II.1: bản gốc in ngược d), c), b), a); gõ lại theo thứ tự a) → d) (nội dung từng ý giữ nguyên chữ cái).
- I.4: "hình vẽ dưới đây" → "hình bên" (hình đặt bên phải phương án).
- I.5: "thang độ X" → "thang đo X"; "68∘ Y" → "68 °Y".
- I.6 A: "tăng thêm 1 độ K" → "tăng thêm 1 K".
- I.7: "Năng lượng liên kết của ²⁰₁₀Ne và 160,64 MeV" → "… là 160,64 MeV"; "MeV/ nucleon" → "MeV/nucleon".
- I.12: "3480 J/kg. K" → "3480 J/(kg.K)"; "334.10³" → "334·10³".
- I.13: "piston" → "pit-tông"; dấu "." cuối câu hỏi → "?".
- I.14: thêm dấu phẩy "Khi nói về sóng điện từ, phát biểu…"; "3.10⁸" → "3·10⁸".
- I.15: "hypebol" → "hyperbol".
- I.18: "vuông góc với trục xx" → "trục xx′"; "15π( V)" → "15π V".
- II.2: "215mg" → "215 mg"; "3, 17.10¹²" → "3,17·10¹²".
- II.3: đơn vị bảng "J/kg. K" → "J/(kg.K)"; số lớn tách nhóm (95 860,8; 1 258 286,4); d) "người thu lấy" → "người ta thu lấy".
- II.4: "3Ω" → "3 Ω"; "5. 10⁻³" → "5·10⁻³"; "suất hiện" → "xuất hiện"; "(Hình vẽ)" → "(hình vẽ)".
- III.1: gộp câu hỏi và ngoặc làm tròn: "…vào thời điểm nào (tính theo đơn vị ms, kết quả làm tròn đến chữ số hàng phần mười)?".
- III.2: thêm "đạt" ("bị đứt ngay sau khi đạt nhiệt độ nóng chảy"); "27, 5 °C" → "27,5 °C"; "J/kg.K" → "J/(kg.K)"; ngoặc làm tròn đưa vào trước dấu "?".
- III.3: "nơtron" → "neutron", "êlectron" → "electron"; "hấp thu" → "hấp thụ"; kí hiệu ⁹⁵₉₂Mo của bản gốc sai số hiệu nguyên tử → ⁹⁵₄₂Mo (molybdenum Z = 42, khớp bảo toàn điện tích 92 = 42 + 57 − 7); ngoặc làm tròn đưa vào trước dấu "?".
- III.4: "làm tròn đến chữ số phần mười" → "(kết quả làm tròn đến chữ số hàng phần mười)".
- III.6: "V₂ = 10dm²" → "10 dm³"; "pa" → "Pa"; "khóa k" → "khóa K"; "p₁ ≥ p₂ + 10⁵Pa, p₁ là…; p₂ là…" → dấu phẩy thống nhất.

## Đánh số lại câu

Đề gốc đã đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6); giữ nguyên.

## Hình

11 hình, vẽ lại bằng TikZ, so hình trong `so-hinh/`:
- I.4 nam châm chữ U + khung dây có nguồn (hình thực tiễn, `% giuhinh`, N đỏ, S xanh như gốc; hướng A, B, C, D đen để không gợi ý), I.5 đồ thị t_Y – t_X, I.9 vết hạt β trong từ trường, I.17 bình cầu – ống ngang – giọt thủy ngân (bốn hình đặt bên phải phương án).
- II.1 đồ thị p – T chu trình hình bình hành; II.2 cây con trên đất (ảnh chụp, vẽ giản lược, chờ phiên vẽ lại); II.3 chảo (ảnh chụp, đặt cạnh bảng số liệu); II.4 khung dây và vùng từ trường.
- III.1 đồ thị i(t) (lưới 10/3 ms × 1 A như gốc); III.2 mạch cầu chì (tự dựng, đề gốc không có hình); III.6 hai bình thông nhau có khóa.

## Vẽ lại hình thực tiễn (PHIÊN FABLE 14/11/2026)

Ảnh gốc lấy bằng `pdfimages` (10 ảnh nhúng của PDF), so hình: `python3 tools/so_hinh.py de/VatLi2026-ThanhHoa-TinhGia1/VatLi2026-ThanhHoa-TinhGia1.tex <thư mục ảnh> "I.4=g-000.png,I.5=g-001.png,I.9=g-002.png,I.17=g-003.png,II.1=g-004.png,II.2=g-006.png,II.3=g-007.png,II.4=g-005.png,III.1=g-008.png,III.6=g-009.png"` (III.2 không có ảnh gốc: hình tự dựng).

- **I.4** (`so-hinh/01-cau-I-4.png`): vẽ lại nam châm chữ U dạng khối nhìn xiên đúng góc nhìn ảnh gốc (mặt trước, mặt bên ngoài cực N, mặt trong cực S, mặt đáy trong, hai đầu cực có mũ màu: N đỏ cam, S xanh đậm; đường chia hai nửa N – S ở đáy chữ U; vệt sáng dọc hai nhánh); khung dây hình bình hành, nguồn điện, hai mũi tên dòng điện $I$, bốn hướng A, B, C, D giữ đúng vị trí và chiều như hình cũ (nội dung vật lí không đổi).
- **II.2** (`so-hinh/06-cau-II-2.png`): vẽ lại cảnh cây con trong chậu sát ảnh gốc: nền đất có hạt giá thể lốm đốm (ba lớp hạt ngẫu nhiên, hạt xa nhỏ dần), nền tối phía sau, vành chậu nhựa trong, 5 cây con đúng vị trí ảnh (cụm lá lớn sát mép trái, cây giữa thân dài một lá mầm lớn còn dính vỏ hạt, cây hai lá bên phải, cây nhỏ phía dưới, cụm ba lá góc phải dưới), thân nhạt có lông tơ, lá tô chuyển màu có gân giữa và bóng đổ. Macro riêng của đề: `\TGla`, `\TGthan`, `\TGhatdat`.
- **II.3** (`so-hinh/07-cau-II-3.png`): vẽ lại chiếc chảo đúng góc nhìn ảnh gốc: thân nhôm xám tô khối (vệt sáng, gờ đáy), vành chảo, lòng chảo phủ đá đen lốm đốm có đáy chảo và vệt sáng, tay cầm đen cong có lỗ treo, tai nối kim loại, bóng đổ.
- Giữ nguyên (sơ đồ, đồ thị, mạch): I.5, I.9, I.17, II.1, II.4, III.1, III.2 (mạch cầu chì tự dựng do đề gốc thiếu hình), III.6.
- Hình chưa ưng: không có hình nào chưa đạt; II.2 là ảnh chụp mờ nên lá, đất vẽ theo kiểu minh họa (không thể giống hệt từng hạt đất).
- Dàn trang: bản đề 7 trang (ĐẠT), bản lời giải 12 trang (như trước khi vẽ lại).

## Chốt đáp án (thầy duyệt 14/11/2026)

- Các điểm còn lại ở `kho/KIEM-DAP-AN-V2.md` — I.2 (A), II.3 (S S S S theo chữ in), III.2 (0,66, mạch tự dựng): giữ như file, thầy chốt 14/11/2026. Các `% KIỂM TRA` khác giữ nguyên.
