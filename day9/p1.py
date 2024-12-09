with open("day9/inp.txt", "r") as f:
    line = f.read().strip()

DOT = "."

vals = list(line[::2])
spcs = line[1::2]
idxs = "".join([str(i) for i in range(len(vals))])
line_len = sum([int(i) for i in vals])


def count_line(line):
    sum = 0
    for i, c in enumerate(line):
        if c == DOT:
            break
        j = int(c)
        sum += j * i
    return sum


def build_value(idx):
    return idxs[idx] * int(vals[idx])


def fill_space(idx):
    spc = spcs[idx]
    _idx = len(vals) - idx - 1
    v = idxs[_idx]
    res = ""
    while len(res) < int(spc):
        if int(vals[_idx]) > 0:
            res += v
            vals[_idx] = str(int(vals[_idx]) - 1)
        else:
            _idx -= 1
            v = idxs[_idx]
    return res


def build_line():
    i = 0
    j = 0
    line = ""
    for _ in range(int(line_len / 4)):
        line += build_value(i)
        line += fill_space(j)
        i += 1
        j += 1
    return line


print(build_line())
