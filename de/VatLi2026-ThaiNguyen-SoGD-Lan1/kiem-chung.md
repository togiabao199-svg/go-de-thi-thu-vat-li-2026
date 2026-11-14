# Kiểm chứng đáp án – VatLi2026-ThaiNguyen-SoGD-Lan1

Đề gốc (PDF SieuGioi "Sở GD&ĐT Thái Nguyên – Lần 1, năm 2025 - 2026", không mã đề) không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | A B C D C D C D D A D A B C C A A C | I.5: ΔT = 30 − 22 = 8 K; I.7: dòng trên DA đi từ D lên A, B hướng ra ⇒ F hướng sang phải, cùng hướng AB; I.13: đồ thị V–T thẳng, kéo dài qua O ⇒ đẳng áp |
| II.1 | không có | Đ Đ Đ S | R = 1,7·10⁻⁸·0,72/3,5·10⁻⁹ = 3,497 Ω; I = 12/(3,497 + 0,5) = 3,002 A; c): dòng đi từ cực dương (bản dài, phía K) qua A, đoạn nằm ngang hướng ra phía sau, về B; B từ N sang S ⇒ lực lên dây hướng xuống, phản lực lên nam châm hướng lên ⇒ số chỉ cân giảm; d): B = 0,006·9,8/(3·0,12) = 0,163 T (đề ghi 0,13 T) |
| II.2 | không có | S S Đ S | đẳng nhiệt (Boyle); p₀·6,5 = p·5 ⇒ ρgh = 0,3p₀ ⇒ h = 0,3·1,013·10⁵/(1030·9,8) = 3,01 m (đề ghi 5 m) |
| II.3 | không có | Đ Đ S S | đẳng tích, N/V không đổi; p₂ = 2,00·318/300 = 2,12 bar (đề ghi 2,35 bar) |
| II.4 | không có | Đ S Đ S | công và nhiệt lượng là số đo độ biến thiên nội năng; xoa tay là thực hiện công |
| III.1–III.6 | không có | 683 / 2,2 / 16 / 1,6 / 301 / 401 | III.1: (0,8·880 + 2·4200)·75 = 682 800 J; III.2: Q₂ = 0,2·2·2,26·10⁶ = 904 000 J, P = 1 586 800/(0,75·960) = 2203,9 W; III.3: e = 0,8·0,4/0,02 = 16 V; III.4: I = 16/10 = 1,6 A; III.5: T₂ = 15·10⁵·10⁻²/(6·8,31) = 300,84 K; III.6: p = 20 − 0,5V, pV cực đại tại V = 20 lít, p = 10·10⁵ Pa ⇒ T = 2·10⁴/49,86 = 401,12 K |

## Điểm cần thầy xem

- **I.17**: bản gốc phương án C trùng phương án B (cả hai là p = nR/(VT)). Đã gõ lại phương án C thành p = nV/(RT) để bốn phương án khác nhau (`% KIỂM TRA` trong file); đáp án A không đổi.
- **II.1 c)**: kết luận dựa vào cực của bộ nguồn trên hình gốc (phóng to 900 dpi: hai pin, bản dài mảnh ở phía K, bản ngắn đậm ở phía B ⇒ cực dương nối về A qua K) và hướng đoạn dây nằm ngang (vẽ xiên theo chiều sâu, từ phía trước ra phía sau). Hình vẽ lại giữ đúng thứ tự bản cực.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi, dòng họ tên, số báo danh, dòng quảng cáo; bỏ dòng "PHẦN I…" lặp hai lần của bản gốc.
- Cho biết: "R = 8,31 J.mol⁻¹" thiếu K⁻¹ → $R=8{,}31$ J·mol⁻¹·K⁻¹.
- I.2: "phân từ" → "phân tử".
- I.6: "vector" → "vectơ"; kí hiệu từ thông φ → Φ. I.7: "vecto AB" → "vectơ".
- I.10: "Theo định luật 1 nhiệt động lực học" → "Theo định luật 1 của nhiệt động lực học".
- I.11: dấu nháy kép thẳng → nháy kép chuẩn.
- I.17: phương án C trùng B (xem trên).
- II.1: kí hiệu suất điện động E → ℰ (`\mathscr{E}`), "3,5Ω" → "3,5 Ω".
- II.2: "thế kỷ" → "thế kỉ"; nháy kép chuẩn.
- II.3: "2,00Bar", "2,35 Bar" → "2,00 bar", "2,35 bar".
- Phần III: "kenvil" → "kelvin" (câu 5, 6); "880 (J/kg.K)" → "880 J/(kg.K)", tương tự 4200, 2,26·10⁶ J/kg, 1000 kg/m³. "Câu 1 và Câu 2" → "câu 1 và câu 2" (đoạn dữ kiện chung đặt trong câu đầu của cặp, dùng `\label`/`\ref`).

