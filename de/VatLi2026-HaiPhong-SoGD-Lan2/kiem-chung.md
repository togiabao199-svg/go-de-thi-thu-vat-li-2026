# Kiểm chứng đáp án – VatLi2026-HaiPhong-SoGD-Lan2

Nguồn: `kho/goc/Hai Phong - So GDDT - Lan 2.docx` (Sở GD&ĐT Hải Phòng, đề khảo sát lần 2, mã đề 0201), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | B B A A D B A C C D D D C A B D A A | trùng | I.4: 6000/6500 = 0,923 atm; I.5: E, B, v tam diện thuận, v Bắc → Nam, B lên ⇒ E tây → đông; I.9: 1,8·2,5·10⁻³·2·10⁻³ = 9·10⁻⁶ N; I.18: 310·0,02·5·10⁻⁴·2·3,14·440 = 8,57 V |
| II.1 | Đ S Đ S | trùng | e = 3 V, I = 0,5 A, P_R = 1,25 W; T = 560 K; Q = 100 + 100 = 200 J, τ = 160 s; từ 160 s đến 200 s thêm 50 J ⇒ ΔT' = 140 K, T' = 700 K, p' = 10⁵·700/560 = 1,25·10⁵ Pa. **Xem ghi chú dữ kiện dưới.** |
| II.2 | Đ S Đ S | trùng | c) 0,035·1800·5 + 0,035·3,4·10⁵ = 315 + 11 900 = 12 215 J. **Xem ghi chú cách hiểu ý c dưới.** |
| II.3 | Đ S Đ S | trùng | c) v = 0,22·10⁻³/(0,04·0,02) = 0,275 m/s; Q = 0,275·3,14·0,02²/4 = 86,35 ml/s ≈ 86,4 (π thật: 86,39) |
| II.4 | Đ S S Đ | trùng | N₀ = 2,782·10²⁵; λ = 2,506·10⁻¹⁰ s⁻¹; P₀ = 6,24 kW; P(12 năm) = 5,67 kW |
| III.1–III.6 | 159 / 354 / 6,4 / 6,5 / 200 / 189 | trùng | xem phép tính dưới |

## Phép tính chính (Python)
- III.1: T = √(0,196² + 0,25²)/2 = 0,1588 N → 159 mN.
- III.2: Δm = (25 − 8) − (8 − 5) = 14 g; λ = 30·165/0,014 = 353 571 J/kg → 354 kJ/kg.
- III.3: I = BrSσ/ρ · t/(2 + σt²), cực đại khi σt² = 2 ⇒ σ = 50 rad/s²; I_max = 0,15·0,24·1,2·10⁻⁶·50/1,7·10⁻⁸ · 0,2/4 = 6,353 A → 6,4.
- III.4: t₅ = 5·2^(28/73,8) = 6,504 phút → 6,5.
- III.5: S = 3·10⁻³ m²; Δp = 10⁵·(2 − 2/3) = 1,333·10⁵ Pa; ΔpS = 400 N = mω²r ⇒ ω = 200 rad/s.
- III.6: V₂ = 30·10·219/300 = 219 m³ ⇒ ΔV = 189 m³.

## Ghi chú dữ kiện (đã ghi `% KIỂM TRA` trong file đề)
- **II.1:** đề cho nội năng tăng 100 J khi khí giãn đẳng áp từ 280 K lên 560 K. Với n = p₀V₀/(RT₀) = 0,043 mol, khí lí tưởng đơn nguyên tử có ΔU = 1,5·nRΔT = 150 J (lưỡng nguyên tử 250 J), nên 100 J không khớp mô hình khí lí tưởng. Các ý vẫn tính theo số liệu đề cho (ΔU tỉ lệ ΔT, 100 J ứng với 280 K) như lời giải gốc; đáp án không đổi.
- **II.2 c):** câu chữ "Nhiệt lượng cần cung cấp cho một viên nước đá nóng chảy hoàn toàn ở nhiệt độ nóng chảy 0 °C là 12 215 J" hiểu là làm viên đá từ −5 °C nóng lên 0 °C rồi nóng chảy hết (12 215 J, Đúng, như đáp án gốc). Nếu hiểu chỉ phần nóng chảy ở 0 °C thì 11 900 J (Sai). Giữ Đúng theo đáp án gốc; thầy xem có cần sửa lời ý c.

