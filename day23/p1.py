inp = [x.strip() for x in open("day23/inp.txt", "r").readlines()]
inp_test = [x.strip() for x in open("day23/inp_test.txt", "r").readlines()]
test_1 = [x.strip() for x in open("day23/test_1.txt", "r").readlines()]


def has_id(inter, id):
    return [inte for inte in inter if any([i.startswith(id) for i in inte])]


def get_inter(prob):
    ret = set()
    conn = {}
    for line in prob:
        a, b = line.split("-")
        if a in conn:
            conn[a].append(b)
        else:
            conn[a] = [b]

    for k, v in conn.items():
        for k_o in v:
            if k_o in conn:
                v_o = conn[k_o]
                for i in v_o:
                    if i in v or (i in conn and k in conn[i]):
                        ret.add(tuple(sorted([k, k_o, i])))

    return ret


def solve(prob):
    inter = get_inter(prob, 3)
    ids = has_id(inter, "t")
    return len(ids)


print(len(get_inter(inp_test, 3)), 12)
print(solve(inp_test), 7)
print(solve(test_1))
print(solve(inp))
