from itertools import permutations
from functools import cache

inp = [x.strip() for x in open("day21/inp.txt", "r").readlines()]

dirs = {0: (1, 0), 4: (2, 0), 3: (0, 1), 2: (1, 1), 1: (2, 1)}
rets = [(0, -1), (1, 0), (0, 1), (-1, 0)]
num_to_ret = ["^", ">", "v", "<", "A"]
num_to_score = [3, 1, 2, 4]


def numer(line):
    return int(line[:3].lstrip("0"))


@cache
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


@cache
def is_disallowed(a, moves, disallow):
    pos = a
    for move in moves:
        pos = sum_pos(pos, rets[move])
        if pos == disallow:
            return True
    return False


@cache
def walk_manhattan(a, b, disallow=(0, 0)):
    x = b[0] - a[0]
    y = b[1] - a[1]

    moves = []
    if x < 0:
        moves.extend([3] * abs(x))
    elif x > 0:
        moves.extend([1] * x)
    if y < 0:
        moves.extend([0] * abs(y))
    elif y > 0:
        moves.extend([2] * y)

    if not moves:
        return (4,)

    max_score = -1e6
    best_perm = tuple()
    for perm in permutations(moves):
        score = 0

        if is_disallowed(a, perm, disallow):
            score -= 1000
        for p in range(len(perm) - 1):
            if perm[p] == perm[p + 1]:
                score += 2
            if num_to_score[perm[p]] > num_to_score[perm[p + 1]]:
                score += 1

        if score > max_score:
            max_score = score
            best_perm = perm

    return best_perm + (4,)


@cache
def sum_pos(a, b):
    return (a[0] + b[0], a[1] + b[1])


def pad_to_dir(inp):
    inp = "A" + inp
    ret = tuple()
    pad = {
        "7": (0, 0),
        "8": (1, 0),
        "9": (2, 0),
        "4": (0, 1),
        "5": (1, 1),
        "6": (2, 1),
        "1": (0, 2),
        "2": (1, 2),
        "3": (2, 2),
        "0": (1, 3),
        "A": (2, 3),
    }
    for i in range(len(inp) - 1):
        ret = ret + walk_manhattan(pad[inp[i]], pad[inp[i + 1]], (0, 3))
    return ret


@cache
def dir_to_dir(dir, max_d, cur_d=0):
    s = 0
    dir = (4,) + dir

    if cur_d == max_d:
        if dir == (4,):
            return 0
        return (
            sum(
                [manhattan(dirs[dir[k]], dirs[dir[k + 1]]) for k in range(len(dir) - 1)]
            )
            + len(dir)
            - 1
        )

    for i in range(len(dir) - 1):
        walk = walk_manhattan(dirs[dir[i]], dirs[dir[i + 1]])
        s += dir_to_dir(walk, max_d, cur_d + 1)
    return s


def length(inp):
    return dir_to_dir(pad_to_dir(inp), 24)


def solve(prob):
    return sum(length(line) * numer(line) for line in prob)


print(solve(inp))
