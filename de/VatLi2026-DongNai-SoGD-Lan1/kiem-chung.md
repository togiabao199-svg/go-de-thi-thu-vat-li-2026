# Kiểm chứng đáp án – VatLi2026-DongNai-SoGD-Lan1

Nguồn: `kho/goc/Dong Nai - So GDDT - Lan 1.docx` (Sở GD&ĐT Đồng Nai, mã đề 0224, có đáp án và lời giải tham khảo). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | C C B B A D C B A C A D B C B A C D | trùng | I.5: 29V = 9(20 − V) ⇒ V = 180/38 ≈ 4,74 lít; I.9: 0,15·4180·10 = 6270 J; I.13: e = 2·10⁻³·1,5/2·10⁻⁴ = 15 V, I = 75 mA; I.16: F = 0,1·3,5·0,02·sin30° = 3,5 mN |
| II.1 | Đ Đ Đ S | trùng | Nhiệt độ đứng yên 80 °C từ phút 8 đến phút 11; 80 + 273 = 353 K |
| II.2 | S Đ Đ S | trùng | |
| II.3 | Đ S Đ Đ | trùng | d) n = p/(kT) với k = R/N_A: các cặp số liệu cho 2,45–2,46·10²⁵ m⁻³, trung bình 2,456·10²⁵ ≈ 2,46·10²⁵ (với k = 1,380649·10⁻²³ thì cặp đầu cho 2,455·10²⁵). |
| II.4 | Đ S Đ S | trùng | B = mg/(NIL) = 0,196/(50·0,30·0,050) ≈ 0,261 T; B hướng ra (chấm), F hướng xuống ⇒ I từ Q đến P |
| III.1, III.2 | 5,33 / 125 | trùng | e = 100·2·10⁻⁴·4·10⁻³·cos60°/2 = 2·10⁻⁵ V; Q = e²t/R = 5,33·10⁻¹⁰ J |
| **III.3** | **63** | **6** | **Lệch.** E₀ = NBSω = 200·0,4·25·10⁻⁴·20π = 4π ≈ 12,57 V; lúc t = 0 mặt phẳng khung song song đường sức nên e = E₀cos ωt, quay 60°: \|e\| = 2π ≈ 6,28 V ⇒ 6. Lời giải gốc viết "4π ≈ 125,6 V" (nhầm hệ số 10) nên ra 63. File gõ theo 6, có `% KIỂM TRA` — thầy xem lại. |
| III.4–III.6 | 7,3 / 1,6 / 4 | trùng | III.4: t = 9250/1260 ≈ 7,34 °C; III.5: 1,5·318/300 = 1,59; III.6: N = 3,62·10²⁵, N/2 : 7,5·10²² = 241,5 phút ≈ 4,02 giờ |

## Sửa lời đề (lỗi chữ bản gốc)
- Tiêu đề gốc ghi nhầm "Môn thi: TOÁN, 60 phút" và không ghi lần: khung tiêu đề theo quy định (Môn Vật lí, 50 phút, Lần 1 theo kiểm kê).
- I.6: in đậm "**không**".
- I.13: "(Transcranial Magnetic Stimulation - TMS)" → dùng gạch nối "--".
- II.3: "đóng - mở" → "đóng -- mở".
- Đơn vị viết lại theo quy chuẩn (μs, cm², phân tử/m³, J/(kg.K)).
- Câu dùng chung dữ kiện (I.8–I.9, III.5–III.6): đoạn "Dùng thông tin sau cho câu … và câu …" đặt trong câu đầu của cặp, tham chiếu bằng `\label`/`\ref`.

## Ghi chú khác
- Đề gốc không có khối "Cho biết" (không cho R, N_A, k) dù II.3d và III.6 cần R, N_A: theo quy định không thêm khối; lời giải dùng R = 8,31 J/(mol.K), N_A = 6,02·10²³ mol⁻¹ như lời giải gốc. Thầy quyết có thêm dòng "Cho biết" hay không.
- Đề gốc đánh số mỗi phần từ câu 1 (giữ nguyên).

## Hình
- 5 hình vẽ lại bằng TikZ có tô màu: I.8 (bếp hâm cà phê), II.1 (thí nghiệm nóng chảy băng phiến), II.2 (sạc không dây, hình phóng to cuộn N_A, N_B), II.3 (quả cầu khí – khí áp kế – bếp điện), II.4 (đòn cân – khung dây MNPQ trong từ trường). Ảnh so trong `so-hinh/`.
- Màn hình nhiệt kế điện tử để trống (bản gốc hiện số không có trong đề).
- II.1, II.2, II.3 đặt hình bên phải đoạn dẫn (như bố cục gốc) để không trống trang.
