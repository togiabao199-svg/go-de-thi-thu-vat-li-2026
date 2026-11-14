# Kiểm đáp án v2 (Fable) — VatLi2026-HaNoi-YenHoa-Lan1

Ngày 14/11/2026. Đề gốc: `kho/goc/Ha Noi - THPT Yen Hoa - Lan 1.pdf`. Giải lại độc lập từ ảnh trang đề gốc trước khi mở file đề; file đề không bị sửa.

## Tóm tắt
- Số câu / ý lệch (file khác kết luận cuối của Fable): 0 (Phần I, III đếm theo câu; Phần II đếm theo ý)
- Câu lệch: không
- Câu đề mơ hồ, hai cách hiểu đều chấp nhận được (file không sai nhưng cần thầy quyết): II.1b (hình không nói hướng nhìn: nhìn từ trên xuống → S, nhìn từ dưới lên → Đ; file và Fable cùng chọn S); III.3 (78,6 nếu dùng hết toàn bộ khí / 78,1 nếu trừ khí còn lại ở áp suất khí quyển; file và Fable cùng chọn 78,6); III.4 (đề gốc in N_A = 6,2·10²³: tính qua k ra 2,97, tính qua R rồi nhân N_A = 6,2·10²³ ra 3,06; file đã sửa N_A thành 6,02·10²³ nên chỉ còn 2,97); III.5 (tan α chỉ có nghĩa khi coi 1 g ứng 1 A trên hai trục; file và Fable cùng hiểu như vậy → 34,7)
- Lỗi gõ lời đề so với bản gốc (nếu thấy): lời đề không thấy lỗi. Lỗi HÌNH vẽ lại câu I.13: kí hiệu nguồn điện bị đảo cực so với hình gốc (hình gốc: vạch dài – cực dương – nằm phía trên / phía xa, vạch ngắn phía dưới; TikZ: vạch ngắn đậm phía trên, vạch dài phía dưới), nên trong hình vẽ lại cực nguồn mâu thuẫn với hai mũi tên I (dòng điện đi ra từ cực âm). Đáp án theo mũi tên I không đổi (hướng A), nhưng học sinh suy chiều dòng điện từ kí hiệu nguồn sẽ ra hướng C. Cần đổi chỗ hai vạch (dòng 366–367 của file .tex).
- Đáp án trên mạng: không tìm thấy

## Bảng đáp án 28 câu
| Câu | Fable (độc lập) | File | Mạng | Khớp |
|---|---|---|---|---|
| I.1 | D | D | — | khớp |
| I.2 | D | D | — | khớp |
| I.3 | A | A | — | khớp |
| I.4 | A | A | — | khớp |
| I.5 | D | D | — | khớp |
| I.6 | B | B | — | khớp |
| I.7 | B | B | — | khớp (KIỂM TRA) |
| I.8 | A | A | — | khớp |
| I.9 | C | C | — | khớp |
| I.10 | C | C | — | khớp |
| I.11 | C | C | — | khớp |
| I.12 | A | A | — | khớp |
| I.13 | B | B | — | khớp (hình vẽ lại sai cực nguồn) |
| I.14 | A | A | — | khớp |
| I.15 | D | D | — | khớp |
| I.16 | D | D | — | khớp |
| I.17 | D | D | — | khớp |
| I.18 | B | B | — | khớp |
| II.1 | Đ S Đ Đ | Đ S Đ Đ | — | khớp (ý b thầy xem) |
| II.2 | Đ S Đ S | Đ S Đ S | — | khớp (KIỂM TRA) |
| II.3 | Đ S Đ S | Đ S Đ S | — | khớp |
| II.4 | Đ Đ S S | Đ Đ S S | — | khớp |
| III.1 | 1,3 | 1,3 | — | khớp |
| III.2 | 3 | 3 | — | khớp |
| III.3 | 78,6 | 78,6 | — | khớp (thầy xem) |
| III.4 | 2,97 | 2,97 | — | khớp (file đã sửa N_A) |
| III.5 | 34,7 | 34,7 | — | khớp |
| III.6 | 11,5 | 11,5 | — | khớp |

