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


sum = 0
for up in upd:
    if is_valid(up):
        sum += up[math.floor(len(up) / 2)]

print(sum)
