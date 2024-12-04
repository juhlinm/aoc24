with open("day4/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

MAS = "MAS"
SAM = "SAM"
PAD = "o"


def get_horizontal(lines):
    return sum([line.count(MAS) + line.count(SAM) for line in lines])


def get_vertical(lines):
    n_lines = [""] * len(lines[0])
    for line in lines:
        for i, char in enumerate(line):
            n_lines[i] += char
    return get_horizontal(n_lines)


def get_diagonal(lines):
    l1 = lines.copy()
    l2 = lines.copy()
    n = len(lines)
    for i in range(0, n):
        l1[i] = PAD * i + l1[i] + PAD * (n - i)
        l2[i] = PAD * (n - i) + l2[i] + PAD * i
    return get_vertical(l1) + get_vertical(l2)


def is_sam(inp):
    return get_diagonal(inp) == 2


res = 0
for i in range(len(lines) - 2):
    for j in range(len(lines[0]) - 2):
        res += is_sam([lines[i][j : j + 3], lines[i + 1][j : j + 3], lines[i + 2][j : j + 3]])

print(res)
