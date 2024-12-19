import re

inp_test = open("day19/inp_test.txt", "r").read().split("\n\n")
inp = open("day19/inp.txt", "r").read().split("\n\n")


def get_idxs(towel, pattern):
    matches = re.finditer(towel, pattern)
    return [match.start() for match in matches]


def sorter(towel):
    s = 0
    # if "w" in towel:
    #     s += 1
    # s += len(towel)
    return s


# def viable(fills, max, i=0):
#     if i == max:
#         return True

#     a = [x for x in fills if x[0] == i]
#     ret = False
#     for k in a:
#         if viable(fills, max, k[1] + 1):
#             ret = True
#     return ret


def viable(tuples_list, end):
    from collections import defaultdict

    start = 0

    # Build a graph from the tuples
    graph = defaultdict(list)
    for a, b in tuples_list:
        for k in range(a, b + 1):
            graph[k].append(k + 1)

    # Perform DFS to find a valid path
    visited = set()

    def dfs(node):
        if node in visited:
            return False
        visited.add(node)
        if node == end:
            return True
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        visited.remove(node)  # Backtrack
        return False

    # Ensure all numbers in the range are visited
    if dfs(start):
        return set(range(start, end + 1)).issubset(visited)
    return False


def solve(prob):
    towels, patterns = prob
    towels = sorted([x.strip() for x in towels.split(",")], key=lambda x: sorter(x), reverse=True)
    patterns = [x.strip() for x in patterns.split("\n")]

    # tows = {}
    # max_len = len(towels[0])
    # for l in range(max_len, 0):
    #     tows[l] = [len(tow) == l for tow in towels]

    s = 0
    for kk, pattern in enumerate(patterns):
        print(kk / len(patterns))
        # o_pattern = pattern
        # used_towels = []
        # fills2 = {towel: [] for towel in towels}
        # fills = set()
        fills3 = []
        for towel in towels:
            idxs = get_idxs(towel, pattern)
            for idx in idxs:
                # fills.add(idx)
                # for k in range(len(towel)):
                #     fills.add(idx + k)
                # fills2[towel].append((idx, idx + len(towel) - 1))
                fills3.append((idx, idx + len(towel) - 1))

        # print(fills)
        # print(fills2)
        # print(len(pattern))
        # fills3 = v for v in fills2.values()]
        # print(fills3)
        print(pattern)
        if viable(fills3, len(pattern)):
            # print(fills)
            # print({k: v for k, v in fills2.items() if len(v)})
            # print(len(pattern))
            # print(pattern)
            # print("----")
            s += 1
        else:
            # print(o_pattern)
            # print(pattern)
            # print(used_towels)
            pass
        # print(pattern)
        # print("----")
    return s


print(solve(inp_test), 6)
print(solve(inp))
