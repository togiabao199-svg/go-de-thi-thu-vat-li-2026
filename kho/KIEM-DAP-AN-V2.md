# KIỂM ĐÁP ÁN V2 — 35 ĐỀ PDF (lô P01–P09), PHIÊN FABLE PHẦN B

Phiên 14/11/2026, nhánh `claude/great-knuth-6gcmjx`. Mỗi đề một agent con: giải lại độc lập 28 câu từ ảnh trang đề gốc và ghi đáp án ra nháp **trước khi** mở file `.tex`; tìm đáp án của chính đề trên mạng; soát câu lý thuyết theo SGK; rồi so với `\True`, `\shortans` trong file đề và giải lại lần hai các câu lệch, câu đang `% KIỂM TRA`, các điểm "thầy xem" / "Chờ thầy quyết" của `kho/TIEN-DO.md`. Kết quả từng đề: `de/<tên đề>/kiem-chung-v2.md` (bảng đáp án Fable đủ 28 câu, bảng câu lệch / câu `% KIỂM TRA`, căn cứ lý thuyết, nguồn trên mạng). Phiên này **không sửa** file `.tex`, `kiem-chung.md`, `kho/TIEN-DO.md` (phiên vẽ hình chạy song song trên nhánh khác): mọi thay đổi đáp án, lời đề, hình đều chờ thầy quyết.

## Kết quả

- **35/35 đề đã kiểm.** 32 đề không có câu / ý lệch: 29 đề trùng 28/28 ngay từ lượt giải độc lập đầu; 3 đề khác ở lượt đầu chỉ vì đề gốc lỗi, kết luận cuối là file không sai — Lương Thế Vinh II.2a (file đã sửa Z của I-131 từ 51 thành 53), Phan Đăng Lưu I.16 (A và C cùng đúng), Quảng Ninh SGD I.16 (không phương án nào đúng, mỗi bên chữa một phương án).
- **3 câu / ý lệch** (file khác kết luận cuối của Fable), cả ba đều do đề mơ hồ — Fable nghiêng về đáp án khác nhưng không khẳng định file sai: Cụm liên trường Hà Tĩnh II.2a, Kinh Môn II II.1a, Ngô Gia Tự I.11 (mục A).
- Không thấy câu nào file sai do tính toán. Phần còn lại là lỗi / chỗ mơ hồ của đề gốc cần thầy quyết (mục B–D), lỗi hình vẽ lại (mục G), sai sót nhỏ (mục H).
- Đáp án trên mạng gần như không đối chiếu được: mạng của phiên chặn các trang đăng đề (mục J).

Cách đếm "lệch": Phần I, III theo câu; Phần II theo ý. Thứ tự làm: đề có `% KIỂM TRA` trong `.tex` (21 đề, STT 1–21) → đề có điểm "Chờ thầy quyết" (8 đề, STT 22–29) → đề chỉ có điểm "thầy xem" (6 đề, STT 30–35).

## Bảng 35 đề

