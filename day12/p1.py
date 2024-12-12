from copy import deepcopy

inp = list(map(lambda x: x.strip(), open("day12/inp.txt", "r").readlines()))
oneforty = list(map(lambda x: x.strip(), open("day12/140.txt", "r").readlines()))
sevenseventwo = list(map(lambda x: x.strip(), open("day12/772.txt", "r").readlines()))
ninetinthirty = list(map(lambda x: x.strip(), open("day12/1930.txt", "r").readlines()))


def get_perimeter(p, f):
    sum = 0
    c = f[p]
    sum += c != f[(p[0] - 1, p[1])]
    sum += c != f[(p[0], p[1] - 1)]
    sum += c != f[(p[0] + 1, p[1])]
    sum += c != f[(p[0], p[1] + 1)]
    return sum


def part_of(p, A):
    for a in A:
        if (p[1] - 1 == a[1] or p[1] + 1 == a[1]) and p[0] == a[0]:
            return True
        if (p[0] - 1 == a[0] or p[0] + 1 == a[0]) and p[1] == a[1]:
            return True
    return False


def add_area(p, f, a):
    c = f[p]
    if not len(a[c]):
        a[c].append([p])
    else:
        area_group = sorted(a[c], key=lambda x: len(x), reverse=True)
        for A in area_group:
            if part_of(p, A):
                A.append(p)
                break
        else:
            area_group.append([p])
        a[c] = area_group
    return a


def solve(prob):
    res = 0
    areas = {c: [] for c in sorted(set("".join(prob)))}
    perims = {}
    y_max = len(prob)
    x_max = len(prob[0])
    fields = {}
    for y in range(-1, y_max + 1):
        for x in range(-1, x_max + 1):
            fields[(x, y)] = "-1"

    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            fields[(x, y)] = c

    for y in range(y_max):
        for x in range(x_max):
            areas = add_area((x, y), fields, areas)
            perims[(x, y)] = get_perimeter((x, y), fields)

    for c, a_group in areas.items():
        a_group = sorted(a_group, key=lambda x: len(x), reverse=True)
        old_group = []
        while old_group != a_group:
            old_group = deepcopy(a_group)
            for A in a_group:
                o_groups = [x for x in a_group if x != A]
                for o in o_groups:
                    for p in o:
                        if part_of(p, A):
                            A.extend(o)
                            if o in a_group:
                                a_group.remove(o)
                            break

        for A in a_group:
            area = len(A)
            perimeter = sum(perims[p] for p in A)
            res += area * perimeter
            
    return res


print(solve(oneforty), 140)
print(solve(sevenseventwo), 772)
print(solve(ninetinthirty), 1930)
print(solve(inp))
