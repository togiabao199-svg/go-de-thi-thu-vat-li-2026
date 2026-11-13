# Kiểm chứng đáp án – VatLi2026-ThanhHoa-SoGD-Lan1

Nguồn: `kho/goc/Thanh Hoa - So GDDT - Lan 1.docx` (mã đề 1201; có bảng đáp án, lời giải gốc chỉ có Phần II, III). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | A B D C A C C D D A D A A B B B B D | trùng | I.3: Φ = 0,12·40·10⁻⁴·cos 60° = 2,4·10⁻⁴ Wb; I.6: 80,6 − 42,4 = 38,2, sai số 0,2 + 0,3 = 0,5; I.7: B tăng, dòng cảm ứng ngược chiều kim đồng hồ MQPNM; I.11: T₄ = 400·(1·3)/(2·1) = 600 K; I.18: t = 0,05·3,4·10⁵/28,3 ≈ 600,7 s |
| **I.13** | **A (Hình 3)** | **A, sau khi sửa kí hiệu hình** | **Hình gốc dùng ⊕ (B ở Hình 1, I ở Hình 2) và ⊗ (F ở Hình 4). Hiểu ⊕, ⊗ là hướng vào trong thì Hình 1 (F phải hướng xuống phải) và Hình 4 (F phải hướng ra) cũng sai, câu có 3 hình sai. Đã vẽ lại: Hình 1 B hướng ra (⊙), Hình 2 I hướng vào (⊗), Hình 4 F hướng ra (⊙) — khi đó chỉ Hình 3 sai (I ngược chiều B, F = 0), khớp đáp án gốc. Có `% KIỂM TRA` — thầy xem lại.** |
| II.1 | S Đ Đ Đ | trùng | e = 150·0,01 = 1,5 V; v = 2ℓf = 2·0,75·460 = 690 m/s |
| II.2 | Đ Đ Đ S | trùng | p₀V/2 = nRT₀; đẳng áp đến 2T₀: Q₁ = 5/4 p₀V; đẳng tích đến 3T₀: Q₂ = 3/4 p₀V; Q = 2p₀V |
| II.3 | Đ Đ S S | trùng | f = 42,6·2 = 85,2 MHz; λ = 3·10⁸/85,2·10⁶ ≈ 3,52 m (không phải cm) |
| II.4 | Đ S Đ S | trùng | m = 120000/(3,3·10⁵ + 4200·100) = 0,16 kg; m_hh = 138000/2,3·10⁶ = 0,06 kg; còn 100 g |
| III.1–III.3 | 2,4 / 25 / 2 | trùng | F = 3·10⁻⁵·800·100 = 2,4 N; T/4 = 0,01 s ⇒ f = 25 Hz; V₂/V₁ = 600/300 = 2 |
| **III.4** | **bảng đáp án: 99920 J; lời giải gốc: 25 J** | **25** | **Lời đề in "105 J" (bảng đáp án hiểu là 10⁵ J: 10⁵ − 80 = 99920, lại quá 4 kí tự). Gõ theo lời đề học sinh thấy: ΔU = 105 − 80 = 25 J. Có `% KIỂM TRA`.** |
| **III.5** | **bảng đáp án: 140; lời giải gốc: 141** | **141** | **ρ = 1,169·0,97·298/288 ≈ 1,1733 kg/m³; m = 120ρ ≈ 140,80 kg → 141. Có `% KIỂM TRA`.** |
| **III.6** | **bảng đáp án: 1142; lời giải gốc: 1149** | **1149** | **Q = 140,796·1005·5 ≈ 707501 J; t = Q/(0,7·880) ≈ 1148,5 s → 1149 (đề yêu cầu không làm tròn trung gian; 1142 là kết quả dùng m = 140 kg đã làm tròn). Có `% KIỂM TRA`.** |

Bảng đáp án gốc và lời giải gốc lệch nhau ở III.4, III.5, III.6 (bảng: 99920 / 140 / 1142; lời giải: 25 / 141 / 1149); file gõ theo kết quả tính lại.

## Sửa lời đề (lỗi chữ bản gốc)
- Khối "Cho biết": bản gốc in lặp hai lần → giữ một lần; thêm dòng "Không làm tròn kết quả các phép tính trung gian" như đề gốc.
- I.2, I.13: in đậm "không".
- I.8: "hìnhảnh" → "hình ảnh"; "kỹ thuật số" → "kĩ thuật số".
- I.12: "chuyê̂n" → "chuyển"; "từ thể lỏng sang khí" → "từ thể lỏng sang thể khí" (phương án B, D).
- I.13: câu hỏi kết thúc bằng dấu ":" → dấu "?"; sửa kí hiệu trên hình (xem bảng trên).
- I.14: kí hiệu $\overline{\text{E}_\text{d}}$ → $\overline{E}_{\text{đ}}$.
- II.2: "piston" → "pit-tông"; "mẩu" → "mấu" (thống nhất); $P_o$, $T_o$ → $p_0$, $T_0$; nhãn hình "Piston" → "Pit-tông", "P₀ : V/2" → "p₀; V/2".
- II.3: "1,5 Tesla đến 3 Tesla" → "1,5 T đến 3 T"; "xử lý" → "xử lí"; "khớp..." → "khớp,…".
- II.1 (hình): nam châm trong hình phóng to ghi "N" ở cả hai đầu → sửa đầu dưới thành "S" (như hình SGK); cực không phải ý hỏi.
- III.2: bỏ "(A)" dính liền biểu thức, gõ $i=4\cos\omega t$ (A).
- III.4: "xi lanh" → "xilanh".
- III.5: "Sử dụng các thông tin sau cho Câu 5 và Câu 6" → mẫu chuẩn "Dùng thông tin sau cho câu 5 và câu 6:" đặt trong câu 5; "1Bar" → "1 bar"; "Hsưởi ấm" → $H_{\text{sưởi ấm}}$; "Nhiệt dung riêng" sau dấu ";" viết thường.
- Màn hình lò sưởi (III.5) ảnh gốc hiện "85": không phải dữ kiện → để trống.

## Ghi chú
- Phần I không có lời giải gốc: lời giải Phần I tự viết. Phần II, III viết lại theo ý lời giải gốc.
- Mã câu: I.8 (ảnh chụp tia X) gắn `VL11-C2` (thang sóng điện từ); II.1 ý c) có phần sóng dừng trên dây (lớp 11) nhưng câu gắn `VL12-C3`.
- Hình thực tiễn (I.8 ảnh X quang, I.9 khói đá khô, II.1 ghi ta điện, II.3 máy MRI, III.5 lò sưởi) vẽ ở mức các lô trước, chờ phiên vẽ lại.
