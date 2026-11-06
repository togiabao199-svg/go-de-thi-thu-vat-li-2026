#!/bin/bash
# ============================================================
#  BIÊN DỊCH THỬ ĐỀ EDUZY
#  Dùng:  bash bien-dich.sh de/<tên>/<tên>.tex   (chạy từ gốc repo)
#  - File có \begin{document}: biên dịch nguyên file (file \input{preamble-eduzy-v2},
#    mặc định, hoặc \input{preamble-eduzy}).
#  - File chỉ gồm các khối \begin{ex}/\begin{bt}: tự bọc vào khung preamble-eduzy-v2.
#  Kết quả: thư mục bien-dich/ cạnh file nguồn (de/<tên>/bien-dich/) gồm <tên>.pdf và ảnh trang-*.png
#  Thư mục hinh/ (và fonts/ của bìa sách) cạnh file nguồn, nếu có, được chép theo.
# ============================================================
set -u
if [ $# -lt 1 ] || [ ! -f "$1" ]; then echo "Cách dùng: bash bien-dich.sh <file.tex>"; exit 1; fi

# gốc repo = thư mục chứa script này (ghi đè được bằng EZ_PROJECT)
P=${EZ_PROJECT:-$(cd "$(dirname "$(readlink -f "$0")")" && pwd)}
SRC=$(readlink -f "$1")
SRC_DIR=$(dirname "$SRC")
W="$SRC_DIR/bien-dich"
rm -rf "$W"; mkdir -p "$W/ans"
NAME=$(basename "$SRC" .tex)

cp "$P"/preamble*.tex "$W/"   # preamble-eduzy-v2, preamble-vatli-hinh...
cp "$P/ex_test.sty" "$W/ex_test.sty"

# esvect: máy biên dịch không có font esvect -> dùng bản thay thế (mũi tên vectơ của amsmath)
if kpsewhich uesvect.fd >/dev/null 2>&1; then
	cp "$P/esvect.sty" "$W/esvect.sty"
else
	printf '%s\n' '\ProvidesPackage{esvect}[sandbox]' '\let\EZarrow\overrightarrow' '\newcommand{\vv}[1]{\EZarrow{#1}}' > "$W/esvect.sty"
fi
# fontawesome: ex_test nạp nhưng đề không dùng -> tạo gói rỗng nếu máy thiếu
if ! kpsewhich fontawesome.sty >/dev/null 2>&1 && ! kpsewhich fontawesome5.sty >/dev/null 2>&1; then
	printf '%s\n' '\ProvidesPackage{fontawesome}[sandbox]' > "$W/fontawesome.sty"
fi

if grep -q '\\begin{document}' "$SRC"; then
	cp "$SRC" "$W/$NAME.tex"
else
	cp "$SRC" "$W/$NAME-than.tex"
	cat > "$W/$NAME.tex" <<EOF
\\def\\CheDo{loigiai}
\\def\\tenchuong{Bản biên dịch thử -- $NAME}
\\input{preamble-eduzy-v2}
\\begin{document}
\\setcounter{ex}{0}
\\Opensolutionfile{ans}[ans/$NAME]
\\input{$NAME-than}
\\Closesolutionfile{ans}
\\end{document}
EOF
fi

# thư mục hình (nếu có) nằm cạnh file nguồn
[ -d "$SRC_DIR/hinh" ] && cp -r "$SRC_DIR/hinh" "$W/"
# thư mục font riêng (bìa sách dùng Montserrat qua fontspec Path=fonts/)
[ -d "$SRC_DIR/fonts" ] && cp -r "$SRC_DIR/fonts" "$W/"

cd "$W"
export TEXINPUTS="$W//:$P//:${TEXINPUTS:-}"
for i in 1 2; do
	xelatex -interaction=nonstopmode -halt-on-error "$NAME.tex" > /dev/null 2>&1 || break
done

echo "===== LỖI (nếu có) ====="
grep -n '^!' -A4 "$NAME.log" | head -40
echo "===== TRÀN LỀ > 5pt (nếu có) ====="
grep -E 'Overfull \\hbox \(([5-9]|[0-9]{2,})\.' "$NAME.log" | head -20
echo "===== THIẾU KÝ TỰ (nếu có) ====="
grep 'Missing character' "$NAME.log" | sort | uniq -c | head -10

if [ -f "$NAME.pdf" ]; then
	pdftoppm -r 60 -png "$NAME.pdf" "$W/trang"
	echo "===== KẾT QUẢ ====="
	echo "PDF: $W/$NAME.pdf ($(pdfinfo "$NAME.pdf" | awk '/^Pages/{print $2}') trang)"
	ls "$W"/trang-*.png
else
	echo "Không tạo được PDF."
fi
