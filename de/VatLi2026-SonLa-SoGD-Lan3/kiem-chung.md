# Kiểm chứng đáp án – VatLi2026-SonLa-SoGD-Lan3

Nguồn: `kho/goc/Son La - So GDDT - Lan 3.docx` (Sở GD&ĐT Sơn La, thi thử lần thứ ba, mã đề 0210; có bảng đáp án và lời giải tham khảo). Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | D A B D D C B D D C D A D A B C A A | trùng | I.9: định luật Boyle, $p$ theo $1/V$ là đường thẳng qua gốc (Hình 2); I.13: $Q=\rho Vc\Delta t=1{,}29\cdot 0{,}45\cdot 10^{-3}\cdot 1005\cdot 27=15{,}75$ J; I.14: định luật Charles (SGK 2018) là đẳng áp. **I.12: xem ghi chú bên dưới** |
| II.1 | S S Đ S | trùng | $Q=24\cdot 180=4320$ J; $\lambda=4320/0{,}015=2{,}88\cdot 10^5$ J/kg ≠ $3{,}3\cdot 10^5$ |
| II.2 | Đ Đ S Đ | trùng | $\lambda=\ln 2/(100\cdot 365\cdot 86\,400)=2{,}198\cdot 10^{-10}$ s⁻¹ (ý c ghi $10^{10}$ nên Sai); $E=2{,}784\cdot 10^{-15}$ J, $N=P/(H\lambda E)=4{,}086\cdot 10^{21}$, $N_0=N\cdot 2^{0,2}=4{,}693\cdot 10^{21}$, $m=0{,}491$ g |
| II.3 | Đ S Đ S | trùng | $T_3=T_1=300$ K; $V_2=V_3=3\cdot 3/1=9$ lít (không phải m³) |
| II.4 | S S Đ S | trùng | $\vv{B}$ hướng vào, lực từ hướng lên khi dòng M → N; $I=mg/(Bl)=5$ A; ý d: $\tan\alpha=0{,}2/0{,}1=2$, $\alpha=63{,}4^\circ$ |
| III.1–III.6 | 97,4 / 18 / 197 / 23 / 0,75 / 0,9 | trùng | III.1: $\Delta m=0{,}1046$ amu, $W=97{,}43$ MeV; III.2: $p_1=1{,}2\cdot 10^5$, $p_2=2{,}7\cdot 10^5$ Pa, $h=0{,}18$ m; III.3: $x=0{,}37141$, $t=197{,}19$ ngày; III.4: $q=2{,}6066\cdot 10^6$ J/kg, $m=23{,}02$ g; III.5: $P=525$ W, $m_0+m_t=1{,}25$ kg (kiểm thêm: nhiệt độ sau khi pha $40\,^\circ$C, $t_x=33{,}3\,^\circ$C, hợp lí); III.6: $e=0{,}008$ V, $R=9{,}067\cdot 10^{-3}$ Ω, $I=0{,}882$ A |

## Chỗ `% KIỂM TRA`
- **I.12**: hình gốc không vẽ chiều dòng điện $I$ nên không xác định được chiều adcba hay dabcd; chỉ phương án A có dòng cảm ứng đổi chiều hai lần (lại gần, qua dây, ra xa). Nói chính xác, dòng cảm ứng đổi chiều khi từ thông qua khung đạt cực trị (trước và sau vị trí đối xứng); tại vị trí đối xứng từ thông bằng 0 nhưng vẫn đang biến thiên cùng chiều nên dòng không đổi chiều ở đó. Lời phương án A chưa chặt; giữ đáp án gốc A.
- **III.5**: đề gốc không yêu cầu làm tròn; đáp số chính xác $0{,}75$ (4 kí tự) nên không cần làm tròn.

## Sửa lời đề (lỗi chữ bản gốc)
- I.1: "kỹ thuật", "Nguyên lý" → "kĩ thuật", "Nguyên lí"; I.7: "Nguyên lý" → "Nguyên lí"; I.15: "vật lý" → "vật lí"; I.18: "Vật lý" → "Vật lí".
- I.3: dấu nhân "." trong các phương án → "$\cdot$".
- I.4: $\overline{E_d}$ → $\overline{E}_{\text{đ}}$.
- I.6, I.15: in đậm "**không**".
- I.10: kí hiệu hạt nhân vỡ "(2⁴He)", "79¹⁹⁷Au" → ${}^4_2\text{He}$, ${}^{197}_{\phantom{1}79}\text{Au}$.
- I.13: "Để làm lượng không khí này lên bằng nhiệt độ cơ thể" (mất chữ) → "Để làm nóng lượng không khí này lên bằng nhiệt độ cơ thể"; bỏ dấu chấm cuối câu dẫn "xấp xỉ là."; tách nhóm số $16\,335{,}0$, $15\,685{,}0$.
- I.17: "vector" → "vectơ"; bỏ dấu chấm cuối câu dẫn "làm cho khung."; "như hình vẽ" → "như hình bên" (hình đặt bên phải phương án).
- II.1: "Lượng nước được sau khi…" (mất chữ) → "Lượng nước thu được sau khi…".
- II.2: "Nickel – 63" → "nickel-63" (tên IUPAC viết thường); "pin Mặt trời" → "pin Mặt Trời"; "1eV", "μW", "8%" gõ lại theo quy chuẩn.
- III.2: "pittông" → "pit-tông", "xi lanh" → "xilanh" (cả nhãn "Xi lanh" trên hình → "Xilanh").
- III.3: "Polonium – 210", "Plumbum – 206" → "Polonium-210", "chì-206" (tên nguyên tố theo SGK); kí hiệu vỡ "84²¹⁰Po", "82²⁰⁶Pb" → ${}^{210}_{\phantom{1}84}\text{Po}$, ${}^{206}_{\phantom{1}82}\text{Pb}$; "Ban đầu một mẫu có trong đó 80% khối lượng…" → "Ban đầu một mẫu có 80 % khối lượng…".
- III.5: đơn vị nhiệt dung riêng "4200 J/kg" → "4200 J/(kg.K)".
- III.6: "$\alpha=POM$" → "$\alpha=\widehat{POM}$"; "$\alpha=2\cdot t$" → "$\alpha=2t$".

## Hình
- 9 hình vẽ lại bằng TikZ (`so-hinh/`): I.9, I.12, I.17, II.1, II.3, II.4, III.2, III.4, III.6.
- II.3: hình gốc vẽ mũi tên trên nhánh hyperbol theo chiều (1) → (3), ngược lời đề "từ (1) đến (2) đến (3) rồi về (1)"; vẽ lại theo lời đề (mũi tên (3) → (1)). Không ảnh hưởng đáp án.
- I.17: hình gốc dùng kí hiệu ⊕ cho $\vv{B}$; vẽ lại theo quy ước ⊗ (vuông góc, hướng vào), lời đề chỉ nói vuông góc nên không ảnh hưởng đáp án.
- II.1: hình gốc chỉ vẽ một dây nối từ oát kế sang nhiệt lượng kế và không vẽ dây điện trở; vẽ lại đủ hai dây nối và cuộn dây điện trở giữa hai cực.
- III.2, III.4 (hình thực tiễn dạng nét vẽ): vẽ có khối, tô nhạt, `% giuhinh`; chờ phiên vẽ lại.
