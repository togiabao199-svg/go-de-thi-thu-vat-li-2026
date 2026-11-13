# Kiểm chứng đáp án – VatLi2026-NinhBinh-SoGD-Lan3

Nguồn: `kho/goc/Ninh Binh - So GDDT - Lan 3.docx` (Sở GD&ĐT Ninh Bình, khảo sát lần 3, mã đề 0201), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại; câu có số liệu tính bằng Python (script ở thư mục nháp).

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | A D C D B B A D C C D A B B A A C C | trùng | I.10: $\vec F=I\vec l\times\vec B$, $\vec l$ hướng Bắc, $\vec B$ hướng xuống → lực hướng Tây; I.15: dòng điện đi vào, tại M (phía Bắc dây) $\vec B$ hướng Đông; I.16: $E_\text{lkr}$ lớn nhất ở $A\approx 50$–$80$ → Cu-63 |
| II.1 | S S S Đ | trùng | phân hạch tỏa năng lượng; neutron chậm bắn vào U-235; sản phẩm không xác định; qua U-236* |
| II.2 | S Đ S Đ | trùng | $e=250\cdot 18\cdot10^{-4}\cdot 14\cdot10^{-3}/(3\cdot10^{-3})=2{,}1$ V |
| **II.3** | **S Đ Đ Đ** | **S Đ Đ S** | **Lệch ý d.** Trên hình, (1) và (3) cùng nằm trên đường nét đứt qua O (đo ảnh gốc: $V_2:V_1:V_3\approx 1:2{,}03:3{,}9$). $p_3=p_2=2p_1$, $p_3/V_3=p_1/V_1$ → $V_3=2V_1=4V_2$ → $T_3=4T_2$, không phải 3 lần. Lời giải gốc ghi "từ hình vẽ có $V_3=3V_2$" là không đúng với hình. File gõ S Đ Đ S — thầy xem lại. |
| II.4 | Đ S Đ Đ | trùng | Ghi chú: nhiệt kế y tế có chỗ thắt (chỉ nhiệt độ cực đại), nhiệt kế ở bình (2) thực tế không hạ xuống được khi nước nguội; đề và đáp án gốc bỏ qua chi tiết này, giữ theo gốc. |
| III.1–III.6 | 90 / **3,7** / 1,94 / 8,36 / 8,9 / 2,8 | 90 / **5,6** / 1,94 / 8,36 / 8,9 / 2,8 | xem dưới |

Các phép tính chính:
- III.1: mỗi chu trình áp suất giảm một nửa: $512/2^n=1\Rightarrow n=9$; $t=9\cdot 10=90$ s.
- **III.2 (lệch đáp án):** lưới hình gốc có 5 đường ngang, $p_0$ ở đường thứ 4, (2) ở đường thứ 1; 5 đường dọc cách đều, $V_0$ ở đường 1, (2) ở đường 4. Đọc theo ô lưới: $p_2=p_0/4$, $V_2=4V_0$ → $p_2V_2=p_1V_1$, $T_2=T_1$, $\Delta U=0$ (không cần biết khí đơn nguyên tử): $Q_a=3p_0V_0$, $Q_b=1{,}875p_0V_0$, $Q_c=0{,}75p_0V_0$ → $x=1{,}6$, $y=4$, $x+y=5{,}6$. Lời giải gốc đọc $p_2=p_0/3$ và dùng $U=\frac32 pV$ (giả thiết khí đơn nguyên tử, đề không cho) → $x=1{,}4$, $y=2{,}33$, $x+y=3{,}7$. Ảnh gốc vẽ lưới không đều (hai hàng dưới cao 60 px, ba hàng trên 44 px) nên đo pixel ra $p_2/p_0\approx 0{,}29$, lưng chừng giữa 1/3 và 1/4. File gõ 5,6 theo lưới (hình TikZ vẽ lưới đều, $p_0$ = 4 ô, (2) ở ô 1). **Thầy quyết:** giữ 5,6; hoặc giữ đáp án gốc 3,7 thì phải sửa hình ($p_0$ ở đường lưới thứ 3) và thêm "khí lí tưởng đơn nguyên tử" vào lời đề.
- III.3: $Q=15\cdot 1000\cdot 1{,}5=22\,500$ cal; $m=22\,500/580=38{,}79$ g; $38{,}79/20=1{,}94$ g/phút.
- III.4: $\Delta m=0{,}2692$ amu; $W_\text{lk}=250{,}76$ MeV; $W_\text{lkr}=8{,}359\approx 8{,}36$ MeV.
- III.5: $\omega=314$ rad/s; $E_0=12{,}56$ V; $E=8{,}88\approx 8{,}9$ V.
- III.6: $e_\text{c}=0{,}16\cdot 15=2{,}4$ V. Hình gốc: kí hiệu $\vec B$ là ⊕ (hiểu là hướng vào trong), nguồn đặt cạnh phải, bản cực dài (cực dương) ở trên → dòng do nguồn ngược chiều kim đồng hồ; $B$ vào trong và tăng → dòng cảm ứng ngược chiều kim đồng hồ: cùng chiều, $I=(6+2{,}4)/3=2{,}8$ A (nếu $B$ hướng ra thì $1{,}2$ A). TikZ vẽ ⊗ (kí hiệu SGK cho hướng vào), khớp đáp án gốc.

