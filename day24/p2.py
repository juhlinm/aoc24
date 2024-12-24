inp = open("day24/inp.txt", "r").read().split("\n\n")
inp_p2 = open("day24/inp_p2.txt", "r").read().split("\n\n")


def get_value(vals, key):
    val = ""
    keys = sorted(vals.keys(), reverse=True)
    for k in keys:
        if k.startswith(key):
            val += str(int(vals[k]))

    return int(val, 2)


def get_n_values(vals, key):
    return len([k for k in vals.keys() if k.startswith(key)])


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
    x = get_value(vals, "x")

    y = get_value(vals, "y")

    s = x + y

    for op in ops:
        action(vals, op)

    n_z = get_n_values(vals, "z")
    bin_s = bin(s)[-n_z:]
    bin_x = bin(x)[-n_z:]
    bin_y = bin(y)[-n_z:]

    # loop over len z
    # if len x < len_z  --> first element 1 if both 1 first x,y

    incorrect = []
    for k in range(len(bin_s) - 1, -1, -1):
        key = "z" + str(k).zfill(2)
        if vals[key] != bool(bin_s[-(k + 1)]):
            incorrect.append(key)

    r = get_value(vals, "z")
    bin_r = bin(r)[2:].zfill(n_z)
    return r


print(solve(inp_p2), "z00,z01,z02,z05")
# print(solve(inp))
