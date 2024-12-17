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
    return (regs[0] // (2**c),) + regs[1:]


def bxl(regs, comb):
    return (regs[0],) + (regs[1] ^ comb,) + (regs[2],)


def bst(regs, comb):
    c = get_comb(regs, comb)
    return (regs[0],) + (c % 8,) + (regs[2],)


def jnz(regs, comb):
    if regs[0] == 0:
        return None
    return comb


def bxc(regs, comb):
    return (regs[0],) + (regs[1] ^ regs[2],) + (regs[2],)


def out(regs, comb, outp):
    c = get_comb(regs, comb)
    return outp + (c % 8,)


def bdv(regs, comb):
    c = get_comb(regs, comb)
    return (regs[0],) + (regs[0] // (2**c),) + (regs[2],)


def cdv(regs, comb):
    c = get_comb(regs, comb)
    return regs[:-1] + (regs[0] // (2**c),)


# @cache
def execute(i_0, ops, regs, outp):
    for i in range(i_0 + 1, len(ops), 2):
        op = ops[i - 1]
        comb = ops[i]

        if op == 0:
            regs = adv(regs, comb)
        elif op == 1:
            regs = bxl(regs, comb)
        elif op == 2:
            regs = bst(regs, comb)
        elif op == 3:
            i = jnz(regs, comb)
            if i is not None:
                outp = execute(i, ops, regs, outp)
        elif op == 4:
            regs = bxc(regs, comb)
        elif op == 5:
            outp = out(regs, comb, outp)
        elif op == 6:
            regs = bdv(regs, comb)
        elif op == 7:
            regs = cdv(regs, comb)
    return outp


def test(x):
    outp = []
    while x != 0:
        outp.append(((x // 2) ^ 7) % 8)
        x = x // 8
    return outp


def solve(prob):
    regs, ops = prob
    regs = regs.split("\n")
    A = int(regs[0].split(": ")[1])
    B = int(regs[1].split(": ")[1])
    C = int(regs[2].split(": ")[1])
    regs = tuple([A, B, C])
    ops = ops.split(": ")[1]
    ops = tuple(map(int, ops.split(",")))

    a_min = A
    a = a_min
    o_regs = regs
    print(a_min)
    for a in range(a_min, 10**30):
        outp = tuple()
        regs = o_regs
        regs = (a,) + regs[1:]
        if a % 10**6 == 0:
            print(a)
        outp = test(a)

        # i = 0
        # outp = execute(i, ops, regs, outp)
        if outp == ops:
            break

    return a


# print(solve(inp_p2), 117440)
print(solve(inp))
