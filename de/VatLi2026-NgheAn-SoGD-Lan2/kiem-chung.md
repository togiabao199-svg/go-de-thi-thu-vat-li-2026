# Kiểm chứng đáp án – VatLi2026-NgheAn-SoGD-Lan2

Nguồn: `kho/goc/Nghe An - So GDDT - Lan 2.docx` (Sở GD&ĐT Nghệ An, KSCL kết hợp thi thử lớp 12, Đợt 2, mã đề 0304; trùng file PDF "Liên trường Nghệ An – Lần 3"), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python (`/tmp/VatLi2026-NgheAn-SoGD-Lan2/py/kiem.py`).

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | B B A C B C B B D C A A A B D C C A | trùng (I.2 xem dưới) | I.6: công = diện tích dưới đường: Hình 1: 2, Hình 2: 4, Hình 3: < 3, Hình 4: 3 (atm·lít); I.10: p = μkT ⇒ μ₁ = 1,5μ₂; I.12: β⁺ ⇒ số neutron tăng 1; I.15: bảo toàn số khối với ⁹⁵Mo (xem sửa lời đề) |
| **I.2** | **B (Hình 2)** | **B và C đều đúng** | **Hình 1 và Hình 2 cùng chiều nam châm (cực S hướng vào vòng dây), chuyển động ngược chiều nhau, chiều i_c vẽ ngược nhau ⇒ cùng đúng hoặc cùng sai; tương tự Hình 3 – Hình 4; Hình 1 – Hình 3 (nam châm ngược, cùng chiều v, cùng chiều i_c) có đúng một hình đúng. Vậy đề luôn có 2 phương án đúng: {Hình 1, Hình 2} hoặc {Hình 3, Hình 4} tùy cách hiểu phần nào của vòng (elip) ở phía trước. Theo quy ước của đáp án gốc (Hình 2 đúng) thì Hình 1 (C) cũng đúng.** Gõ `\True` ở B theo đáp án gốc, hình giữ nguyên bản gốc, `% KIỂM TRA`. Đề xuất sửa: đổi chiều i_c ở Hình 1 (khi đó chỉ B đúng). Thầy quyết. |
| II.1 | Đ S Đ S | trùng | |
| II.2 | S Đ Đ S | trùng | v hướng ra (+z), B sang phải (+x): F = qv × B hướng lên ⇒ M dương, N âm (a Sai); U = 2rBv, Q = πr²v ⇒ U = 2BQ/(πr) (c Đúng); Q = πrU₀/(2B) ≠ πU₀r/B (d Sai) |
| II.3 | S S Đ Đ | trùng | ¹³¹₅₃I → ⁰₋₁e + ¹³¹₅₄Xe |
| **II.4** | **Đ Đ Đ Đ** | **Đ Đ S Đ** | **Lệch ý c.** Hình: B ở vị trí (1) (bên phải), khung quay (1)→(2)→(3) (ngược chiều kim đồng hồ khi nhìn từ phía trước, BC ở đầu xa), $\vec B$ từ N sang S (sang phải). Tại t = 0 cạnh AB đi lên: v × B = (lên) × (phải) hướng ra xa người nhìn, tức từ A đến B ⇒ trong BC dòng điện chạy **từ B đến C**. Kiểm lại bằng Lenz: khung nghiêng (cạnh B lên, cạnh C xuống), từ thông qua mặt có pháp tuyến hướng lên (chiều A→B→C→D) âm và tăng độ lớn ⇒ e > 0 theo chiều A→B→C→D. Vectơ tính bằng numpy: ω = −ŷ, r_B = x̂ ⇒ v = ẑ, v × B = ŷ. Lời giải gốc chỉ ghi "dùng quy tắc bàn tay phải… từ C đến B", không có lập luận. Gõ c) Sai, `% KIỂM TRA: Đ / S`. |
| III.1–III.6 | 9,6 / 19 / 67 / 3,26 / 22,9 / 31,4 | trùng | |

## Phép tính chính
- III.1: 13,5·2^(−43/88) = 9,621 kg.
- III.2: N = 13 500/238·6,02·10²³·2^(−53/88) = 2,249·10²⁵; λ = ln2/(88·365·86 400); H = 5,618·10¹⁵ Bq; P = H·5,6·1,6·10⁻¹³·0,064 = 322,2 W; E/phút = 19,33 kJ.
- III.3: T = 15 ms (đọc đồ thị: hai cực đại/cực tiểu cách nhau 15 ms; nửa chu kì 7,5 ms) ⇒ f = 66,7 Hz.
- III.4: F_max = NBI₀πd = 45·0,08·4·3,14·0,072 = 3,2556 N (π chính xác: 3,2572 N, vẫn 3,26).
- III.5: n = 1,01·10⁵·0,565/(8,31·300) = 22,89 mol.
- III.6: n₁ = 1,01·10⁵·0,465/(8,31·300) = 18,84 mol; 25n₁ = 470,97 mol; m = 470,97/15 = 31,40 kg.
- Đề gốc không có khối "Cho biết" và không cho N_A, R (III.2, III.5, III.6 dùng N_A = 6,02·10²³, R = 8,31 như lời giải gốc). Kết quả không đổi khi dùng N_A = 6,022·10²³ (19,34 kJ) hay R = 8,314 (22,88 mol; 31,38 kg). Giữ nguyên đề (không thêm "Cho biết") — thầy xem có thêm không.

