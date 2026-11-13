# Kiểm chứng đáp án – VatLi2026-TuyenQuang-SoGD-Lan2

Nguồn: `kho/goc/Tuyen Quang - So GDDT - Lan 2.docx` (mã đề 0102, có đáp án + lời giải tham khảo). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | A C C C D B B D B A B D B C A B A C | trùng | I.3: 0,5·6,02·10²³ = 3,01·10²³; I.4: t₁ = 90 − 37 700/650 = 32 °C; I.8: E₀ = NBS·2πn = 0,03768 V (π = 3,14); I.11: 25·√2 ≈ 35,36 phút; I.14: N = pV/(kT) ≈ 2,968·10²³, N/6 ≈ 4,95·10²² (mô hình 6 hướng chuyển động như lời giải gốc); I.17: theo chiều quấn trên hình và cực nguồn, mặt dây phía trước có dòng điện đi từ trên xuống, đầu phải ống dây là cực N → đẩy cực N của kim, cực S bị hút |
| II.1 | Đ S Đ Đ | trùng | Φ(0) = 0; Φ(100) = 0,20; Φ(300) = Φ(500) = 0,15 Wb. q = 0,10 + 0,025 = 0,125 C; e₂ = 0,25 V; e₁ = 2 V; e₁/e₂ = 8 |
| II.2 | S S Đ Đ | trùng | Q₁ = 504 000 J; Q₂ = 42 240 J; Q₃ = 678 000 J; P = 1 224 240/(0,75·2100) ≈ 777,3 J/s (582,97 J/s là Q_ích/t) |
| II.3 | Đ Đ Đ S | trùng | T₂ = 522 K; T₃ = 522 + 580 = 1102 K; V₃ = 400·1102/(1,8·290) ≈ 844,4 cm³; V₄ = 1200 cm³ ≠ V₃ |
| II.4 | S Đ S Đ | trùng | X là ⁴₂He, số phản ứng N_A/2 = 3,01·10²³; Δm = 0,0187 amu, E ≈ 17,42 MeV; E tổng ≈ 5,24·10²⁴ MeV |
| III.1–III.6 | 1,18 / 0,42 / 0,19 / 0,4 / 1,99 / 0,03 | trùng | III.1: 0,5/(0,6·sin45°) = 1,1785; III.2: p = 1,02·10⁵ Pa, h = 2Q/(5pS) = 0,4235 m; III.3: x = 4/21 = 0,1905; III.4: a³ = 2/3, x = 4a − 1 = 2,4943, 1/x = 0,4009; III.5: I = 2,857 A, F = 0,1143 N, N = 0,4653 N, a = 1,988 m/s²; III.6: Δm = 0,0345 amu → 0,03 |

III.5: nguồn có cực dương (bản dài) nối với thanh ray phía sau, nên dòng điện qua thanh từ N đến M; với B thẳng đứng hướng xuống, lực từ nằm ngang hướng về phía chân dốc (thành phần dọc dốc F cos β hướng xuống, thành phần vuông góc F sin β làm giảm áp lực), đúng như lời giải gốc. P sin β + F cos β = 0,216 N > μN = 0,116 N nên thanh trượt xuống.

## Sửa lời đề (lỗi chữ bản gốc)
- "lý tưởng" → "lí tưởng" (I.9, III.2, III.3); "kỹ thuật", "vật lý" → "kĩ thuật", "vật lí" (I.10); "chu kỳ" → "chu kì" (I.11); "xi lanh", "piston" → "xilanh", "pit-tông"; "giãn nở" → "dãn nở" (III.2).
- I.4: "Hỏi nhiệt độ ban đầu…" → "Nhiệt độ ban đầu…".
- I.5: bỏ dấu chấm thừa cuối câu dẫn ("… công thức tính ε là.").
- I.18: bản gốc "Khối khí lý tưởng khối lượng m, có mật độ hạt là μ" (m trong công thức là khối lượng MỘT phân tử) → "Một khối khí lí tưởng có mật độ phân tử là μ, khối lượng mỗi phân tử là m, áp suất p; …".
- II.2: "nhiệt hóa hơi riêng của nước sôi 100 °C" → "của nước ở 100 °C"; "540.000 J", "42.240 J" → 540 000 J, 42 240 J; L = Q/m viết dạng phân số.
- III.1–III.6: dấu hỏi chuyển ra sau ngoặc làm tròn ("… bao nhiêu mét (làm tròn …)?"), như các đề đã duyệt. III.5: thêm chữ "điện trở trong" trước r = 0,1 Ω.
- Kí hiệu hạt nhân gõ lại chuẩn (bản gốc vỡ: ^42He, ^73Li, ^{210}84Po, ^63Li).

## Hình
- 5 hình vẽ lại bằng TikZ, so hình trong `so-hinh/`: I.8 (máy phát điện xoay chiều, hình thực tiễn, `% giuhinh`; nam châm phải ghi N tô đỏ, nam châm trái không ghi cực tô xanh), I.17 (ống dây – nguồn – khóa k – kim nam châm; giữ đúng chiều quấn dây và cực nguồn của bản gốc vì đáp án phụ thuộc), II.1 (đồ thị Φ–t), II.3 (chu trình p–T, vẽ đúng tỉ lệ: (2) trên đường qua O, T₃ = 1102 K), III.5 (thanh MN trên ray nghiêng, giữ cực nguồn như gốc).
- II.1: đồ thị gốc vẽ điểm đầu hơi cao hơn trục t (≈ 0,01 Wb) và điểm gấp hơi lệch trước vạch 300 ms — lỗi vẽ tay; lời giải gốc đọc Φ(0) = 0, Φ(300 ms) = 0,15 Wb, file vẽ theo số liệu đó.
