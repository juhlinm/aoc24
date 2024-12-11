import sys

sys.setrecursionlimit(10**6)

seven = list(map(int, open("day11/seven.txt", "r").read().strip().split()))
twentytwo = list(map(int, open("day11/twentytwo.txt", "r").read().strip().split()))
inp = list(map(int, open("day11/inp.txt", "r").read().strip().split()))


def split_integer(num, c):
    return int(str(num)[: c // 2]), int(str(num)[c // 2 :])


def rool(inp):
    if inp == 0:
        return [1]
    else:
        c = len(str(inp))
        if c % 2 == 0:
            x, y = split_integer(inp, c)
            return [x, y]
        else:
            return [inp * 2024]


def solve(prob, iter):
    trans = {}
    for i in range(iter):
        o_prob = prob.copy()
        prob = []
        for x in o_prob:
            if x in trans:
                prob.extend(trans[x])
            else:
                r = rool(x)
                trans[x] = r
                prob.extend(r)
    return len(prob)


print(solve(seven, 1), 7)
print(solve(twentytwo, 6), 22)
print(solve(twentytwo, 25), 55312)
print(solve(inp, 75))
