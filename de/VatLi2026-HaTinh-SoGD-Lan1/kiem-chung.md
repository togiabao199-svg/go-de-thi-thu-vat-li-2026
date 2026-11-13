# Kiểm chứng đáp án – VatLi2026-HaTinh-SoGD-Lan1

Nguồn: `kho/goc/Ha Tinh - So GDDT - Lan 1.docx` (Sở GD&ĐT Hà Tĩnh, mã đề 0303), có bảng đáp án và lời giải tham khảo (lời giải gốc chỉ có Phần II, III). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | C B C C D B B C A A D B C D C C D D | trùng | I.10: p₂ = 12·400/300 = 16 atm; xem I.5, I.8, I.9 dưới |
| **I.5** | **D** | **D (câu lỗi)** | **Câu hỏi lỗi từ bản gốc**: "Hai vật có cùng nội năng khi chúng … D. có cùng nội năng" — phương án D lặp lại câu dẫn (bản thuvienhoclieu tự ghi chú "(lặp do lỗi đề)"). Gõ theo đáp án gốc D, bỏ chú thích "(lặp do lỗi đề)", có `% KIỂM TRA`. Thầy xem có sửa lại câu không. |
| **I.8** | **C (30)** | **C** | **Bản gốc ghi hạt nhân ⁵⁵₂₆Fe** (N = 29, không có phương án). Sửa thành ⁵⁶₂₆Fe (khớp đáp án gốc 30 và câu I.9). Có `% KIỂM TRA`. |
| **I.9** | **A** | **A** | **Đề thiếu dữ kiện**: không cho khối lượng hạt nhân Fe hay năng lượng liên kết riêng. Đáp án A = 8,8 MeV/nucleon × 56 = 492,8 MeV (giá trị thực ≈ 492,3 MeV). Lời giải dùng W_lkr ≈ 8,8 MeV/nucleon. Có `% KIỂM TRA`. |
| II.1 | Đ S Đ S | trùng | (t_max − t₀)/d = 7,40; 7,60; 7,53; 7,45 (TB 7,50); b) Δt = 30,4 °C; d) t_max ≈ 25 + 7,5·5 = 62,5 °C ≠ 57,5 |
| II.2 | Đ Đ S Đ | trùng | n = 2,1·1,013·10⁵·0,03/(8,31·300) = 2,560 mol; p₂ = 2,31 atm; 1 − 300/330 = 9,09 % |
| II.3 | Đ S Đ S | trùng | |
| II.4 | Đ S S Đ | trùng | d) V₂/V₁ = 1,00·360/(1,15·300) = 1,0435 → 4,35 % |
| III.1–III.6 | 2,5 / 450 / 8,5 / 7,1 / 4200 / 2 | trùng | xem phép tính dưới |

## Phép tính chính (Python)
- III.1: p = 1·(50 + 75)/50 = 2,5 atm.
- III.2: 12·50/360 = 1·(50 + N)/300 → N = 450.
- III.3: F = BIb = 0,5·200·0,05 = 5 N; v = Q/(ab) = 1,7·10⁻³/(0,02·0,05) = 1,7 m/s; P = Fv = 8,5 W.
- III.4: Δm = 2·1,0073 + 2·1,0087 − 4,0015 = 0,0305 amu; W_lk = 28,41 MeV; W_lkr = 7,10 MeV/nucleon → 7,1.
- III.5: P = 0,7·1000·6 = 4200 W.
- III.6: m/t = 4200/(4200·30) = 1/30 kg/s = 2 kg/phút.

## Sửa lời đề (lỗi chữ bản gốc)
- I.3: phương án C "λ = 3,34×10⁵, J/kg" bỏ dấu phẩy thừa trước đơn vị.
- I.4: viết số tách nhóm "33 400", "334 000".
- I.5: bỏ chú thích "(lặp do lỗi đề)" ở phương án D (xem bảng trên).
- I.8: ⁵⁵₂₆Fe → ⁵⁶₂₆Fe (xem bảng trên).
- I.11: "(p − V)" → "(p, V)"; "hypebol" → "hyperbol" (thuật ngữ SGK).
- I.14: bỏ dấu hai chấm và kí tự rác sau công thức "Φ = BS cos α"; viết vectơ $\vv{B}$, $\vv{n}$ ở các phương án (ảnh trang mất mũi tên).
- I.16: gộp hai dòng câu dẫn.
- II.4: ý d) bản gốc lặp câu cuối ("Dựa vào số liệu thực nghiệm, thể tích của bình thủy tinh ở 87 °C đã tăng xấp xỉ 4,35% so với ban đầu.") và có dấu chấm thừa trước "1,15·10⁵ Pa": bỏ câu lặp, bỏ dấu chấm.
- II.4: hình gốc có chữ rác "a" trên cảm biến và "........" sau nhãn "Cảm biến áp suất": bỏ, giữ nhãn "Cảm biến áp suất".
- III.1, III.3: "làm tròn kết quả đến 1 chữ số sau dấu phẩy thập phân" → "làm tròn kết quả đến chữ số hàng phần mười" (thống nhất cách viết); III.1, III.2 đặt dấu "?" sau ngoặc làm tròn.
- III.4: "Heli" → "helium", "MeV/nuclon" → "MeV/nucleon" (thuật ngữ SGK 2018); làm tròn như III.3.
- III.5: "bao nhiêu Watt" → "bao nhiêu W".
- Không câu nào có từ phủ định cần in đậm.

## Trình bày
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại).
- Hai khối "Dùng thông tin sau cho câu 1 và câu 2", "… câu 5 và câu 6" (Phần III) đặt trong câu đầu của cặp, mở đầu bằng `\textit{Dùng thông tin sau cho câu~\ref{..} và câu~\ref{..}:}`.
- Hình: 4 hình vẽ lại bằng TikZ, có `% giuhinh` ở 3 hình thực tiễn:
  - I.10 bình chữa cháy (ảnh chụp): thân đỏ `\shade`, nhãn "BÌNH CHỮA CHÁY / BỘT ABC" như ảnh, van đồng, cần bóp đỏ, vòi đen; đặt bên phải câu dẫn + phương án.
  - II.1 bộ thí nghiệm (ảnh chụp): ống đong, giá, cốc nước trên bếp, nhiệt kế điện tử, bình tam giác, bộ điều khiển, nguồn một chiều, dây đỏ/đen; màn hình để trống (ảnh gốc ghi 24.5 °C, 100.0, 10.0 V, 10.0 A — không phải số liệu của bài; phiên chính bỏ cho thống nhất với các đề khác). Đặt cạnh bảng số liệu (bảng cột đầu xuống dòng) để gọn trang.
  - II.4 chậu nước – bình cầu – cảm biến áp suất – nhiệt kế – kiềng – đèn cồn (dùng `\VLnhietke`, `\VLdencon`); đặt bên phải câu dẫn.
  - III.3 sơ đồ hệ thống lò phản ứng (ảnh gốc chữ tiếng Anh "A system layout of a nuclear test facility"): vẽ lại sơ đồ khối (vỏ lò, vùng hoạt, thanh điều khiển, vòng sơ cấp nóng đỏ / nguội xanh, bộ trao đổi nhiệt ống xoắn, tuabin, máy phát), **bỏ toàn bộ chú thích tiếng Anh** vì đề không có chú thích tiếng Việt (theo ghi chú kiem-ke). Hình chỉ minh họa, không dùng để giải.
- Ảnh so ở `so-hinh/`.
