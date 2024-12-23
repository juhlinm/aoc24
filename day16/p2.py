inp = open("day16/inp.txt", "r").readlines()
inp_11048 = open("day16/inp_11048.txt", "r").readlines()
inp_7036 = open("day16/inp_7036.txt", "r").readlines()
# inp_21148 = open("day16/inp_21148.txt", "r").readlines()
# inp_4013 = open("day16/inp_4013.txt", "r").readlines()
# inp_5078 = open("day16/inp_5078.txt", "r").readlines()


# def get_paths(unexplored, explore):
#     paths = []
#     for dir, diff in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
#         n_pos = (explore[0] + diff[0], explore[1] + diff[1])
#         if n_pos in unexplored:
#             paths.append((n_pos, dir))
#     return paths


# def minimum(unexplored):
#     min_key = list(unexplored.keys())[0]
#     for i in list(unexplored.keys())[1:]:
#         if unexplored[i][0] < unexplored[min_key][0]:
#             min_key = i
#     return min_key


# def djikstras(unexplored, start, end, start_dir):
#     unexplored[start] = (0, start_dir)
#     visited = {}
#     while len(unexplored) != 0:
#         explore = minimum(unexplored)
#         if explore == end:
#             break
#         else:
#             dir = unexplored[explore][1]
#             for path, n_dir in get_paths(unexplored, explore):
#                 s = 1
#                 if abs(dir - n_dir) in [1, 3]:
#                     s += 1000
#                 if abs(dir - n_dir) == 2:
#                     s += 2000
#                 time = unexplored[explore][0] + s
#                 if time < unexplored[path][0]:
#                     unexplored[path] = (time, n_dir)
#         visited[explore] = unexplored[explore]
#         del unexplored[explore]

#     visited[explore] = unexplored[explore]
#     return visited


def get_path(unexplored, explore):
    pos, dir = explore
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    n_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
    if (n_pos, dir) in unexplored:
        return n_pos
    else:
        return None


def minimum(unexplored):
    min_key = list(unexplored.keys())[0]
    for i in list(unexplored.keys())[1:]:
        if unexplored[i] < unexplored[min_key]:
            min_key = i
    return min_key


def djikstras(unexplored, start, end, start_dir):
    unexplored[(start, start_dir)] = 0
    visited = {}
    while len(unexplored) != 0:
        explore = minimum(unexplored)
        if explore[0] == end:
            break
        else:
            n_pos = get_path(unexplored, explore)
            if n_pos:
                n_dir = explore[1]
                s = 1
            else:
                n_pos = explore[0]
                n_dir = (explore[1] + 1) % 4
                s = 1000
            path = (n_pos, n_dir)
            if path not in unexplored:
                continue

            time = unexplored[explore] + s
            if time < unexplored[path]:
                unexplored[path] = time
        visited[explore] = unexplored[explore]
        del unexplored[explore]

    visited[explore] = unexplored[explore]
    return visited


def solve(prob):
    unexplored = {}
    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "E":
                end = (x, y)
            if c != "#":
                # unexplored[(x, y)] = (float("inf"), -1)
                for dir in range(4):
                    unexplored[((x, y), dir)] = float("inf")

    u_1 = unexplored.copy()
    from_start = djikstras(u_1, start, end, 1)
    cost = from_start[end][0]

    from_end = []
    for dir in [0, 1, 2, 3]:
        u = unexplored.copy()
        from_end.append(djikstras(u, end, start, dir))

    s = 0
    # for pos in from_start.keys():
    #     for f_e in from_end:
    #         if pos in f_e:
    #             cost_correct = from_start[pos][0] + f_e[pos][0] == cost
    #             dir_correct = (from_start[pos][1] + 2) % 4 == f_e[pos][1]
    #             s += cost_correct and dir_correct

    return s


print(solve(inp_7036), 45)
print(solve(inp_11048), 64)
# print(solve(inp_21148), 149)
# print(solve(inp_4013), 14)
# print(solve(inp_5078), 413)
# print(solve(inp))
