# Kiểm chứng đáp án – VatLi2026-Hue-PhanDangLuu-Lan1

Đề gốc (PDF SieuGioi, THPT Phan Đăng Lưu – Sở GD&ĐT Huế, lần 1, năm học 2025 – 2026) không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | A D A A A C A C B C C B D B A C C B | I.3: t = 52·100/104 = 50 °C; I.5: 10⁵·(0,4 + 2·0,12)/0,4 = 1,6·10⁵ Pa; I.11: b = 0,5·0,4/1 = 0,2; I.12: c = (0,4·4180 + 0,1·380)·9/(0,25·84) = 732,86 J/(kg.K) ≈ 0,733 J/(g.K); I.18: V₂ = 15·300/450 = 10 cm³ |
| II.1 | không có | Đ Đ Đ S | Q = 50·380·1057 + 50·180000 = 29,083 MJ; than = 29,083/(0,6·30) = 1,62 kg (đề ghi 24,25 kg) |
| II.2 | không có | S Đ S S | **n = 3·10⁵·1,5·10⁻³/(8,31·303) = 0,1787 mol ≈ 0,18 (đề ghi "xấp xỉ 0,17")**; V₂ = 4,5 L; (2)→(3) T tăng 3 lần; T₅ = 303·1,5 = 454,5 K (đề ghi 1090,5 K) |
| II.3 | không có | S Đ S Đ | đồ thị: ô 10 s × 10 °C, qua (0; 20) và (50; 30) ⇒ 0,2 °C/s; P = 0,2·400·0,2 = 16 W ⇒ 144R = 16(R + 2)² ⇒ R = 1 Ω hoặc 4 Ω; t(60 s) = 32 °C |
| II.4 | không có | Đ Đ Đ Đ | (1)→(2) cùng T, V 2,4 → 7,2 L: giãn đẳng nhiệt; p₁ = 3,6·7,2/2,4 = 10,8 atm |
| III.1–III.6 | không có | 20 / 10 / 4 / 20,7 / 6,6 / 1,2 | III.1: ΔV = π·1,25²·30 = 147,26 cm³; N = 58,6·5000/(100·147,26) = 19,9 ⇒ 20; III.3: 2CΔt₁ = 75k, CΔt₂ = 15k, CΔt₃ = 60k ⇒ 4; III.4: (1,29·273/300 − 1,29·273/340)·0,15 = 20,72 g; III.5: h = 74/[(440·1510 + 270000)·7800·π·0,7²·10⁻⁶] = 6,596 mm; III.6: pV = 20V − 0,5V², max 200, min 150 ⇒ √(4/3) = 1,155 |

## Điểm cần thầy xem (`% KIỂM TRA` trong file)

- **I.16**: phương án A "Các chất được cấu tạo từ các hạt riêng biệt gọi là phân tử" cũng là nguyên văn một ý của mô hình động học phân tử trong SGK, nên đề có hai phương án đúng. Gõ đáp án C (chuyển động hỗn loạn không ngừng); thầy quyết giữ C hay sửa lời phương án A.
- **II.2 a)**: n = 0,1787 mol; làm tròn hai chữ số là 0,18, đề ghi "xấp xỉ bằng 0,17 mol" → gõ **Sai**. Nếu người ra đề cắt bớt chữ số (0,17) thì ý này là Đúng.
- **III.2**: đề không cho công khí sinh ra khi pit-tông tự trở về vị trí ban đầu (và lời đề tự mâu thuẫn: pit-tông nhẹ, khí trở về đúng thể tích ban đầu ở áp suất khí quyển thì nội năng phải như cũ). Gõ theo cách hiểu hợp lý nhất của người ra đề: khí trả lại công 5 J ⇒ ΔU = 10 + 5 − 5 = **10 J**. Nếu chỉ xét giai đoạn nhận nhiệt và công: 15 J.
- **III.1**: "áp suất 58,6 kPa" hiểu là áp suất dư (áp suất tiêu chuẩn của bóng rổ), bóng xẹp ban đầu chứa 5 lít khí ở áp suất khí quyển: N = 19,9 ⇒ 20 lần. Cách hiểu 58,6 kPa là áp suất tuyệt đối và bóng ban đầu không có khí cũng ra 19,9 ⇒ 20; chỉ cách hiểu "áp suất dư + bóng rỗng" mới ra 54. Đáp số nguyên (số lần bơm), không cần yêu cầu làm tròn.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi, dòng họ tên / số báo danh, "ĐỀ THI CHÍNH THỨC", "(Đề thi gồm 08 trang)", dòng quảng cáo chân trang, "----HẾT----".
- Đơn vị nhiệt dung riêng thống nhất "J/(kg.K)" (bản gốc lẫn "J/kg.K" và "J/(kg.K)"): I.4 (cả phương án "J/(mol.kg)"), I.12, II.1, II.3; R: "J/(mol.K)".
- I.5: thêm dấu phẩy sau "lọ thuốc kín"; "như hình vẽ, một chai thuốc" → "như hình bên. Một chai thuốc" (hình đặt bên phải phương án); bỏ ngoặc đơn vị "0,9 (ml)", "10⁵ (Pa)"… → "0,9 ml", "10⁵ Pa".
- I.6: "thì thu được với bốn đường đẳng áp" → "thì thu được bốn đường đẳng áp" (chữ thừa).
- I.8: "Boltzman" → "Boltzmann"; kí hiệu "E_d" → $\overline{E}_{\text{đ}}$.
- I.11: "sự phụ thuộc của áp suất theo thể tích" → "sự phụ thuộc của thể tích theo áp suất" (đúng với đồ thị V theo p của hình). Hình: nhãn trục "V (m¹)" (lỗi in) → "V (m³)".
- I.13: "hệ p − T" → "hệ pOT".
- II.2: "hypebol" → "hyperbol". II.4 a): "Hypebol" → "hyperbol"; b): "biến đổi thông qua định luật Boyle" → "biến đổi theo định luật Boyle".
- II.3: suất điện động "E" → $\mathcal{E}$ (cả trên hình).
- III.1: "58,6kPa" → "58,6 kPa"; "V_bong" → $V_{\text{bóng}}$.
- III.2: "piston" → "pit-tông" (thuật ngữ SGK 2018); "bao nhiêu Jun" → "bao nhiêu J"; bỏ ngoặc đơn vị "10 (J)".
- III.4: "P₀" → "p₀"; "(Kết quả làm tròn đến 1 số thập phân)" → "(kết quả làm tròn đến chữ số hàng phần mười)", đặt trước dấu "?".
- III.5: "Laze" → "laser"; "milimet (mm)" → "milimét"; "(Kết quả làm tròn đến 1 số thập phân)" → "(kết quả làm tròn đến chữ số hàng phần mười)"; "25 °C" viết đứng.
- III.6: "khí H₂" → "khí hydrogen (H₂)" (tên IUPAC theo SGK mới); "(Kết quả làm tròn kết quả đến…)" → bỏ chữ "kết quả" lặp; bỏ ngoặc đơn vị "(lít)", "(atm)".
- Các phương án Phần I bỏ dấu chấm cuối theo quy ước ex_test.

