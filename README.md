# Gõ lại đề thi thử tốt nghiệp THPT 2026 môn Vật lí (trường, sở)

Dự án của thầy Tô Gia Bảo: gõ lại bằng LaTeX (template Eduzy, gói ex_test) các đề thi thử tốt nghiệp THPT 2026 môn Vật lí của các trường, sở. Làm bằng Claude Code đám mây, cách làm kế thừa dự án 40 đề Toán (repo `soan-de-thi-thu-thptqg-2027`).

## Thư mục

| Thư mục / file | Nội dung |
|---|---|
| `kho/goc/` | Đề nguồn tải về: 83 file (42 Word `.docx`, 41 PDF) và `danh-sach-de.csv` (tỉnh, đơn vị, lần, nguồn, link). Không sửa file trong thư mục này. |
| `preamble-eduzy-v2.tex`, `ex_test.sty`, `esvect.sty` | Template Eduzy và gói lệnh, chép nguyên từ dự án Toán. |
| `bien-dich.sh`, `dong-goi.sh`, `tron_de.py` | Biên dịch thử, đóng gói thành phẩm, trộn mã đề (chép từ dự án Toán). |
| `XuatDe_LoiGiai.bat`, `DeleteAuxliaryFilesV5_2022.bat` | Kèm trong mỗi gói thành phẩm cho máy Windows. |
| `tools/dan_trang/` | Công cụ dàn trang: `needspace`, `kiem`, `xuat`, `thu-hinh` (xem `tham-khao/CLAUDE-toan.md`, mục HÌNH VẼ và BIÊN DỊCH THỬ). |
| `tools/soan_de/` | `kiem_tra.py` soát file đề, `khung.py` dựng khung đề. |
| `tools/docx_doc.py`, `mtef.py`, `tach_cau.py`, `hinh_word.py`, `pdf_dap_an.py`, `xem_thu.py` | Công cụ đọc đề Word (giải mã công thức MathType ra LaTeX), tách câu, dựng ảnh hình vẽ Word, đọc đáp án PDF. Viết cho dự án Toán, cần chỉnh lại khi dùng cho Vật lí. Cách dùng: `tools/README-toan.md`. |
| `tham-khao/` | Tài liệu của dự án Toán để tham khảo: `CLAUDE-toan.md` (quy chuẩn soạn đề), `mau-de-thi-thu-toan.tex`, `mau-chuan-toan.tex`, `du-an-40-de-toan.md`. |

## Trạng thái

- Giai đoạn 0 (06/11/2026): tạo repo, chép khung và công cụ từ dự án Toán, đưa đề nguồn vào `kho/goc/`.
- Chưa có `CLAUDE.md` cho Vật lí: soạn ở phiên đầu tiên, sau khi thầy chốt quy cách (có đáp án/lời giải hay không, tiêu đề, đặt tên file, cấu trúc đề, quy tắc hình vẽ Vật lí).