## Sửa lời đề (lỗi chữ bản gốc)
- I.4: "…của một vật. Một bạn học sinh…" → "…của một vật, một bạn học sinh…".
- I.7: "…của khí lí tưởng. Hằng số Boltzmann là $k$…" → "…của khí lí tưởng, hằng số Boltzmann là $k$…"; kí hiệu $\overline{E_\text{d}}$ → $\overline{E}_\text{đ}$.
- I.8, I.9, I.18: in đậm "không đúng", "không" (I.8, I.9, I.18 gốc đã in đậm; giữ).
- I.12: thêm dấu phẩy "…và bàn gỗ, mối liên hệ…".
- I.14, I.16, II.1, III.4: kí hiệu hạt nhân gõ lại đúng dạng (bản gốc vỡ: "29^{63}Cu", "92^{235}U", "15^{30}P", "z_1^{A_1}X"); chỉ số $z_1$, $z_2$ → $Z_1$, $Z_2$.
- I.15: "địa lý" → "địa lí"; "Véc tơ" → "Vectơ". Kí hiệu dòng điện ⊕ trong hình → ⊗ (lời đề đã nói dòng điện đi vào).
- I.16: "đơn giản hoá" → "đơn giản hóa"; $E_{lkr}$ → $E_\text{lkr}$.
- II.1 b): "…động năng rất lớn (cỡ MeV) đến bắn vào…" → "…để bắn vào…".
- II.4: "hợp lý" → "hợp lí"; danh sách dụng cụ giữ dấu "•".
- III.3: "nhiệt hoá hơi của nước" → "nhiệt hóa hơi riêng của nước" (đơn vị cal/g).
- III.5: "quay đều với tốc độ 3000 vòng/phút quay quanh trục" → bỏ chữ "quay" lặp.
- III.6: "$B=2+15\cdot t$" → "$B=2+15t$"; kí hiệu $\vec B$ ⊕ trong hình → ⊗.
- Bỏ "Đáp án: …", "Vì vậy chọn …" của lời giải gốc (ex_test tự in).

## Hình
9 hình vẽ lại bằng TikZ, tô màu (so hình ở `so-hinh/`): I.2 (4 đồ thị), I.5 (xilanh, áp kế, khung phóng to mặt đồng hồ; giữ số chỉ 4 vì có trong lời đề), I.15, I.16 (đồ thị $E_\text{lkr}$, số liệu điểm đo từ ảnh gốc), II.2 (máy đo địa chấn; nam châm để xám vì đề không ghi cực), II.3, II.4 (cốc, bình, nhiệt kế; nhiệt kế y tế bằng macro riêng `\VLnhietkeyte`), III.2 (lưới vẽ đều), III.6 (mạch circuitikz, nguồn `battery1` cực dương ở trên).
