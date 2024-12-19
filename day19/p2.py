import re
from collections import defaultdict
from functools import cache

inp_test = open("day19/inp_test.txt", "r").read().split("\n\n")
inp = open("day19/inp.txt", "r").read().split("\n\n")

def get_idxs(towel, pattern):
    matches = re.finditer(towel, pattern)
    return [match.start() for match in matches]


def viable(tuples_list, end):
    graph = defaultdict(set)
    for a, b in tuples_list:
        graph[a].add(b)
    return 0


def solve(prob):
    towels, patterns = prob
    towels = [x.strip() for x in towels.split(",")]
    patterns = [x.strip() for x in patterns.split("\n")]

    s = 0
    for pattern in patterns:
        print(pattern)
        fills = []
        for towel in towels:
            idxs = get_idxs(towel, pattern)
            for idx in idxs:
                fills.append((idx, idx + len(towel)))
        s += viable(fills, len(pattern))
    return s

print(solve(inp_test), 16)
print(solve(inp), 752461716635602) # prob right
