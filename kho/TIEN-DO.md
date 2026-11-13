# TIẾN ĐỘ DỰ ÁN GÕ LẠI ĐỀ THI THỬ TN THPT 2026 MÔN VẬT LÍ

Đọc cùng `CLAUDE.md` (quy chuẩn, quy trình một lô) và `kho/kiem-ke.md` (kiểm kê 83 đề nguồn). Mỗi lô xong: cập nhật bảng dưới (trạng thái từng đề), mục "Việc đã xong", push và tạo PR.

## Giai đoạn hiện tại

- **Phiên 1a (06/11/2026) — xong, thầy duyệt 06/11/2026**: `CLAUDE.md` cho Vật lí; bộ macro hình chung `preamble-vatli-hinh.tex` (thêm circuitikz european), `tools/so_hinh.py` đọc macro từ file chung, dựng lại đề mẫu (bản đề 7 trang, lời giải 10 trang, PDF trùng bản cũ); `tools/README.md`; kiểm kê 83 đề `kho/kiem-ke.md`; chia lô (file này).
- **Lô M (13/11/2026) — xong, thầy duyệt 13/11/2026**: `VatLi2026-LaoCai-CumPhiaBac-Lan2` (mẫu thứ hai: đề PDF không đáp án, tự giải toàn bộ 28 câu, vẽ lại 14 hình). Bản đề 8 trang (ĐẠT), bản lời giải 12 trang. Thành phẩm trong `thanh-pham/`, kiểm chứng ở `de/VatLi2026-LaoCai-CumPhiaBac-Lan2/kiem-chung.md`.
- **Lô W01 (13/11/2026) — xong, thầy duyệt 13/11/2026**: 4 đề Word (Bắc Ninh ×3, Cà Mau), chạy Opus, 4 agent con song song (thầy cho phép trong phiên), phiên chính soát, thống nhất, gom macro. Chi tiết ở bảng dưới và mục "Chờ thầy quyết".
- **Tô màu lại 6 đề đã xong (13/11/2026) — chờ duyệt**: Cao Bằng, Lào Cai, 4 đề lô W01 (Opus, 6 agent con song song). Số trang bản đề / lời giải không đổi, cả 6 đề `kiem` ĐẠT, thành phẩm xuất lại. Điểm cần thầy quyết ở mục "Chờ thầy quyết".
- **Tiếp theo**: lô W02 (Opus, song song): `Đọc CLAUDE.md và kho/TIEN-DO.md rồi làm lô W02, chạy song song.`

## Quyết định của thầy

