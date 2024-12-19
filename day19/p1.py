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


def solve(prob):
    towels, patterns = prob
    towels = sorted([x.strip() for x in towels.split(",")], key=lambda x: sorter(x), reverse=True)
    patterns = [x.strip() for x in patterns.split("\n")]

    # tows = {}
    # max_len = len(towels[0])
    # for l in range(max_len, 0):
    #     tows[l] = [len(tow) == l for tow in towels]

    s = 0
    for pattern in patterns:
        o_pattern = pattern
        # used_towels = []
        fills2 = {towel: [] for towel in towels}
        fills = set()
        for towel in towels:
            idxs = get_idxs(towel, pattern)
            for idx in idxs:
                fills.add(idx)
                for k in range(len(towel)):
                    fills.add(idx + k)
                fills2[towel].append((idx, idx + len(towel) - 1))

        # print(fills)
        # print(fills2)
        # print(len(pattern))
        if all(i in fills for i in range(len(pattern))):
            print(fills)
            print({k: v for k, v in fills2.items() if len(v)})
            print(len(pattern))
            print(pattern)
            print("----")
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