## Các câu lệch, câu đang `% KIỂM TRA` / "thầy xem"
| Câu | File | Fable lần 1 | Mạng (link) | Kết luận của Fable | Căn cứ |
|---|---|---|---|---|---|
| I.7 (`% KIỂM TRA`) | B (14,018 MJ), giữ λ = 34·10⁵ J/kg của đề gốc | B | — | File đúng: giữ số liệu đề, chọn B | Đã đọc lại ảnh trang 1: đề in rõ "34.10⁵ J/kg". Q = 4·34·10⁵ + 4·4180·25 = 13,6·10⁶ + 0,418·10⁶ = 14,018 MJ, trùng đúng phương án B. Với 3,4·10⁵: 1,778 MJ; với 3,34·10⁵: 1,754 MJ — không có phương án. Bốn phương án (18,96; 14,018; 16,94; 21,23) đều cỡ chục MJ nên người ra đề đã tính theo 34·10⁵; số liệu phi thực tế nhưng đề tự nhất quán. Nếu thầy muốn sửa λ về 3,4·10⁵ thì phải sửa cả bốn phương án (chia 10 không được vì phần mcΔt không đổi). |
| II.2 (`% KIỂM TRA`) | Đ S Đ S | Đ S Đ S | — | File đúng; ghi chú của file về I = 0,46 A là xác đáng | Ảnh trang 5: dòng 3 in "0,46". F/I lần lượt 0,300; 0,275; 0,370 — dòng 3 lệch hẳn; với I = 0,6 A thì F/I = 0,283 và B = 0,170/(0,6·16) = 0,0177 ≈ 0,018 (NL ≈ 16 suy từ hai dòng đầu), tức bản gốc gõ nhầm 0,6 thành 0,46. Bốn ý chỉ dùng cột F₁ và cột B nên không đổi: a) F = F₂ − F₁ tính từ hai số đọc → gián tiếp (Đ); b) F₁ = 0,210 N, không phải 0,021 N (S); c) B tb = 0,018; ΔB tb = (0,001 + 0,001 + 0)/3 = 0,00067 ≈ 0,001 → (0,018 ± 0,001) T (Đ); d) 0,001/0,018 = 5,6 % (hoặc 0,00067/0,018 = 3,7 %), không ra 6,5 % (S). Lưu ý nhỏ: lời giải ý b) trong file viết "P = 0,210 N (hai cánh tay đòn bằng nhau)" là giả thiết thêm, đề không cho; kết luận Sai không phụ thuộc giả thiết này. |
| II.1b (thầy xem) | S | S (khá chắc) | — | File đúng theo cách hiểu tự nhiên; đề hơi mơ hồ | Ảnh gốc (phóng to): đường sức hướng lên–phải, M ở trên–trái, N ở dưới–phải. B và MN cùng nằm ngang nên mặt phẳng hình là mặt phẳng ngang; nhìn từ trên xuống: chiều M→N = (1; −1), B = (1; 1) ⇒ (M→N) × B hướng ra khỏi mặt giấy = hướng lên. Lực nâng khi dòng điện chạy M → N ⇒ "từ N đến M" là Sai. Nếu coi hình nhìn từ dưới lên thì đảo lại (Đ), nhưng không có lí do gì để hiểu vậy. Bố cục đáp án Đ S Đ Đ cũng hợp lí. |
| III.3 (thầy xem) | 78,6 | 78,6 (khá chắc) | — | File đúng theo ý người ra đề; 78,1 là cách hiểu thứ hai | V₀ = 15·10⁶·14·273/(300·1,013·10⁵) = 1886,5 lít chuẩn; 24 lít/giờ ⇒ 78,60 h. Trừ khí còn lại khi áp suất bình bằng 1,013·10⁵ Pa (14·273/300 = 12,7 lít chuẩn): 78,07 h ≈ 78,1. Đề nói "dùng hết bình" và không nhắc áp suất còn lại ⇒ 78,6. T₀ = 273,15 K vẫn ra 78,6. |
| III.4 (file sửa lời đề) | 2,97 (N_A sửa 6,2 → 6,02·10²³) | 2,97 | — | File đúng; việc sửa N_A hợp lí | N = pV/(kT) = 1,2·10⁶·10⁻³/(1,38·10⁻²³·293) = 2,968·10²³ ⇒ 2,97 (không cần N_A). Ảnh trang 6 đề gốc in "N_A = 6,2.10²³ mol⁻¹", lệch với khối Cho biết (6,02·10²³). Theo đề gốc chưa sửa: n = pV/(RT) = 0,4928 mol; n·6,2·10²³ = 3,06·10²³ (đáp số khác), n·6,02·10²³ = 2,967·10²³ (2,97). Sau khi file sửa thành 6,02·10²³ thì hai đường tính cùng ra 2,97. |
| III.5 (ghi chú của file) | 34,7 | 34,7 (khá chắc) | — | File đúng theo ý đề | (m − m₀)g = BIl ⇒ hệ số góc Δm/ΔI = Bl/g; lấy tan 28° = 0,5317 g/A ⇒ B = 0,5317·10⁻³·9,8/0,15 = 0,03474 T = 34,7 mT. Đồ thị gốc không có số trên lưới (chỉ mốc 80 g) nên không kiểm được tỉ lệ trục; chỉ có cách dùng tan α. |
| I.13 (hình) | B (hướng A) | B | — | Đáp án đúng; HÌNH vẽ lại sai cực nguồn | Ảnh gốc phóng to 900 dpi: trên cạnh phải của khung, vạch dài (cực dương) ở phía trên (phía xa), vạch ngắn ở dưới ⇒ dòng điện ra từ cực dương, chạy cạnh trên sang trái, qua đoạn dây giữa hai cực từ sau ra trước, cạnh dưới sang phải — khớp hai mũi tên I. I (ra trước) × B (N→S, sang phải) ⇒ F hướng lên = hướng A. Trong TikZ (dòng 366–367) vạch ngắn đậm ở trên, vạch dài ở dưới: ngược hình gốc và ngược với mũi tên I. |