## Sửa lời đề (lỗi chữ bản gốc)
- Cho biết: "R = 8,31; J.mol⁻¹" → "R = 8,31 J·mol⁻¹·K⁻¹" (thiếu K⁻¹, có dấu ";" thừa); viết "1 eV = 1,6·10⁻¹⁹ J"; "Các phép tính KHÔNG làm tròn…" → "Không làm tròn kết quả các phép tính trung gian." (theo khung chung).
- I.5: "véc tơ" → "vectơ"; "Rađa" → "rađa".
- I.6: "chất phóng xạ $X$" → X đứng (tên hạt nhân); "Ban đầu $(t=0)$" giữ.
- I.10: kí hiệu hạt nhân ở phương án bản gốc vỡ ("82^206 Pb", "92^238 U"…) → gõ đúng ²⁰⁶₈₂Pb, ²³⁸₉₂U, ⁴₂He, ⁶³₂₉Cu; câu dẫn bỏ dấu ";" thừa giữa các hạt nhân; "đơn giản hoá" → "đơn giản hóa".
- I.11: "56neutron" → "56 neutron" (thêm cách).
- I.13: "toả" → "tỏa"; từ "sai" đã in đậm sẵn.
- I.17: "kỹ thuật" → "kĩ thuật", "mẫu gỗ" → "mẩu gỗ"; câu dẫn bỏ dấu chấm cuối "là quá trình."; phương án "toả" → "tỏa".
- I.18: bỏ dấu hai chấm cuối câu dẫn "có độ lớn bằng:".
- II.1: "piston" → "pit-tông" (thuật ngữ SGK, cả nhãn hình "Piston" → "Pit-tông", "Khí lý tưởng" → "Khí lí tưởng"); ý a) "$P'$" → "$p'$" (kí hiệu áp suất).
- II.3: "$U=B.v.d$" → "$U=Bvd$"; gộp hai dòng câu dẫn.
- II.4: kí hiệu "94^238 Pu", "90^232 Th" vỡ → ²³⁸₉₄Pu, ²³²₉₀Th; "tỷ năm" → "tỉ năm"; bỏ in nghiêng lẫn vào câu dẫn bản gốc.
- III.1: đơn vị "(mN)" giữ; câu hỏi đặt ngoặc làm tròn trước dấu "?" (thống nhất các câu Phần III).
- III.3: "$1{,}7\cdot 10^{-8}\Omega m$" → "Ω·m"; công thức góc "α = ?POM" (vỡ) → "α = ∠POM" ($\widehat{POM}$).
- III.4: "chu kỳ" → "chu kì"; "vật lý" → "vật lí"; "Iridium-192" → "iridium-192".
- III.5: "pittông" → "pit-tông"; câu hỏi kết thúc bằng dấu chấm, đưa ngoặc làm tròn vào cuối câu.
- III.6: "H₂" gõ $\text{H}_2$; "khí heli" → "khí helium" (thống nhất trong câu); "trái đất" → "Trái Đất".
- Không câu nào khác có từ phủ định cần in đậm.

## Trình bày
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại). Không có cặp câu dùng chung dữ kiện.
- Hình: 9 hình vẽ lại bằng TikZ (ảnh so ở `so-hinh/`):
  - I.5 cảnh sát giao thông dùng súng bắn tốc độ (ảnh chụp): vẽ lại có khối (mũ bảo hiểm chữ "CSGT", súng, đường, dải phân cách, cây, xe xa); `% giuhinh`.
  - I.10 đồ thị E_lkr theo A: giữ lưới (ô 20 theo A, 1 MeV theo E), số trên trục như gốc; đường cong đỏ.
  - I.14 sạc không dây (ảnh chụp): bàn tay, điện thoại, đĩa sạc vòng xanh; `% giuhinh`.
  - I.18 pickup đàn guitar (ảnh chụp): mặt đàn gỗ, lỗ thoát âm, pickup có 2×6 cực, dây đàn, cần đàn, hộp xử lí có hai núm (`\VLnumvan`); bỏ logo "unica"; `% giuhinh`.
  - II.1 khung dây trong từ trường (dấu nhân xanh, nền xanh nhạt), khung dây màu đồng, bình – điện trở R – khí – pit-tông – vòng chặn, các nhãn đóng khung như gốc.
  - II.3 máy đo lưu lượng máu: mạch máu trong từ trường (chấm), mặt cắt với điện cực, vôn kế; mũi tên dòng máu màu `VLluc` (vận tốc).
  - III.1 đoạn dây MN treo lệch góc α, B hướng lên; đặt bên phải câu dẫn để gọn trang.
  - III.2 bộ thí nghiệm nhiệt nóng chảy (biến áp nguồn, oát kế, nhiệt lượng kế có dây nung, cốc trên cân, giá, đồng hồ bấm giây); màn hình cân, nguồn, mặt đồng hồ để trống số; đặt bên phải các bước thí nghiệm; `% giuhinh`.
  - III.3 nửa vòng tròn MPN, OP, OM màu đồng, hai kí hiệu ⊗ B̄ (`\VLnhantron`); đặt bên phải câu dẫn ("như hình vẽ" → "như hình bên") để gọn trang 8 (phiên chính).

