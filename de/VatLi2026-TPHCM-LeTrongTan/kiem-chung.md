# Kiểm chứng đáp án – VatLi2026-TPHCM-LeTrongTan

Nguồn: `kho/goc/TP HCM - THPT Le Trong Tan.docx` (mã đề 0201, có bảng đáp án và lời giải tham khảo). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | C C D A B A B B D A B D B D A B C D | trùng | I.9: hóa hơi 1025 − 125 = 900 kJ, Δt = 78 − 28 = 50 K; I.15: V₂ = 1,6·15/3 = 8 lít, ΔV = 7 lít; I.17: W_lkr = 1,11 / 2,83 / 7,04 MeV/nucleon; I.18: A = 200 − 120 = 80 J (nhận công) |
| II.1 | S Đ Đ Đ | trùng (ý b: xem ghi chú) | m = 97 − 25 = 72 g; Q = 408·60 = 24 480 J; λ = 24 480/0,072 = 3,4·10⁵ J/kg. **Ý b) đề không cho số liệu nhiệt độ nước trong hai cốc; lời giải gốc chỉ viện dẫn "theo đáp án tham khảo". Gõ theo gốc (Đúng), lập luận: cốc B ít nước hơn nên nhận nhiệt môi trường nóng lên nhanh hơn. Có `% KIỂM TRA` — thầy xem.** |
| II.2 | Đ Đ S Đ | trùng | e = IR = 3·10⁻³·2 = 6·10⁻³ Wb/s |
| II.3 | Đ S S Đ | trùng | W_lk = 1,862·931,5 ≈ 1734 MeV (7,38 là W_lkr); E = 1000/235·6,02·10²³·175·1,6·10⁻¹³ ≈ 7,17·10¹³ J |
| II.4 | S Đ Đ S | trùng | T = pV/(nR) = 1,1·10⁵·25·10⁻⁶/(9,11·10⁻⁴·8,31) ≈ 363,26 K → 90,26 °C |
| III.1–III.6 | 2288 / 5,16 / 12 / 28,4 / 2,9 / 62,8 | trùng | III.1: n(D₂O) = 0,15/20 = 7,5·10⁻³ mol, số phản ứng = số phân tử D₂O, E ≈ 2287,9 MJ; III.2: r₂ = 4·(15/7)^(1/3) ≈ 5,157 mm; III.3: 308/275 − 1 = 12 %; III.4: E₀ = 125,6 V, Q = E₀²t/(2R) ≈ 28 396 J (π chính xác: 28,42 kJ, vẫn 28,4); III.5: N_Pb/N_U ≈ 0,5694, t = 4,47·ln1,5694/0,693 ≈ 2,907 tỉ năm; III.6: Q = 59 535 J < 80 640 J, nước đá tan 177,19 g, còn 62,8 g |

## Sửa lời đề (lỗi chữ bản gốc)
- **I.17: bản gốc in phương án B và C giống hệt nhau (²₁H; ³₁H; ⁴₂He), đáp án gốc C. Sửa phương án C thành ⁴₂He; ³₁H; ²₁H (thứ tự giảm dần độ bền, khớp lời giải gốc). Thầy xem lại.**
- I.5: dấu chấm cuối câu hỏi "ứng dụng nào sau đây." → "?".
- I.8: phương án viết hoa đầu ("Các hạt phấn hoa…", "Nhiệt độ…", "Quỹ đạo…") → viết thường (nối tiếp câu dẫn "Kết quả cho thấy").
- I.9: "rượu Etylic" → "rượu ethylic".
- I.10: tên đơn vị viết thường theo SI: tesla, volt, ohm, ampere.
- I.13: "heli" → "helium" (thống nhất với I.17).
- I.18: "piston" → "pit-tông" (thuật ngữ SGK).
- II.4: câu dẫn bị ngắt "…không đổi (1,1.10⁵ Pa). Một nhóm học sinh…" → "…không đổi ($1{,}1\cdot 10^5$ Pa), một nhóm học sinh…".
- II.4 (hình): nhãn "Xi lanh" → "Xilanh".
- III.6: đơn vị "J/kg.K" → "J/(kg.K)".

## Hình
- 4 hình, vẽ lại bằng TikZ, so hình ở `so-hinh/`: I.9 (đồ thị t – Q), II.1 (bộ thí nghiệm đo nhiệt nóng chảy riêng; Bảng 1 gõ bằng `tabular` đặt cạnh hình), II.2 (cuộn dây – nam châm – điện kế), II.4 (thí nghiệm đẳng áp: giá đỡ, nhiệt kế, xilanh, áp kế).
- II.1, II.2, II.4 là hình thực tiễn: `% giuhinh`. Màn hình cân điện tử để trống; mặt Joulemeter, áp kế không ghi số.
- II.2: nam châm N đỏ, S xanh (đề có ghi cực).
- II.1 có `% tachDS` (cho tách câu dẫn – bảng của câu đầu Phần II) để trang 3 không trống 13,5 cm; bản đề còn 6 trang.