## Hình
- 6 hình gốc: I.2 (4 hình nam châm – vòng dây), I.6 (4 đồ thị p–V), I.8 (bảng thời tiết dạng ảnh → gõ lại thành `tabular`, biểu tượng nhỏ vẽ bằng `\tikz` nội dòng), II.2 (ảnh lưu lượng kế + sơ đồ), II.4 (máy phát điện), III.3 (loa điện động: hình a mặt cắt loa + nam châm hình trụ có cuộn dây; hình b đồ thị i–t).
- II.2: ảnh lưu lượng kế vẽ lại chi tiết theo yêu cầu bổ sung 13/11 (ống thép mạ kẽm có vân, mặt bích, kẹp có bulông, thân cảm biến bóng, thanh đỡ dưới, khung ngang + 6 thanh đứng có đầu tròn, giá chữ U, cổ nối, đầu hiển thị tròn có gờ, kính, 4 nút, hai đầu cáp, bóng đổ, nghiêng 7° như ảnh). Màn hình của ảnh gốc có số (17909.00, 0.00007) không phải dữ kiện ⇒ để trống. Macro riêng trong file đề: `\VLtrudoc`, `\VLgalvan`, `\VLdauhienthi`.
- III.3 hình a: tô lại nón loa (chuyển màu ngang, viền gân), nam châm hình trụ phóng to, bóng đổ, phản quang lõi N.
- II.4: nam châm N đỏ, S xanh (ảnh gốc trắng xám); điện trở R tô màu gỗ nhạt (gốc xanh dương, tránh trùng màu từ trường).
- III.3 hình b: ảnh gốc có hai đoạn đường cong chồng nhau (một đoạn i = 4cos(2πt/15) từ 0 đến 7,5 ms, một đoạn cực tiểu tại ≈ 3 ms, cực đại tại ≈ 10,5 ms, kết thúc tại (16,7; −3)); cả hai đều có chu kì 15 ms. Vẽ lại đúng như gốc (không ảnh hưởng đáp số); thầy có thể muốn gộp thành một đường.

## Sửa lời đề (lỗi chữ bản gốc)
- I.3, I.4: in đậm từ phủ định "**không**", "**sai**".
- I.5, II.4: "khí lý tưởng", "tỷ lệ", "nguyên lý" → "khí lí tưởng", "tỉ lệ", "nguyên lí"; I.18, III: "chu kỳ" → "chu kì".
- **I.15 phương án D: "⁸⁵₄₂Mo" → "⁹⁵₄₂Mo"** (bản gốc không bảo toàn số khối: 235 + 1 ≠ 85 + 139 + 2; với 95 thì 236 = 95 + 139 + 2, điện tích 92 = 42 + 57 − 7).
- II.2: "$\vec B$ vuông góc…": kí hiệu vectơ thống nhất `\vv`; dấu ";" trước "làm tích điện" → ",".
- II.3: "các Sao" → "các sao"; "Đồng vị Iod (¹³¹53I)", "Xenon (¹³¹54Xe)" → "Đồng vị iodine ¹³¹₅₃I", "xenon ¹³¹₅₄Xe" (thuật ngữ SGK, bỏ ngoặc).
- II.4: "stato" → "stator" (thống nhất với "Rotor").
- III (dữ kiện câu 1–2): "chu kỳ phóng xạ là 88 năm" → "chu kì bán rã là 88 năm"; "nhiệt lượng tỏa ra trong một phóng xạ" → "trong mỗi phân rã"; "238 g/mol" viết đơn vị thường; III.2 "kilôJun" → "kilôjun".
- III.3, III.4: "Hertz (Hz)", "Newton (N)" → "hertz (Hz)", "newton (N)".
- III.5–III.6: "Oxygen", "Carbon dioxide" → "oxygen", "carbon dioxide".
- Ba cặp câu dùng chung dữ kiện ("Sử dụng các thông tin sau cho Câu 1 và Câu 2"…): đoạn dữ kiện đặt trong câu đầu của cặp, mở đầu "Dùng thông tin sau cho câu 1 và câu 2:" (nhãn `NgheAn-SoGD-Lan2-III1`…`III6`).
