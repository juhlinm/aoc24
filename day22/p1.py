from functools import cache
from sys import setrecursionlimit

setrecursionlimit(4000)

inp = [x.strip() for x in open("day22/inp.txt", "r").readlines()]
inp_test = [x.strip() for x in open("day22/inp_test.txt", "r").readlines()]

MOD = 16777216


@cache
def secret(inp, max_d, d=0):
    if d == max_d:
        return inp

    A = ((inp * 64) ^ inp) % MOD
    A = ((A // 32) ^ A) % MOD
    A = ((A * 2048) ^ A) % MOD
    return secret(A, max_d, d + 1)


def solve(prob):
    return sum([secret(int(line), 2000) for line in prob])


print(solve(inp_test), 37327623)
print(solve(inp))
