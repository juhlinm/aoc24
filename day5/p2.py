import math

with open("day5/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

rules = {}
upd = []
for line in lines:
    if "|" in line:
        x, y = line.split("|")
        x = int(x)
        y = int(y)
        if x in rules:
            rules[x].append(y)
        else:
            rules[x] = [y]
    elif line:
        upd.append([int(x) for x in line.split(",")])


def is_valid(up):
    return not any(up[i + 1] in rules and up[i] in rules[up[i + 1]] for i in range(len(up) - 1))


def make_valid(up):
    n1 = up.copy()
    n2 = []
    while n2 != n1:
        n2 = n1.copy()
        for i in range(len(up) - 1):
            for j in range(1, len(up) - i):
                if n2[i + j] in rules and n2[i] in rules[n2[i + j]]:
                    n1[i] = n2[i + j]
                    n1[i + j] = n2[i]
                    n2 = n1.copy()
    return n1


sum = 0
for i, up in enumerate(upd):
    if not is_valid(up):
        up = make_valid(up)
        sum += up[math.floor(len(up) / 2)]

print(sum)
