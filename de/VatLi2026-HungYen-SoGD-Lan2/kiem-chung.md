# Kiểm chứng đáp án – VatLi2026-HungYen-SoGD-Lan2

Nguồn: `kho/goc/Hung Yen - So GDDT - Lan 2.docx` (Sở GD&ĐT Hưng Yên, kì thi thử lần 2, mã đề 0215), có bảng đáp án (không có dòng tiêu đề "ĐÁP ÁN") và lời giải tham khảo đủ ba phần. Bản PDF `Hung Yen - So GDDT - chua ro lan.pdf` trùng (cùng mã 0215), không gõ; đã dùng để đối chiếu hình I.2 (cũng không có nhãn $t_1$). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | D D B B D D C C C C B D C C C D B B | trùng | I.2: xem dưới; I.8: e = 1000·0,02·0,3/0,1 = 60 V; I.12: T = (V/nR)p, dốc nhất ↔ V lớn nhất; I.14: đầu phải ống dây là cực Nam ⇒ Hình 2; I.15: E × B cùng hướng v (Nam), B hướng lên ⇒ E hướng Đông |
| **I.2** | **D (1,70)** | **D** | **Hình gốc không ghi nhãn $t_1$** (cả bản Word và bản PDF trùng). Đồ thị có 3 vạch trên trục thời gian; $N_X = N_Y$ tại vạch thứ 3 (t = T). Đáp án gốc 1,70 ứng với vạch thứ 2 (t₁ = 2T/3: 2^(−2/3)/(1 − 2^(−2/3)) = 1,702); vạch thứ 1 (T/3) cho 3,85, không có phương án. Đã ghi nhãn $t_1$ ở vạch thứ 2, ghi `% KIỂM TRA` trong câu. |
| II.1 | Đ Đ S Đ | trùng | |
| II.2 | S S Đ Đ | trùng | Q = 1,2·2,1·18 + 1,2·334 = 446,16 kJ; H = 446,16/(2,5·220) = 81,12 %; c = 0,8112·2,5·250/(1,2·100) = 4,225 ≈ 4,2 kJ/(kg.K); 1,2·4,2·57/24 = 11,97 ≈ 12 kJ/h (dùng c = 4,225 thì 12,04) |
| II.3 | S Đ Đ Đ | trùng | d) e = IR = 4·10⁻³·2 = 8·10⁻³ V = \|ΔΦ/Δt\|. a), b) phụ thuộc chiều quấn dây: hình gốc không thể hiện rõ chiều quấn; hình TikZ vẽ chiều quấn (mặt trước các vòng dây) khớp đáp án gốc (dòng điện ở mạch ngoài từ N đến M khi nam châm ra xa). a) và b) cùng một chuyển động tương đối nên luôn ngược đúng/sai. |
| **II.4** | **Đ Đ Đ S** | **S Đ Đ S** | **Lệch ý a).** "Tổng số proton được bảo toàn": vế trái 92 proton, vế phải 60 + 40 = 100 proton (8 neutron biến thành proton, phát 8 electron); chỉ điện tích được bảo toàn (92 = 60 + 40 − 8). Lời giải gốc "hiểu theo bảo toàn điện tích hay số Z". File gõ theo S, ghi `% KIỂM TRA: Đ / S` — **thầy xem lại**. d) m = 3,456·10¹³/(3,2·10⁻¹¹)/6,02·10²³·235 = 421,6 g ≠ 360 g. |
| III.1–III.6 | 1,04 / 0,21 / 25,8 / 400 / 0,1 / 18 | trùng | xem phép tính dưới |

## Phép tính chính (Python)
- III.1: I = mg·tan 30°/(BL) = 0,0045·10·0,5774/(0,25·0,1) = 1,039 → 1,04 A.
- III.2: N = ½·¼·6,02·10²³ = 7,525·10²² phản ứng; E = 7,525·10²²·17,3·1,6·10⁻¹³ = 2,083·10¹¹ J = 0,208·10¹² J → x = 0,21.
- III.3: Q = 10·4200·75 + 10·2,26·10⁶ = 25,75·10⁶ J → 25,8 MJ (25,75 làm tròn lên, theo đáp án gốc).
- III.4: ΔU = 2500 − 3·10⁵·7·10⁻³ = 400 J.
- III.5: V₁ = 0,3·5/15 = 0,1 lít/phút.
- III.6: T₁ = 320/1,1 = 290,91 K → 17,91 °C → 18.