## Vẽ lại hình thực tiễn (14/11/2026, Opus 5.5)

Vẽ lại hai ảnh chụp I.5, I.14 (thay hình vẽ ở mục Trình bày), dò theo toạ độ điểm ảnh của ảnh gốc (`image18.png` 245 × 167, `image63.png` 214 × 183; trục y hướng xuống), soát nhiều vòng bằng ảnh ghép gốc | hình vẽ và từng vùng phóng to. Chỉ sửa `tikzpicture` của hai câu và khai báo riêng của đề; lời đề, `\True`, `\loigiai` giữ nguyên; `dan_trang.py` ghi lại `\NeedspaceCau` của I.5, I.6, I.14. Ảnh so: `so-hinh/01-cau-I-5.png`, `so-hinh/03-cau-I-14.png` (dựng lại cả 9 hình).

- **I.5** (9,2 × 6,3 cm, trước 5,4 × 3,5 cm): vẽ mới hoàn toàn theo ảnh gốc (không chép mã Lương Thế Vinh I.4, chỉ tham khảo bố cục). Nền: trời xanh đậm ở trên, nhạt dần về chân trời; mây tích trắng sáng có đáy xám xanh nhạt, đám lớn ở trên giữa và bên trái, đám bên phải, vài vệt mây mỏng giữa trời; dây điện, cột điện, cột đèn; tán lá sẫm góc trên trái có trời lọt qua; dãy nhà xa, nhà mái trắng có đầu hồi, hàng cây xa có hoa cam, hàng quán dưới tán; dải cây rậm liên tục từ giữa ảnh tới sau mũ (mép trên lởm chởm, xanh đậm có mảng sáng mép mềm, tối dần xuống dưới); cây, nhà bên phải mũ. Đường: nửa trái gần lề chìm trong bóng râm xám xanh, vệt nắng xám sáng ở giữa và vùng nắng bên phải (mép mềm), dải bóng cây rộng mép mềm chéo qua vệt nắng, mảng bóng lớn góc dưới trái (không chấm, không nét mảnh); vạch sơn trắng hội tụ về điểm tụ bên trái, dải phân cách sọc đỏ – trắng thu nhỏ dần về xa; lề trái có vỉa hè, rãnh nước từng tấm (khe nối, vệt sáng), bó vỉa, rác trắng. Xa: xe buýt trắng – xanh lá (kính, đèn, bánh), người đi xe máy giữa đường, hai người bên lề trái, bóng đổ. Súng rađa: hộp phát kính xám sáng hình chữ nhật bo góc hướng sang trái, thân đen phía sau, vỏ ống ngắm đen lớn bo tròn trên nóc kéo tới sát mũ (nhãn trắng ở đầu, ánh xám, mép sáng), một ống kính tròn nhỏ có ánh xanh, giá đỡ, cò, báng cầm ngay dưới thân trước. Tay da ngăm: một tay nắm báng (lưng bàn tay, khớp ngón, các ngón quấn quanh báng, ngón trỏ ở cò), tay kia nắm đỡ cạnh súng, ngón cái dựng (móng, khe ngón, đốt, nếp gấp), cẳng tay sáng – tối, khuỷu sẫm; cánh tay phía sau trong bóng. Cảnh sát: mũ bảo hiểm vàng kem bóng (đổ bóng tròn nhiều nấc, điểm sáng, viền tối, vành đen, lỗ thoáng có viền), chữ CSGT xanh đậm kiểu chữ có chân có ánh trắng, lưỡi trai kính và quai mũ, gáy, cổ áo, áo sơ mi vàng kem (nếp áo, vai sau tối), cầu vai đỏ sẫm bện trắng – xanh đậm, phù hiệu tay áo hình khiên xanh có huy hiệu. Chỉ có chữ CSGT như gốc.
- **I.14** (6,3 × 5,4 cm, trước 4,3 × 3,2 cm): thảm vải xám tím (vân hạt sáng – tối, loang mờ); đế sạc tròn trắng nhìn xiên (bóng đổ mềm, thành bên tối, gờ ngoài dày có viền sáng, mặt trong lõm, rãnh vòng tối có viền sáng, tâm phát sáng xanh nhạt mờ dần, vạch LED nhỏ ở mép trước bên phải); bàn tay da sáng từ mép trái (ngón cái đặt trên màn hình dọc mép trên, có móng và nếp đốt; ngón trỏ co trong bóng ửng đỏ ánh màn hình; các ngón đỡ dưới máy, đầu ngón có móng lộ dưới cạnh máy, nếp đốt, bóng đổ); điện thoại tràn viền cầm nghiêng (trục dài từ dưới – trái lên trên – phải, viền đen, khung kim loại lộ độ dày ở cạnh dưới, tai thỏ đầu phải, màn hình hồng tím – đỏ cam – xanh lam, biểu tượng pin sạc xanh lá có tia sét, vệt sáng trên kính). Không có chữ.
- Cách đặt: hai hình lớn hơn nên đặt bên phải phương án bằng hai `minipage` (I.5: 0,42 / 0,56; I.14: 0,6 / 0,38) như câu I.5 đề mẫu; lời đề I.5 sẵn "hình vẽ bên", I.14 "như hình", không đổi.
- Khai báo riêng của đề (thay hai màu cũ `HPda`, `HPkaki`): `\usetikzlibrary{fadings}`; vệt mờ `HPhaimo` (tròn, mờ dần ra mép), `HPhaimep` (bóng đổ mép mờ), `HPhaidau` (mờ theo chiều ngang, dùng kèm `fading angle`); đổ bóng mũ `HPhaimuSh`; màu I.5: `HPhaitroi`, `HPhaila`, `HPhailasang`, `HPhaiduong`, `HPhaiduongsang`, `HPhaida`, `HPhaidatoi`, `HPhaimu`, `HPhaiao`, `HPhaichu`, `HPhaido`; macro mây tích `\HPhaimaytich{y đỉnh}{y đáy}{x/y/r,...}` (bọng tròn hợp thành đám mây, quầng mờ, đáy xám xanh); màu I.14: `HPhaitham`, `HPhaitay`, `HPhaihong`, `HPhaicam`, `HPhaimanxanh`. Ngoài `\HPhaimaytich` không thêm macro; vân lá, vân thảm rải bằng `rnd` với `\pgfmathsetseed` cố định (hình như nhau mỗi lần biên dịch).
- In xám (`pdftoppm -gray`): các mảng (trời, cây, đường, súng, mũ, áo; thảm, tay, màn hình, đế sạc) khác độ sáng, vẫn rõ.
- Vòng 2 (phiên chính soát, chỉ I.5): bỏ mảng sáng loang lổ có chấm và hai nét mảnh tối hình chữ X trên mặt đường, vẽ lại vệt nắng, dải bóng cây rộng mép mềm, mảng bóng góc dưới trái; súng bỏ ô màn hình vuông và ống kính đôi (trông như máy quay phim), vẽ lại hộp phát kính xám sáng, vỏ ống ngắm đen lớn tới sát mũ, một ống kính ánh xanh, báng dưới thân trước, tay nắm báng thấy lưng bàn tay và các ngón quấn; trời xanh đậm hơn ở trên, mây tích rõ khối; dải cây rậm xanh đậm có mảng sáng, mép trên lởm chởm; nhà mái trắng có đầu hồi. Người, mũ, áo, cầu vai, phù hiệu, xe xa, lề đường, cỡ và cách đặt hình giữ nguyên.
- Còn khác gốc: I.5 hậu cảnh (mây, tán cây, nhà, xe ở xa) cách điệu vì ảnh gốc nhỏ và mờ, đám mây trên giữa dàn ngang hơn gốc; súng vẽ theo các khối chính (ảnh gốc không rõ nút); huy hiệu trên phù hiệu và dây bện cầu vai giản lược. I.14 bàn tay vẽ rõ nét (ảnh gốc nhòe do chuyển động), đế sạc là elip đều (ảnh gốc hơi méo do ống kính), vết in mờ trên mặt đế không vẽ.
- Dàn trang sau khi vẽ lại (cả vòng 2): bản đề 9 trang ĐẠT, bản lời giải 12 trang (cùng số trang như trước); lưu ý: trang 10 bản lời giải trống 8,7 cm (1/4–1/3 trang, có từ trước, không do hai hình).
