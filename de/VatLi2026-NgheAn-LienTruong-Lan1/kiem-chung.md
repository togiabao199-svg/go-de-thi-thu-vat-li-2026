# Kiểm chứng đáp án – VatLi2026-NgheAn-LienTruong-Lan1

Đề gốc (PDF SieuGioi, "Sở GD&ĐT Nghệ An – Liên trường", không có mã đề) không có đáp án, không có lời giải: mọi câu tự giải, các câu có số liệu tính kiểm bằng Python.

| Câu | Đáp án gốc | Giải lại | Ghi chú |
|---|---|---|---|
| I.1–I.18 | không có | D D D D C D A B A B A C C B C B A A | I.8: dòng điện ra từ cực dương (bên trái), chạy ở mặt trước các vòng dây từ trên xuống ⇒ đầu phải ống dây là cực Bắc, tại O đường sức hướng Đ ⇒ cực Nam kim chỉ T (cùng câu, cùng hình, cùng kết luận với đề Lào Cai Sở GD Lần 1); I.10: I hướng Nam, B hướng xuống ⇒ F = Il × B hướng Đông; I.15: phòng thông với ngoài ⇒ p không đổi, mật độ giảm; I.17: pV nhỏ nhất ở (4) |
| II.1 | không có | Đ Đ S Đ | h/T = 0,03168…0,03213 cm/K (trung bình 0,03190, lệch tối đa 0,74 %); theo định luật Charles h tăng bậc nhất theo t (≈ 0,032 cm/°C, các khoảng bằng nhau); h gấp đôi ⇒ T gấp đôi ⇒ v_rms tăng √2 |
| II.2 | không có | Đ S Đ S | p₀(L₀ − L₁) = p(L₀ − L₂), p + DgL₂ = p₀ ⇒ p₀ = DgL₂(L₀ − L₂)/(L₁ − L₂) (đề ghi L₀ − L₁ ở tử) |
| II.3 | không có | S S Đ Đ | F₁ > F₀ ⇒ lực từ hướng xuống; B từ N (trái) sang S (phải), P ở phía trước, Q phía sau ⇒ I từ P đến Q; quay khung góc α quanh dây treo: F' = BIL cos α = 0,6(F₁ − F₀) ⇒ F = 0,4F₀ + 0,6F₁ |
| II.4 | không có | Đ S S Đ | d): N = pV/(kT), p, V không đổi, T tăng ⇒ N giảm ⇒ số phân tử bị hút ra lớn hơn số phân tử thoát ra từ sản phẩm |
| III.1–III.6 | không có | 233 / 3,36 / 4,25 / 17 / 192 / 640 | III.1: −40 + 273; III.2: λ = 4·40·2100 = 3,36·10⁵ J/kg; III.3: 3,80·∛1,4 = 4,2510 mm; III.4: n₂/n₁ = 4,10³/(1,4·3,80³) = 0,89717, x = (1 − 0,89717)/3 · n₁, x/(0,2n₁) = 17,14 %; III.5: BIL sin α = 0,5·4·0,16·0,6 = 0,192 N; III.6: BIL·L cos α = (2P/3)·L sin α ⇒ P = 3·0,32·0,8/(2·0,6) = 0,64 N |

## Điểm cần thầy xem

- **I.8**: hình gốc vẽ vòng dây cả hai nhánh đè lên lõi (không phân biệt nét trước/sau). Lời giải hiểu nét xiên đi từ trên xuống là mặt trước (như đề Lào Cai Sở GD Lần 1, cùng câu): đáp án B (điểm T). Hiểu ngược lại thì ra C (điểm Đ).
- **II.1 c)**: số liệu đo tăng 0,1 hoặc 0,2 cm mỗi 5 °C (không đều do sai số); lời giải theo định luật: các khoảng bằng nhau ⇒ Sai.
- **II.4 d)**: hiểu theo N = pV/(kT) (áp suất, thể tích buồng không đổi, nhiệt độ tăng thì số phân tử khí trong buồng giảm) ⇒ Đúng. Ý này diễn đạt chưa chặt (không nói rõ trong khoảng thời gian nhiệt độ tăng).
- **III.3, III.4**: bỏ qua áp suất phụ do căng mặt ngoài của bọt khí (đề không cho), nhiệt độ không đổi.
- **III.5, III.6**: đề không yêu cầu làm tròn; đáp số nguyên 192, 640.

## Sửa lời đề (lỗi chữ bản gốc)

