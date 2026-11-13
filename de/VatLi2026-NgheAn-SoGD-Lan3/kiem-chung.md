# Kiểm chứng đáp án – VatLi2026-NgheAn-SoGD-Lan3

Nguồn: `kho/goc/Nghe An - So GDDT - Lan 3.docx` (Sở GD&ĐT Nghệ An, kì khảo sát kết hợp thi thử lớp 12 – Đợt 3, mã đề 0304), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python (`/tmp/VatLi2026-NgheAn-SoGD-Lan3/py/kiem.py`).

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | D C A C A A C A A B C D C A C B C C | trùng, trừ I.11 (xem dưới) | I.1: đường sức đi ra từ cả A và B ⇒ N, N; I.12: p không đổi, T giảm ⇒ nén đẳng áp; I.14: A = 1, Z = 1 ⇒ ¹₁H; I.15: f = 120π/2π = 60 Hz; I.18: 44 + 273 = 317 K |
| **I.11** | **C (thẳng đứng lên trên)** | **A (về phía sau tàu)** | **Trong vòng tròn có ba nam châm: S trên thân tàu nằm chính giữa S (phía trước, mũi tàu bên trái) và N (phía sau) của ray. S ray đẩy, N ray hút nam châm S thân tàu; hai lực đối xứng nên thành phần thẳng đứng triệt tiêu, thành phần ngang cùng hướng về phía sau tàu.** Lời giải gốc chỉ xét cặp S – S "đẩy nhau, hướng lên", bỏ qua nam châm N của ray trong vòng tròn. Đề có nhắc cơ chế "lùi", phương án A khớp. File gõ theo A, `% KIỂM TRA` trong file — thầy xem lại. |
| II.1 | S Đ S Đ | trùng | khớp nối dựa vào tương tác nam châm vĩnh cửu; vách sắt từ làm giảm truyền động; đĩa đồng: cảm ứng, quay chậm hơn |
| II.2 | S S Đ S | trùng | c) I_hổng/I_đặc = e^{μd} = 2 ⇒ d = ln2/μ |
| II.3 | Đ S S S | trùng | nén đoạn nhiệt: Q = 0, A > 0 ⇒ U, T tăng; d) nén nhanh nhận công lớn hơn ⇒ Sai |
| II.4 | Đ S Đ S | trùng | |
| III.1–III.6 | 2,3 / 1,9 / 0,4 / 3,8 / 28,4 / 28 | trùng | |

## Phép tính chính
- III.1: p = 84 cmHg = 84/76·1,01·10⁵ = 1,1163·10⁵ Pa; V = 4,2·20 = 84 cm³; N = pVN_A/(RT) = 2,264·10²¹ ⇒ x = 2,3.
- III.2: (1) l₁ = 84·20/68 = 24,706 cm ⇒ L₁ = 28,706 cm. (2) khí B ban đầu 40 cm, 76 cmHg; 3040/(60 − x) = 1680/x + 8 ⇒ x = 22,793 cm ⇒ L₂ = 26,793 cm (kiểm: p_A' = 73,71 cmHg, p_B' = 81,71 cmHg). ΔL = 1,913 ≈ 1,9 cm.
- III.3: I = 1,5/0,5 = 3 A; B = 0,48/(3·0,4) = 0,4 T.
- III.4: e_c = 0,4·0,4·2,5 = 0,4 V. Lực kế (sợi chỉ chỉ kéo được) ở bên phải ⇒ lực từ ban đầu hướng về phía nguồn; khi MN chạy sang phải, lực từ của dòng cảm ứng cản chuyển động (cũng hướng về phía nguồn) ⇒ dòng cảm ứng cùng chiều dòng nguồn: I = (1,5 + 0,4)/0,5 = 3,8 A (hình gốc: bản cực dài của nguồn nối về ray M, khớp chiều này).
- III.5: Δm = 2·1,0073 + 2·1,0087 − 4,0015 = 0,0305 u; W_lk = 0,0305·931,5 = 28,41 MeV.
- III.6: H = 1,6·10⁸·2^(−0,5) = 1,1314·10⁸ Bq; V = 1,1314·10⁸·0,1/400 = 28 284 lít ⇒ x = 28.

## Sửa lời đề (lỗi chữ bản gốc)
- Cho biết: "T(K)=t(°C)+273", "J.mol⁻¹K⁻¹" gõ lại theo quy chuẩn ($T(\text{K})=t\,(^\circ\text{C})+273$, J·mol⁻¹·K⁻¹).
- I.1: "ký hiệu" → "kí hiệu". I.3, I.16, II.3: "khí lý tưởng" → "khí lí tưởng". I.11: "Nguyên lý" → "Nguyên lí". I.7: "quản lý" → "quản lí"; II.1: "cách ly" → "cách li"; II.2: "xử lý" → "xử lí" (cả nhãn trong hình). I.18: "kỷ lục" → "kỉ lục", bỏ dấu chấm thừa sau "Kelvin là".
- I.9, III.5: "notron" → "neutron"; I.9 viết $Z\cdot m_\text{p}$ thay cho "Z.m_p".
- I.14: kí hiệu hạt nhân bản gốc vỡ ("^42He+^147N→^178O") gõ lại ${}^4_2\text{He}+{}^{14}_{7}\text{N}\to{}^{17}_{8}\text{O}+\text{X}$; phương án C (positron) ghi ${}^{0}_{+1}\text{e}$.
- II.2: "Iridium - ¹⁹²₇₇Ir" → "iridium ¹⁹²₇₇Ir".
- II.3: "xi lanh" → "xilanh".
- III.1–2 (dữ kiện chung): bỏ chữ "A." gạch chân thừa ("đáy kín A. Ban đầu" là lỗi định dạng); dữ kiện chung đặt trong câu III.1 theo mẫu "Dùng thông tin sau cho câu 1 và câu 2". Hình hai giá đỡ (có ΔL) đặt ở câu III.2 như bản gốc.
- III.3: "sợi chỉ nhẹ, mảnh, không dẫn" → "không dẫn điện"; kí hiệu suất điện động gõ $\mathscr{E}$.
- III.5: "Hạt nhân Heli" → "Hạt nhân helium".
- Nhãn hình II.1 "Rôto" → "Rotor" cho khớp lời đề.
- Đề không có từ phủ định cần in đậm; I.3 giữ in đậm "đúng" như bản gốc.

## Hình
7 hình, vẽ lại bằng TikZ, so hình ở `so-hinh/`: I.1 (đường sức hai nam châm, cạnh phương án), I.11 (tàu đệm từ), I.12 (đồ thị p–T, cạnh phương án), II.1 (khớp nối từ: phối cảnh + mặt cắt), II.2 (kiểm tra mối hàn bằng tia phóng xạ), III.2 (hai ống thủy tinh trên giá chân ba, cạnh lời đề), III.3 (ray, thanh MN, lực kế điện tử, giá đế chữ nhật).
- Nam châm có ghi cực (I.11, II.1) tô N đỏ, S xanh; I.1 đề hỏi cực nên để xám.
- Màn hình lực kế III.3 giữ "0.48 N" vì là dữ kiện trong lời đề.
