with open("day9/inp.txt", "r") as f:
    line = f.read().strip()

vals = list(line[::2])
vals_o = vals.copy()
spcs = line[1::2]
idxs = [i for i in range(len(vals))]
line_len = sum([int(i) for i in vals])


def count_line(line):
    sum = 0
    for i, c in enumerate(line):
        if c != "":
            j = int(c)
            sum += j * i
    return sum


def build_value(idx):
    if idx < len(vals) and vals[idx] == vals_o[idx]:
        res = [str(idxs[idx])] * int(vals[idx])
        vals[idx] = "0"
        return res
    else:
        return []
    
def get_highest_v():
    k = [i for i, x in enumerate(vals) if x != "0"]
    if not k:
        return ""
    vals[k[-1]] = str(int(vals[k[-1]]) - 1)
    return str(idxs[k[-1]])

def fill_space(idx):
    res = []
    if idx < len(spcs):
        spc = spcs[idx]
        while len(res) < int(spc):
            res.append(get_highest_v())
    return res


def build_line():
    nums = []
    for i in range(int(line_len / 4)):
        nums.extend(build_value(i))
        nums.extend(fill_space(i))
    return nums

res = build_line()
print(count_line(res))