- 06/11/2026 — đề mẫu chuẩn: `de/VatLi2026-CaoBang-SoGD-Lan1/` (thầy đã duyệt chữ, lời giải, hình). Điều rút ra: `tham-khao/bai-hoc-de-mau.md`.
- 06/11/2026 — quy cách chốt (đã đưa vào `CLAUDE.md`): mỗi đề gốc thành 1 file đề hoàn chỉnh có đáp án và lời giải chi tiết, trình bày như đề mẫu; đề Word có lời giải thì viết lại theo ý lời giải gốc, đề không có thì tự giải; mọi câu tự giải lại, tính kiểm bằng Python, ghi `de/<tên>/kiem-chung.md`; lời giải xúc tích; tên file `VatLi2026-<Tinh>-<DonVi>-Lan<n>`; khung tiêu đề, `\tenchuong`, `\thuonghieu` theo mẫu; giữ cấu trúc và khối "Cho biết" của đề gốc; thành phẩm `<tên>.zip`, `<tên>-DE.pdf`, `<tên>.pdf`; không trộn mã đề; mọi hình vẽ lại bằng TikZ (circuitikz european cho mạch), chạy `so_hinh.py` tự soát; dàn trang bằng `tools/dan_trang`; đề lẻ là thành phẩm chính, gõ thống nhất để ghép sách sau.
- 06/11/2026 — duyệt PR phiên 1a: lô M là `VatLi2026-LaoCai-CumPhiaBac-Lan2`; loại 4 file trùng hẳn (bảng "Đề không gõ"); bỏ THPT Quế Võ 1 – Lần 1 (gần trùng Cụm TT1-QV1-LVT, chung 17/28 câu), giữ đề Cụm; tên đơn vị, số lần đặt theo tiêu đề đề gốc (không theo CSV) như `kho/kiem-ke.md`; mỗi phần đánh số lại từ câu 1; lô W11 (Vĩnh Long) gộp vào W10 (W10 có 5 đề); lô P đánh lại (P09 còn 3 đề, gồm 2 đề scan).
- 06/11/2026 — màu hình: không dùng blue/cyan/teal (preamble đổi sang vàng); đề mẫu đã đổi bình cầu I.5 và mặt phẳng sóng I.16 sang `VLxanh`.
- 06/11/2026 — model: từ lô M, các phiên gõ đề (giải đề, vẽ hình) thầy chạy bằng Fable; đo hạn mức ở lô M rồi chốt cỡ lô (Fable tối đa 50% hạn mức tuần).
- 06/11/2026 — chia lô: lô M (1 đề PDF không đáp án làm mẫu thứ hai, ưu tiên hình thực tiễn, mạch điện), rồi đề Word (W01…), đề PDF có chữ (P01…), 2 đề scan ở lô cuối; trong mỗi nhóm xếp theo tỉnh A → Z (tên tỉnh không dấu; TP HCM xếp theo "Hồ Chí Minh"); 4 đề/lô.

- 13/11/2026 — duyệt lô M (Lào Cai): giữ đáp án tự giải; II.4 hiểu "giá trị cực đại" là e = +E₀ (S Đ S S); I.10 giữ B (thể lỏng và thể hơi); các lược bớt ở hình II.2, II.4, III.1 giữ như PR; đề gốc không có khối "Cho biết" thì không thêm.
- 13/11/2026 — in đậm mọi từ phủ định ("không", "sai") trong câu hỏi cho mọi đề, kể cả khi đề gốc không in đậm (đã ghi vào `CLAUDE.md`).
- 13/11/2026 — model: lô W (đề Word có lời giải gốc) chạy Opus; lô P (đề PDF tự giải) chạy Fable. Lô M bằng Fable tốn khoảng 4 vạch thanh Fable, chạy khoảng 35–40 phút; giữ 4 đề/lô.

- 13/11/2026 — duyệt lô W01: Bắc Ninh SGD Lần 2 câu I.9 sửa đáp án gốc C thành B (mạch nối M và con chạy; đã đối chiếu hình gốc); Cụm TT1–QV1–LVT câu I.1 giữ B (326 K) theo đáp án gốc, giữ `% KIỂM TRA`; các câu khớp đáp án gốc theo cách hiểu ghi trong `kiem-chung.md` giữ nguyên; đoạn "Dùng thông tin sau cho câu … và câu …" đặt trong câu đầu của cặp (đã ghi `CLAUDE.md`).
- 13/11/2026 — chạy song song: từ lô W01 mỗi phiên mở một agent con cho mỗi đề (mục CHẠY SONG SONG trong `CLAUDE.md`); prompt: `Đọc CLAUDE.md và kho/TIEN-DO.md rồi làm lô <tên lô>, chạy song song.` Lô W01 (4 đề) xong trong khoảng 40 phút.

- 13/11/2026 — tô màu: MỌI hình đều tô màu theo bảng màu trong `CLAUDE.md` (mục HÌNH VẼ, phần Màu; mẫu `tham-khao/to-mau/`). Thêm màu `VLluc`. 6 đề đã xong tô lại trong một phiên riêng (Opus, song song) với prompt: `Đọc CLAUDE.md (mục HÌNH VẼ, phần Màu) và tham-khao/to-mau/ rồi tô màu lại toàn bộ hình của 6 đề đã xong (VatLi2026-CaoBang-SoGD-Lan1, VatLi2026-LaoCai-CumPhiaBac-Lan2 và 4 đề lô W01), chạy song song.`

