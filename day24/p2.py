inp = open("day24/inp.txt", "r").read().split("\n\n")

OPERATORS = ["AND", "OR", "XOR"]


class Operation:
    a: str
    b: str
    op: int
    res: str

    def __init__(self, a: str, op: int, b: str, res: str) -> None:
        self.a = a
        self.op = op
        self.b = b
        self.res = res

    def __eq__(self, other: object) -> bool:
        nums = (self.a == other.a and self.b == other.b) or (
            self.a == other.b and self.b == other.a
        )
        return nums and self.op == other.op

    def __repr__(self) -> str:
        return f"{self.a} {OPERATORS[self.op]} {self.b} -> {self.res}"

    def is_xy(self) -> bool:
        return self.a.startswith(("x", "y")) and self.b.startswith(("x", "y"))

    def half_eq(self, other: object) -> bool:
        nums = (
            (self.a == other.a and self.b != other.b)
            or (self.a == other.b and self.b != other.a)
            or (self.a != other.a and self.b == other.b)
            or (self.a != other.b and self.b == other.a)
        )
        return nums and self.op == other.op


def get_value(vals, key):
    val = ""
    keys = sorted(vals.keys(), reverse=True)
    for k in keys:
        if k.startswith(key):
            val += str(int(vals[k]))

    return int(val, 2)


def action(vals, o):
    a = vals[o.a]
    b = vals[o.b]
    if o.op == 0:
        vals[o.res] = a and b
    elif o.op == 1:
        vals[o.res] = a or b
    elif o.op == 2:
        vals[o.res] = a != b


def sorter(vals, ops):
    n_ops = []
    avail = [op for op in ops if op.a in vals and op.b in vals]
    n_ops.extend(avail)

    avail_res = [op.res for op in avail]
    stack = [op for op in ops if op not in avail]

    while len(stack):
        c_o = stack[-1]

        if (c_o.a in vals and c_o.b in avail_res) or (
            c_o.b in vals and c_o.a in avail_res
        ):
            n_ops.append(stack.pop())
        elif c_o.a in avail_res and c_o.b in avail_res:
            n_ops.append(stack.pop())
            avail_res.append(c_o.res)
        else:
            stack = stack[-1:] + stack[:-1]
    return n_ops


def secret_op(vals, ops):
    wanted_ops = []
    wanted_ops.append(Operation("x00", 2, "y00", "z00"))
    wanted_ops.append(Operation("x00", 0, "y00", "B00"))

    length = (len(ops) - 2) // 5
    for i in range(length):
        n = str(i + 1).zfill(2)
        x = "x" + n
        y = "y" + n
        A = "A" + n
        C = "C" + n
        wanted_ops.append(Operation(x, 2, y, A))
        wanted_ops.append(Operation(x, 0, y, C))

    for i in range(length):
        n = str(i + 1).zfill(2)
        z = "z" + n
        z_plus = "z" + str(i + 2).zfill(2)
        A = "A" + n
        B = "B" + n
        B_last = "B" + str(i).zfill(2)
        C = "C" + n
        D = "D" + n
        wanted_ops.append(Operation(A, 2, B_last, z))
        wanted_ops.append(Operation(A, 0, B_last, D))
        if i != length - 1:
            wanted_ops.append(Operation(C, 1, D, B))
        else:
            wanted_ops.append(Operation(C, 1, D, z_plus))

    os = ops.copy()
    switcheroon = {}
    switcherone = {}
    xy_list = [w for w in wanted_ops if w.is_xy()]
    for wanted_op in xy_list:
        for op in os:
            if wanted_op == op:
                switcheroon[wanted_op.res] = op
                switcherone[op.res] = wanted_op
                break

    non_xy = [w for w in wanted_ops if not w.is_xy()]
    for wanted_op in non_xy:
        temp_op = Operation(
            switcheroon[wanted_op.a].res, wanted_op.op, switcheroon[wanted_op.b].res, ""
        )
        for op in os:
            if temp_op == op:
                switcheroon[wanted_op.res] = op
                switcherone[op.res] = wanted_op
                break
        else:
            for op in ops:
                if temp_op.half_eq(op):
                    switcheroon[wanted_op.res] = op
                    switcherone[op.res] = wanted_op
                    break

    switched = set()
    for k, v in switcheroon.items():
        if k.startswith("z"):
            if not v.res.startswith("z"):
                switched.add(k)
                switched.add(v.res)
            if k not in ["z00", "z45"]:
                idx = int(k[1:])
                A = "A" + str(idx).zfill(2)
                B = "B" + str(idx - 1).zfill(2)
                s_A = switcheroon[A].res
                s_B = switcheroon[B].res
                source = [s_A, s_B]
                if v.a not in source or v.b not in source:
                    if not v.a == s_A and not v.b == s_A:
                        switched.add(s_A)
                        if not v.a in source:
                            switched.add(v.a)
                        else:
                            switched.add(v.b)
                    if not v.a == s_A and not v.b == s_B:
                        switched.add(s_B)
                        if not v.a in source:
                            switched.add(v.a)
                        else:
                            switched.add(v.b)
        if k.startswith("A"):
            if not v.op == 2 or not v.is_xy():
                switched.add(k)
                switched.add(v.res)
        if k.startswith("C"):
            if not v.op == 0 or not v.is_xy():
                switched.add(k)
                switched.add(v.res)

    return wanted_ops, ",".join(sorted(list(switched)))


def solve(prob):
    init, ops_raw = prob
    vals = {
        line.split(": ")[0]: bool(int(line.split(": ")[1])) for line in init.split("\n")
    }
    ops = []

    for line in ops_raw.split("\n"):
        split = line.split()
        ops.append(Operation(split[0], OPERATORS.index(split[1]), split[2], split[4]))

    ops, ret = secret_op(vals, ops)
    ops = sorter(vals, ops)

    x = get_value(vals, "x")
    y = get_value(vals, "y")

    s = x + y

    for op in ops:
        action(vals, op)

    z = get_value(vals, "z")
    print(f"{z}\n{s}")
    return ret


print(solve(inp))