Không có câu nào file và Fable khác nhau; lời giải lần 1 của Fable không phải sửa sau khi xem file.

## Căn cứ các câu lý thuyết
- I.3 — Nén khí: thể tích giảm, mật độ phân tử tăng nên áp suất tăng (SGK 12, bài Mô hình động học phân tử chất khí / Định luật Boyle).
- I.5 — Tốc kế đo tốc độ; ba dụng cụ còn lại là nhiệt kế (SGK 12, bài Nhiệt độ – Thang nhiệt độ – Nhiệt kế).
- I.6 — Đúc kim loại: nóng chảy rồi đông đặc (SGK 12, bài Cấu trúc của chất – Sự chuyển thể).
- I.8 — Quy tắc bàn tay trái, F cùng chiều I × B (SGK 12, bài Lực từ tác dụng lên dây dẫn mang dòng điện – Cảm ứng từ): a) I sang phải, B vào ⇒ F lên (đúng); b) I ra, B sang phải ⇒ F lên (hình vẽ xuống); c) I ra, B lên ⇒ F sang trái (hình vẽ sang phải); d) I xuống, B vào ⇒ F sang phải (hình vẽ sang trái).
- I.9 — Đẳng áp: đường qua O trên (V, T), nằm ngang trên (p, T); đẳng nhiệt nén: p tăng; đẳng tích: đường qua O trên (p, T) (SGK 12, bài Định luật Boyle, Định luật Charles, Phương trình trạng thái).
- I.10 — Nhiệt độ sôi của chất lỏng tăng khi áp suất trên mặt thoáng tăng (SGK 12, bài Sự chuyển thể – mục sự sôi).
- I.11 — ΔU = A + Q; quy ước: nhận công A > 0, thực hiện công A < 0; nhận nhiệt Q > 0, truyền nhiệt Q < 0 (SGK 12, bài Nội năng – Định luật I của nhiệt động lực học).
- I.12 — V tỉ lệ thuận với T (đường kéo dài qua O) ⇒ đẳng áp; V tăng ⇒ giãn (định luật Charles).
- I.13 — Đường sức từ ngoài nam châm đi ra từ cực N, vào cực S; quy tắc bàn tay trái.
- I.14 — Phân tử chất rắn dao động quanh vị trí cân bằng xác định, không đứng yên (SGK 12, bài Cấu trúc của chất). Phương án B (chất khí dễ nén vì lực liên kết yếu hơn) diễn đạt chưa đủ (nguyên nhân chính là khoảng cách giữa các phân tử khí rất lớn) nhưng không sai rõ như A.
- I.15 — Quy tắc nắm tay phải cho dòng điện tròn: dòng ngược chiều kim đồng hồ ⇒ B tại tâm hướng ra; cùng chiều ⇒ hướng vào; B luôn vuông góc mặt phẳng vòng dây (SGK 12, bài Từ trường).
- I.16 — Bay hơi xảy ra ở mặt thoáng, ở mọi nhiệt độ; sôi xảy ra ở nhiệt độ sôi xác định (ứng với áp suất cho trước), cả trong lòng và trên mặt thoáng.
- I.17 — Mô hình khí lí tưởng: phân tử coi là chất điểm, chuyển động hỗn loạn không ngừng, chỉ tương tác khi va chạm (SGK 12, bài Mô hình động học phân tử chất khí).
- I.18 — Đẳng áp, T tăng ⇒ V tăng, số phân tử không đổi ⇒ khoảng cách trung bình giữa các phân tử tăng.
- II.2a — Phép đo gián tiếp: đại lượng được tính qua công thức từ các đại lượng đo trực tiếp (SGK 10, bài Sai số trong phép đo các đại lượng vật lí); F = F₂ − F₁. Quy trình thí nghiệm: SGK KNTT 12, bài 15 (Lực từ tác dụng lên dây dẫn mang dòng điện – Cảm ứng từ, mục thí nghiệm đo cảm ứng từ).
- II.2c, d — Giá trị trung bình, sai số tuyệt đối trung bình, sai số tỉ đối δ = ΔB/B tb (SGK 10, cùng bài).
- II.3a, b, c — Thí nghiệm kiểm chứng định luật Boyle (SGK 12, bài Định luật Boyle): áp kế đo áp suất khí trong xilanh; dịch chuyển pit-tông chậm để nhiệt độ khí không đổi; pV = hằng số nên V tăng thì p giảm.
- II.4a — Hơi nước trong không khí gặp thành cốc lạnh thì ngưng tụ (sự chuyển thể). II.4b — nhiệt độ cân bằng nằm giữa nhiệt độ thấp nhất và cao nhất của các vật trao đổi nhiệt. II.4c, d — nước đá ở −5 °C là thể rắn; nhận nhiệt thì nóng chảy (rắn → lỏng).

