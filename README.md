# Gõ lại đề thi thử tốt nghiệp THPT 2026 môn Vật lí (trường, sở)

Dự án của thầy Tô Gia Bảo: gõ lại bằng LaTeX (template Eduzy, gói ex_test) các đề thi thử tốt nghiệp THPT 2026 môn Vật lí của các trường, sở. Làm bằng Claude Code đám mây, cách làm kế thừa dự án 40 đề Toán (repo `soan-de-thi-thu-thptqg-2027`).

## Thư mục

| Thư mục / file | Nội dung |
|---|---|
| `CLAUDE.md` | Quy chuẩn soạn đề Vật lí và quy trình một lô (đọc trước mọi việc). |
| `kho/goc/` | Đề nguồn tải về: 83 file (42 Word `.docx`, 41 PDF) và `danh-sach-de.csv` (tỉnh, đơn vị, lần, nguồn, link). Không sửa file trong thư mục này. |
| `kho/kiem-ke.md` | Kiểm kê 83 đề: loại file, số câu, đáp án/lời giải, hình, trùng, tên file, dòng 1 khung tiêu đề, `\tenchuong` đề xuất. |
| `kho/TIEN-DO.md` | Tiến độ, quyết định của thầy, kế hoạch lô (M, W01–W11, P01–P09) và trạng thái từng đề. |
| `de/<tên>/` | File đề `.tex`, `kiem-chung.md`, `so-hinh/` (ảnh so hình gốc – TikZ). Đề mẫu chuẩn: `de/VatLi2026-CaoBang-SoGD-Lan1/`. |
| `thanh-pham/` | Thành phẩm mỗi đề: `<tên>.zip`, `<tên>-DE.pdf` (bản đề), `<tên>.pdf` (bản lời giải). |
| `preamble-eduzy-v2.tex`, `ex_test.sty`, `esvect.sty` | Template Eduzy và gói lệnh, chép nguyên từ dự án Toán. |
| `preamble-vatli-hinh.tex` | Bộ macro hình Vật lí dùng chung (circuitikz european, điện kế, nam châm, màu VL...); đề gọi ngay sau `preamble-eduzy-v2`. |
| `bien-dich.sh`, `dong-goi.sh`, `tron_de.py` | Biên dịch thử, đóng gói thành phẩm, trộn mã đề (chép từ dự án Toán; dự án này không trộn mã đề). |
| `XuatDe_LoiGiai.bat`, `DeleteAuxliaryFilesV5_2022.bat` | Kèm trong mỗi gói thành phẩm cho máy Windows. |
| `tools/` | Đọc đề Word (`docx_doc.py`), so hình (`so_hinh.py`), dàn trang (`dan_trang/`), dựng ảnh hình vẽ Word (`hinh_word.py`)... Cách dùng: `tools/README.md` (bản của dự án Toán: `tools/README-toan.md`). |
| `tham-khao/` | `bai-hoc-de-mau.md` (điều rút ra từ đề mẫu Vật lí); tài liệu dự án Toán: `CLAUDE-toan.md`, `mau-de-thi-thu-toan.tex`, `mau-chuan-toan.tex`, `du-an-40-de-toan.md`. |

## Trạng thái

- Giai đoạn 0 (06/11/2026): tạo repo, chép khung và công cụ từ dự án Toán, đưa đề nguồn vào `kho/goc/`.
- 06/11/2026: đề mẫu chuẩn đã duyệt `de/VatLi2026-CaoBang-SoGD-Lan1/` (thành phẩm trong `thanh-pham/`, điều rút ra ở `tham-khao/bai-hoc-de-mau.md`).
- 06/11/2026, phiên 1a: `CLAUDE.md` cho Vật lí; `preamble-vatli-hinh.tex`; dựng lại đề mẫu (7 trang đề, 10 trang lời giải); `tools/README.md`; kiểm kê `kho/kiem-ke.md`; kế hoạch lô `kho/TIEN-DO.md`. Tiếp theo: lô M (đề PDF không đáp án làm mẫu thứ hai).
