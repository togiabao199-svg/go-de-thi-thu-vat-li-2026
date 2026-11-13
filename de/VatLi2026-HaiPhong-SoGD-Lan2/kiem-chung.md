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
  - III.3 nửa vòng tròn MPN, OP, OM màu đồng, hai kí hiệu ⊗ B̄ (`\VLnhantron`).; đặt bên phải câu dẫn ("như hình vẽ" → "như hình bên") để gọn trang 8 (phiên chính).