## Chờ thầy quyết

Phiên tô màu (13/11/2026):
- Nam châm theo quy ước N `VLdo` / S `VLxanh` khác màu ảnh gốc: Cao Bằng II.4 (ảnh gốc N xanh, S đỏ), Bắc Ninh SGD Lần 2 II.1 (ảnh gốc đen). Đề không ghi cực thì KHÔNG tô cực (giữ màu gốc/xám để khỏi lộ đáp án): Cà Mau II.3 (nam châm chữ U xám), Lào Cai II.3 (micro, giữ đỏ / xanh lá như gốc).
- Màu ngoài bảng: Lào Cai II.3 sóng âm tím (`violet`, ảnh gốc xanh dương trùng màu từ trường) — thầy chốt màu chung cho sóng âm? Khí trong bình (Cà Mau III.1) tô `VLxanh!10` — bảng màu chưa quy định chất khí.
- Giữ màu "thật" của ảnh chụp: dây nối đỏ/xanh ở hình thực tiễn (Lào Cai I.16), màu trang trí (Bắc Ninh SGD III.1 ghế xanh, III.5 tia vàng), cột nhiệt kế "thủy ngân" vàng cam (Cụm HH–NSL–TD1 I.2).
- Không tô nước nóng / lạnh khác màu khi đó là ý cần suy luận (Cụm HH–NSL–TD1 II.2); các tia X, Y, Z (Lào Cai I.5) và hai vết hạt (I.7) cùng màu `VLdo`.
- Cao Bằng (đề mẫu) nay gọi thẳng macro chung `\VLcham`, `\VLnhan`, `\VLthanhngang`, `\VLthanhdung` (đã mang màu); `tham-khao/to-mau/mau-to-mau.tex` vẫn dùng scope màu và `\Dngang`/`\Ddung` riêng (cùng kết quả).

## Việc đã xong

- Giai đoạn 0 (06/11/2026): repo, khung, công cụ chép từ dự án Toán; đề nguồn vào `kho/goc/`.
- 06/11/2026: đề mẫu Cao Bằng – Lần 1 (thầy duyệt).
- 06/11/2026, phiên 1a: như mục "Giai đoạn hiện tại".
- 13/11/2026, lô M: đề `VatLi2026-LaoCai-CumPhiaBac-Lan2` (thầy duyệt 13/11). Thêm vào `preamble-vatli-hinh.tex`: thư viện `decorations.pathmorphing`, macro `\VLongday` (ống dây quấn trên lõi trụ), `\VLdongho` (đồng hồ đo dạng hộp); dựng lại đề mẫu Cao Bằng với preamble mới (vẫn 7 trang đề ĐẠT, 10 trang lời giải). `tools/so_hinh.py` dựng hình ở cỡ chữ 12pt như file đề.
- 13/11/2026, lô W01 (thầy duyệt 13/11): 4 đề `VatLi2026-BacNinh-CumHHNSLTD1-Lan2`, `VatLi2026-BacNinh-CumTT1QV1LVT-Lan1`, `VatLi2026-BacNinh-SoGD-Lan2`, `VatLi2026-CaMau-SoGD-Lan1` (bản đề đều ĐẠT). Thêm vào `preamble-vatli-hinh.tex`: `\VLnhietke`, `\VLvienda`, `\VLngonlua`, `\VLdencon`, `\VLgiado`, `\VLongnghiem`, `\VLvongsau`/`\VLvongtruoc`, `\VLnumvan` (chuyển từ file đề, dựng lại các đề dùng; đề mẫu Cao Bằng, Lào Cai biên dịch lại vẫn như cũ). Thống nhất đoạn "Dùng thông tin sau cho câu …" đặt trong câu đầu của cặp (chờ thầy duyệt).
- 13/11/2026, tô màu (chờ duyệt): `preamble-vatli-hinh.tex` — `\VLcham`, `\VLnhan` màu `VLxanh!85!black`; `\VLthanhngang`, `\VLthanhdung`, `\VLvongsau`/`\VLvongtruoc` màu đồng. Tô lại toàn bộ hình 6 đề (mỗi đề một commit), dựng lại `so-hinh/`, soát bản xám, `kiem` ĐẠT, xuất lại thành phẩm; số trang không đổi (Cao Bằng 7/10, Lào Cai 8/12, Cụm HH–NSL–TD1 7/10, Cụm TT1–QV1–LVT 7/11, Bắc Ninh SGD 7/11, Cà Mau 6/10).

