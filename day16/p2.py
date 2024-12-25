inp = open("day16/inp.txt", "r").readlines()
inp_11048 = open("day16/inp_11048.txt", "r").readlines()
inp_7036 = open("day16/inp_7036.txt", "r").readlines()
inp_62 = open("day16/inp_62.txt", "r").readlines()
inp_21148 = open("day16/inp_21148.txt", "r").readlines()
inp_4013 = open("day16/inp_4013.txt", "r").readlines()
inp_5078 = open("day16/inp_5078.txt", "r").readlines()
inp_264 = open("day16/inp_264.txt", "r").readlines()
inp_514 = open("day16/inp_514.txt", "r").readlines()
inp_x = open("day16/inp_x.txt", "r").readlines()

DELTAS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_path(unexplored, explore):
    pos, dir = explore
    n_pos = (pos[0] + DELTAS[dir][0], pos[1] + DELTAS[dir][1])
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


def p_sum(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])


def djikstras(unexplored, start, end, start_dir):

    if start_dir == -1:
        unexplored[(start, 0)] = 0
        unexplored[(start, 1)] = 0
        unexplored[(start, 2)] = 0
        unexplored[(start, 3)] = 0
    else:
        unexplored[(start, start_dir)] = 0
        unexplored[(start, (start_dir + 1) % 4)] = 1000
        unexplored[(start, (start_dir + 3) % 4)] = 1000
        unexplored[(start, (start_dir + 2) % 4)] = 2000
    visited = {}
    kpp = 0
    while len(unexplored) != 0:
        kpp += 1
        if kpp % 2500 == 0:
            print(len(unexplored))
        explore = minimum(unexplored)
        if explore[0] == end:
            break
        else:
            n_pos = get_path(unexplored, explore)
            if n_pos:
                dir = explore[1]
                s = 1
            else:
                visited[explore] = unexplored[explore]
                del unexplored[explore]
                continue

            path = (n_pos, dir)
            time = unexplored[explore] + s
            if time < unexplored[path]:
                unexplored[path] = time
                right = (dir + 1) % 4
                left = (dir + 3) % 4
                right_path = (p_sum(n_pos, DELTAS[right]), right)
                left_path = (p_sum(n_pos, DELTAS[left]), left)
                if right_path in unexplored:
                    unexplored[(n_pos, right)] = time + 1000
                else:
                    if (n_pos, right) in unexplored:
                        del unexplored[(n_pos, right)]
                if left_path in unexplored:
                    unexplored[(n_pos, left)] = time + 1000
                else:
                    if (n_pos, left) in unexplored:
                        del unexplored[(n_pos, left)]

        visited[explore] = unexplored[explore]
        del unexplored[explore]

    visited[explore] = unexplored[explore]
    return visited


def solve(prob):
    unexplored = {}
    for y, line in enumerate(prob):
        for x, c in enumerate(line.strip()):
            if c == "S":
                start = (x, y)
            if c == "E":
                end = (x, y)
            if c != "#":
                for dir in range(4):
                    unexplored[((x, y), dir)] = float("inf")

    u_1 = unexplored.copy()
    from_start = djikstras(u_1, start, end, 1)
    costs = [from_start[(end, i)] for i in range(4) if (end, i) in from_start]
    cost = min(costs)

    u = unexplored.copy()
    from_end = djikstras(u, end, start, -1)

    poses = set()
    for pos in from_start.keys():
        rev_pos = (pos[0], (pos[1] + 2) % 4)

        if rev_pos in from_end:
            if from_start[pos] + from_end[rev_pos] == cost:
                poses.add(pos[0])
    return len(poses)


print(solve(inp_7036), 45)
print(solve(inp_11048), 64)
print(solve(inp_62), 62)
print(solve(inp_21148), 149)
print(solve(inp_4013), 14)
print(solve(inp_5078), 413)
print(solve(inp_264), 264)
print(solve(inp_514), 514)
print(solve(inp_x), 14)
print(solve(inp))