## Đánh số câu

Đề gốc đã đánh số theo từng phần (Phần I câu 1–18, Phần II câu 1–4, Phần III câu 1–6): giữ nguyên. Ba cặp câu dùng chung dữ kiện ở Phần III (1–2, 3–4, 5–6) tham chiếu bằng nhãn `ThaiNguyen-SoGD-Lan1-III1` … `-III6`.

## Hình

4 hình gốc → 4 `tikzpicture`, ảnh so ở `so-hinh/`. Vùng cắt ảnh trang (150 dpi, tỉ lệ khổ trang): I.7 tr.2 `0.39:0.065:0.62:0.215`; I.13 tr.2 `0.39:0.725:0.68:0.86`; II.1 tr.4 `0.32:0.065:0.70:0.29`; III.5 tr.5 `0.33:0.585:0.67:0.74`.

- II.1: dựng lại theo tọa độ hình gốc (cân, nam châm chữ U, dây, khóa K mở, bộ nguồn hai pin); tô nhánh N đỏ, nhánh S xanh như quy ước; gắn `% giuhinh`.
- I.13, III.5: thêm chấm trạng thái viền đen theo quy ước đồ thị.

## Vẽ lại hình thực tiễn (PHIÊN FABLE 14/11/2026)

- II.1 (cân – nam châm chữ U – khung dây – khóa K – bộ nguồn, `% giuhinh`): vẽ lại theo toạ độ điểm ảnh của ảnh nhúng trong PDF (656 × 534, phóng 2 lần), rộng 7,6 cm. Giữ đủ mọi nét của hình gốc (kể cả đoạn cạnh trái mặt cân, vách trái và đáy lòng nam châm, mặt trong cực N nhìn qua khe); tô khối theo một hướng sáng (trên – trái – trước): mặt trên sáng, mặt trước chuyển màu, mặt bên phải tối; nhánh N đỏ, nhánh S xanh (đậm hơn để bản in xám vẫn phân biệt), đáy lòng nam châm chia hai màu theo vạch giữa; bóng nam châm đổ trên mặt cân; mặt cân, mặt trước, mặt bên của cân ba độ xám, viền sáng mép trên; khung dây màu đồng hai lớp nét có vệt sáng; chốt A, B là hai núm kim loại nhỏ; khóa K mở và bộ nguồn hai pin vẽ đúng vị trí gốc.
- **Nội dung vật lí giữ nguyên như hình TikZ trước**: thứ tự bản cực tính từ phía K đến B là dài – ngắn – dài – ngắn (bản dài mảnh = cực dương ở phía K, nối về A qua K); đoạn dây đi từ A thẳng xuống (phía trước nam châm), chạy xiên theo chiều sâu qua khe giữa hai cực ra phía sau rồi thẳng lên B; N bên trái, S bên phải.
- Đối chiếu lại cực nguồn trên ảnh gốc (ảnh nhúng phóng 6 lần và ảnh trang 400 dpi): bốn vạch bản cực từ K đến B có chiều cao lần lượt khoảng 42, 20, 40, 18 điểm ảnh gốc, tức dài – ngắn – dài – ngắn; cách đọc "cực dương (bản dài) ở phía K" khớp ảnh gốc. Lưu ý: trên ảnh gốc bốn vạch có bề dày nét như nhau (không thấy rõ "bản ngắn đậm"), nên cực chỉ phân biệt được bằng độ dài vạch; hình vẽ lại vẽ bản ngắn đậm hơn theo kí hiệu SGK.
- I.7 (khung dây ABCD trong từ trường), I.13, III.5 (đồ thị): sơ đồ, giữ nguyên.
- Hình chưa ưng: không.
