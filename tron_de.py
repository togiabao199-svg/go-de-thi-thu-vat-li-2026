# -*- coding: utf-8 -*-
"""
TRỘN ĐỀ THI THỬ TN THPT (gói ex_test, template Eduzy)

Cách dùng:
    python3 tron_de.py <de-goc.tex> [ma_de ...] [--seed N] [--dao-ds]

Ví dụ:
    python3 tron_de.py de/ThiThu-TN-Lan1-2026/ThiThu-TN-Lan1-2026.tex 101 102 103 104

Quy tắc trộn:
  - Đảo thứ tự câu trong TỪNG PHẦN (giữa \\Opensolutionfile và \\Closesolutionfile).
  - Phần có \\choice: đảo 4 phương án; \\True đi theo phương án đúng.
    Mỗi mã đề được cân đáp án A/B/C/D đều nhau, không quá 2 câu liền cùng chữ cái.
  - Phần \\choiceTFt / \\choiceTF: chỉ đảo thứ tự câu (thêm --dao-ds để đảo cả 4 ý,
    khi đó các \\itemch trong lời giải được đảo theo).
  - Phần \\shortans: chỉ đảo thứ tự câu.
  - Câu có comment "% khongtron" ngay trong khối ex: giữ nguyên phương án / ý.
  - Câu có comment "% codinh": giữ nguyên vị trí trong phần.

Kết quả (cạnh file gốc):
  <ten>-<made>.tex       mỗi mã đề một file, lưu đáp án vào ans/<ten>-<made>-k
  <ten>-DapAn.tex        bảng đáp án tổng hợp mọi mã đề
  <ten>-DapAn.csv        bảng đáp án dạng CSV để nhập phần mềm chấm
"""
import re, sys, random, csv, os

LETTERS = "ABCD"


# ---------------------------------------------------------------- tiện ích
def read_group(s, i):
    """s[i] là '{' (sau khi bỏ khoảng trắng). Trả (nội dung, vị trí sau '}')."""
    while s[i] in " \t\r\n":
        i += 1
    assert s[i] == "{", "Không thấy dấu { ở vị trí %d: %r" % (i, s[i:i + 30])
    depth, j = 0, i
    while True:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "%":                      # bỏ qua comment
            j = s.index("\n", j)
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1


def find_cmd(block, name):
    """Vị trí ngay sau lệnh \\name (không ăn vào \\nameXYZ)."""
    m = re.search(r"\\" + name + r"(?![A-Za-z])", block)
    return m


def options_span(block, name, k=4):
    """Trả (đầu, cuối, [k phương án], [k khoảng trắng đứng trước]) của \\name{..}{..}."""
    m = find_cmd(block, name)
    if not m:
        return None
    pos, opts, pres = m.end(), [], []
    start = pos
    for _ in range(k):
        q = pos
        while block[q] in " \t\r\n":
            q += 1
        pres.append(block[pos:q])
        body, pos = read_group(block, q)
        opts.append(body)
    return start, pos, opts, pres


def is_true(opt):
    return opt.lstrip().startswith("\\True")


def strip_true(opt):
    return re.sub(r"^\s*\\True\s*", "", opt)


# ---------------------------------------------------------------- tách đề
def split_parts(text):
    """Tách văn bản thành các đoạn: ('raw', str) hoặc ('part', ansname, [khối câu])."""
    pat = re.compile(r"(\\Opensolutionfile\{ans\}\[([^\]]+)\])(.*?)(\\Closesolutionfile\{ans\})", re.S)
    out, last = [], 0
    for m in pat.finditer(text):
        out.append(("raw", text[last:m.start()]))
        out.append(("part", m.group(2), split_blocks(m.group(3))))
        last = m.end()
    out.append(("raw", text[last:]))
    return out


def split_blocks(body):
    """Mỗi khối = [\\Needspace... / \\NeedspaceCau[..]{..}] + \\begin{ex}...\\end{ex} (kèm comment ngay trên).
    Đổi thứ tự câu làm đổi dàn trang: sau khi trộn chạy tools/dan_trang/dan_trang.py needspace cho từng mã đề."""
    pat = re.compile(r"((?:[ \t]*(?:\\Needspace(?:Cau)?(?:\[[^\]]*\])?\{[^}]*\}|%[^\n]*)[ \t]*\n)*"
                     r"[ \t]*\\begin\{ex\}.*?\\end\{ex\})", re.S)
    blocks = [b.strip("\n") for b in pat.findall(body)]
    return blocks


def part_kind(blocks):
    joined = "\n".join(blocks)
    if re.search(r"\\choiceTFt?(?![A-Za-z])", joined):
        return "TF"
    if re.search(r"\\choice(?![A-Za-z])", joined):
        return "MC"
    return "SA"


