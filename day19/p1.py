import re
from collections import defaultdict

inp_test = open("day19/inp_test.txt", "r").read().split("\n\n")
inp = open("day19/inp.txt", "r").read().split("\n\n")

def get_idxs(towel, pattern):
    matches = re.finditer(towel, pattern)
    return [match.start() for match in matches]

def find_path_dfs(graph, start, end):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current == end:
            return True

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return False

def viable(tuples_list, end):
    graph = defaultdict(set)
    for a, b in tuples_list:
        graph[a].add(b)
    return find_path_dfs(graph, 0, end)


def solve(prob):
    towels, patterns = prob
    towels = [x.strip() for x in towels.split(",")]
    patterns = [x.strip() for x in patterns.split("\n")]

    s = 0
    for pattern in patterns:
        fills = []
        for towel in towels:
            idxs = get_idxs(towel, pattern)
            for idx in idxs:
                fills.append((idx, idx + len(towel)))
        s += viable(fills, len(pattern) - 1)
    return s

print(solve(inp_test), 6)
print(solve(inp))
