# Kiểm chứng đáp án – VatLi2026-CaMau-SoGD-Lan1

Nguồn: `kho/goc/Ca Mau - So GDDT - Lan 1.docx` (Sở GD&ĐT Cà Mau, mã đề 0201, thi ngày 24/4/2026), có bảng đáp án và lời giải tham khảo. Mọi câu đã giải lại, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | B D A B A D B B C D B D A D C A B D | trùng | I.11: 357 − 100 = 257 K; I.13: p/T của (1) lớn hơn của (2) nên V₁ < V₂; I.14: I = 0,05/(4·10⁻⁵·10) = 125 A; I.15: 423/323 ≈ 1,31; I.16: 13·0,01·6,02·10²³ = 7,826·10²²; I.17: m = 661 680/63 000 ≈ 10,50 kg; I.18: 1784/235 ≈ 7,59 |
| II.1 | S Đ Đ Đ | trùng | Q₁ = 3150 J; 63 630 = 3150 + 0,15λ + 10 080 ⇒ λ = 336 000 J/kg |
| II.2 | Đ S Đ S | trùng | N = 30; R = 1,2·10⁻¹⁵·56^(1/3) ≈ 4,59·10⁻¹⁵ m ≠ 3,55·10⁻¹⁵ m |
| II.3 | S Đ Đ Đ | trùng | B₂ = 50; B₃ ≈ 46,67; B₄ = 45 mT; B̄ ≈ 47,22 mT; ΔB̄ ≈ 1,85 ≈ 1,9 mT; c) (5 − 2,5)·10⁻³/(50·0,01·0,1) = 0,05 T. Ý a): lời giải gốc chỉ nói "dùng quy tắc bàn tay trái xác định được chiều từ trường không phải từ phải sang trái"; lời giải gõ lại: cạnh BC nằm ngang theo phương trái – phải trong hình (C trái, B phải) và vuông góc với đường sức nên đường sức không thể có chiều phải → trái. |
| II.4 | S Đ Đ S | trùng | ΔT = 12 K; n₁ ≈ 2045,3 mol, N ≈ 1,231·10²⁷; Δm ≈ 2,296 kg ≈ 2,3 kg ≠ 2,2 kg |
| III.1–III.6 | 6,21 / 42,4 / 6 / 4,3 / 0,05 / 2,4 | trùng | III.1: 1,5·(8,31/6,02·10²³)·300 = 6,212·10⁻²¹; III.2: p₁ = 124 650 Pa, Δp = 6410,3 Pa, T₂ = 315,43 K → 42,4 °C; III.3: N = 50, S = 2,4·10⁻³ m², R = 0,2 Ω, I = 6 mA; III.4: Q = 1,44·10⁻⁶ + 2,88·10⁻⁶ = 4,32·10⁻⁶ J; III.5: λ = 1,531·10⁻⁶ s⁻¹, N = 2,077·10¹⁴, m = 0,0459 μg; III.6: 0,85·3,18·10⁸·2^(−1/5,24) = 2,368·10⁸ Bq |

## Sửa lời đề (lỗi chữ bản gốc)
- Khối "Cho biết": gõ lại theo quy chuẩn kí hiệu (J$\cdot$mol⁻¹$\cdot$K⁻¹, 6,02·10²³, ln 2 = 0,693); giữ dòng "Không làm tròn kết quả các phép tính trung gian".
- I.1: "V.T", "p.T" → $V\cdot T$, $p\cdot T$.
- I.2: in đậm "sai"; "vector" → "vectơ"; câu dẫn hai dòng gộp thành một đoạn.
- I.3: phương án "Q = L2m", "Q = Lm2" (mất chỉ số mũ) → $Q=L^2m$, $Q=Lm^2$; "hoá" → "hóa".
- I.4: in đậm "không" (thầy chốt 13/11/2026).
- I.14: "có cảm từ B" → "có cảm ứng từ B".
- I.15: "50 0C", "150 0C" → $50\,^\circ$C, $150\,^\circ$C (cũng sửa ở II.4, III.1).
- I.16: "7,826.10²²" → $7{,}826\cdot 10^{22}$ (các phương án).
- Phần III: "xi lanh" → "xilanh", "pít-tông" → "pit-tông" (thuật ngữ SGK 2018).
- III.2: "bằng bao nhiêu celsius" → "bằng bao nhiêu °C".
- III.5: "microgram ($\mu g$)" → "microgram ($\mu$g)".

## Câu dùng chung dữ kiện
- Phần III có ba cặp câu dùng chung dữ kiện ("Dùng thông tin sau cho câu 1 và câu 2", câu 3 và 4, câu 5 và 6). Đoạn dữ kiện chung (kèm hình) đặt trong câu đầu của cặp, mở đầu bằng chữ nghiêng "Dùng thông tin sau cho câu~\ref{..} và câu~\ref{..}:" (tham chiếu bằng `\label`/`\ref`, nhãn `CaMau1-III1`…`CaMau1-III6`), để `dan_trang.py` đo, giữ trọn khối với câu hỏi.

## Hình
- Cả 4 hình là shape/canvas Word, ảnh gốc dựng bằng `tools/hinh_word.py`. Hình II.3 (ảnh chụp bộ thí nghiệm + các ô chữ Word đè lên số thứ tự): LibreOffice đặt lệch các ô chữ, nên ảnh so `II3-goc.png` được ghép lại từ `image19.png` theo tọa độ ô chữ trong `document.xml` (D trên trái, A trên phải, C dưới trái, B dưới phải khung dây; vôn kế bên trái, ampe kế bên phải).
- Hình II.3 vẽ lại có khối, tô nhạt (`% giuhinh`); bảng số liệu đặt cạnh hình.
- Tô màu lại hình theo bảng màu 13/11/2026 (I.13, II.3, III.1, III.3); ảnh gốc so hình lấy lại từ nửa trái các ảnh `so-hinh/` cũ.