# ---------------------------------------------------------------- trộn
def balanced_targets(n, rng):
    base = [LETTERS[i % 4] for i in range(n)]
    for _ in range(1000):
        rng.shuffle(base)
        if all(not (base[i] == base[i - 1] == base[i - 2]) for i in range(2, n)):
            return base
    return base


def shuffle_mc(block, target, rng):
    if "khongtron" in block:
        sp = options_span(block, "choice")
        ans = LETTERS[[is_true(o) for o in sp[2]].index(True)]
        return block, ans
    start, end, opts, pres = options_span(block, "choice")
    idx_true = [is_true(o) for o in opts].index(True)
    others = [o for i, o in enumerate(opts) if i != idx_true]
    rng.shuffle(others)
    t = LETTERS.index(target)
    new = others[:t] + [opts[idx_true]] + others[t:]
    seg = "".join(p + "{" + o + "}" for p, o in zip(pres, new))
    return block[:start] + seg + block[end:], target


def tf_answer(block):
    m = find_cmd(block, "choiceTFt") or find_cmd(block, "choiceTF")
    name = "choiceTFt" if find_cmd(block, "choiceTFt") else "choiceTF"
    sp = options_span(block, name)
    return name, sp


def shuffle_tf(block, rng, dao):
    name, (start, end, opts, pres) = tf_answer(block)
    perm = list(range(4))
    if dao and "khongtron" not in block:
        rng.shuffle(perm)
        new = [opts[i] for i in perm]
        seg = "".join(p + "{" + o + "}" for p, o in zip(pres, new))
        block = block[:start] + seg + block[end:]
        # đảo các \itemch trong lời giải cho khớp
        m = re.search(r"(\\begin\{itemchoice\})(.*?)(\\end\{itemchoice\})", block, re.S)
        if m:
            items = re.split(r"(?=\\itemch)", m.group(2))
            head, items = items[0], items[1:]
            if len(items) == 4:
                tail_ws = re.search(r"\s*$", items[-1]).group(0)
                items = [it.rstrip() for it in items]
                items = [items[i] for i in perm]
                sep = re.search(r"\n[ \t]*$", head).group(0) if re.search(r"\n[ \t]*$", head) else "\n"
                inner = head + sep.join(items).lstrip() + tail_ws
                block = block[:m.start(2)] + inner + block[m.end(2):]
        opts = new
    return block, "".join("Đ" if is_true(o) else "S" for o in opts)


def sa_answer(block):
    m = find_cmd(block, "shortans")
    if not m:
        return ""
    s = block[m.end():]
    s = re.sub(r"^\[[^\]]*\]", "", s)
    body, _ = read_group(s, 0)
    return body.replace("{,}", ",")


def shuffle_part(blocks, rng):
    fixed = {i: b for i, b in enumerate(blocks) if "codinh" in b}
    movable = [b for i, b in enumerate(blocks) if i not in fixed]
    rng.shuffle(movable)
    it = iter(movable)
    return [fixed[i] if i in fixed else next(it) for i in range(len(blocks))]


# ---------------------------------------------------------------- chính
def make_version(text, base, made, rng, dao_ds):
    k = text.index("\\begin{document}")
    preamble, text = text[:k], text[k:]
    parts = split_parts(text)
    out, answers, part_no, renames = [], [], 0, []
    for p in parts:
        if p[0] == "raw":
            out.append(p[1])
            continue
        _, ansname, blocks = p
        part_no += 1
        kind = part_kind(blocks)
        new_blocks = shuffle_part(blocks, rng)
        ans = []
        if kind == "MC":
            targets = balanced_targets(len(new_blocks), rng)
            res = [shuffle_mc(b, t, rng) for b, t in zip(new_blocks, targets)]
            new_blocks, ans = [r[0] for r in res], [r[1] for r in res]
        elif kind == "TF":
            res = [shuffle_tf(b, rng, dao_ds) for b in new_blocks]
            new_blocks, ans = [r[0] for r in res], [r[1] for r in res]
        else:
            ans = [sa_answer(b) for b in new_blocks]
        answers.append((kind, ans))
        if base in ansname:
            newans = ansname.replace(base, base + "-" + made, 1)
        else:
            d = os.path.dirname(ansname)
            newans = (d + "/" if d else "") + "%s-%s-%d" % (base, made, part_no)
        renames.append((ansname, newans))
        out.append("\\Opensolutionfile{ans}[%s]\n\t\n\t" % newans
                   + "\n\n\t".join(b.lstrip() for b in new_blocks)
                   + "\n\t\n\t\\Closesolutionfile{ans}")
    res = "".join(out)
    # đổi tên file đáp án trong bảng đáp án (comment) cho khớp mã đề
    for a, b in renames:
        res = res.replace("{" + a + "}", "{" + b + "}")
    # hộp mã đề ngay dưới khung tiêu đề
    box = ("\n\t\\vspace*{-2mm}\\hfill{\\setlength\\fboxrule{1pt}\\setlength\\fboxsep{4pt}"
           "\\fbox{\\textbf{Mã đề thi: %s}}}\\par\n" % made)
    m = re.search(r"\\khungtieude", res)
    if m:
        _, pos = read_group(res, m.end())
        for _ in range(3):
            _, pos = read_group(res, pos)
        res = res[:pos] + box + res[pos:]
    return preamble + res, answers


