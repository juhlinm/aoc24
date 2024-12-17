inp = open("day17/inp.txt", "r").read().split("\n\n")
inp_p2 = open("day17/inp_p2.txt", "r").read().split("\n\n")


def get_comb(regs, comb):
    if comb < 4:
        return comb
    if comb == 4:
        return regs[0]
    if comb == 5:
        return regs[1]
    if comb == 6:
        return regs[2]
    else:
        raise Exception("7 not valid")


def adv(regs, comb):
    c = get_comb(regs, comb)
    regs[0] = regs[0] // (2**c)


def bxl(regs, comb):
    regs[1] = regs[1] ^ comb


def bst(regs, comb):
    c = get_comb(regs, comb)
    regs[1] = c % 8


def jnz(regs, comb):
    if regs[0] == 0:
        return None
    return comb


def bxc(regs, comb):
    regs[1] = regs[1] ^ regs[2]


def out(regs, comb, outp):
    c = get_comb(regs, comb)
    outp.append(c % 8)


def bdv(regs, comb):
    c = get_comb(regs, comb)
    regs[1] = regs[0] // (2**c)


def cdv(regs, comb):
    c = get_comb(regs, comb)
    regs[2] = regs[0] // (2**c)


def execute(i_0, ops, regs, outp):
    for i in range(i_0 + 1, len(ops), 2):
        op = ops[i - 1]
        comb = ops[i]

        if op == 0:
            adv(regs, comb)
        elif op == 1:
            bxl(regs, comb)
        elif op == 2:
            bst(regs, comb)
        elif op == 3:
            i = jnz(regs, comb)
            if i is not None:
                execute(i, ops, regs, outp)
        elif op == 4:
            bxc(regs, comb)
        elif op == 5:
            out(regs, comb, outp)
        elif op == 6:
            bdv(regs, comb)
        elif op == 7:
            cdv(regs, comb)


def solve(prob):
    regs, ops = prob
    regs = regs.split("\n")
    A = int(regs[0].split(": ")[1])
    B = int(regs[1].split(": ")[1])
    C = int(regs[2].split(": ")[1])
    regs = [A, B, C]
    ops = ops.split(": ")[1]
    ops = list(map(int, ops.split(",")))
    outp = []

    i = 0
    a_min = A
    a = a_min
    o_regs = regs.copy()
    for a in range(a_min, 10**12):
        outp = []
        regs = o_regs
        regs[0] = a
        execute(i, ops, regs, outp)
        if outp == ops:
            break

    return a


print(solve(inp_p2), 117440)
print(solve(inp))
