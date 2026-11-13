# Kiểm chứng đáp án – VatLi2026-LangSon-SoGD-Lan1

Nguồn: `kho/goc/Lang Son - So GDDT - Lan 1.docx`, gõ mã đề 201 (file gốc có bảng đáp án 6 mã 201–206; dùng cột 201). Lời giải gốc chỉ có cho các câu vận dụng (I.7, II.1–II.4, III.1–III.6); các câu còn lại tự giải. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | D D B A D B D C C A B B C B B A B D | trùng | I.3: đường CD và AB kéo dài qua O (đẳng áp), BC, DA nằm ngang (đẳng tích); I.7: F = 0,02·4·0,5 = 0,04 N; I.18: c đồng nhỏ nhất nên Δt lớn nhất |
| II.1 | S Đ Đ S | trùng | m = 15 kg; Q = 15·4180·55 = 3 448 500 J; A = Q/0,95 = 3 630 000 J; t = 1452 s = 24,2 phút |
| II.2 | Đ Đ S S | trùng | T₂ = 400·6/2 = 1200 K = 927 °C. Ý d: lời giải gốc viết "V₂ = V₃" (sai, trên đồ thị V₂ = 6 lít, V₃ = 2 lít) và ra p₃ = 10⁵ Pa; tính đúng: p₃ = p₂V₂/(2V₃) = 3·10⁵ Pa ≠ 6·10⁵ Pa — kết luận Sai không đổi, lời giải đã viết lại |
| II.3 | Đ Đ S Đ | trùng | F = 0,5·2·0,1 = 0,1 N; 2T = √(P² + F²) > P nên lực căng tăng; tan 45° = F/P ⇒ I = 2 A |
| II.4 | Đ Đ Đ Đ | trùng | e = 100·20·10⁻⁴·0,5/0,1 = 1 V; định luật Lenz |
| III.1–III.6 | 5 / 47 / 5,8 / 1367 / 8 / 2 | trùng | III.1: p = 10⁵·10·0,125/2,5 = 5·10⁴ N/m²; III.2: T₁ = 368/1,15 = 320 K; III.3: 1,05·1,01/1,002 = 1,0583; III.4: √(3·8,31·300/0,004) = 1367,4 m/s; III.5: F = 0,08·2·0,05 = 8 mN; III.6: e = 500·10⁻³·0,2/0,05 = 2 V |

Không có câu lệch đáp án gốc, không có `% KIỂM TRA`.

## Sửa lời đề (lỗi chữ bản gốc)
- "Cho biết": `R = 8,31 J/ mol.K` → `R = 8,31 J/(mol.K)`.
- I.1, I.6, II.3, II.4, III.5, III.6: "vectơ cảm ứng từ B" → `\vv{B}`. I.1 phương án C "cực bắc" → "cực Bắc" (thống nhất với B, D).
- I.4: tên đơn vị viết thường theo SGK (vêbe, vôn, ampe, tesla).
- I.9: thêm dấu "?" cuối câu hỏi; chữ **không** in đậm (bản gốc đã in đậm). I.15: **không** in đậm (bản gốc đã in đậm).
- I.17: "2 V₀" → "2V₀".
- II.2: "khí lý tưởng" → "khí lí tưởng".
- III.2: "Hãy xác định nhiệt độ ban đầu của khối khí này là theo đơn vị °C?" → "… của khối khí này theo đơn vị °C." (bỏ chữ "là" thừa).
- III.4: dấu "?" đưa ra sau ngoặc yêu cầu làm tròn.
- III.5: "milliNewtons (mN)" → "milinewton (mN)"; "I = 2A" → "I = 2 A".
- III.6: "Vôn (V)" → "vôn (V)".
- Bỏ khung tiêu đề, họ tên/số báo danh, mã đề, "Thí sinh không được sử dụng tài liệu…", "HẾT" của bản gốc.

## Hình (4 hình, đều vẽ lại bằng TikZ, so hình trong `so-hinh/`)
- I.3: đồ thị V–T (ảnh `image2.png`, so với vùng cắt ảnh trang 1), bốn quá trình bốn màu, vùng chu trình tô `VLla!35`.
- II.1: sơ đồ máy làm nóng nước (shape Word, cắt ảnh trang 3). Nhãn bản gốc "Núm điều…" bị cắt mất chữ trong textbox → gõ "Núm điều chỉnh". Màn hình giữ "70 °C" (dữ kiện có trong lời đề). Ống nước nóng tô đỏ, ống nước lạnh tô xanh (đã ghi rõ trên nhãn, không phải ý suy luận). Hình đặt bên phải phần câu dẫn (hai `minipage`, câu đầu giữ ngoài) như bản gốc, để Phần II bắt đầu trên trang 3, không để trang 3 trống 15,6 cm; câu có `% giuhinh`.
- II.2: đồ thị V–T chu trình (1)→(2)→(3) (shape Word, cắt ảnh trang 3). Không ghi nhiệt độ ở (2) (học sinh phải tính).
- II.4: đồ thị B–t (shape Word, cắt ảnh trang 4), đường màu `VLxanh`.

## Dàn trang
- Bản đề 5 trang (ĐẠT), bản lời giải 9 trang (trang cuối gần trống, được miễn).