- Bỏ tiêu đề mẫu SieuGioi ("ĐỂ THI THỬ TỐT NGHIỆP THPT / Lần 3, năm 2025 - 2026", dòng họ tên, "ĐỀ THI CHÍNH THỨC", "Đề thi gồm 08 trang"), chân trang quảng cáo. Lần thi đặt Lần 1 theo `kho/kiem-ke.md` (tên file nguồn ghi Lần 1, tiêu đề gõ lại ghi Lần 3).
- I.5, I.9, I.12, I.14: in đậm "không" (bản gốc không in đậm).
- I.6 A: "Nhắc nhiệt kế" → "Nhấc nhiệt kế".
- I.8: "kim châm thử" → "kim nam châm thử"; "điểm N ." → "điểm N".
- I.10: "Bắc - Nam" → "Bắc – Nam".
- I.13, I.15: "7°C", "20°C" gõ theo quy chuẩn `7\,^\circ\text{C}`.
- I.18: "E_d" → "$\overline{E}_{\text{đ}}$".
- II.1: "(°C)" trong bảng gõ lại; hình: "Ống thuỷ tinh" → "Ống thủy tinh"; "như hình vẽ" → "như hình bên" (hình đặt cạnh lời đề).
- II.2: "sau: Một" → "sau: một"; bỏ chữ nhãn hiệu "VINH HAO" trên bình nước.
- II.3 c): "là L và I.Cảm ứng" → "là $L$ và $I$. Cảm ứng"; "I.L" → "$IL$".
- II.4: "Để giữ được tính của" → "Để giữ được dược tính của" (thiếu chữ); "nguyên lý" → "nguyên lí"; "Xử lý" → "Xử lí"; "20°C đến 30°C", "−20°C đến −5°C" gõ theo quy chuẩn.
- III: "Sử dụng các thông tin sau cho Câu 23 và Câu 24" (25–26, 27–28) → đoạn dữ kiện đặt trong câu đầu của cặp, "Dùng thông tin sau cho câu 1 và câu 2:" (3–4, 5–6) bằng `\label`/`\ref`.
- III.1: "thang độ K" → "thang nhiệt độ Kelvin là bao nhiêu K"; dấu chấm hỏi đặt sau ngoặc làm tròn.
- III.2: "2,1.10³ J / kg.K" → "2,1·10³ J/(kg.K)"; "θ₂ = 5.θ₁" → "θ₂ = 5θ₁"; "x.10⁵ J / kg" → "x·10⁵ J/kg"; chuyển "?" ra sau ngoặc làm tròn.
- III.4: "chiếm mấy phần trăm" → "chiếm bao nhiêu phần trăm".
- III.5: "vecto" → "vectơ"; "x.10⁻³", "y.10⁻³" → "x·10⁻³", "y·10⁻³".

## Đánh số lại câu

Đề gốc đánh số liên tục 1–28. File gõ đánh số lại theo từng phần: Phần I câu 1–18 (gốc 1–18), Phần II câu 1–4 (gốc 19–22), Phần III câu 1–6 (gốc 23–28). Tham chiếu "Câu 23 và Câu 24", "Câu 25 và Câu 26", "Câu 27 và Câu 28" đổi thành câu 1–2, 3–4, 5–6 bằng `\label`/`\ref`.

## Hình

8 hình gốc → 8 `tikzpicture`, ảnh so ở `so-hinh/`. Vùng cắt ảnh trang (150 dpi, tỉ lệ khổ trang): I.8 tr.2 `0.30:0.16:0.72:0.30`; I.17 tr.3 `0.36:0.30:0.66:0.44`; II.1 tr.3 `0.35:0.635:0.67:0.80`; II.2 tr.4 `0.40:0.37:0.61:0.52`; II.3 tr.5 `0.38:0.145:0.63:0.355`; II.4 tr.5 `0.27:0.60:0.75:0.775`; III.1 tr.6 `0.29:0.46:0.72:0.60`; III.5 tr.7 `0.35:0.375:0.65:0.535`.

- Hình thực tiễn (II.1 bộ thí nghiệm Charles, II.2 bình nước và ống thủy tinh, II.3 lực kế – nam châm – khung dây, II.4 hệ thống sấy) vẽ có khối, `\shade`, gắn `% giuhinh`; chờ phiên vẽ lại chi tiết.
- II.1, II.2, II.3, III.1, III.5: hình đặt bên cạnh lời đề (hai `minipage`) để dàn trang ĐẠT.
- II.3: cực N đỏ, S xanh (đề ghi cực). II.4: lược bớt chi tiết ống nối, đai ốc, chân đế của ảnh gốc.
