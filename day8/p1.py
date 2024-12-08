with open("day8/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

y_max = len(lines)
x_max = len(lines[0])

ants = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            if c in ants:
                ants[c].append((x, y))
            else:
                ants[c] = [(x,y)]
pairs = {}
for c, poses in ants.items():
    pairs[c] = [(poses[i], poses[j]) for i in range(len(poses)) for j in range(i + 1, len(poses))]

def is_inside(p):
    px, py = p
    return px < x_max and px >= 0 and py < y_max and py >= 0

def get_antis(pr):
    res = []
    delta = (pr[1][0]-pr[0][0], pr[1][1] - pr[0][1])
    a1 = tuple(a + b for a, b in zip(pr[1], delta))
    a2 = tuple(a - b for a, b in zip(pr[0], delta))
    if is_inside(a1):
        res.append(a1)
    if is_inside(a2):
        res.append(a2)
    return res
    

anti = {ant for prs in pairs.values() for pr in prs for ant in get_antis(pr)}

print(len(anti))