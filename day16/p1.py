inp = open("day16/inp.txt", "r").readlines()
inp_11048 = open("day16/inp_11048.txt", "r").readlines()
inp_7036 = open("day16/inp_7036.txt", "r").readlines()
inp_21148 = open("day16/inp_21148.txt", "r").readlines()
inp_4013 = open("day16/inp_4013.txt", "r").readlines()
inp_5078 = open("day16/inp_5078.txt", "r").readlines()


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


def solve(prob):
    walls = []
    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "#":
                walls.append((x, y))
            if c == "E":
                end = (x, y)
    y_max = y + 1
    x_max = x + 1

    unexplored = {}
    for y in range(y_max):
        for x in range(x_max):
            if (x, y) not in walls:
                unexplored[(x, y)] = (float("inf"), -1)

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
                    unexplored[path] = (time, n_dir)
        del unexplored[explore]

    return unexplored[explore][0]


print(solve(inp_7036), 7036)
print(solve(inp_11048), 11048)
print(solve(inp_21148), 21148)
print(solve(inp_4013), 4019)
print(solve(inp_5078), 5078)
print(solve(inp))