## Nguồn trên mạng
(Bổ sung 14/11/2026: xem mục "Đối chiếu mạng bổ sung" cuối file.)

Không tìm thấy đáp án trên mạng. Các truy vấn đã thử (WebSearch, sau khi đã ghi xong `fable.md`):
1. đề thi thử tốt nghiệp THPT 2026 Vật lí THPT Yên Hòa Hà Nội lần 1 đáp án lời giải
2. "tàu mini chạy trên đệm từ trường" "thanh dẫn kim loại MN" 10 gam/mét đáp án
3. "Hương vị của bia Hà nội" "rót 200 g bia vào cốc" "40 g nước đá" −2,8 lời giải
4. "Yên Hòa" đề thi thử vật lí 12 lần 1 2025-2026 "bia Hà nội" OR "trà sữa" "bạn Linh" đáp án
5. "Bạn Linh pha chế một mẫu trà sữa" "nước trà đen (mẫu A)" "sữa tươi (mẫu C)" đúng sai
6. "y tá thường sử dụng ống tiêm để bơm một lượng nhỏ khí vào lọ thuốc" "0,9ml" "0,5ml"
7. "Yên Hòa" "Vật lí" thi thử tốt nghiệp 2026 lần 1 (giới hạn thi247, hoatieu, thuvienvatly, vndoc, tailieumoi)
8. "Quả cầu có nhiệt dung riêng" "460" "46 cm" "nâng lên đến B rồi thả rơi" "60% độ giảm thế năng"
9. "Bạn Trang đã tiến hành thí nghiệm" "cảm ứng từ B trong lòng của nam châm" "α = 28" cân điện tử PQ

