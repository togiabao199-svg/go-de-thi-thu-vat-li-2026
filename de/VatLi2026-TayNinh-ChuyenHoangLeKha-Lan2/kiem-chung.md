# Kiểm chứng đáp án – VatLi2026-TayNinh-ChuyenHoangLeKha-Lan2

Nguồn: `kho/goc/Tay Ninh - THPT chuyen Hoang Le Kha - Lan 2.docx` (Trường THPT chuyên Hoàng Lê Kha, Tây Ninh, thi thử TN THPT 2026 lần 2, mã đề 126), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python (`/tmp/VatLi2026-TayNinh-ChuyenHoangLeKha-Lan2/py/kiem.py`).

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | A B C C A D D B D A D B B A D D A C | trùng (I.3, I.13, I.17 xem dưới) | I.4: F = 0,05·2·0,4 = 0,04 N; I.6: Δm/A: He 0,00763, I 0,00891, U 0,00818 amu (lời giải gốc tính sai Δm của I, U: 1,2021 / 1,9337, đúng là 1,2381 / 1,9224; thứ tự không đổi); I.7: T = 24 ms, t₁ = 1 ms, t₁₉ = 1 + 18·6 = 109 ms; I.8: x = 16 °C, C = C₀/3, Δt = 6,4 °C; I.14: x² − 133x + 4080 = 0 ⇒ x = 48 cm, bơm thêm 5 cm; I.18: 3T/4 = 25 ms ⇒ ω = 60π |
| **I.3** | **C** | **C — có `% KIỂM TRA`** | Lời đề "Coi như bốn lốp xe chứa cùng một lượng khí như nhau" mâu thuẫn với áp suất ban đầu khác nhau (244, 244, 252, 248 kPa) ở cùng nhiệt độ: nếu hiểu đúng chữ thì T ∝ p₂ và lốp nhỏ nhất là trước trái (260). Đáp án gốc hiểu "lượng khí trong mỗi lốp không đổi": T₂/T₁ = p₂/p₁; tỉ số trước trái 1,066, trước phải 1,082, sau trái 1,063, sau phải 1,065 ⇒ sau trái (tính theo áp suất tuyệt đối, cộng 101,3 kPa, vẫn là sau trái). Giữ lời đề, gõ theo đáp án gốc C; thầy xem có sửa lời đề thành "lượng khí trong mỗi lốp không đổi". |
| **I.13** | **B** | **B — sau khi sửa hình** | **Hình gốc vẽ B ở phút 8** (nóng chảy 8 → 12 phút: λ = 200·240/0,24 = 2·10⁵ J/kg, không có phương án), còn lời đề gốc có chữ nghiêng "(đồ thị nhiệt độ - thời gian, đoạn nằm ngang ở 60 °C từ phút 10 đến 12)". Hình vẽ lại đặt B ở phút 10 (giữ vạch chia 0, 4, 8, 10, 12, 16 của hình gốc) cho khớp lời đề và đáp án gốc: λ = 200·120/0,24 = 10⁵ J/kg; bỏ dòng chữ nghiêng mô tả hình khỏi lời đề. `% KIỂM TRA` trong file. |
| **I.17** | **A** | **A — theo hình vẽ lại** | Ảnh gốc là hình minh họa vẽ không đúng phối cảnh (các múi "nằm ngang" vẽ lệch pha, không xác định được chiều), nên không suy ra được X, Y bằng quy tắc tam diện thuận E⃗, B⃗, v⃗. Hình TikZ vẽ lại theo phối cảnh đúng: X là thành phần thẳng đứng, Y là thành phần nằm ngang, cùng pha, khi X hướng lên thì Y hướng ra phía sau; với v⃗ hướng sang phải – ra trước, Y × X cùng chiều v⃗ ⇒ X là B⃗, Y là E⃗ (khớp đáp án gốc). Hai thành phần tô cùng màu tím (không tô đỏ/xanh để khỏi lộ đáp án). Thầy xem lại hình. |
| II.1 | Đ Đ S S | trùng | p_B2 = 101·25/21,7 = 116,4 cmHg; p_A2 = 91,4 cmHg; ℓ_A2 = 76·40/91,4 = 33,3 cm; pit-tông xuống (40 + 25) − (33,3 + 21,7) ≈ 10,0 cm |
| II.2 | Đ S S Đ | trùng | H = 1100/3400 = 32,4%; m(²³⁵U) = 2562,8 kg; R = 3,4·10⁹/(200·1,6·10⁻¹³) = 1,06·10²⁰ s⁻¹; N = 6,57·10²⁷; t = N/(1,25R) = 4,94·10⁷ s ≈ 572 ngày (lời giải gốc 573 ngày) ≠ 300 ngày |
| II.3 | S Đ Đ S | trùng | e = 0,2 V; I = 0,4 A; F = 0,02 N; P = 0,08 W. a) B⃗ hướng ra (chấm), thanh sang phải ⇒ dòng trong thanh a → b, qua R từ d đến c ⇒ Sai |
| II.4 | S Đ S S | trùng | c = 0,225·4180·11,5/(0,409·29) = 912 J/kg.K |
| III.1–III.6 | 1,5 / 120 / 0,4 / 32 / 45 / 33 | trùng | III.1: 10·25·10⁻⁴·2,4·10⁻³/0,04 = 1,5 mV; III.2: p₂ = 8·10⁴ Pa, ℓ₂ = 20 cm, T₂ = 120 K; III.3: B = 0,08/(2·10·0,1·0,1) = 0,4 T; III.4: N = 3,52·10¹⁸, H_K = 61,9 Bq/l, x = 32,3 → 32; III.5: 80m = 3600 ⇒ 45 g; III.6: T₁/(T₁ − 6) = 1,02 ⇒ 306 K = 33 °C |

