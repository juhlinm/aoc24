import sys

sys.setrecursionlimit(10**6)

two = list(map(lambda x: x.strip(), open("day10/two.txt", "r").readlines()))
three = list(map(lambda x: x.strip(), open("day10/three.txt", "r").readlines()))
four = list(map(lambda x: x.strip(), open("day10/four.txt", "r").readlines()))
threesix = list(map(lambda x: x.strip(), open("day10/threesix.txt", "r").readlines()))
inp = list(map(lambda x: x.strip(), open("day10/inp.txt", "r").readlines()))


def find_num(lines, num):
    xs = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == str(num):
                xs.append((x, y))
    return xs


def is_next(a, b):
    return (abs(a[0] - b[0]) == 1 and a[1] == b[1]) or (abs(a[1] - b[1]) == 1 and a[0] == b[0])


def paths(a, nums, ls):
    cnt = 0
    for n in nums:
        if is_next(a, n) and n not in ls:
            cnt += 1
    if cnt > 1:
        return a
    else:
        return None


def walk(pos, ls, nums, pcs, num):
    for n_pos in nums:
        if is_next(pos, n_pos) and n_pos not in ls:
            p = paths(pos, nums, ls)
            if p:
                pcs.append((p, num))
            ls.append(n_pos)
            break
    return n_pos, ls, pcs


def solve(prob):
    res = 0
    nums = {}
    for i in range(10):
        nums[i] = find_num(prob, i)

    for x0 in range(len(nums[0])):
        ls = []
        pcs = []
        o_ls = [(-1, -1)]
        pos = nums[0][x0]
        i = 1
        while ls != o_ls:
            o_pos = [(-1, -1)]
            while pos != o_pos and i < 10:
                o_pos = pos
                o_ls = ls.copy()
                pos, ls, pcs = walk(pos, ls, nums[i], pcs, i)
                if i == 9 and pos != o_pos:
                    res += 1
                i += 1
            if len(pcs):
                print(ls)
                print(pcs)
                print("--------------")
                pos, i = pcs.pop()
            else:
                break
    return res


assert solve(two) == 2
assert solve(three) == 3
print(solve(four))
# print(solve(threesix) == 36)
# print(solve(inp))
