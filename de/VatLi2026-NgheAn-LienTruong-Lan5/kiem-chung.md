# Kiểm chứng đáp án – VatLi2026-NgheAn-LienTruong-Lan5

Nguồn: `kho/goc/Nghe An - Lien truong Nghe An - Lan 5.docx` (Liên trường THPT Nghệ An, thi thử lần 5; đề không ghi mã). Có bảng đáp án và lời giải tham khảo.
Mọi câu đã giải lại; các câu có số liệu tính lại bằng Python (script ở thư mục nháp).

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | B C D A D B A A C B B D D B A B B A | trùng | I.8: $p=\frac13\rho v^2$; I.10: dưới dây, $\vec B$ hướng vào; dòng cảm ứng cùng chiều kim đồng hồ ⇒ từ thông vào đang giảm ⇒ ra xa dây, hướng (4) |
| II.1 | S S Đ Đ | trùng | |
| II.2 | Đ Đ S Đ | trùng | d) độ dốc $p$ theo $1/V$ bằng $pV=nRT$ |
| II.3 | S S Đ Đ | trùng | d) từ $t_1$ đến $t_3$ $i$ giảm liên tục; theo chiều quấn trên Hình 2a (dòng từ $a$ chạy mặt trước từ trái sang phải: ngược chiều kim đồng hồ nhìn từ trên; cuộn nhận đi từ $c$ mặt trước từ phải sang trái) và định luật Lenz, dòng cảm ứng ra mạch ngoài ở đầu $c$ ⇒ $V_c>V_d$ |
| II.4 | S Đ Đ S | trùng | d) đọc đồ thị: $(90;\,6{,}24)$, $(160;\,6{,}00)$ (đơn vị $\times10^{-1}$) ⇒ $\lambda=3{,}43\cdot10^{-4}$ ngày$^{-1}$ ($T\approx5{,}5$ năm, khớp Co-60); $H/H_0=e^{-0{,}257}=0{,}773$ ⇒ $t=15/0{,}773=19{,}4$ phút ≠ 25 phút |
| III.1–III.6 | 3,0 / 1,3 / 9,7 / 21 / 163 / 5,7 | trùng | III.1: $33/11=3$; III.2: $1+1/3=1{,}33$; III.3: $n=\frac{pV}{RT}=0{,}019603$ mol, $n_{O_2}=0{,}0495n=9{,}704\cdot10^{-4}$; III.4: $1{,}2/9{,}704\cdot10^{-4}=1236{,}7$ nhịp/giờ ⇒ $20{,}6$ ⇒ 21; III.5: $115\sqrt2=162{,}6$; III.6: $3{,}5\cdot10^{-5}\cdot162{,}6=5{,}69\cdot10^{-3}$ N |

Ghi chú: đề gốc không có khối "Cho biết"; III.3 dùng $R=8{,}31$ J/(mol.K) như lời giải gốc (lấy $8{,}314$ vẫn ra $9{,}7$). Không bổ sung "Cho biết".

## Sửa lời đề (lỗi chữ bản gốc)
- I.2: "10C" (lỗi MathType) → "$1\,^\circ$C".
- I.6: "hypebol" → "hyperbol" (thuật ngữ SGK 2018).
- I.8: "khí lý tưởng" → "khí lí tưởng" (thống nhất trong đề).
- I.12: "đóng – mở" giữ, câu hỏi "Lực hút thanh sắt..." xuống dòng như bản gốc.
- II.1: "ghi nhân" → "ghi nhận".
- II.2: "xi lanh" → "xilanh", "pittông" → "pit-tông", "( T₂, T₃,...)" → "($T_2$, $T_3$, …)"; c) "loại bỏ toàn bộ bộ số liệu" giữ nguyên (đúng nghĩa: cả bộ số liệu).
- II.3: "như Hình 2b,  Quy ước" → "như Hình 2b. Quy ước".
- II.4: "Cobalt-60" → "cobalt-60"; "kỹ thuật", "ký sinh", "kỹ sư" → "kĩ thuật", "kí sinh", "kĩ sư"; "bảo quan" → "bảo quản"; "để để đo" → "để đo"; "ln(H)" → $\ln H$; bỏ dòng chữ thừa "ĐS: 19" (đáp số lọt vào cuối câu II.4 bản gốc).
- III.1–2: "$t_l=11$°C" → "$t_1=11\,^\circ$C"; "44 0C" → "$44\,^\circ$C".
- III.3: "0,50 l" → "0,50 lít"; "1,01.105Pa" → "$1{,}01\cdot10^5$ Pa"; "370C" → "$37\,^\circ$C"; "x.10-4" → "$x\cdot10^{-4}$".
- Phần III: "Sử dụng các thông tin sau cho câu 1 và Câu 2" → khối dữ kiện chung đặt trong câu đầu cặp, mở bằng "Dùng thông tin sau cho câu 1 và câu 2:" (tương tự cặp 3–4, 5–6).
- I.5 "sai" đã in đậm trong bản gốc (giữ \textbf).

## Hình
- 6 hình vẽ lại bằng TikZ: I.10 (sơ đồ dây – vòng dây, đặt bên phải phương án), I.12 (mạch rơ-le, đặt bên phải phương án), II.1 (sơ đồ thí nghiệm Brown + đường gấp khúc), II.2 (bộ thí nghiệm Boyle: áp kế, xilanh, bình nước, nhiệt kế, tay quay; đặt bên phải đoạn dẫn như bản gốc), II.3 (ô tô sạc không dây, cuộn phát/nhận, đồ thị $i(t)$), II.4 (đồ thị $\ln H$ theo $t$).
- II.2: mặt áp kế và thước xilanh chỉ giữ vạch chia, bỏ số (không phải dữ kiện của đề).
- II.4: trục $\ln H$ của ảnh gốc chia không đều (6,24 đặt sát 6,25); bản vẽ lại dùng thang đều, ghi 6,24 tại vạch gióng và chỉ để vạch (không ghi số) ở 6,25 cho khỏi chồng chữ. Các điểm đo vẽ theo vị trí tương đối như ảnh gốc (đường thẳng qua hai điểm gióng $(90;\,6{,}24)$ và $(160;\,6{,}00)$).