## Đánh số lại câu

Đề gốc đánh số liên tục 1–28. File gõ đánh số lại theo từng phần: Phần I câu 1–18 (gốc 1–18), Phần II câu 1–4 (gốc 19–22), Phần III câu 1–6 (gốc 23–28). Đề không có tham chiếu chéo giữa các câu.

## Hình

15 hình gốc + bảng (I.1, gõ `tabular`) → 16 `tikzpicture` (II.3 có mạch điện và đồ thị). Ảnh so ở `so-hinh/`, ảnh gốc cắt từ ảnh trang 150 dpi (tỉ lệ khổ trang): I.5 tr.2 `0.46:0.065:0.55:0.2`; I.6 tr.2 `0.38:0.283:0.63:0.425`; I.9 tr.2 `0.33:0.665:0.68:0.857`; I.11 tr.3 `0.28:0.163:0.72:0.35`; I.13 tr.3 `0.37:0.563:0.64:0.705`; I.17 tr.4 `0.43:0.186:0.575:0.327`; II.1 tr.4 `0.37:0.702:0.645:0.835`; II.2 tr.5 `0.325:0.343:0.685:0.48`; II.3 tr.5 `0.295:0.717:0.72:0.843`; II.4 tr.6 `0.31:0.144:0.7:0.303`; III.1 tr.6 `0.435:0.54:0.575:0.668`; III.3 tr.7 `0.4:0.14:0.61:0.275`; III.4 tr.7 `0.41:0.508:0.6:0.643`; III.5 tr.8 `0.355:0.066:0.656:0.195`; III.6 tr.8 `0.35:0.326:0.665:0.497`.

- Hình thực tiễn (chờ phiên vẽ lại chi tiết): I.17 nhiệt kế hồng ngoại — màn hình để trống (số 36,8 / 29 / 35 trên ảnh không phải dữ kiện); II.1 ảnh thợ chạm khắc bình đồng → vẽ quả chuông đồng có hoa văn và bàn tay cầm đục (lược người thợ, nền xưởng); III.1 ảnh học sinh bơm bóng → vẽ bơm tay nối dây vào quả bóng rổ (lược người, sân bóng); III.4 đèn trời → vẽ đèn trời phát sáng có khung dây, ngọn lửa (lược nền trời đêm, bàn tay thả đèn); III.5 đầu cắt laser trên tấm thép có lỗ cắt, tia lửa (lược máy phía sau).
- II.1: hình đặt bên phải danh sách 6 bước (minipage), câu có `% tachDS` để câu dẫn ở trang 4, bảng ở trang 5.
- I.5: hình đặt bên phải phương án (minipage), lời đề sửa "như hình vẽ" → "như hình bên".