| STT | Lô | Đề (mở `kiem-chung-v2.md`) | Trạng thái | Số lệch | Câu lệch (file / Fable) | Kết luận của Fable | Đáp án trên mạng |
|---|---|---|---|---|---|---|---|
| 1 | P01 | [`VatLi2026-HaNoi-ChuyenKHTN-Lan3`](../de/VatLi2026-HaNoi-ChuyenKHTN-Lan3/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. I.10 giữ C (tính ra 3,19 kW, không có phương án; nhiều khả năng đề chép sai H = 90 % thay cho 95 %). II.1d Sai chắc (12,4 T). III.4 = 0,09 sát ngưỡng làm tròn. | trang VietJack đúng đề, bị chặn |
| 2 | P01 | [`VatLi2026-HaNoi-LuongTheVinh-Lan1`](../de/VatLi2026-HaNoi-LuongTheVinh-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp theo đề đã sửa. II.2a: Sai với Z = 53 (file đã sửa), Đúng với nguyên văn Z = 51 — thầy quyết. III.2 = 200 W, III.4 = 2,7 đúng. | trang VietJack đúng đề, bị chặn |
| 3 | P02 | [`VatLi2026-HaNoi-YenHoa-Lan1`](../de/VatLi2026-HaNoi-YenHoa-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. I.7 giữ B (theo λ = 34·10⁵ J/kg in trên đề). Hai cách hiểu: II.1b (hướng nhìn), III.3 (78,6 / 78,1). **Hình I.13 đảo cực nguồn.** | không tìm thấy |
| 4 | P02 | [`VatLi2026-HaTinh-CamXuyen-Lan2`](../de/VatLi2026-HaTinh-CamXuyen-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.3d Sai (1282 kg / đề "khoảng 1250 kg") — thầy quyết. III.4 = 3,46, không còn mơ hồ. | trang VietJack đúng đề, bị chặn |
| 5 | P03 | [`VatLi2026-HaTinh-CumLienTruong`](../de/VatLi2026-HaTinh-CumLienTruong/kiem-chung-v2.md) | xong | 1 | II.2a: S / Đ | Đề mơ hồ (lần đo 7 bất thường); Fable nghiêng Đ, không khẳng định file sai. III.3 = 4,65 (4,68 cũng có cơ sở). II.3c, d định tính giữ Đ. | câu II.1 trên VietJack, bị chặn |
| 6 | P03 | [`VatLi2026-HaiPhong-Cum13Truong-Lan2`](../de/VatLi2026-HaiPhong-Cum13Truong-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. I.17 giữ B (0,7 N mỗi dây; D nếu hiểu tổng hai dây 1,4 N) — thầy quyết. | không tìm thấy |
| 7 | P03 | [`VatLi2026-HaiPhong-KinhMonII-Lan2`](../de/VatLi2026-HaiPhong-KinhMonII-Lan2/kiem-chung-v2.md) | xong | 1 | II.1a: S / Đ | Đề mơ hồ (nguyên tắc phép đo → Đ; xét hao phí → S). II.2b, III.6 giữ như file. Điểm mới: II.3d (2,5 W của đề đúng bằng kết quả khi bỏ sót cos α). | không tìm thấy |
| 8 | P04 | [`VatLi2026-Hue-PhanDangLuu-Lan1`](../de/VatLi2026-Hue-PhanDangLuu-Lan1/kiem-chung-v2.md) | xong | 0 | — (I.16: đề có hai phương án đúng) | I.16 A và C cùng đúng theo SGK, file gõ C — thầy quyết. II.2a Sai (0,1787 mol / "xấp xỉ 0,17"). III.2 = 10, III.1 = 20. | trang VietJack đúng đề, bị chặn; đoạn trích khớp II.1a, III.1, III.2 |
| 9 | P04 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1b Đ (đã sửa "3 V" → 3 A). II.4c mơ hồ (85 % / 92 %), II.4d Sai. Hình II.4, II.2 lệch nhỏ. | câu II.1, II.2 trên VietJack, chuvanbien, bị chặn |
| 10 | P04 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan3`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan3/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1b, II.1d Sai theo chữ in (II.1d: tính ra 34,1 kJ, đề in "41 kJ" — nghi mất kí tự) — thầy quyết. | không tìm thấy |
| 11 | P05 | [`VatLi2026-HungYen-SoGD-Lan1`](../de/VatLi2026-HungYen-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28 theo đề đã sửa P = 1,2 kW (giữ 12 kW thì II.2a Sai). II.1c S, II.1d Đ mơ hồ nhẹ. | hoatieu bị chặn |
| 12 | P05 | [`VatLi2026-NgheAn-ChuyenDHVinh-Lan1`](../de/VatLi2026-NgheAn-ChuyenDHVinh-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; I.17, II.3 đọc hình độc lập khớp; không câu mơ hồ. **Hình III.3 vẽ sai chiều vòng từ trường quanh một thanh ray.** | chuvanbien bị chặn |
| 13 | P06 | [`VatLi2026-NgheAn-LienTruong-Lan2`](../de/VatLi2026-NgheAn-LienTruong-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. Đồng ý sửa I.8 thành (3/2)kT. II.4c Đ. II.2d Sai (9,84 °C / đề ghi 8,9). | câu III.1–2 trên VietJack, bị chặn |
| 14 | P07 | [`VatLi2026-PhuTho-NgoGiaTu-Lan1`](../de/VatLi2026-PhuTho-NgoGiaTu-Lan1/kiem-chung-v2.md) | xong | 1 | I.11: C / D | Fable nghiêng D (đoạn trích loigiaihay, tuyensinh247 cũng D); cần đối chiếu SBT KNTT bài 8. II.4d Sai (4461 / đề in 4160 — nghi 4460). | đoạn trích câu I.11 ghi D; trang bị chặn |
| 15 | P07 | [`VatLi2026-QuangNinh-CamPha-Lan1`](../de/VatLi2026-QuangNinh-CamPha-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. III.6 = 14 chỉ đúng với hình phòng tự dựng 8 × 5 × 4 m (đề gốc mất hình) — thầy quyết. | chuvanbien có thể có hình gốc, bị chặn |
| 16 | P08 | [`VatLi2026-QuangNinh-SoGD-Lan1`](../de/VatLi2026-QuangNinh-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — (I.16: đề gốc không có phương án đúng) | I.16: file chữa C, đoạn trích VietJack ghi B — thầy quyết chữa phương án nào. Điểm mới: II.3d (2,56·10⁻⁴ W / đề in 2,65·10⁻⁴). III.2, III.3, III.6 đúng. | trang VietJack đúng đề, bị chặn; đoạn trích: I.16 B, II.2 Đ Đ Đ S |
| 17 | P08 | [`VatLi2026-ThaiNguyen-SoGD-Lan1`](../de/VatLi2026-ThaiNguyen-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.1c đo điểm ảnh cực nguồn khớp; không câu mơ hồ. | câu II.1 trên VietJack, bị chặn |
| 18 | P08 | [`VatLi2026-ThanhHoa-HamRong-Lan1`](../de/VatLi2026-ThanhHoa-HamRong-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.4c Sai, mơ hồ (MN không thuộc mạch kín; trường có thể Đ). III.6 = 2108 theo hằng số SGK. | hoatieu bị chặn |
| 19 | P09 | [`VatLi2026-ThanhHoa-TinhGia1`](../de/VatLi2026-ThanhHoa-TinhGia1/kiem-chung-v2.md) | xong | 0 | — | II.3 S S S S theo chữ in; sửa lỗi in thì S Đ Đ Đ (bản lời khác trên VietJack cũng S Đ Đ Đ) — thầy quyết. III.2 = 0,66 với mạch tự dựng. | câu II.3 (bản lời khác) trên VietJack |
| 20 | P01 | [`VatLi2026-BacNinh-SoGD-Lan1`](../de/VatLi2026-BacNinh-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.2c Đ mơ hồ nhẹ; III.5 = 8,01, III.6 = 0,6 đúng. | hoatieu, laodong bị chặn |
| 21 | P09 | [`VatLi2026-BacNinh-SoGD`](../de/VatLi2026-BacNinh-SoGD/kiem-chung-v2.md) (scan) | xong | 0 | — | Khớp 28/28. II.4d Sai (3888 / 3995; 3995 ứng với m = 0,18 kg) — thầy quyết. Có thể là đề cuối học kì I (mục I). | chuvanbien bị chặn |
| 22 | P01 | [`VatLi2026-HaNoi-ChuyenKHTN-Lan1`](../de/VatLi2026-HaNoi-ChuyenKHTN-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. III.4 = 16 (18 nếu không trừ khí còn lại) — thầy quyết. III.6 = 0,05 theo cả lời đề lẫn hình gốc. | câu I.4 trên VietJack, bị chặn |
| 23 | P02 | [`VatLi2026-HaNoi-NguyenThiMinhKhai-Lan1`](../de/VatLi2026-HaNoi-NguyenThiMinhKhai-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.4c mơ hồ nhẹ (99 / 100 kJ). **Hình II.2 (Hình a) đảo cực nguồn.** | trang VietJack đúng đề, bị chặn; đoạn trích I.3, II.1, II.2a, II.3, II.4 khớp |
| 24 | P03 | [`VatLi2026-HaiPhong-CumCM10-Lan1`](../de/VatLi2026-HaiPhong-CumCM10-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.3b, c, II.4a, b đọc hình khớp. I.6 = A theo lời đề "Mười độ chia" (C nếu là "Một độ chia"). | trang VietJack, hoatieu đúng đề, bị chặn; đoạn trích II.2c, d, II.4c, III.3 khớp |
| 25 | P04 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.1b đọc chiều quấn, cực nguồn khớp. | không tìm thấy |
| 26 | P05 | [`VatLi2026-LaoCai-SoGD-Lan1`](../de/VatLi2026-LaoCai-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; I.6, II.1c đọc hình khớp; không câu mơ hồ. | không tìm thấy |
| 27 | P06 | [`VatLi2026-NgheAn-LienTruong-Lan1`](../de/VatLi2026-NgheAn-LienTruong-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; I.8 = B. II.1c, II.4d mơ hồ nhẹ. | trang VietJack, hoatieu đúng đề, bị chặn |
| 28 | P06 | [`VatLi2026-NinhBinh-SoGD-Lan2`](../de/VatLi2026-NinhBinh-SoGD-Lan2/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. III.5 = 6,23 (6,24 nếu R = 8,314 — đề không cho R). III.6 = 1,98. | vietnamnet, plo bị chặn |
| 29 | P07 | [`VatLi2026-QuangNinh-ChuyenHaLong-Lan1`](../de/VatLi2026-QuangNinh-ChuyenHaLong-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.1b đọc cực nguồn khớp. | trang hoatieu, VietJack đúng đề, bị chặn |
| 30 | P02 | [`VatLi2026-HaNoi-SoGD-Lan1`](../de/VatLi2026-HaNoi-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.2b mơ hồ ("cùng chuyển động"). | docs.google bị chặn |
| 31 | P05 | [`VatLi2026-NgheAn-ChuyenPhanBoiChau-Lan1`](../de/VatLi2026-NgheAn-ChuyenPhanBoiChau-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; II.2b, II.4b mơ hồ nhẹ. **Hình I.6 vẽ electron thành nhãn dòng điện I.** | trang VietJack đúng đề (VIP), bị chặn |
| 32 | P06 | [`VatLi2026-NinhBinh-SoGD-Lan1`](../de/VatLi2026-NinhBinh-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28; không câu mơ hồ. | vietnamnet, hoatieu bị chặn |
| 33 | P07 | [`VatLi2026-PhuTho-SoGD-Lan1`](../de/VatLi2026-PhuTho-SoGD-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1a Sai, mơ hồ (lượng khí thay đổi) — thầy quyết. II.2b, II.2c Sai theo số in (75 kJ; "10,8 J"). | hoatieu bị chặn |
| 34 | P08 | [`VatLi2026-ThanhHoa-LuongDacBang-Lan1`](../de/VatLi2026-ThanhHoa-LuongDacBang-Lan1/kiem-chung-v2.md) | xong | 0 | — | Khớp 28/28. II.1d Đ, II.4c S — mơ hồ, thầy quyết. II.2d S, II.3c Đ (tính cả N vòng). | docs.google bị chặn |
| 35 | P09 | [`VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10`](../de/VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10/kiem-chung-v2.md) (scan) | xong | 0 | — | Khớp 28/28. II.3a S (Đ nếu coi miệng ống ngang mặt thoáng), II.4b S — thầy quyết. III.6 = 0,82 (đẳng nhiệt theo lời đề). | câu II.3 trên VietJack, bị chặn |

## Các điểm chờ thầy quyết (gom từ báo cáo 35 agent)

Độ tin cậy: mỗi đề có một lượt giải lại độc lập, không có đáp án chính thức để chốt. "Khớp" nghĩa là hai lượt giải (lô P và Fable) ra cùng đáp án. Với các ý phụ thuộc đọc hình mờ, hai lượt cùng đọc một ảnh gốc nên có thể cùng sai theo một hướng. Phiên chính soát bằng script: mỗi `kiem-chung-v2.md` đủ 28 dòng, cột "File" trùng `\True` / `\shortans` trong `.tex`. Phiên chính không giải lại từng câu.

### A. Câu / ý lệch (file khác kết luận cuối của Fable) — 3

| Đề | Câu | File | Fable | Ghi chú |
|---|---|---|---|---|
| Cụm liên trường Hà Tĩnh | II.2a | S | Đ (nghiêng, khoảng 2/3) | pV sáu lần đầu lệch dưới 0,7 %, riêng lần 7 lệch +12,9 %; ý d đã tách lần 7 thành số liệu nghi ngờ. Không khẳng định file sai; chọn Đ thì phải viết lại lời giải ý a. |
| Kinh Môn II – Lần 2 | II.1a | S | Đ (nghiêng, khoảng 60 %) | "Nhiệt lượng nước thu vào bằng điện năng cung cấp": theo nguyên tắc phép đo (ý c tính đúng bằng đẳng thức này) → Đ; xét hao phí → S. Chọn Đ thì II.1 thành Đ S Đ Đ. |
| Ngô Gia Tự – Lần 1 | I.11 | C | D | Đoạn trích tìm kiếm của loigiaihay, tuyensinh247 cũng ghi D (chưa mở được trang). `kiem-chung.md` cũ ghi chọn C "theo SBT Vật lí 12" — cần thầy đối chiếu bản in SBT KNTT bài 8. |

### B. Hai lượt giải khớp nhau, nhưng đáp án phụ thuộc cách xử lí lỗi đề gốc

- **Lương Thế Vinh II.2a**: file sửa Z của I-131 từ 51 thành 53 nên a Sai; theo nguyên văn đề gốc (Z = 51, in ở 6 chỗ) thì a Đúng.
- **Chuyên KHTN Lần 3 I.10**: giữ C (3,0 kW). Cùng bài ở đề Liên trường Nghệ An Lần 2 dùng H = 95 % với cùng bộ phương án → nhiều khả năng đề KHTN chép sai H = 90 %; thầy quyết giữ 90 % kèm ghi chú hay sửa 95 %.
- **Hưng Yên SGD Lần 1 II.2**: đồng ý sửa P = 12 kW → 1,2 kW (cho m₂ = 2,53 kg, khớp ý a); giữ 12 kW thì a Sai.
- **Liên trường Nghệ An Lần 2 I.8**: đồng ý sửa (2/2)kT → (3/2)kT.
- **Thái Nguyên SGD Lần 1 I.17**: phương án C trùng B ở đề gốc; đáp án A không đổi dù sửa hay không.
- **Quảng Ninh SGD I.16**: đề gốc không có phương án đúng; file chữa C. Đoạn trích VietJack ghi đáp án **B** (tức trường chữa dấu "+" ở B thành "·"). Thầy quyết chữa C hay chữa B.
- **Yên Hòa I.7**: giữ B theo λ = 34·10⁵ J/kg in trên đề (bốn phương án đều tính theo số này). III.4: file sửa N_A 6,2 → 6,02·10²³ (đáp số 2,97); theo nguyên văn có thể ra 3,06 tùy cách tính.
- **Tĩnh Gia I II.3**: theo chữ in là S S S S (như file); nếu sửa lỗi in ("20 °C", "J/(kg.K)", ý d "nhiệt lượng cần cung cấp cho chảo") thì S Đ Đ Đ — bản lời khác của câu này trên VietJack cũng ghi S Đ Đ Đ.
- **Cẩm Phả III.6**: đề gốc mất hình kích thước phòng; 14 kg chỉ đúng với phòng tự dựng 8 × 5 × 4 m (Δm = 0,0884·V). Chưa xác minh được kích thước gốc.
- **Tĩnh Gia I III.2**: 0,66 đúng với mạch nối tiếp tự dựng (đề gốc thiếu hình).

### C. Mệnh đề lệch số liệu — tính chặt là Sai như file, nhưng đề có dấu hiệu gõ nhầm (đáp án của trường có thể là Đúng)

- Cẩm Xuyên II.3d (1282 kg / đề "khoảng 1250 kg"); Phan Đăng Lưu II.2a (0,1787 mol / "xấp xỉ 0,17"); Ngô Gia Tự II.4d (4461 / đề in 4160 — nghi 4460); Nguyễn Khuyến Lần 3 II.1d (34,1 kJ / đề in "41 kJ" — nghi mất kí tự), II.1b (2,50·10⁶ / 2,64·10⁶); Nguyễn Khuyến LTT Lần 1 II.4c (85 % nếu chỉ tính nước / 92 % nếu tính cả vỏ ấm), II.4d (1,67 h / 1,8 h); Bắc Ninh SGD (scan) II.4d (3888 / 3995 — 3995 đúng với m = 0,18 kg); Liên trường Nghệ An Lần 2 II.2d (9,84 °C / đề ghi 8,9); Phú Thọ SGD Lần 1 II.2b (75,6 kJ / 75 kJ), II.2c (10 080 J / đề in "10,8 J").
- **Điểm mới (chưa có trong TIEN-DO)**: Kinh Môn II II.3d (3,33 W; 2,5 W của đề đúng bằng kết quả khi bỏ sót cos α); Chuyên KHTN Lần 3 II.1d (12,4 T; 4,0 T của đề đúng bằng kết quả khi áp nhầm công thức dây thẳng); Quảng Ninh SGD II.3d (2,56·10⁻⁴ W / đề in 2,65·10⁻⁴ — nghi đảo chữ số); Tĩnh Gia I II.3d ("nhiệt lượng mà nhôm thu vào" / số của đề là nhiệt lượng cả chảo thu); Cụm CM10 I.6 (đề ghi "Mười độ chia (10 °C)" → A như file; câu quen thuộc là "Một độ chia" → C).

### D. Hai cách hiểu — Fable chọn cùng cách với file

Chuyên KHTN Lần 1 III.4 (16; không trừ khí còn lại thì 18); Yên Hòa III.3 (78,6; trừ khí còn lại thì 78,1), II.1b (hướng nhìn hình); Cụm 13 trường I.17 (B mỗi dây 0,7 N; D tổng 1,4 N); Cụm liên trường Hà Tĩnh III.3 (4,65; 4,68); Phan Đăng Lưu I.16 (A và C cùng đúng theo SGK — KNTT / CTST, Cánh diều; file gõ C), III.2 (10 J; đoạn trích VietJack cũng 10), III.1 (20; đoạn trích VietJack cũng 20); Kinh Môn II III.6 (2,25 A → 2,3; gợi ý đổi yêu cầu làm tròn sang hàng phần trăm); Hàm Rồng II.4c (S; đáp án trường có thể Đ), III.6 (2108 theo hằng số SGK; 2105–2107 với hằng số khác); Hà Nội SGD II.2b; Hưng Yên SGD II.1c, d; Bắc Ninh SGD Lần 1 II.2c; Liên trường Nghệ An Lần 1 II.1c, II.4d; Phú Thọ SGD Lần 1 II.1a; Chuyên Phan Bội Châu II.2b, II.4b; Nguyễn Thị Minh Khai II.4c (99 kJ / 100 kJ); Ninh Bình SGD Lần 2 III.5 (6,23 với R = 8,31; 6,24 với 8,314), III.6 (1,98); Lương Đắc Bằng II.1d (Đ; Sai nếu hiểu chặt chữ "chứng minh được định luật"), II.4c (S; Đ nếu hiểu "do hao phí nên giá trị đo lớn hơn"), II.3c (Đ khi tính cả N = 1000 vòng; một vòng thì S); Nguyễn Khuyến LTT Lần 10 II.3a (S vì miệng ống sâu dưới mặt thoáng; Đ nếu coi ngang mặt thoáng), II.4b (S; chấm lỏng có thể Đ), III.6 (0,82 đẳng nhiệt theo lời đề, dù đề cũng ghi "cách nhiệt").

### E. Ý phụ thuộc đọc hình (chiều quấn dây, cực nguồn, phối cảnh, vị trí điểm) — Fable đọc độc lập trên ảnh gốc phóng to, đều khớp file

Nguyễn Thị Minh Khai I.3 (đoạn trích VietJack cũng D); Cụm CM10 II.4a, b, II.3b, c; Kinh Môn II II.2b; Nguyễn Khuyến LTT Lần 1 II.1c, II.2a, I.10; Nguyễn Khuyến LTT Lần 2 II.1b; Lào Cai SGD I.6, II.1c; Chuyên ĐH Vinh I.17, II.3; Liên trường Nghệ An Lần 1 I.8 (ghi chú "không phân biệt trước / sau" trong `kiem-chung.md` cũ chưa chính xác: mỗi vòng chỉ có một nét vắt qua mặt trước lõi); Chuyên Hạ Long II.1b; Thái Nguyên SGD Lần 1 II.1c (đo điểm ảnh bốn vạch cực); Ninh Bình SGD Lần 2 II.4a; Hà Nội SGD II.3; Lương Đắc Bằng II.2d (điểm (4) là giao của đường qua O với đường đẳng nhiệt → S).

### F. Đáp số Phần III đề không yêu cầu làm tròn / thiếu hằng số — đều khớp file

Bắc Ninh SGD Lần 1 III.6 (0,6 là giá trị đúng, không cần làm tròn); Quảng Ninh SGD III.2 (608), III.3 (0,44), III.6 (2,15; lấy 1 eV = 1,602·10⁻¹⁹ J thì 2,14); Chuyên ĐH Vinh II.4d, III.2 (14; không đổi với c = 4180 hay 4200); Nguyễn Khuyến LTT Lần 10 III.1 (0,88 chính xác); các đề không có "Cho biết" (Chuyên KHTN Lần 3, Nguyễn Khuyến LTT Lần 2, Hàm Rồng, Ninh Bình SGD Lần 2): đổi N_A, R, k không làm đổi đáp số, trừ Ninh Bình SGD Lần 2 III.5 và Hàm Rồng III.6 nêu ở mục D.

### G. Lỗi HÌNH vẽ lại sai quan hệ so với hình gốc (chuyển phiên vẽ hình; phiên này không sửa)

- **Yên Hòa I.13**: kí hiệu nguồn bị đảo cực (gốc: vạch dài ở trên / phía xa; TikZ: vạch ngắn ở trên) → cực nguồn mâu thuẫn với mũi tên I.
- **Nguyễn Thị Minh Khai II.2 (Hình a)**: đảo cực nguồn và chỉ vẽ 1 pin (gốc 2 pin, bản dài bên phải nối biến trở) → theo hình vẽ lại, lực từ lên X hướng lên, mâu thuẫn Hình b và đáp án ý a.
- **Chuyên Phan Bội Châu I.6**: hai electron ⊖ ở dây trái, phải của hình gốc bị vẽ thành nhãn "I" đỏ nhưng giữ chiều mũi tên của electron → đọc thành dòng điện chạy vào cực dương ở mạch ngoài.
- **Chuyên ĐH Vinh III.3**: vòng mũi tên từ trường quanh hai thanh ray vẽ cùng chiều (gốc ngược chiều nhau); thiếu dấu "−" ở đầu ray phía sau.
- Lệch nhỏ, không ảnh hưởng đáp án: Nguyễn Khuyến LTT Lần 1 II.4 (trục chia 5 khoảng tới 240 s, gốc 4 khoảng), II.2 (thiếu nét dây nối hai cuộn); Cẩm Phả II.1 (lưới 9 hàng, gốc 8); Cẩm Xuyên II.2 (nét đứt đường sức); Lào Cai SGD I.6, Liên trường Nghệ An Lần 1 I.8 (móc thừa ở vòng dây cuối); Chuyên KHTN Lần 1 III.6 (đầu pin hở với dây nối); Chuyên Phan Bội Châu II.3 (chấm xanh thiếu dấu "−"); Cụm CM10 II.4 (chi tiết móc dưới của cuộn dây).

### H. Lời đề, lời giải, ghi chú — sai sót nhỏ agent thấy (không đổi đáp án)

Cẩm Xuyên II.4d (lời giải ghi 18 070 s, đúng là 18 059 s); Phan Đăng Lưu II.2d (lời giải ghi "(2) → (5) đẳng áp" trong khi chu trình không có đoạn này); Chuyên Phan Bội Châu II.2c (14,14 → 14,13 m/s); Yên Hòa II.2b (lời giải thêm giả thiết "hai cánh tay đòn bằng nhau"). Sửa chữ chưa ghi ở mục "Sửa lời đề" của `kiem-chung.md`: Cụm liên trường Hà Tĩnh I.13 ("nhiệt T₁" → "nhiệt độ T₁"), Hưng Yên SGD I.18 (bỏ chữ "đó"), Bắc Ninh SGD (scan) I.16 (thêm "trạng thái"), Ninh Bình SGD Lần 2 III.3 ("phần chục" → "phần mười"). Lương Thế Vinh: `kiem-chung.md` ghi sửa ¹³¹₅₁I "cả 4 chỗ", thực tế 6 chỗ (file đã sửa đủ). Kinh Môn II: `kiem-chung.md` ghi bỏ dòng "…" ở bảng II.1 nhưng file vẫn giữ.

### I. Tên, lần thi

- Liên trường Nghệ An Lần 1: trang hoatieu (theo đoạn trích tìm kiếm) gọi là "Sở Nghệ An Lần 1", 24 mã đề 3101–3124 → ủng hộ cách đặt "Lần 1".
- **Bắc Ninh SGD (scan)**: theo đoạn trích tìm kiếm của chuvanbien.vn (file `LOP12_DEKTCUOIKI1_SOBACNINH_SOCANTHO.pdf`), đây có thể là đề **kiểm tra cuối học kì I** Vật lí 12 của Sở Bắc Ninh (45 phút), bên sưu tầm đổi tiêu đề thành "khảo sát chất lượng tốt nghiệp THPT, 50 phút". Chưa xác nhận được (trang bị chặn) — thầy xem có giữ đề này trong bộ thi thử không.

### J. Hạn chế: đối chiếu trên mạng gần như không làm được

Mạng của phiên (môi trường Default, mức Limited, danh sách tên miền cho phép trống) chặn các trang đăng đề: `khoahoc.vietjack.com`, `hoatieu.vn`, `chuvanbien.vn`, `loigiaihay.com`, `tuyensinh247.com`, `docs.google.com`, `vietnamnet.vn`, `image.plo.vn`, `news.laodong.vn`. Agent chỉ đọc được đoạn trích của công cụ tìm kiếm (một phần ở 5 đề: Phan Đăng Lưu, Quảng Ninh SGD, Nguyễn Thị Minh Khai, Cụm CM10, câu I.11 Ngô Gia Tự). Link đã ghi ở mục "Nguồn trên mạng" của từng `kiem-chung-v2.md`:

- VietJack có trang cả đề cho 10 đề (Lương Thế Vinh, Cẩm Xuyên, Chuyên KHTN Lần 3, Phan Đăng Lưu, Quảng Ninh SGD, Nguyễn Thị Minh Khai, Cụm CM10, Liên trường Nghệ An Lần 1, Chuyên Hạ Long, Chuyên Phan Bội Châu) và trang câu lẻ cho 7 đề (Cụm liên trường Hà Tĩnh, Thái Nguyên SGD Lần 1, Liên trường Nghệ An Lần 2, Chuyên KHTN Lần 1, Tĩnh Gia I, Nguyễn Khuyến LTT Lần 1, Nguyễn Khuyến LTT Lần 10). Đáp án cả đề trên VietJack có khi nằm sau gói VIP.
- hoatieu.vn có trang cho ít nhất 8 đề (Hưng Yên SGD, Bắc Ninh SGD Lần 1, Hàm Rồng, Chuyên Hạ Long, Phú Thọ SGD, Cụm CM10, Liên trường Nghệ An Lần 1, Ninh Bình SGD), nhiều trang kèm file đáp án.
- Cuối phiên (14/11/2026) thầy đã duyệt thêm 5 tên miền `khoahoc.vietjack.com`, `hoatieu.vn`, `chuvanbien.vn`, `loigiaihay.com`, `tuyensinh247.com` vào danh sách cho phép của môi trường Default. Tuy vậy, trong phiên này lệnh đọc các trang đó (cả `curl` lẫn WebFetch) vẫn bị chế độ cấp quyền tự động của Claude Code chặn (lí do "Unauthorized Access"), nên chưa chạy bổ sung. Muốn chạy: thêm luật cho phép đọc các tên miền này (ví dụ `WebFetch(domain:khoahoc.vietjack.com)`) vào `permissions.allow` của `.claude/settings.json` trong repo, rồi chạy bổ sung riêng bước đối chiếu mạng cho các điểm ở mục A–D (rẻ, không phải giải lại); chỉ đọc phần công khai, không vượt nội dung trả phí (VIP).

### K. Quy trình

- Phiên chính kiểm bằng dấu thời gian truy cập tệp: với cả 35 đề, `fable.md` (nháp đáp án độc lập) được ghi **trước** lần đầu `kiem-chung.md` của đề đó được mở (cách nhau từ khoảng 45 giây đến 2 phút). Không kiểm được theo cách này với file `.tex` (phiên chính đã đọc các file `.tex` từ đầu phiên để dựng công cụ trích đáp án).
- 4 agent tự báo có chạy `git status --short` (chỉ đọc) — trái quy định "không chạy git" nhưng không thay đổi repo. Thay đổi của nhánh so với `main` chỉ gồm 35 file `kiem-chung-v2.md` mới và file này; không file nào có sẵn bị sửa.
- Nháp của từng agent (`fable.md`, `mang.md`, script tính) ở `/tmp/<tên đề>/` của máy phiên, không commit.

### L. Việc tiếp theo đề xuất

1. Thầy quyết các điểm mục A–D (nhất là 3 ý lệch mục A, các câu sửa lời đề mục B, các mệnh đề nghi gõ nhầm mục C), rồi một phiên sửa `.tex`, `kiem-chung.md`, `TIEN-DO.md` theo quyết định.
2. Chuyển 4 lỗi hình mục G (Yên Hòa I.13, Nguyễn Thị Minh Khai II.2, Chuyên Phan Bội Châu I.6, Chuyên ĐH Vinh III.3) cho phiên vẽ hình (phần A).
3. Khi phiên được phép đọc các trang ở mục J (tên miền đã mở trong môi trường, còn thiếu quyền đọc trang): chạy bổ sung đối chiếu mạng cho các điểm mục A–D.
4. Sửa các sai sót nhỏ mục H cùng lúc với việc 1.
