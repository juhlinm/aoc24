inp = open("day24/inp.txt", "r").read().split("\n\n")
inp_test = open("day24/inp_test.txt", "r").read().split("\n\n")
inp_4 = open("day24/inp_4.txt", "r").read().split("\n\n")


def get_z_value(vals):
    val = ""
    keys = sorted(vals.keys(), reverse=True)
    for k in keys:
        if k.startswith("z"):
            val += str(int(vals[k]))

    return int(val, 2)


def action(vals, op):
    a, act, b, res = op
    a = vals[a]
    b = vals[b]
    if act == 0:
        vals[res] = a and b
    elif act == 1:
        vals[res] = a or b
    elif act == 2:
        vals[res] = a != b


def sorter(vals, ops):
    n_ops = []
    avail = [op for op in ops if op[0] in vals and op[2] in vals]
    n_ops.extend(avail)

    avail_res = [op[3] for op in avail]
    stack = [op for op in ops if op not in avail]

    while len(stack):
        a, _, b, res = stack[-1]

        if (a in vals and b in avail_res) or (b in vals and a in avail_res):
            n_ops.append(stack.pop())
        elif a in avail_res and b in avail_res:
            n_ops.append(stack.pop())
            avail_res.append(res)
        else:
            stack = stack[-1:] + stack[:-1]
    return n_ops


def solve(prob):
    init, ops_raw = prob
    vals = {
        line.split(": ")[0]: bool(int(line.split(": ")[1])) for line in init.split("\n")
    }
    ops = []
    operators = ["AND", "OR", "XOR"]
    for line in ops_raw.split("\n"):
        split = line.split()
        ops.append((split[0], operators.index(split[1]), split[2], split[4]))

    ops = sorter(vals, ops)

    for op in ops:
        action(vals, op)
    return get_z_value(vals)


print(solve(inp_4), 4)
print(solve(inp_test), 2024)
print(solve(inp))
