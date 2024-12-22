from functools import cache

inp_test = open("day19/inp_test.txt", "r").read().split("\n\n")
inp_6 = open("day19/inp_6.txt", "r").read().split("\n\n")
inp = open("day19/inp.txt", "r").read().split("\n\n")


def solve(prob):
    towels, patterns = prob
    towels = [x.strip() for x in towels.split(",")]
    patterns = [x.strip() for x in patterns.split("\n")]

    @cache
    def count_builds(pattern):
        if len(pattern) == 0:
            return 1

        return sum(
            count_builds(pattern.removeprefix(p))
            for p in towels
            if pattern.startswith(p)
        )

    return sum(list(map(count_builds, patterns)))


print(solve(inp_test), 16)
print(solve(inp_6), 6)
print(solve(inp))
