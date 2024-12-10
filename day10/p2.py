import sys

sys.setrecursionlimit(10**6)

twotwoseven = list(map(lambda x: x.strip(), open("day10/twop2.txt", "r").readlines()))
three = list(map(lambda x: x.strip(), open("day10/threep2.txt", "r").readlines()))
thirteen = list(map(lambda x: x.strip(), open("day10/four.txt", "r").readlines()))
eightyone = list(map(lambda x: x.strip(), open("day10/threesix.txt", "r").readlines()))
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


def paths(a, nums, ls, num):
    n_poses = []
    for n_pos in nums:
        if is_next(a, n_pos) and (n_pos, num) not in ls:
            n_poses.append((a, n_pos))
    if len(n_poses) > 1:
        return n_poses
    else:
        return None


def walk(pos, ls, nums, pcs, num):
    ppcs = [pc[0] for pc in pcs]
    for n_pos in nums:
        if is_next(pos, n_pos) and (pos, n_pos) not in ppcs:
            _paths = paths(pos, nums, ls, num)
            if _paths:
                pcs.extend([(p[0], p[1], num) for p in _paths])
                print([(p[0], p[1], p[2] - 1) for p in pcs])
            ls.append((n_pos, num))
            return n_pos, ls, pcs
    return pos, ls, pcs


def solve(prob):
    ress = 0
    nums = {}
    for i in range(10):
        nums[i] = find_num(prob, i)

    for x0 in range(len(nums[0])):
        res = []
        ls = []
        pcs = []
        o_ls = [(-1, -1)]
        pos = nums[0][x0]
        i = 1
        while ls != o_ls or len(pcs):
            o_pos = [(-1, -1)]
            while pos != o_pos and i < 10:
                o_pos = pos
                o_ls = ls.copy()
                pos, ls, pcs = walk(pos, ls, nums[i], pcs, i)
                if i == 9 and pos != o_pos:
                    res.append(pos)
                i += 1
            if len(pcs):
                pos, _, i = pcs.pop()
                # print([(p[0][0], p[0][1] - 1) for p in pcs])
            else:
                break
        ress += len(res) - 1
    return ress


# assert solve(three) == 3


print(solve(thirteen))



# assert solve(thirteen) == 13
# assert solve(eightyone) == 81
# assert solve(twotwoseven) == 227
# print(solve(inp))
