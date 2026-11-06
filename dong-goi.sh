#!/bin/bash
# ============================================================
#  ĐÓNG GÓI THÀNH PHẨM ĐỀ THI THỬ -> thanh-pham/<tên>.zip
#  Dùng:  bash dong-goi.sh de/<tên>/<tên>.tex [file .tex/.csv kèm thêm ...]   (chạy từ gốc repo)
#  Zip gồm thư mục <tên>/ chứa:
#    - file đề .tex (+ các file kèm thêm: mã đề, bảng đáp án... nếu có)
#    - đúng preamble mà file đề \input (preamble-eduzy-v2.tex mặc định, hoặc preamble-eduzy.tex)
#    - hinh/ (nếu có thư mục hinh cạnh file đề)
#    - XuatDe_LoiGiai.bat, DeleteAuxliaryFilesV5_2022.bat
#  Không chép PDF xem thử, không chép ans/ (bat tự tạo khi biên dịch).
# ============================================================
set -u
if [ $# -lt 1 ] || [ ! -f "$1" ]; then echo "Cách dùng: bash dong-goi.sh <file-đề.tex> [file kèm ...]"; exit 1; fi

# gốc repo = thư mục chứa script này (ghi đè được bằng EZ_PROJECT)
P=${EZ_PROJECT:-$(cd "$(dirname "$(readlink -f "$0")")" && pwd)}
SRC=$(readlink -f "$1")
NAME=$(basename "$SRC" .tex)
SRC_DIR=$(dirname "$SRC")
T=$(mktemp -d)
D="$T/$NAME"
OUT="$P/thanh-pham"
trap 'rm -rf "$T"' EXIT

mkdir -p "$D" "$OUT"
cp "$SRC" "$D/"
shift
for f in "$@"; do
	if [ -f "$f" ]; then cp "$f" "$D/"; else echo "Bỏ qua (không thấy file): $f"; fi
done

# preamble: chép đúng các file preamble-*.tex mà đề, file kèm (và chính preamble đó) \input
for lan in 1 2 3; do
	for p in $(grep -ho '\\input{preamble[^}]*}' "$D"/*.tex 2>/dev/null | sed 's/\\input{\(.*\)}/\1/' | sort -u); do
		p=${p%.tex}
		[ -f "$D/$p.tex" ] && continue
		if [ -f "$P/$p.tex" ]; then cp "$P/$p.tex" "$D/"; else echo "CẢNH BÁO: không thấy $p.tex ở gốc repo"; fi
	done
done
ls "$D"/preamble*.tex >/dev/null 2>&1 || cp "$P/preamble-eduzy-v2.tex" "$D/"

[ -d "$SRC_DIR/hinh" ] && cp -r "$SRC_DIR/hinh" "$D/"
cp "$P/XuatDe_LoiGiai.bat" "$P/DeleteAuxliaryFilesV5_2022.bat" "$D/"

cd "$T"
rm -f "$OUT/$NAME.zip"
zip -qr "$OUT/$NAME.zip" "$NAME"
echo "===== ĐÃ ĐÓNG GÓI: $OUT/$NAME.zip ====="
unzip -l "$OUT/$NAME.zip" | awk 'NR>3 && $4!="" {print "  " $4}' | grep -v -- '^  -*$'
