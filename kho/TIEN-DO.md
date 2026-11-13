# TIẾN ĐỘ DỰ ÁN GÕ LẠI ĐỀ THI THỬ TN THPT 2026 MÔN VẬT LÍ

Đọc cùng `CLAUDE.md` (quy chuẩn, quy trình một lô) và `kho/kiem-ke.md` (kiểm kê 83 đề nguồn). Mỗi lô xong: cập nhật bảng dưới (trạng thái từng đề), mục "Việc đã xong", push và tạo PR.

## Giai đoạn hiện tại

- **Phiên 1a (06/11/2026) — xong, thầy duyệt 06/11/2026**: `CLAUDE.md` cho Vật lí; bộ macro hình chung `preamble-vatli-hinh.tex` (thêm circuitikz european), `tools/so_hinh.py` đọc macro từ file chung, dựng lại đề mẫu (bản đề 7 trang, lời giải 10 trang, PDF trùng bản cũ); `tools/README.md`; kiểm kê 83 đề `kho/kiem-ke.md`; chia lô (file này).
- **Lô M (13/11/2026) — xong, thầy duyệt 13/11/2026**: `VatLi2026-LaoCai-CumPhiaBac-Lan2` (mẫu thứ hai: đề PDF không đáp án, tự giải toàn bộ 28 câu, vẽ lại 14 hình). Bản đề 8 trang (ĐẠT), bản lời giải 12 trang. Thành phẩm trong `thanh-pham/`, kiểm chứng ở `de/VatLi2026-LaoCai-CumPhiaBac-Lan2/kiem-chung.md`.
- **Lô W01 (13/11/2026) — xong, thầy duyệt 13/11/2026**: 4 đề Word (Bắc Ninh ×3, Cà Mau), chạy Opus, 4 agent con song song (thầy cho phép trong phiên), phiên chính soát, thống nhất, gom macro. Chi tiết ở bảng dưới và mục "Chờ thầy quyết".
- **Tô màu lại 6 đề đã xong (13/11/2026) — xong (PR #5)**: Cao Bằng, Lào Cai, 4 đề lô W01 (Opus, 6 agent con song song). Số trang bản đề / lời giải không đổi, cả 6 đề `kiem` ĐẠT, thành phẩm xuất lại.
- **Lô W02 + W03 (13/11/2026) — xong, thầy duyệt 13/11/2026 (PR #6, một nhánh, một PR)**: 8 đề Word, Opus, 8 agent con song song (W03 thầy yêu cầu làm luôn trong phiên W02). Phiên chính soát từng đề, thống nhất (nhãn `\label`, bỏ số ảnh chụp trên màn hình thiết bị), gom 5 macro vào `preamble-vatli-hinh.tex`. Chi tiết ở bảng dưới.
- **Lô W04 + W05 (13/11/2026) — xong, thầy duyệt 13/11/2026 (PR #7, một nhánh, một PR)**: 8 đề Word, Opus, 8 agent con song song. Phiên chính soát từng đề (kiem-chung, ảnh so hình, bản đề, bản xám), sửa `tools/so_hinh.py` (chạy song song bắt nhầm `hinh.tex` của đề khác), chuyển `\VLchamtron` vào `preamble-vatli-hinh.tex`. Chi tiết ở bảng dưới và mục "Chờ thầy quyết".
- **Lô W06 + W07 (13/11/2026) — chờ duyệt (một nhánh, một PR)**: 8 đề Word, Opus, 8 agent con song song; giữa phiên chạm hạn mức 5 giờ, chạy tiếp sau 17:00 UTC. Phiên chính soát từng đề (kiem-chung, ảnh so hình, bản đề, tự kiểm các câu lệch đáp án), gom 24 macro hình vào `preamble-vatli-hinh.tex` (dựng lại 8 đề, số trang không đổi, đều ĐẠT). Chi tiết ở bảng dưới và mục "Chờ thầy quyết".
- **Hình thực tiễn các đề đã gõ: chờ phiên vẽ lại riêng** (thầy quyết 13/11/2026: rà và vẽ lại trong một phiên riêng sau khi gõ xong hết đề, theo mục HÌNH VẼ — "Vẽ chi tiết, trau chuốt" trong `CLAUDE.md`; các lô gõ đề ưu tiên đáp án, lời giải, sơ đồ, đồ thị, dàn trang). Lô W06 + W07 đã vẽ chi tiết một phần trước khi thầy quyết.
- **Tiếp theo**: lô W08 + W09 (Opus, song song, 8 đề một PR): `Đọc CLAUDE.md và kho/TIEN-DO.md rồi làm lô W08 và W09 (8 đề) trong phiên này, chạy song song, chung một nhánh và một PR.`

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

- 13/11/2026 — chốt các điểm của phiên tô màu (PR #5, đã ghi `CLAUDE.md`): nam châm luôn N `VLdo` / S `VLxanh` kể cả khi ảnh gốc tô ngược (Cao Bằng II.4, Bắc Ninh SGD II.1); đề không ghi cực thì để xám (Cà Mau II.3; micro Lào Cai II.3 giữ như gốc); sóng âm, sóng cơ dùng màu chung `VLtim` (thêm vào `preamble-vatli-hinh.tex`, Lào Cai II.3 đổi `violet` → `VLtim`, hình không đổi); chất khí trong bình `VLxanh!10` hoặc để trắng; ảnh chụp giữ màu thật của vật khi màu không mang thông tin; không tô khác màu những gì học sinh phải suy luận (nước nóng / lạnh, cực, loại tia); `tham-khao/to-mau/mau-to-mau.tex` giữ nguyên, cách gọi macro màu chung theo đề mẫu Cao Bằng.

- 13/11/2026 — duyệt lô W02 + W03 (PR #6): 4 câu sửa đáp án gốc giữ như PR (Đà Nẵng III.3 → 3, Đồng Nai III.3 → 6, Gia Lai I.5 → D, Yên Viên I.13 → D; đã đối chiếu lời giải gốc, hình gốc). Sửa lời đề: Đắk Lắk II.3 chu kì bán rã Sr-90 288,8 → 28,8 năm (ý b, d dựng từ 28,8 năm; đáp án Đ S Đ S → S Đ Đ S); Đắk Lắk III.2 dây dài 2,0 m → 2,0 cm, hỏi theo T, đáp số 0,37; Hà Tĩnh I.5 câu dẫn lặp phương án D → "Hai vật tiếp xúc nhau **không** truyền nhiệt cho nhau khi chúng", đáp án C; Hà Tĩnh I.8 ⁵⁵Fe → ⁵⁶Fe; Hà Tĩnh I.9 thêm năng lượng liên kết riêng 8,8 MeV/nucleon vào câu dẫn. Giữ như PR: Đà Nẵng I.3 (D), Đồng Tháp II.3 c) Đúng (ý d dựng từ 1 224 240 J), Gia Lai II.4 d) Sai, Hà Tĩnh III.3 sơ đồ không chú thích. Khối "Cho biết": đề gốc không có thì không thêm (như 13/11, lô M). Mã câu lớp 10, 11 theo chương SGK Kết nối tri thức (`VL10-C<n>`, `VL11-C<n>`). Số trên màn hình thiết bị: chỉ giữ số đề dùng làm dữ kiện. Ba quy định này đã ghi `CLAUDE.md`. Từ lô W04 mỗi phiên làm 8 đề (2 lô, một PR) — W02 + W03 chạy khoảng 55 phút.

- 13/11/2026 — duyệt lô W04 + W05 (PR #7): giữ toàn bộ như PR sau khi đối chiếu đề gốc, lời giải gốc, hình gốc — Huế I.10 (5,8 J → 5,7·10³ J), I.12 (1 g → 12 g) sửa dữ kiện cho khớp phương án; Huế III.1 = 4,36 (gốc 2,18), III.4 đọc đồ thị B = 0,2 T tại 0,2 s, 30° là góc giữa mặt phẳng vòng dây và B, hỏi theo cm² → 160 (gốc 3700 mm² đọc sai đồ thị), III.6 = 1571 (đề không cho π = 3,14); Lâm Đồng III.1 = 521 theo lưới đồ thị (gốc 1067), III.2 dùng k = 1,38·10⁻²³ (không thêm vào "Cho biết"); Hưng Yên II.4 a) Sai (92 → 100 proton); Lê Trọng Tấn I.17 sửa phương án C trùng B; Hà Tĩnh Lần 2 I.4 vẽ lại Hình 3 (I hướng xuống), I.5 cực N theo lời giải gốc, III.1 = 727 theo gốc; Hải Phòng SGD Lần 1 III.3 = 4,71, I.4 giữ lời đề; các ý Đúng/Sai còn lại theo gốc. Ngọn lửa dùng `\VLngonlua` (cam – đỏ), không sửa macro (đã ghi `CLAUDE.md`).

## Chờ thầy quyết

Lô W06 + W07 (chi tiết trong `kiem-chung.md` của từng đề):
- **Nghệ An SGD Lần 2 II.4c, Ninh Bình SGD Lần 4 II.3a,d** (cùng loại hình máy phát: khung ABCD, B từ N sang S, quay (1)→(2)→(3)): tính lại theo hình (cạnh AB phía sau, A, D gần vòng khuyên) thì chiều dòng điện ngược đáp án gốc → gõ theo tính lại (NA L2 c) Sai; NB L4 S Đ S Đ). Phiên chính đã kiểm lại cả hai. Hai đáp án gốc cùng ngược chiều — thầy xem có giữ theo gốc không.
- **Nghệ An SGD Lần 2 I.2**: Hình 1 và Hình 2 cùng đúng theo một quy ước → hai phương án đúng; gõ B theo gốc. Sửa hình (đổi chiều i_c ở Hình 1) hay giữ?
- **Nghệ An SGD Lần 3 I.11** (tàu đệm từ, ba nam châm trong vòng tròn): gốc C (thẳng đứng lên), gõ A (về phía sau tàu: S ray phía trước đẩy, N ray phía sau hút). Phiên chính đã kiểm.
- **Ninh Bình SGD Lần 3 II.3d**: theo hình V₃ = 2V₁ = 4V₂ → T₃ = 4T₂, gốc Đ (3 lần), gõ S. **III.2**: lưới gốc không đều; đếm ô ra p₂ = p₀/4 → 5,6 (gốc 3,7 đọc p₀/3 và coi khí đơn nguyên tử). Giữ 5,6, hay giữ 3,7 (sửa hình, thêm "đơn nguyên tử")?
- **Ninh Bình SGD Lần 4 I.13**: đề gốc ghi "như hình vẽ bên" nhưng không có hình; tự dựng hình nam châm và 4 kim (khớp ĐA A). **I.17**: hình gốc S₁′, S₃′ cùng diện tích (hai đáp án đúng) → vẽ S₃′ rộng 4 ô cho khớp ĐA B.
- **Ninh Bình Cụm 9 II.3d, Liên trường NA Lần 5 II.3d**: kết luận V_c > V_d phụ thuộc chiều quấn cuộn dây, hình gốc không rõ; giữ Đúng theo gốc.
- **Ninh Bình Cụm 9 I.17**: sửa kí hiệu ²²²₈₆Ra → Rn, ²⁰⁹₈₄Pb → Po (giữ A, Z); I.3 phương án C "d, c, b, d" (lặp d) giữ như gốc.
- **Nghệ An SGD Lần 1 I.13**: phương án D gốc trùng B, gõ "tăng 4 lần" (ĐA A không đổi); "nitơ" → "nitrogen" (thống nhất?).
- **Lạng Sơn I.7** mã TH (gốc xếp nhóm vận dụng); II.1 ống nước nóng đỏ / lạnh xanh (nhãn đã ghi rõ).

## Việc đã xong

- Giai đoạn 0 (06/11/2026): repo, khung, công cụ chép từ dự án Toán; đề nguồn vào `kho/goc/`.
- 06/11/2026: đề mẫu Cao Bằng – Lần 1 (thầy duyệt).
- 06/11/2026, phiên 1a: như mục "Giai đoạn hiện tại".
- 13/11/2026, lô M: đề `VatLi2026-LaoCai-CumPhiaBac-Lan2` (thầy duyệt 13/11). Thêm vào `preamble-vatli-hinh.tex`: thư viện `decorations.pathmorphing`, macro `\VLongday` (ống dây quấn trên lõi trụ), `\VLdongho` (đồng hồ đo dạng hộp); dựng lại đề mẫu Cao Bằng với preamble mới (vẫn 7 trang đề ĐẠT, 10 trang lời giải). `tools/so_hinh.py` dựng hình ở cỡ chữ 12pt như file đề.
- 13/11/2026, lô W01 (thầy duyệt 13/11): 4 đề `VatLi2026-BacNinh-CumHHNSLTD1-Lan2`, `VatLi2026-BacNinh-CumTT1QV1LVT-Lan1`, `VatLi2026-BacNinh-SoGD-Lan2`, `VatLi2026-CaMau-SoGD-Lan1` (bản đề đều ĐẠT). Thêm vào `preamble-vatli-hinh.tex`: `\VLnhietke`, `\VLvienda`, `\VLngonlua`, `\VLdencon`, `\VLgiado`, `\VLongnghiem`, `\VLvongsau`/`\VLvongtruoc`, `\VLnumvan` (chuyển từ file đề, dựng lại các đề dùng; đề mẫu Cao Bằng, Lào Cai biên dịch lại vẫn như cũ). Thống nhất đoạn "Dùng thông tin sau cho câu …" đặt trong câu đầu của cặp (chờ thầy duyệt).
- 13/11/2026, lô W02 + W03 (thầy duyệt 13/11, PR #6): 8 đề `VatLi2026-CanTho-SoGD-Lan1`, `VatLi2026-DaNang-SoGD-Lan1`, `VatLi2026-DakLak-Cum1`, `VatLi2026-DongNai-SoGD-Lan1` (W02), `VatLi2026-DongThap-SoGD-Lan1`, `VatLi2026-GiaLai-SoGD`, `VatLi2026-HaNoi-YenVien-Lan1`, `VatLi2026-HaTinh-SoGD-Lan1` (W03); bản đề đều ĐẠT. Thêm vào `preamble-vatli-hinh.tex`: `\VLbienbao`, `\VLbepdien`, `\VLnhietkedt`, `\VLlucke`, `\VLnhantron` (chuyển từ file đề Đà Nẵng, Đồng Nai, Gia Lai; dựng lại 3 đề, số trang không đổi). Nhãn `\label` thống nhất mẫu `<tên đề>-<phần><câu>` (5 đề, gồm Bắc Ninh SGD Lần 2 và Cà Mau của W01; xuất lại, bản in không đổi), ghi vào `CLAUDE.md`.
- 13/11/2026, lô W04 + W05 (thầy duyệt 13/11, PR #7): 8 đề `VatLi2026-HaTinh-SoGD-Lan2`, `VatLi2026-HaiPhong-CumCM5`, `VatLi2026-HaiPhong-SoGD-Lan1`, `VatLi2026-HaiPhong-SoGD-Lan2` (W04), `VatLi2026-TPHCM-LeTrongTan`, `VatLi2026-Hue-SoGD-Lan1`, `VatLi2026-HungYen-SoGD-Lan2`, `VatLi2026-LamDong-SoGD` (W05); bản đề đều ĐẠT. `tools/so_hinh.py` tìm `hinh.tex` ở thư mục hiện hành trước (chạy song song không bắt nhầm hình đề khác). Thêm `\VLchamtron` (⊙ có vòng) vào `preamble-vatli-hinh.tex` (từ đề Hà Tĩnh Lần 2). Phiên chính: ngọn lửa Hải Phòng Cụm CM5 III.3 đổi sang `VLdo`; hình III.3 Hải Phòng SGD Lần 2 đặt bên câu dẫn.
- 13/11/2026, tô màu (thầy duyệt PR #5): `preamble-vatli-hinh.tex` — `\VLcham`, `\VLnhan` màu `VLxanh!85!black`; `\VLthanhngang`, `\VLthanhdung`, `\VLvongsau`/`\VLvongtruoc` màu đồng. Tô lại toàn bộ hình 6 đề (mỗi đề một commit), dựng lại `so-hinh/`, soát bản xám, `kiem` ĐẠT, xuất lại thành phẩm; số trang không đổi (Cao Bằng 7/10, Lào Cai 8/12, Cụm HH–NSL–TD1 7/10, Cụm TT1–QV1–LVT 7/11, Bắc Ninh SGD 7/11, Cà Mau 6/10).

- 13/11/2026, lô W06 + W07 (chờ duyệt): 8 đề `VatLi2026-LangSon-SoGD-Lan1`, `VatLi2026-NgheAn-LienTruong-Lan5`, `VatLi2026-NgheAn-SoGD-Lan1`, `VatLi2026-NgheAn-SoGD-Lan2` (W06), `VatLi2026-NgheAn-SoGD-Lan3`, `VatLi2026-NinhBinh-Cum9-Lan1`, `VatLi2026-NinhBinh-SoGD-Lan3`, `VatLi2026-NinhBinh-SoGD-Lan4` (W07); bản đề đều ĐẠT. Gom 24 macro hình vào `preamble-vatli-hinh.tex` (danh sách ở `CLAUDE.md`, mục FILE TRONG REPO); `\VLcuonphang` thống nhất theo bản 6 tham số (đổi lời gọi ở Cụm 9), cốc có vành của Ninh Bình Lần 3 đổi tên `\VLbinhthuytinh` (khỏi trùng `\VLcocthuytinh`). `tools/so_hinh.py` nạp thêm `mathrsfs`. `CLAUDE.md` mục HÌNH VẼ thêm yêu cầu vẽ hình thực tiễn chi tiết (áp dụng ở phiên vẽ lại riêng).

## Số đề

83 file nguồn − 4 trùng − 1 gần trùng (Quế Võ 1) = 78 đề dùng được; Cao Bằng xong (đề mẫu), Lào Cai Cụm phía Bắc – Lần 2 xong (lô M), lô W01 4 đề xong, lô W02 + W03 8 đề xong, lô W04 + W05 8 đề xong, lô W06 + W07 8 đề chờ duyệt → còn 48 đề chưa gõ: W08–W10 13 đề Word (W10 có 5 đề), P01–P09 35 đề (33 PDF có chữ + 2 PDF scan; P09 có 3 đề gồm 2 scan).

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
| W02 | `VatLi2026-CanTho-SoGD-Lan1` | Can Tho - So GDDT - Lan 1.docx | Word | ĐA + LG | mã 0201; khớp ĐA 28/28; 2 hình; II.2 `% tachDS`; đề 5 trang, lời giải 9 trang | xong |
| W02 | `VatLi2026-DaNang-SoGD-Lan1` | Da Nang - So GDDT - Lan 1.docx | Word | ĐA + LG | KIỂM TRA III.3 (gốc 4, gõ 3), I.3 (B, D tương đương); 8 hình; đề 7 trang, lời giải 10 trang | xong |
| W02 | `VatLi2026-DakLak-Cum1` | Dak Lak - Cum thi thu TN so 1.docx | Word | ĐA + LG | khớp ĐA; sửa lời đề II.3 (T = 28,8 năm, đáp án S Đ Đ S), III.2 (l = 2,0 cm, đáp số 0,37); 8 hình; đề 7 trang, lời giải 10 trang | xong |
| W02 | `VatLi2026-DongNai-SoGD-Lan1` | Dong Nai - So GDDT - Lan 1.docx | Word | ĐA + LG | KIỂM TRA III.3 (gốc 63, gõ 6); 5 hình; đề 7 trang, lời giải 10 trang | xong |
| W03 | `VatLi2026-DongThap-SoGD-Lan1` | Dong Thap - So GDDT - Lan 1.docx | Word | ĐA + LG | khớp ĐA; KIỂM TRA II.3c (hai cách hiểu); 11 hình; đề 8 trang, lời giải 11 trang | xong |
| W03 | `VatLi2026-GiaLai-SoGD` | Gia Lai - So GDDT.docx | Word | ĐA + LG | KIỂM TRA I.5 (gốc B, gõ D); 8 hình; đề 7 trang, lời giải 11 trang | xong |
| W03 | `VatLi2026-HaNoi-YenVien-Lan1` | Ha Noi - THPT Yen Vien - Lan 1.docx | Word | chỉ ĐA | tự giải 28 câu; KIỂM TRA I.13 (gốc C, gõ D); 6 hình; đề 6 trang, lời giải 9 trang | xong |
| W03 | `VatLi2026-HaTinh-SoGD-Lan1` | Ha Tinh - So GDDT - Lan 1.docx | Word | ĐA + LG | sửa lời đề I.5 (câu dẫn mới, đáp án C), I.8 (⁵⁵Fe → ⁵⁶Fe), I.9 (thêm 8,8 MeV/nucleon); 4 hình; đề 6 trang, lời giải 10 trang | xong |
| W04 | `VatLi2026-HaTinh-SoGD-Lan2` | Ha Tinh - So GDDT - Lan 2.docx | Word | ĐA + LG | mã 0306; khớp ĐA; KIỂM TRA I.4, I.5 (sửa hình theo lời giải gốc), III.1 (727 hay 182); 9 hình; đề 7 trang, lời giải 11 trang | xong |
| W04 | `VatLi2026-HaiPhong-CumCM5` | Hai Phong - Cum chuyen mon so 5.docx | Word | ĐA + LG | mã 0301; khớp ĐA 28/28; KIỂM TRA II.2c, II.3b,d (dữ kiện mâu thuẫn); 10 hình; đề 6 trang, lời giải 9 trang | xong |
| W04 | `VatLi2026-HaiPhong-SoGD-Lan1` | Hai Phong - So GDDT - Lan 1.docx | Word | ĐA + LG | KIỂM TRA III.3 (gốc 4,70, gõ 4,71), I.4 (³¹P không phóng xạ); 11 hình; đề 9 trang, lời giải 12 trang | xong |
| W04 | `VatLi2026-HaiPhong-SoGD-Lan2` | Hai Phong - So GDDT - Lan 2.docx | Word | ĐA + LG | khớp ĐA 28/28; KIỂM TRA II.1 (ΔU), II.2c (hai cách hiểu); 9 hình; đề 9 trang, lời giải 12 trang | xong |
| W05 | `VatLi2026-TPHCM-LeTrongTan` | TP HCM - THPT Le Trong Tan.docx | Word | ĐA + LG | mã 0201; khớp ĐA 28/28; sửa phương án C câu I.17 (gốc trùng B); KIỂM TRA II.1b; II.1 `% tachDS`; 4 hình; đề 6 trang, lời giải 9 trang | xong |
| W05 | `VatLi2026-Hue-SoGD-Lan1` | Hue - So GDDT - Lan 1.docx | Word | ĐA + LG | mã 0201; sửa số liệu I.10 (5,7·10³ J), I.12 (12 g); KIỂM TRA III.1 (gốc 2,18, gõ 4,36), III.4 (gốc 3700 mm², gõ 160 cm²), III.6 (gốc 1570, gõ 1571), II.1b; 5 hình; đề 6 trang, lời giải 9 trang | xong |
| W05 | `VatLi2026-HungYen-SoGD-Lan2` | Hung Yen - So GDDT - Lan 2.docx | Word | ĐA + LG | mã 0215; KIỂM TRA II.4a (gốc Đ, gõ S), I.2 (thêm nhãn t₁); 8 hình; đề 7 trang, lời giải 11 trang | xong |
| W05 | `VatLi2026-LamDong-SoGD` | Lam Dong - So GDDT.docx | Word | ĐA + LG | KIỂM TRA III.1 (gốc 1067, gõ 521 theo đồ thị), III.2 (thiếu k); 10 hình; đề 7 trang, lời giải 11 trang | xong |
| W06 | `VatLi2026-LangSon-SoGD-Lan1` | Lang Son - So GDDT - Lan 1.docx | Word | ĐA 6 mã + LG câu VD | mã 201; khớp ĐA 28/28 (câu không có LG gốc tự giải); 4 hình (3 shape Word); đề 5 trang, lời giải 9 trang | chờ duyệt |
| W06 | `VatLi2026-NgheAn-LienTruong-Lan5` | Nghe An - Lien truong Nghe An - Lan 5.docx | Word | ĐA + LG | khớp ĐA 28/28; II.3d theo chiều quấn hình gốc (không rõ); 6 hình; đề 8 trang, lời giải 11 trang | chờ duyệt |
| W06 | `VatLi2026-NgheAn-SoGD-Lan1` | Nghe An - So GDDT - Lan 1.docx | Word | ĐA + LG | khớp ĐA 28/28; sửa phương án D câu I.13 (gốc trùng B → "tăng 4 lần"); 11 hình + 1 bảng; đề 8 trang, lời giải 11 trang | chờ duyệt |
| W06 | `VatLi2026-NgheAn-SoGD-Lan2` | Nghe An - So GDDT - Lan 2.docx | Word | ĐA + LG | mã 0304; KIỂM TRA II.4c (gốc Đ, gõ S), I.2 (hai phương án đúng B, C; gõ B); sửa ⁹⁵Mo I.15; 6 hình + bảng thời tiết; đề 6 trang, lời giải 10 trang | chờ duyệt |
| W07 | `VatLi2026-NgheAn-SoGD-Lan3` | Nghe An - So GDDT - Lan 3.docx | Word | ĐA + LG | KIỂM TRA I.11 (gốc C, gõ A); 7 hình; đề 7 trang, lời giải 10 trang | chờ duyệt |
| W07 | `VatLi2026-NinhBinh-Cum9-Lan1` | Ninh Binh - Cum truong THPT so 9 - Lan 1.docx | Word | ĐA + LG | khớp ĐA 28/28; KIỂM TRA II.3d (chiều quấn không rõ, giữ Đ); sửa kí hiệu I.17 (Rn, Po); 13 tikzpicture (9 hình gốc); đề 6 trang, lời giải 10 trang | chờ duyệt |
| W07 | `VatLi2026-NinhBinh-SoGD-Lan3` | Ninh Binh - So GDDT - Lan 3.docx | Word | ĐA + LG | KIỂM TRA II.3d (gốc Đ, gõ S), III.2 (gốc 3,7, gõ 5,6 theo lưới); 9 hình; đề 7 trang, lời giải 11 trang | chờ duyệt |
| W07 | `VatLi2026-NinhBinh-SoGD-Lan4` | Ninh Binh - So GDDT - Lan 4.docx | Word | ĐA + LG | KIỂM TRA II.3a,d (gốc Đ Đ S S, gõ S Đ S Đ), I.13 (gốc thiếu hình, tự dựng), I.17 (sửa hình S₃′); 8 hình; đề 7 trang, lời giải 11 trang | chờ duyệt |
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