## Sửa lời đề (lỗi chữ bản gốc)
- Cho biết: "J/mol.K" → "J/(mol.K)"; thống nhất đơn vị ghép "kJ/(kg.K)", "J/(kg.K)" (II.2, III.3).
- I.2, I.12: "như hình vẽ" → "như hình bên" (hình đặt bên phải câu dẫn); I.2 nhãn $N_y$, $N_x$ trên hình đổi thành $N_\text{Y}$, $N_\text{X}$ cho khớp lời đề; thêm nhãn $t_1$ (xem bảng).
- I.5: (2) "λ = T.ln2" → "λ = T ln 2".
- I.6: "nguyên lý" → "nguyên lí".
- I.10: "hiđrô" → "hydrogen", "cacbon" → "carbon" (thuật ngữ SGK 2018); kí hiệu ¹₁H, ¹²₆C gõ lại (bản gốc vỡ thành "1¹H", "6¹²C").
- I.11: "B.I.L.cos α" → "BIL cos α" (cả bốn phương án).
- I.13: in đậm "**không phải**" (bản gốc đã in đậm).
- I.14: "kim-nam châm" → "kim nam châm".
- I.18: phương án viết thường ("sự nóng chảy"...) vì nối tiếp câu dẫn.
- II.1: "xi lanh", "xi-lanh" → "xilanh"; "pit tông" → "pit-tông"; dấu ";" cuối câu dẫn → ":"; mở ngoặc kép viết hoa "Nếu".
- **II.2: "nhiệt hóa hơi riêng của nước là 230,0 kJ/kg" → "2300 kJ/kg"** (sai chữ số/đơn vị; số liệu này không dùng trong các ý). Ý b) "bình nhiệt lượng" → "bình nhiệt lượng kế"; ý d) "của lượng nước bình nhiệt lượng kế ra môi trường coi là không đổi" → "của lượng nước trong bình nhiệt lượng kế ra môi trường là không đổi".
- II.3 d): "4 m.A" → "4 mA".
- **II.4: hạt nhân "⁹⁰₄₀La" → "⁹⁰₄₀Zr"** (Z = 40 là zirconium; phản ứng chuẩn ²³⁵U + n → ¹⁴³Nd + ⁹⁰Zr + 3n + 8e⁻).
- III.2: "Helium" → "helium"; "Nếu tổng hợp từ 1 g hạt ⁴₂He" → "Nếu tổng hợp được 1 g ⁴₂He"; "(J)" → "J".
- III.1, III.2, III.6: thống nhất cách viết yêu cầu làm tròn "(kết quả làm tròn đến chữ số hàng …)" đặt trước dấu "?".
- III.5: "oxy" → "oxygen", "bệnh lý" → "bệnh lí".

## Trình bày
- Đề gốc đánh số từng phần từ câu 1 (không cần đánh số lại). Không có cặp câu dùng chung dữ kiện.
- 8 hình vẽ lại bằng TikZ, tô màu theo bảng màu chung:
  - I.2 đồ thị $N_X$ (đỏ, nét đứt như gốc), $N_Y$ (xanh), lưới dọc chấm; đặt bên phải câu dẫn.
  - I.6 sạc không dây (`% giuhinh`): tay – điện thoại – đế sạc, vòng phóng to hai cuộn dây $N_\text{A}$, $N_\text{B}$ (màu đồng) và đường sức (xanh), khối "ĐIỆN THOẠI / ĐẾ SẠC" với vòng tròn nhỏ; đặt bên phải câu dẫn.
  - I.12 ba đường đẳng tích trên hệ trục $(p, T)$, phần gần gốc nét đứt; đặt bên phải câu dẫn.
  - I.14 bốn ô ống dây có lõi, nguồn "+ −", kim nam châm (cực N đỏ, S xanh). Mặt trước các vòng dây nghiêng "/" như hình gốc (dòng điện vào đầu trái, đi lên ở mặt trước ⇒ đầu phải là cực Nam).
  - I.16 bộ dụng cụ (`% giuhinh`): cân điện tử, biến thế nguồn (biển cảnh báo, núm vặn), oát kế, nhiệt lượng kế, nhiệt kế điện tử; màn hình cân, oát kế để trống (ảnh gốc ghi 0.00); bỏ chữ "DEGASSER UNIT", "DANGER HIGH VOLTAGE..." và số trên núm vặn, giữ "DIGITAL METER", "TARE".
  - II.1 xilanh trong bình nước, giá đỡ, nhãn "Giá đỡ", "Khí", "Nước" (nước tô xanh nhạt trung tính vì thí nghiệm dùng cả nước nóng và nước đá).
  - II.2 đồ thị nhiệt độ – thời gian giữ các mốc 19, 100, 200, 220, 300, 400, 470, 500 s và các điểm đo.
  - II.3 cuộn dây – nam châm (N đỏ, S xanh, nằm trước cuộn dây như gốc) – điện kế mA, điểm M, N (`% giuhinh`). Cuộn dây vẽ dạng xoắn có mặt trước/mặt sau để thấy chiều quấn.
- Ảnh so ở `so-hinh/`.
