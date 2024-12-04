with open("day4/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

XMAS = "XMAS"
SAMX = "SAMX"
PAD = "o"


def get_horizontal(lines):
    return sum([line.count(XMAS) + line.count(SAMX) for line in lines])


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


print(get_horizontal(lines) + get_vertical(lines) + get_diagonal(lines))