## Số đề

83 file nguồn − 4 trùng − 1 gần trùng (Quế Võ 1) = 78 đề dùng được; Cao Bằng xong (đề mẫu), Lào Cai Cụm phía Bắc – Lần 2 xong (lô M), lô W01 4 đề chờ duyệt → còn 72 đề chưa gõ: W02–W10 37 đề Word (W10 có 5 đề), P01–P09 35 đề (33 PDF có chữ + 2 PDF scan; P09 có 3 đề gồm 2 scan).

## Kế hoạch lô và trạng thái từng đề

Trạng thái: chưa gõ → đang gõ → chờ duyệt → xong. Cột "Đáp án gốc": ĐA = bảng đáp án, LG = lời giải.

| Lô | Đề (tên file) | File gốc | Loại | Đáp án gốc | Ghi chú | Trạng thái |
|---|---|---|---|---|---|---|
| — | `VatLi2026-CaoBang-SoGD-Lan1` | Cao Bang - So GDDT - Lan 1.docx | Word | ĐA + LG | đề mẫu chuẩn | xong |
| M | `VatLi2026-LaoCai-CumPhiaBac-Lan2` | Lao Cai - So GDDT - Lan 2.pdf | PDF chữ | không | mẫu thứ hai (đề PDF không đáp án); tên/lần theo tiêu đề gốc; đánh số câu liên tục; đề 8 trang, lời giải 12 trang | xong |
| W01 | `VatLi2026-BacNinh-CumHHNSLTD1-Lan2` | Bac Ninh - Cum truong Bac Ninh Hiep Hoa - Ngo Si Lien - Tien Du 1 - Lan 1.docx | Word | chỉ ĐA | tên/lần theo tiêu đề gốc; tự giải 28 câu khớp ĐA; 11 hình; đề 7 trang, lời giải 10 trang | xong |
| W01 | `VatLi2026-BacNinh-CumTT1QV1LVT-Lan1` | Bac Ninh - Lien truong Bac Ninh - Lan 1.docx | Word | chỉ ĐA | gần trùng Quế Võ 1 – Lần 1; Phần II đánh số lại (19–22 → 1–4); tự giải khớp ĐA; KIỂM TRA I.1; 8 hình; đề 7 trang, lời giải 11 trang | xong |
| W01 | `VatLi2026-BacNinh-SoGD-Lan2` | Bac Ninh - So GDDT - Lan 2.docx | Word | ĐA + LG | KIỂM TRA I.9 (gốc C, gõ B); 9 hình; đề 7 trang, lời giải 11 trang | xong |
| W01 | `VatLi2026-CaMau-SoGD-Lan1` | Ca Mau - So GDDT - Lan 1.docx | Word | ĐA + LG | khớp ĐA 28/28; 4 hình shape Word; đề 6 trang, lời giải 10 trang | xong |
| W02 | `VatLi2026-CanTho-SoGD-Lan1` | Can Tho - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W02 | `VatLi2026-DaNang-SoGD-Lan1` | Da Nang - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W02 | `VatLi2026-DakLak-Cum1` | Dak Lak - Cum thi thu TN so 1.docx | Word | ĐA + LG | — | chưa gõ |
| W02 | `VatLi2026-DongNai-SoGD-Lan1` | Dong Nai - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W03 | `VatLi2026-DongThap-SoGD-Lan1` | Dong Thap - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W03 | `VatLi2026-GiaLai-SoGD` | Gia Lai - So GDDT.docx | Word | ĐA + LG | — | chưa gõ |
| W03 | `VatLi2026-HaNoi-YenVien-Lan1` | Ha Noi - THPT Yen Vien - Lan 1.docx | Word | chỉ ĐA | — | chưa gõ |
| W03 | `VatLi2026-HaTinh-SoGD-Lan1` | Ha Tinh - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W04 | `VatLi2026-HaTinh-SoGD-Lan2` | Ha Tinh - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W04 | `VatLi2026-HaiPhong-CumCM5` | Hai Phong - Cum chuyen mon so 5.docx | Word | ĐA + LG | — | chưa gõ |
| W04 | `VatLi2026-HaiPhong-SoGD-Lan1` | Hai Phong - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W04 | `VatLi2026-HaiPhong-SoGD-Lan2` | Hai Phong - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W05 | `VatLi2026-TPHCM-LeTrongTan` | TP HCM - THPT Le Trong Tan.docx | Word | ĐA + LG | — | chưa gõ |
| W05 | `VatLi2026-Hue-SoGD-Lan1` | Hue - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W05 | `VatLi2026-HungYen-SoGD-Lan2` | Hung Yen - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W05 | `VatLi2026-LamDong-SoGD` | Lam Dong - So GDDT.docx | Word | ĐA + LG | — | chưa gõ |
| W06 | `VatLi2026-LangSon-SoGD-Lan1` | Lang Son - So GDDT - Lan 1.docx | Word | ĐA 6 mã + LG câu VD | — | chưa gõ |
| W06 | `VatLi2026-NgheAn-LienTruong-Lan5` | Nghe An - Lien truong Nghe An - Lan 5.docx | Word | ĐA + LG | — | chưa gõ |
| W06 | `VatLi2026-NgheAn-SoGD-Lan1` | Nghe An - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W06 | `VatLi2026-NgheAn-SoGD-Lan2` | Nghe An - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W07 | `VatLi2026-NgheAn-SoGD-Lan3` | Nghe An - So GDDT - Lan 3.docx | Word | ĐA + LG | — | chưa gõ |
| W07 | `VatLi2026-NinhBinh-Cum9-Lan1` | Ninh Binh - Cum truong THPT so 9 - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W07 | `VatLi2026-NinhBinh-SoGD-Lan3` | Ninh Binh - So GDDT - Lan 3.docx | Word | ĐA + LG | — | chưa gõ |
| W07 | `VatLi2026-NinhBinh-SoGD-Lan4` | Ninh Binh - So GDDT - Lan 4.docx | Word | ĐA + LG | — | chưa gõ |
| W08 | `VatLi2026-PhuTho-SoGD-Lan2` | Phu Tho - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W08 | `VatLi2026-QuangNgai-ChuyenLeKhiet-Lan1` | Quang Ngai - THPT chuyen Le Khiet - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W08 | `VatLi2026-QuangTri-SoGD-Lan1` | Quang Tri - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W08 | `VatLi2026-SonLa-SoGD-Lan2` | Son La - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W09 | `VatLi2026-SonLa-SoGD-Lan3` | Son La - So GDDT - Lan 3.docx | Word | ĐA + LG | — | chưa gõ |
| W09 | `VatLi2026-TayNinh-ChuyenHoangLeKha-Lan2` | Tay Ninh - THPT chuyen Hoang Le Kha - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W09 | `VatLi2026-TayNinh-THPTTayNinh` | Tay Ninh - THPT Tay Ninh.docx | Word | ĐA + LG | — | chưa gõ |
| W09 | `VatLi2026-ThaiNguyen-SoGD-Lan2` | Thai Nguyen - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W10 | `VatLi2026-ThanhHoa-SoGD-Lan1` | Thanh Hoa - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W10 | `VatLi2026-ThanhHoa-SoGD-Lan2` | Thanh Hoa - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W10 | `VatLi2026-TuyenQuang-SoGD-Lan1` | Tuyen Quang - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| W10 | `VatLi2026-TuyenQuang-SoGD-Lan2` | Tuyen Quang - So GDDT - Lan 2.docx | Word | ĐA + LG | — | chưa gõ |
| W10 | `VatLi2026-VinhLong-SoGD-Lan1` | Vinh Long - So GDDT - Lan 1.docx | Word | ĐA + LG | — | chưa gõ |
| P01 | `VatLi2026-BacNinh-SoGD-Lan1` | Bac Ninh - So GDDT - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P01 | `VatLi2026-HaNoi-ChuyenKHTN-Lan1` | Ha Noi - THPT chuyen KHTN - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P01 | `VatLi2026-HaNoi-ChuyenKHTN-Lan3` | Ha Noi - THPT chuyen KHTN - Lan 3.pdf | PDF chữ | không | — | chưa gõ |
| P01 | `VatLi2026-HaNoi-LuongTheVinh-Lan1` | Ha Noi - THPT Luong The Vinh - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P02 | `VatLi2026-HaNoi-NguyenThiMinhKhai-Lan1` | Chua ro tinh - THPT Nguyen Thi Minh Khai - Lan 1.pdf | PDF chữ | không | đánh số câu liên tục | chưa gõ |
| P02 | `VatLi2026-HaNoi-SoGD-Lan1` | Ha Noi - So GDDT - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P02 | `VatLi2026-HaNoi-YenHoa-Lan1` | Ha Noi - THPT Yen Hoa - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P02 | `VatLi2026-HaTinh-CamXuyen-Lan2` | Ha Tinh - THPT Cam Xuyen - Lan 1.pdf | PDF chữ | không | tên/lần theo tiêu đề gốc; đánh số câu liên tục | chưa gõ |
| P03 | `VatLi2026-HaTinh-CumLienTruong` | Ha Tinh - Cum lien truong Ha Tinh.pdf | PDF chữ | không | — | chưa gõ |
| P03 | `VatLi2026-HaiPhong-Cum13Truong-Lan2` | Hai Phong - Cum 13 truong - Lan 2.pdf | PDF chữ | không | — | chưa gõ |
| P03 | `VatLi2026-HaiPhong-CumCM10-Lan1` | Hai Phong - Cum chuyen mon so 10 - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P03 | `VatLi2026-HaiPhong-KinhMonII-Lan2` | Hai Phong - THPT Kinh Mon II - Lan 1.pdf | PDF chữ | không | tên/lần theo tiêu đề gốc; đánh số câu liên tục | chưa gõ |
| P04 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan1` | TP HCM - Nguyen Khuyen - Le Thanh Tong - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P04 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan2` | TP HCM - Nguyen Khuyen - Le Thanh Tong - Lan 2.pdf | PDF chữ | không | — | chưa gõ |
| P04 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan3` | TP HCM - THPT Nguyen Khuyen - Lan 3.pdf | PDF chữ | không | tên/lần theo tiêu đề gốc | chưa gõ |
| P04 | `VatLi2026-Hue-PhanDangLuu-Lan1` | Hue - THPT Phan Dang Luu - Lan 1.pdf | PDF chữ | không | đánh số câu liên tục | chưa gõ |
| P05 | `VatLi2026-HungYen-SoGD-Lan1` | Hung Yen - So GDDT - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P05 | `VatLi2026-LaoCai-SoGD-Lan1` | Lao Cai - So GDDT - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P05 | `VatLi2026-NgheAn-ChuyenDHVinh-Lan1` | Nghe An - THPT chuyen DH Vinh - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P05 | `VatLi2026-NgheAn-ChuyenPhanBoiChau-Lan1` | Nghe An - THPT chuyen Phan Boi Chau - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P06 | `VatLi2026-NgheAn-LienTruong-Lan1` | Nghe An - Lien truong Nghe An - Lan 1.pdf | PDF chữ | không | tên/lần theo tiêu đề gốc; đánh số câu liên tục | chưa gõ |
| P06 | `VatLi2026-NgheAn-LienTruong-Lan2` | Nghe An - Lien truong Nghe An - Lan 2.pdf | PDF chữ | không | — | chưa gõ |
| P06 | `VatLi2026-NinhBinh-SoGD-Lan1` | Ninh Binh - So GDDT - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P06 | `VatLi2026-NinhBinh-SoGD-Lan2` | Ninh Binh - So GDDT - Lan 2.pdf | PDF chữ | không | đánh số câu liên tục | chưa gõ |
| P07 | `VatLi2026-PhuTho-NgoGiaTu-Lan1` | Phu Tho - THPT Ngo Gia Tu - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P07 | `VatLi2026-PhuTho-SoGD-Lan1` | Phu Tho - So GDDT - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P07 | `VatLi2026-QuangNinh-CamPha-Lan1` | Quang Ninh - THPT Cam Pha - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P07 | `VatLi2026-QuangNinh-ChuyenHaLong-Lan1` | Quang Ninh - THPT chuyen Ha Long - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P08 | `VatLi2026-QuangNinh-SoGD-Lan1` | Quang Ninh - So GDDT - Lan 1.pdf | PDF chữ | không | đánh số câu liên tục | chưa gõ |
| P08 | `VatLi2026-ThaiNguyen-SoGD-Lan1` | Thai Nguyen - So GDDT - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P08 | `VatLi2026-ThanhHoa-HamRong-Lan1` | Thanh Hoa - THPT Ham Rong - Lan 1.pdf | PDF chữ | không | đánh số câu liên tục | chưa gõ |
| P08 | `VatLi2026-ThanhHoa-LuongDacBang-Lan1` | Thanh Hoa - THPT Luong Dac Bang - Lan 1.pdf | PDF chữ | không | — | chưa gõ |
| P09 | `VatLi2026-ThanhHoa-TinhGia1` | Thanh Hoa - THPT Tinh Gia I.pdf | PDF chữ | không | — | chưa gõ |
| P09 | `VatLi2026-BacNinh-SoGD` | Bac Ninh - So GDDT - chua ro lan.pdf | PDF scan | không | scan | chưa gõ |
| P09 | `VatLi2026-TPHCM-NguyenKhuyenLTT-Lan10` | TP HCM - Nguyen Khuyen - Le Thanh Tong - Lan 10.pdf | PDF scan | không | scan | chưa gõ |

## Đề không gõ (trùng)

| File gốc | Trùng với | Lý do giữ bản kia |
|---|---|---|
| Ha Noi - THPT Luong The Vinh - Lan 2.pdf | Lương Thế Vinh – Lần 1 (PDF) | cùng 28 câu, cùng hình, chỉ khác dàn trang; tiêu đề SieuGioi gõ lại |
| Hung Yen - So GDDT - chua ro lan.pdf | Hưng Yên SGD – Lần 2 (Word) | cùng mã 0215; bản Word có lời giải |
| Nghe An - Lien truong Nghe An - Lan 3.pdf | Nghệ An SGD – Lần 2 (Word) | cùng 28 câu, cùng thứ tự; bản Word có lời giải |
| Thanh Hoa - Cum lien truong Thanh Hoa - Lan 1.pdf | Thanh Hóa SGD – Lần 1 (Word) | cùng mã 1201; bản Word có lời giải |
| Bac Ninh - THPT Que Vo 1 - Lan 1.pdf | Cụm TT1-QV1-LVT – Lần 1 (Word) | gần trùng 17/28 câu; thầy quyết bỏ (06/11/2026) |