Ghi nhận: hoatieu.vn chỉ có đề Hóa của THPT Yên Hòa 2026 (https://hoatieu.vn/de-thi-thu-tot-nghiep-mon-hoa-thpt-yen-hoa-ha-noi-249457), không có đề Vật lí. Truy vấn 9 trả về một file Google Docs (https://docs.google.com/document/d/1LEI_3e3SCxiItANFCEmIhDVc6Esb0O-5) có thể chứa câu cân điện tử – thanh PQ, nhưng docs.google.com nằm ngoài các miền mạng được phép của phiên nên không mở được (không cố vượt). Các kết quả khác là đề của đơn vị khác hoặc bài tương tự, không khớp lời câu và số liệu.

## Đối chiếu mạng bổ sung (14/11/2026)

**Không tìm thấy đáp án trên mạng của đúng đề này** (0/28 câu có đáp án mạng). Không giải lại đề, không sửa đáp án.

### (a) Nguồn

- **Nguồn đúng đề:** không tìm thấy. Không trang nào trong kết quả tìm kiếm khớp lời câu và số liệu của đề (đã thử các câu đặc trưng I.7, II.1, II.4, III.5, III.6).
- **Nguồn đã xét nhưng KHÔNG đúng đề:**
  - https://hoatieu.vn/de-thi-thu-tot-nghiep-mon-hoa-thpt-yen-hoa-ha-noi-249457 — đề môn **Hóa** của THPT Yên Hòa 2026, không phải Vật lí (theo đoạn trích tìm kiếm); hoatieu.vn bị chặn (WebFetch: HTTP 403).
  - https://khoahoc.vietjack.com/question/2084863/tau-dem-tu-la-mot-phuong-tien-giao-thong-chay-tren-dem-tu-truong-uu-diem-chinh-cua-tau-dem-tu-so-voi (và bản 2310663) — câu lí thuyết về ưu điểm tàu đệm từ, không phải câu II.1 (thanh MN 10 g/m, B = 0,1 T); không mở.
  - https://khoahoc.vietjack.com/question/2311678/mot-nhom-hoc-sinh-tien-hanh-thi-nghiem-do-su-phu-thuoc-cua-ap-suat-khi-p-vao-nhiet-do-tuyet-doi-t — câu khác (p theo T), không thuộc đề này; không mở.
  - https://docs.google.com/document/d/1LEI_3e3SCxiItANFCEmIhDVc6Esb0O-5/export?format=pdf — hiện ra khi tìm câu III.5 (bạn Trang, cân điện tử, thanh PQ) và câu "bia Hà Nội"; WebFetch báo ENOTFOUND (bị chặn), không biết có đúng đề hay không.
- **Tên miền bị chặn trong lượt này:** docs.google.com (WebFetch: ENOTFOUND), hoatieu.vn (WebFetch: HTTP 403), news.laodong.vn (WebFetch: ENOTFOUND). Đọc được: khoahoc.vietjack.com (`curl`) — nhưng không tìm thấy trang nào của đề này trên VietJack.
- **Truy vấn đã thử (WebSearch, 6; cộng 9 truy vấn của phiên trước ở mục "Nguồn trên mạng"):**
  1. đề thi thử tốt nghiệp THPT 2026 môn Vật lí THPT Yên Hòa Hà Nội lần 1
  2. site:khoahoc.vietjack.com "mô hình tàu mini chạy trên đệm từ trường"
  3. "Bạn Linh pha chế một mẫu trà sữa" "mẫu A" "mẫu B" "mẫu C" nhiệt độ cân bằng
  4. "Yên Hòa" Vật lí 2026 đề thi thử có đáp án khoahoc.vietjack OR thuvienvatly OR tuyensinh247
  5. "Một gia đình đang chuẩn bị bữa ăn ngoài trời vào mùa hè" "4 kg nước đá" 25 nhiệt lượng
  6. site:khoahoc.vietjack.com "bia Hà Nội" "40 g nước đá" OR "Bạn Trang đã tiến hành thí nghiệm" cân điện tử nam châm

### (b) Bảng đối chiếu

| Câu (file) | File | Mạng | Link | So sánh |
|---|---|---|---|---|
| I.1 | D | — | — | không có đáp án mạng |
| I.2 | D | — | — | không có đáp án mạng |
| I.3 | A | — | — | không có đáp án mạng |
| I.4 | A | — | — | không có đáp án mạng |
| I.5 | D | — | — | không có đáp án mạng |
| I.6 | B | — | — | không có đáp án mạng |
| I.7 | B | — | — | không có đáp án mạng |
| I.8 | A | — | — | không có đáp án mạng |
| I.9 | C | — | — | không có đáp án mạng |
| I.10 | C | — | — | không có đáp án mạng |
| I.11 | C | — | — | không có đáp án mạng |
| I.12 | A | — | — | không có đáp án mạng |
| I.13 | B | — | — | không có đáp án mạng |
| I.14 | A | — | — | không có đáp án mạng |
| I.15 | D | — | — | không có đáp án mạng |
| I.16 | D | — | — | không có đáp án mạng |
| I.17 | D | — | — | không có đáp án mạng |
| I.18 | B | — | — | không có đáp án mạng |
| II.1 | Đ S Đ Đ | — | — | không có đáp án mạng |
| II.2 | Đ S Đ S | — | — | không có đáp án mạng |
| II.3 | Đ S Đ S | — | — | không có đáp án mạng |
| II.4 | Đ Đ S S | — | — | không có đáp án mạng |
| III.1 | 1,3 | — | — | không có đáp án mạng |
| III.2 | 3 | — | — | không có đáp án mạng |
| III.3 | 78,6 | — | — | không có đáp án mạng |
| III.4 | 2,97 | — | — | không có đáp án mạng |
| III.5 | 34,7 | — | — | không có đáp án mạng |
| III.6 | 11,5 | — | — | không có đáp án mạng |

### (c) Câu mạng khác file

Không có (không tìm được đáp án mạng nào của đúng đề). Các điểm mục B (I.7 — λ = 34·10⁵ J/kg; III.4 — N_A in 6,2·10²³) và mục D (III.3 — 78,6 / 78,1; II.1b — hướng nhìn hình): không có nguồn để đối chiếu.

### (d) Tổng

Số câu có đáp án mạng: 0/28; khớp: 0; khác: 0.
