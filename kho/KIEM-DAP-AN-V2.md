# KIỂM ĐÁP ÁN V2 — 35 ĐỀ PDF (lô P01–P09), PHIÊN FABLE PHẦN B

Phiên 14/11/2026, nhánh `claude/great-knuth-6gcmjx`. Mỗi đề một agent con giải lại độc lập 28 câu từ ảnh trang đề gốc (ghi đáp án trước khi mở file `.tex`), tìm đáp án trên mạng, soát câu lý thuyết theo SGK, rồi so với `\True`, `\shortans` trong file đề. Kết quả từng đề: `de/<tên đề>/kiem-chung-v2.md` (bảng đáp án Fable 28 câu, bảng câu lệch / câu đang `% KIỂM TRA`, căn cứ lý thuyết, nguồn trên mạng). Phiên này KHÔNG sửa file `.tex`, `kiem-chung.md`, `kho/TIEN-DO.md`: mọi thay đổi đáp án chờ thầy quyết.

**Tiến độ: 3/35 đề đã kiểm; tổng 0 câu / ý lệch (file khác kết luận cuối của Fable).**

Cách đếm "lệch": Phần I, III theo câu; Phần II theo ý. Thứ tự làm: đề có `% KIỂM TRA` trong file `.tex` (21 đề) → đề có điểm ở mục "Chờ thầy quyết" của TIEN-DO (8 đề) → đề chỉ có điểm "thầy xem" (6 đề).

## Bảng 35 đề