## Sửa lời đề (lỗi chữ bản gốc)
- Kí hiệu hạt nhân vỡ ("2^4He", "53^139I", "92^235U", "19^40K", "53^131I", "92^238U") gõ lại ${}^4_2$He, ${}^{139}_{53}$I, ${}^{235}_{92}$U, ${}^{40}_{19}$K, ${}^{131}_{53}$I, ${}^{238}_{92}$U (I.6, II.2, III.4); III.4 bỏ chữ nghiêng lẫn vào câu dẫn.
- I.7, I.8: bỏ dấu chấm thừa cuối câu dẫn trước phương án ("lần thứ 19 là.", "sẽ tăng thêm.").
- I.13: bỏ dòng chữ nghiêng mô tả hình "(đồ thị nhiệt độ - thời gian, đoạn nằm ngang ở 60 °C từ phút 10 đến 12)" (đã thể hiện trên hình vẽ lại, xem trên); phương án "6.10⁵" gõ $6\cdot 10^5$.
- I.17: "$v$" → "$\vv{v}$" (vectơ vận tốc), hình thêm nhãn $\vv{v}$ ở đầu mũi tên "Phương truyền sóng" cho khớp lời đề.
- "thuỷ", "hoá", "minh hoạ", "toả" → "thủy", "hóa", "minh họa", "tỏa"; "bất kỳ" → "bất kì" (I.12); "lý tưởng" → "lí tưởng" (III.2); "nguyên lý" → "nguyên lí" (II.2a).
- II.1, III.2: "piston" → "pit-tông" (cả "Ấn piston", "Piston đã được ấn").
- II.2: "quặng oxit uranium" → "quặng oxide uranium" (IUPAC); "86000", "57000" → $86\,000$, $57\,000$; "2,0.10²" → $2{,}0\cdot 10^2$; "Trái đất" → "Trái Đất"; bỏ chữ nghiêng lẫn vào lời đề.
- II.3: lực kéo "F" → $\vv{F}$ trong câu dẫn và hình; "$R=0,3\Omega$" → $R=0{,}3~\Omega$.
- II.4 c): "kết quả tính được ở câu a)" → "ở ý a)".
- III.1, III.3: "(làm tròn kết quả đến chữ số hàng phần chục)?" → "(làm tròn kết quả đến chữ số hàng phần mười)?" và bỏ dấu "?" trước ngoặc; III.1 "xuất hiện trên khung" → "xuất hiện trong khung".
- III.2, III.5: dấu "?" trước ngoặc làm tròn chuyển ra sau ngoặc như các câu khác.
- Tiêu đề Phần III gốc "Câu hỏi trắc nghiệm trả lời ngắn" → theo đề mẫu "Câu trắc nghiệm trả lời ngắn".

## Hình
- 12 hình TikZ (I.3, I.13, I.14, I.16, I.17, I.18, II.1, II.3, II.4, III.1, III.2, III.3); I.3 (hai bảng áp suất lốp dạng ảnh) vẽ lại khung + ô tô nhìn từ trên.
- **II.3: bỏ hai mũi tên rỗng trên ray** của hình gốc (ray trên chỉ sang phải a → c, ray dưới chỉ sang trái d → b, tức dòng qua R từ c đến d) vì ngược chiều dòng điện cảm ứng thật (B⃗ hướng ra, thanh sang phải ⇒ qua R từ d đến c) và làm lộ/lệch ý a). Thầy xem lại.
- I.13: điểm B dời từ phút 8 sang phút 10 (xem bảng trên).
- II.4 (bình nhiệt lượng kế, hình thực tiễn) `% giuhinh`, vẽ như các lô trước, chờ phiên vẽ lại; II.3 có điện trở circuitikz, `% giuhinh`; I.17 `% giuhinh`.
- Dàn trang: III.1 đặt đồ thị bên phải câu dẫn; III.2 thu hình scale 0,82; II.3, II.4 phóng hình (scale 1,2 / 1,05) để trang 6 bản đề không trống quá 1/4.
