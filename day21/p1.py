from itertools import permutations

inp_test = [x.strip() for x in open("day21/inp_test.txt", "r").readlines()]
inp = [x.strip() for x in open("day21/inp.txt", "r").readlines()]

dir = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}
rets = [(0, -1), (1, 0), (0, 1), (-1, 0)]
num_to_ret = ["^", ">", "v", "<"]
num_to_score = [3, 1, 2, 4]


def numer(line):
    return int(line[:3].lstrip("0"))


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_disallowed(a, moves, disallow):
    pos = a
    for move in moves:
        pos = sum_pos(pos, rets[move])
        if pos == disallow:
            return True
    return False


def walk_manhattan(a, b, prev_end, disallow=(0, 0)):
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
        return ""

    prev_end = int(prev_end[-1]) if len(prev_end) else None

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

    return "".join([str(i) for i in best_perm])


def sum_pos(a, b):
    return (a[0] + b[0], a[1] + b[1])


def num_to_dir_str(num):
    return "".join([num_to_ret[int(i)] for i in num]) + "A"


def pad_to_dir(inp):
    ret = ""
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
    inp = "A" + inp
    prev_walk = ""
    for i in range(len(inp) - 1):
        walk = walk_manhattan(pad[inp[i]], pad[inp[i + 1]], prev_walk, (0, 3))
        ret += num_to_dir_str(walk)
        prev_walk = walk
    return ret


def dir_to_dir(inp):
    ret = ""
    inp = "A" + inp
    prev_walk = ""
    for i in range(len(inp) - 1):
        walk = walk_manhattan(dir[inp[i]], dir[inp[i + 1]], prev_walk)
        ret += num_to_dir_str(walk)
        prev_walk = walk
    return ret


def dir_to_length(inp):
    ret = ""
    inp = "A" + inp
    for i in range(len(inp) - 1):
        walk = walk_manhattan(dir[inp[i]], dir[inp[i + 1]], "5")
        ret += num_to_dir_str(walk)
    return len(ret)


def length(inp):
    return dir_to_length(dir_to_dir(pad_to_dir(inp)))


def solve(prob):
    return sum(length(line) * numer(line) for line in prob)


print(solve(inp_test), 126384)
print(solve(inp))
