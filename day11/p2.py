import sys

from line_profiler import profile

sys.setrecursionlimit(10**6)

seven = list(map(int, open("day11/seven.txt", "r").read().strip().split()))
twentytwo = list(map(int, open("day11/twentytwo.txt", "r").read().strip().split()))
inp = list(map(int, open("day11/inp.txt", "r").read().strip().split()))


def count_digits(num):
    if num == 0:
        return 1

    c = 0
    while num > 0:
        num //= 10
        c += 1

    return c


def split_integer(num, c):
    if num == 0:
        return 0, 0

    pwr = 10 ** (c // 2)
    x = num // pwr
    y = num % pwr

    return x, y


@profile
def rool(inp):
    if inp == 0:
        return [1]
    else:
        s = count_digits(inp)
        if s % 2 == 0:
            x, y = split_integer(inp, s)
            return [x, y]
        else:
            return [inp * 2024]


def solve(prob, iter):
    for i in range(iter):
        # print(i)
        o_prob = prob.copy()
        prob = []
        for x in o_prob:
            prob.extend(rool(x))
        # print(prob)
    return len(prob)


print(solve(seven, 1))
print(solve(twentytwo, 6))
print(solve(twentytwo, 25))
# print(solve(inp, 75))
