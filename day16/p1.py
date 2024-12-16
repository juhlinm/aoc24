inp = open("day16/inp.txt", "r").readlines()
inp_11048 = open("day16/inp_11048.txt", "r").readlines()
inp_7036 = open("day16/inp_7036.txt", "r").readlines()


def find_path(walls, end, walked, rotated, pos, dir):
    if pos == end:
        return walked, rotated, True

    if dir == 1:
        n_x = pos[0] + 1
        n_y = pos[1]
    elif dir == 2:
        n_x = pos[0]
        n_y = pos[1] + 1
    elif dir == 3:
        n_x = pos[0] - 1
        n_y = pos[1]
    elif dir == 0:
        n_x = pos[0]
        n_y = pos[1] - 1

    n_pos = (n_x, n_y)
    t1 = (pos, (dir, (dir + 1) % 4))
    t2 = (pos, (dir, (dir + 2) % 4))
    t3 = (pos, (dir, (dir - 1) % 4))

    if n_pos in walls:
        if pos == (3, 9):
            apa = 1
        for t in [t1, t2, t3]:
            if (t, False) not in rotated:
                n_dir = t[1][1]
                print(dir, n_dir)
                walked, rotated, found = find_path(walls, end, walked, rotated, pos, n_dir)
                if found:
                    return walked, rotated, found
                else:
                    rotated.append(t, False)
                    return walked, rotated, False
    else:
        walked.append((pos, n_pos))
        print((pos, n_pos))
        return find_path(walls, end, walked, rotated, n_pos, dir)


def solve(prob):
    walked = []
    rotated = []
    walls = []
    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "#":
                walls.append((x, y))
            if c == "E":
                end = (x, y)

    dir = 1
    pos = start
    walked, rotated, _ = find_path(walls, end, walked, rotated, pos, dir)
    return 1000 * len(rotated) + len(walked)


print(solve(inp_7036), 7036)
# print(solve(inp_11048), 11048)
# print(solve(inp))