## Vẽ lại hình thực tiễn (PHIÊN FABLE 14/11/2026)

Các hình vẽ theo toạ độ điểm ảnh của ảnh gốc (`x=…cm, y=−…cm`), mỗi cảnh cắt trong khung bo góc. Màu riêng của đề (`PDLda…`, `PDLvang`, `PDLnau…`, `PDLdoao…`, `PDLthau…`) khai báo giữa `\input{preamble-vatli-hinh}` và `\begin{document}`. Sơ đồ, đồ thị, mạch điện (I.6, I.9, I.11, I.13, II.2, II.3, II.4, III.3, III.6) giữ nguyên.

- **I.5** (`01-cau-I-5.png`): vẽ lại lọ thuốc úp ngược (vai lọ vát, thuốc có chấm, nút cao su) và ống tiêm đúng dáng hình gốc (vai ống rộng, đầu gắn kim hình vòm, thân ống dài, pit-tông đen ở cuối thân, cán hai nét, đế ấn). Bố cục: câu đầu của lời đề để nguyên dòng, phần lời còn lại + 4 phương án đặt trong `minipage` 0,84 `\linewidth`, hình bên phải (0,14 `\linewidth`) — lời đề không đổi; nhờ vậy hình cao 3,3 cm mà câu vẫn nằm trọn trang 1.
- **I.17** (`06-cau-I-17.png`): nhiệt kế hồng ngoại đúng góc nhìn nghiêng của ảnh (mặt trước cong, mặt bên, đầu đo nhô ra sau, viền màn hình dày phía trên, ba nút M / = / −, nút SCAN, biểu tượng pin). Màn hình để trống (36,8 / 29 / 35 không phải dữ kiện).
- **II.1** (`07-cau-II-1.png`): dựng lại cả cảnh người thợ chạm bình đồng: bình đồng lớn (miệng tối, cổ chạm chìm, dải chữ triện, thân đắp nổi, quai đầu rồng), bàn tay trái chỉ ngón trỏ vào bình, tay phải cầm đục, đầu người thợ nhìn nghiêng (tóc, tai, áo đỏ), nền xưởng (người thợ phía sau, bình thứ hai, bạt xanh, bàn ghế). Thay hình "quả chuông + bàn tay" cũ.
- **III.1** (`12-cau-III-1.png`): dựng lại cảnh học sinh bơm bóng: học sinh áo trắng, cà vạt sọc, quai ba lô, tay phải nắm tay bơm chữ T, thân bơm đen chéo xuống, tay trái giữ đầu bơm trên quả bóng rổ, quần jean, nền sân bóng (bảng rổ, hàng cây, người ở xa).
- **III.4** (`14-cau-III-4.png`): đèn trời nhìn từ dưới lên như ảnh: thân giấy phồng, vành miệng elip, mặt trong, hai dây chéo đỡ bấc, ngọn lửa, các bàn tay giữ đèn, trời đêm có các đèn ở xa.
- **III.5** (`15-cau-III-5.png`): đầu cắt laser đúng các tầng của ảnh (thân đồng thau, vòng đai thép, tầng giữa có núm tròn, tai kẹp, ốc tai hồng, thân dưới, bép đồng đỏ), tia lửa tại điểm cắt và vệt phản chiếu, tấm thép tối với các lỗ tròn đã cắt (mép bắt sáng), khối máy và bó dây phía sau.

Hình chưa thật ưng:
- II.1: hoa văn đắp nổi trên thân bình và quai đầu rồng chỉ vẽ cách điệu (ảnh gốc 413 × 273 điểm ảnh, mờ, không đọc được hình chạm cụ thể); gương mặt người thợ vẽ kiểu minh hoạ phẳng.
- III.1: gương mặt học sinh vẽ kiểu minh hoạ phẳng (ảnh gốc 243 × 350 điểm ảnh).

Dàn trang sau khi vẽ lại: bản đề 8 trang (ĐẠT), bản lời giải 12 trang (trang 11 trống 7,5 cm, trong giới hạn 1/3).

## Chốt đáp án (thầy duyệt 14/11/2026)

- **I.16: C → A.** Lời giải ghi thêm: phương án C (các phân tử chuyển động hỗn loạn không ngừng) cũng là một nội dung của mô hình động học phân tử trong SGK — đề có hai phương án đúng. Giữ `% KIỂM TRA` cho câu này (sửa lời ghi chú theo đáp án A).
- **II.2 a): sửa lời đề "xấp xỉ bằng 0,17 mol" thành "0,18 mol"; Sai → Đúng** (n = 3·10⁵·1,5·10⁻³/(8,31·303) ≈ 0,179 mol). Câu II.2 thành Đ Đ S S. Viết lại lời giải ý a, bỏ `% KIỂM TRA` của ý này.
- Các điểm còn lại ở `kho/KIEM-DAP-AN-V2.md` — III.1 (20), III.2 (10): giữ như file, thầy chốt 14/11/2026. Các `% KIỂM TRA` khác giữ nguyên.