def write_key(base, folder, versions, ten="", head=""):
    made_list = list(versions)
    first = versions[made_list[0]]
    rows_csv = [["Phần", "Câu"] + made_list]
    if head:
        head = re.sub(r"\\def\\CheDo\{[^}]*\}", lambda m: r"\def\CheDo{dethi}", head, count=1)
        head = re.sub(r"\\def\\tenchuong\{.*\}", lambda m: r"\def\tenchuong{Bảng đáp án các mã đề -- %s}" % (ten or base), head, count=1)
        tex = [head.rstrip("\n"), r"\begin{document}",
               r"\begin{center}\indam{BẢNG ĐÁP ÁN CÁC MÃ ĐỀ}\end{center}"]
    else:
        tex = [r"\def\CheDo{dethi}",
           r"\def\tenchuong{Bảng đáp án các mã đề -- %s}" % (ten or base),
           r"\input{preamble-eduzy-v2}", r"\begin{document}",
           r"\begin{center}\indam{BẢNG ĐÁP ÁN CÁC MÃ ĐỀ}\end{center}"]
    names = {"MC": "PHẦN I", "TF": "PHẦN II", "SA": "PHẦN III"}
    for k, (kind, ans) in enumerate(first):
        tex.append(r"\noindent\indam{%s.}\par\smallskip" % names.get(kind, "PHẦN %d" % (k + 1)))
        tex.append(r"\begin{center}\renewcommand{\arraystretch}{1.3}")
        tex.append(r"\begin{tabular}{|c|" + "c|" * len(made_list) + "}")
        tex.append(r"\hline \textbf{Câu} & " + " & ".join(r"\textbf{%s}" % m for m in made_list) + r"\\ \hline")
        for q in range(len(ans)):
            vals = [versions[m][k][1][q] for m in made_list]
            rows_csv.append([names.get(kind), q + 1] + vals)
            tvals = [v.replace(",", "{,}") for v in vals]
            tex.append("%d & %s \\\\ \\hline" % (q + 1, " & ".join(tvals)))
        tex.append(r"\end{tabular}\end{center}")
    tex.append(r"\centerline{--- HẾT ---}")
    tex.append(r"\end{document}")
    with open(os.path.join(folder, base + "-DapAn.tex"), "w", encoding="utf-8") as f:
        f.write("\n".join(tex) + "\n")
    with open(os.path.join(folder, base + "-DapAn.csv"), "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(rows_csv)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    src = args[0]
    dao_ds = "--dao-ds" in args
    seed, skip = None, set()
    if "--seed" in args:
        i = args.index("--seed")
        seed, skip = int(args[i + 1]), {i, i + 1}
    made_list = [a for j, a in enumerate(args) if j >= 1 and j not in skip and a.isdigit()]
    made_list = made_list or ["101", "102", "103", "104"]
    folder, fname = os.path.split(os.path.abspath(src))
    base = fname[:-4]
    text = open(src, encoding="utf-8").read()
    versions = {}
    for made in made_list:
        rng = random.Random((seed or 2026) * 1000 + int(made))
        res, answers = make_version(text, base, made, rng, dao_ds)
        with open(os.path.join(folder, "%s-%s.tex" % (base, made)), "w", encoding="utf-8") as f:
            f.write(res)
        versions[made] = answers
        mc = [a for k, a in answers if k == "MC"]
        print("Mã đề %s: PHẦN I %s" % (made, " ".join(mc[0]) if mc else ""))
    m = re.search(r"\\def\\tenchuong\{(.*)\}", text)
    write_key(base, folder, versions, m.group(1) if m else "", text[:text.index("\\begin{document}")])
    print("Xong: %d mã đề + %s-DapAn.tex/.csv" % (len(made_list), base))


if __name__ == "__main__":
    main()
