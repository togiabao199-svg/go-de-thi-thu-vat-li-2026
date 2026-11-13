# Kiểm chứng đáp án – VatLi2026-HaNoi-SoGD-Lan1

Đề gốc (PDF SieuGioi, "Sở GD&ĐT Hà Nội – Đề thi chính thức – Lần 1, năm 2025 - 2026") không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | A B D A B C D C D D A C B A D D A B | I.6: ΔU = A + Q, Q < 0, A < 0 ⇒ giảm; I.8: từ thông đo bằng Wb, ba đại lượng kia đo bằng V; I.14: S₁ = p_B·V_B = p_E·V_E = S₂; I.16: khí lí tưởng bỏ qua thế năng tương tác (phân tử vẫn va chạm nên B không chọn); I.17: A đúng; D sai vì đường sức từ khép kín hoặc vô hạn ở hai đầu (SGK) |
| II.1 | không có | Đ Đ S Đ | giả thuyết xét khi thể tích không đổi ⇒ phải giữ pit-tông cố định ở cả bước 2 |
| II.2 | không có | Đ S Đ S | b): "cùng chuyển động" chưa chắc cùng vận tốc ⇒ vẫn có thể có chuyển động tương đối, có dòng điện cảm ứng |
| II.3 | không có | S S Đ Đ | khung nằm ngang giữa hai cực, trục Δ nằm ngang theo chiều sâu hình; bc ∥ B; dòng vào cực + đi a→b (vào trong), F = I·ℓ × B ⇒ lực lên ab hướng xuống |
| II.4 | không có | Đ Đ S S | 1→2 đường qua O (đẳng áp, Charles); 2→3 đẳng tích, T giảm ⇒ p giảm; 3→1 đẳng nhiệt nén ⇒ Q = −A < 0, tỏa nhiệt |
| III.1–III.6 | không có | 3,5 / 1,46 / 32 / 69,2 / 5,6 / 1,16 | III.1: 2·125·0,150·98,0·10⁻⁴/0,105 = 3,500 V; III.2: 3,5/2,40 = 1,4583 A; III.3: (1,10 − 1,00)·10⁵·32,0·10⁻⁴ = 32,0 N; III.4: p = 10⁵ + 45/0,0032 = 1,140625·10⁵ Pa ⇒ T = 342,19 K ⇒ 69,19 °C; III.5: v = E/B = 5600 m/s; III.6: r = mv/(qB) = 1,162·10⁻³ m |

## Điểm cần thầy xem

- **II.2 b)** "Không có dòng điện trong khung dây nếu khung dây và nam châm cùng chuyển động": gõ **Sai** (cùng chuyển động nhưng khác vận tốc vẫn có dòng điện cảm ứng). Nếu hiểu là "cùng chuyển động như một vật" (không có chuyển động tương đối) thì là Đúng.
- **II.3**: hình gốc vẽ khung theo phối cảnh xiên; hiểu khung nằm ngang giữa hai cực (ad, bc ∥ B; ab, cd và trục Δ theo chiều sâu) như hình động cơ điện SGK. Ý b) Sai theo cả hai cách hiểu (khung đứng thì lực lên ab nằm ngang; khung ngang thì lực lên ab hướng xuống với dòng vào ở cực +).
- **I.17**: chọn A; D "luôn là những đường cong khép kín" coi là sai theo phát biểu SGK ("khép kín hoặc vô hạn ở hai đầu").
- **III.6**: dùng vận tốc ở câu III.5 (v = 5,6 km/s). Công thức r = mv/(|q|B) suy từ lực hướng tâm; đề đã cho F = Bv|q|.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi, dòng họ tên / số báo danh, "ĐỀ THI CHÍNH THỨC", "(Đề thi gồm 05 trang)", dòng quảng cáo, "---HẾT---" của bản gốc.
- "Cho biết": "J.mol‒1.K‒1", "NA = 6,02.1023 mol‒1" gõ lại theo quy chuẩn kí hiệu.
- Chính tả, thuật ngữ SGK 2018: "toả" → "tỏa" (I.6, II.4 a); "xi-lanh" → "xilanh", "pít-tông" → "pit-tông" (II.1, thống nhất với Phần III); "Niutơn (N)" → "newton (N)" (III.3); "oC" → "°C" (III.4).
- I.8: in đậm "**không**".
- I.14: "hình vẽ" → "hình bên" (hình đặt bên phải phương án); trục "P" gõ $p$.
- II.1: tiêu đề "Bước 1/Bước 2" giữ in nghiêng; sau dấu ";" viết thường ("Ghi số chỉ" → "ghi số chỉ", "Giữ" → "giữ").
- Phần III: đoạn "Sử dụng các thông tin sau cho Câu 1 và Câu 2/3 và 4/5 và 6" đặt trong câu đầu của cặp, mở đầu bằng "Dùng thông tin sau cho câu … và câu …:" (`\label`/`\ref`). Câu III.1, III.2: đoạn dữ kiện gốc kết thúc bằng "Trong thời gian đổi chiều của cảm ứng từ," — chuyển cụm này vào đầu câu hỏi III.1 và III.2 cho câu hỏi đủ ý ("Trong thời gian đổi chiều của cảm ứng từ, độ lớn suất điện động…", "…, cường độ dòng điện trung bình…").
- III.5: "2,80kV / m" → "2,80 kV/m"; "Vận tốc v" → "Vận tốc $v$".
- Tiêu đề Phần II, III gõ theo câu chữ đề mẫu.

## Đánh số lại câu

Đề gốc đã đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6): giữ nguyên. Tham chiếu "Câu 1 và Câu 2", "Câu 3 và Câu 4", "Câu 5 và Câu 6" của Phần III gõ bằng `\label`/`\ref` (nhãn `HaNoi-SoGD-Lan1-III1` … `-III6`).

## Hình

7 hình gốc → 7 `tikzpicture`, ảnh so ở `so-hinh/`. Vùng cắt ảnh trang (150 dpi, tỉ lệ khổ trang): I.14 tr.2 `0.71:0.53:0.94:0.665`; II.1 tr.3 `0.755:0.40:0.94:0.53`; II.3 tr.4 `0.39:0.065:0.62:0.195`; II.4 tr.4 `0.705:0.305:0.93:0.435`; III.1 tr.4 `0.32:0.61:0.70:0.805`; III.3 tr.5 `0.31:0.12:0.70:0.23`; III.5 tr.5 `0.33:0.465:0.68:0.58`.

- I.14: đặt bên phải phương án (hai `minipage`). II.1: hình đặt bên phải đoạn "Bước 1, Bước 2" (bản gốc cũng đặt bên phải); câu gắn `% tachDS` để câu dẫn ở trang 3, bảng ở trang 4 (tránh trang 3 trống 13,8 cm).
- II.3: nam châm tô N đỏ, S xanh (đề có ghi cực); khung dây màu đồng.
- II.4: ba quá trình ba màu (đỏ, xanh, xanh lá), không mang thông tin riêng.
- III.5: ion dương ⊕ đỏ, $\vv{v}$ xanh lá, vùng từ trường nền `VLxanh!8`, dấu ⊙ dùng `\VLchamtron`.

## Dàn trang

Bản đề 6 trang (ĐẠT), bản lời giải 9 trang (trang cuối trống 6,9 cm).
