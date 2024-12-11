import sys

sys.setrecursionlimit(10**6)

seven = open("day11/seven.txt", "r").read().strip().split()
twentytwo = open("day11/twentytwo.txt", "r").read().strip().split()
inp = open("day11/inp.txt", "r").read().strip().split()


def rool(inp):
    if inp == "0":
        return ["1"]
    elif len(inp) % 2 == 0:
        half = int(len(inp) / 2)
        return [inp[:half], inp[half:].lstrip("0") or "0"]
    else:
        return [str(int(inp) * 2024)]


def solve(prob, iter):
    for i in range(iter):
        o_prob = prob.copy()
        prob = []
        for x in o_prob:
            prob.extend(rool(x))
    return len(prob)


print(solve(seven, 1))
print(solve(twentytwo, 6))
print(solve(twentytwo, 25))
print(solve(inp, 25))