| STT | Lô | Đề (mở `kiem-chung-v2.md`) | Trạng thái | Số lệch | Câu lệch (file / Fable) | Đề mơ hồ, cần thầy quyết | Lỗi gõ lời đề | Đáp án trên mạng |
|---|---|---|---|---|---|---|---|---|
| 1 | P01 | `VatLi2026-HaNoi-ChuyenKHTN-Lan3` | đang kiểm | | | | | |
| 2 | P01 | [`VatLi2026-HaNoi-LuongTheVinh-Lan1`](../de/VatLi2026-HaNoi-LuongTheVinh-Lan1/kiem-chung-v2.md) | xong | 0 | II.2a: file S (theo đề đã sửa ¹³¹₅₃I) / Fable lần 1 Đ (theo nguyên văn đề gốc ¹³¹₅₁I). Kết luận: với lời đề trong file thì S là đúng; với nguyên văn đề gốc thì Đ. | II.2a (giữ cách sửa Z = 53, a Sai; hay theo đề gốc Z = 51, a Đúng — đáp án ý đồ của trường có thể là Đúng). | không thấy (đã so lời đề, số liệu, thứ tự phương án và thứ tự ý của cả 28 câu với ảnh trang; các chỗ khác bản gốc đều là sửa có chủ ý và đã ghi ở `kiem-chung.md`). Ghi chú nhỏ: `kiem-chung.md` ghi ¹³¹₅₁I sai "cả 4 chỗ", thực tế bản gốc ghi 6 chỗ (4 trong lời dẫn, ý b, ý d) — file đã sửa đủ cả 6. | không tìm thấy |
| 3 | P02 | [`VatLi2026-HaNoi-YenHoa-Lan1`](../de/VatLi2026-HaNoi-YenHoa-Lan1/kiem-chung-v2.md) | xong | 0 | không | II.1b (hình không nói hướng nhìn: nhìn từ trên xuống → S, nhìn từ dưới lên → Đ; file và Fable cùng chọn S); III.3 (78,6 nếu dùng hết toàn bộ khí / 78,1 nếu trừ khí còn lại ở áp suất khí quyển; file và Fable cùng chọn 78,6); III.4 (đề gốc in N_A = 6,2·10²³: tính qua k ra 2,97, tính qua R rồi nhân N_A = 6,2·10²³ ra 3,06; file đã sửa N_A thành 6,02·10²³ nên chỉ còn 2,97); III.5 (tan α chỉ có nghĩa khi coi 1 g ứng 1 A trên hai trục; file và Fable cùng hiểu như vậy → 34,7) | lời đề không thấy lỗi. Lỗi HÌNH vẽ lại câu I.13: kí hiệu nguồn điện bị đảo cực so với hình gốc (hình gốc: vạch dài – cực dương – nằm phía trên / phía xa, vạch ngắn phía dưới; TikZ: vạch ngắn đậm phía trên, vạch dài phía dưới), nên trong hình vẽ lại cực nguồn mâu thuẫn với hai mũi tên I (dòng điện đi ra từ cực âm). Đáp án theo mũi tên I không đổi (hướng A), nhưng học sinh suy chiều dòng điện từ kí hiệu nguồn sẽ ra hướng C. Cần đổi chỗ hai vạch (dòng 366–367 của file .tex). | không tìm thấy |
| 4 | P02 | `VatLi2026-HaTinh-CamXuyen-Lan2` | đang kiểm | | | | | |
| 5 | P03 | `VatLi2026-HaTinh-CumLienTruong` | đang kiểm | | | | | |
| 6 | P03 | [`VatLi2026-HaiPhong-Cum13Truong-Lan2`](../de/VatLi2026-HaiPhong-Cum13Truong-Lan2/kiem-chung-v2.md) | xong | 0 | không | I.17 ("lực căng của dây treo": mỗi dây 0,7 N = B như file; tổng hai dây 1,4 N = D). Lưu ý nhẹ, không đổi đáp án: III.1 (đề ghi "xilanh cách nhiệt" nhưng yêu cầu coi nhiệt độ không đổi), III.4 ("tăng bao nhiêu lần" hiểu là V₂/V₁), III.6 (đề gốc hỏi "tốc độ … đạt được", file đã thêm chữ "lớn nhất"). | không thấy (số liệu, phương án, thứ tự ý của 28 câu khớp ảnh trang; các chỗ sửa lời đề đều đã ghi ở `kiem-chung.md`) | không tìm thấy |
| 7 | P03 | `VatLi2026-HaiPhong-KinhMonII-Lan2` | đang kiểm | | | | | |
| 8 | P04 | `VatLi2026-Hue-PhanDangLuu-Lan1` | đang kiểm | | | | | |
| 9 | P04 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1` | đang kiểm | | | | | |
| 10 | P04 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan3` | đang kiểm | | | | | |
| 11 | P05 | `VatLi2026-HungYen-SoGD-Lan1` | đang kiểm | | | | | |
| 12 | P05 | `VatLi2026-NgheAn-ChuyenDHVinh-Lan1` | chưa kiểm | | | | | |
| 13 | P06 | `VatLi2026-NgheAn-LienTruong-Lan2` | chưa kiểm | | | | | |
| 14 | P07 | `VatLi2026-PhuTho-NgoGiaTu-Lan1` | chưa kiểm | | | | | |
| 15 | P07 | `VatLi2026-QuangNinh-CamPha-Lan1` | chưa kiểm | | | | | |
| 16 | P08 | `VatLi2026-QuangNinh-SoGD-Lan1` | chưa kiểm | | | | | |
| 17 | P08 | `VatLi2026-ThaiNguyen-SoGD-Lan1` | chưa kiểm | | | | | |
| 18 | P08 | `VatLi2026-ThanhHoa-HamRong-Lan1` | chưa kiểm | | | | | |
| 19 | P09 | `VatLi2026-ThanhHoa-TinhGia1` | chưa kiểm | | | | | |
| 20 | P01 | `VatLi2026-BacNinh-SoGD-Lan1` | chưa kiểm | | | | | |
| 21 | P09 | `VatLi2026-BacNinh-SoGD` | chưa kiểm | | | | | |
| 22 | P01 | `VatLi2026-HaNoi-ChuyenKHTN-Lan1` | chưa kiểm | | | | | |
| 23 | P02 | `VatLi2026-HaNoi-NguyenThiMinhKhai-Lan1` | chưa kiểm | | | | | |
| 24 | P03 | `VatLi2026-HaiPhong-CumCM10-Lan1` | chưa kiểm | | | | | |
| 25 | P04 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2` | chưa kiểm | | | | | |
| 26 | P05 | `VatLi2026-LaoCai-SoGD-Lan1` | chưa kiểm | | | | | |
| 27 | P06 | `VatLi2026-NgheAn-LienTruong-Lan1` | chưa kiểm | | | | | |
| 28 | P06 | `VatLi2026-NinhBinh-SoGD-Lan2` | chưa kiểm | | | | | |
| 29 | P07 | `VatLi2026-QuangNinh-ChuyenHaLong-Lan1` | chưa kiểm | | | | | |
| 30 | P02 | `VatLi2026-HaNoi-SoGD-Lan1` | chưa kiểm | | | | | |
| 31 | P05 | `VatLi2026-NgheAn-ChuyenPhanBoiChau-Lan1` | chưa kiểm | | | | | |
| 32 | P06 | `VatLi2026-NinhBinh-SoGD-Lan1` | chưa kiểm | | | | | |
| 33 | P07 | `VatLi2026-PhuTho-SoGD-Lan1` | chưa kiểm | | | | | |
| 34 | P08 | `VatLi2026-ThanhHoa-LuongDacBang-Lan1` | chưa kiểm | | | | | |
| 35 | P09 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10` | chưa kiểm | | | | | |
