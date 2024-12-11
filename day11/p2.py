import sys
from functools import cache

sys.setrecursionlimit(10**6)

seven = list(map(int, open("day11/seven.txt", "r").read().strip().split()))
twentytwo = list(map(int, open("day11/twentytwo.txt", "r").read().strip().split()))
inp = list(map(int, open("day11/inp.txt", "r").read().strip().split()))


def split_integer(num, c):
    return int(str(num)[: c // 2]), int(str(num)[c // 2 :])


    

@cache
def rool(inp, max_depth, depth = 0):
    if depth == max_depth:

        return 1
    n_depth = depth + 1
    if inp == 0:
        return rool(1, max_depth, n_depth)
    else:
        c = len(str(inp))
        if c % 2 == 0:
            x, y = split_integer(inp, c)
            return rool(x, max_depth, n_depth) + rool(y, max_depth, n_depth)
        return rool(inp * 2024, max_depth, n_depth)



def solve(prob, iter):
    return sum(rool(x, iter) for x in prob)


print(solve(seven, 1), 7)
print(solve(twentytwo, 6), 22)
print(solve(twentytwo, 25), 55312)
print(solve(inp, 75))
