inp = open("day16/inp.txt", "r").readlines()
inp_11048 = open("day16/inp_11048.txt", "r").readlines()
inp_7036 = open("day16/inp_7036.txt", "r").readlines()
# inp_21148 = open("day16/inp_21148.txt", "r").readlines()
# inp_4013 = open("day16/inp_4013.txt", "r").readlines()
# inp_5078 = open("day16/inp_5078.txt", "r").readlines()


def get_paths(unexplored, explore):
    paths = []
    for dir, diff in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
        n_pos = (explore[0] + diff[0], explore[1] + diff[1])
        if n_pos in unexplored:
            paths.append((n_pos, dir))
    return paths


def minimum(unexplored):
    min_key = list(unexplored.keys())[0]
    for i in list(unexplored.keys())[1:]:
        if unexplored[i][0] < unexplored[min_key][0]:
            min_key = i
    return min_key


def djikstras(unexplored, start, end):
    unexplored[start] = (0, 1)
    while len(unexplored) != 0:
        explore = minimum(unexplored)
        if explore == end:
            break
        else:
            dir = unexplored[explore][1]
            for path, n_dir in get_paths(unexplored, explore):
                s = 1
                if abs(dir - n_dir) in [1, 3]:
                    s += 1000
                time = unexplored[explore][0] + s
                if time < unexplored[path][0]:
                    unexplored[path][0] = (time, n_dir)
        del unexplored[explore]

    return unexplored[explore][0]


def solve(prob):
    unexplored = {}
    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "E":
                end = (x, y)
            if c != "#":
                unexplored[(x, y)] = (float("inf"), -1)

    u_1 = unexplored.copy()
    o_len = djikstras(u_1, start, end)
    # Use information gained

    return len(poses)


print(solve(inp_7036), 45)
print(solve(inp_11048), 64)
# print(solve(inp_21148), 149)
# print(solve(inp_4013), 14)
# print(solve(inp_5078), 413)
# print(solve(inp))
