import heapq as hq

inp_test = open("day20/inp_test.txt", "r").readlines()
inp = open("day20/inp.txt", "r").readlines()


def get_paths(unexplored, explore):
    paths = []
    for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        if (explore[0] + x, explore[1] + y) in unexplored:
            paths.append((explore[0] + x, explore[1] + y))
    return paths


def minimum(unexplored):
    min_key = list(unexplored.keys())[0]
    for i in list(unexplored.keys())[1:]:
        if unexplored[i] < unexplored[min_key]:
            min_key = i
    return min_key


def get_nearby_cheats(pos, o_path):
    nearby = []
    cheat_l = 20
    pos_top = pos[1]-cheat_l
    pos_bottom = pos[1]+cheat_l
    pos_left = pos[0]-cheat_l
    pos_right = pos[0]+cheat_l
    for i, y in enumerate(range(pos_top, pos_bottom + 1)):
        offset = cheat_l-i if i<=cheat_l else i-cheat_l
        for x in range(pos_left + offset, pos_right + 1 - offset):
            end_cheat = (x,y)
            if end_cheat in o_path and o_path.index(end_cheat) > o_path.index(pos):
                nearby.append((x,y))
    return nearby

def find_len(track, start, end, max_y, max_x, visit=False):
    distances = {}
    heap = [(0, start)]

    unexplored = {}
    for y in range(max_y):
        for x in range(max_x):
            if track[(x, y)] == 0:
                unexplored[(x, y)] = float("inf")
    if visit:
        visited = []

    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue
        if visit:
            visited.append(node)
        distances[node] = dist
        for path in get_paths(unexplored, node):
            if path not in distances:
                hq.heappush(heap, (dist + 1, path))
    if visit:
        return distances[end], visited
    return distances[end]

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_cheats(prob):
    track = {}

    y_max = len(prob)
    x_max = len(prob[0])

    for a in range(-30, y_max + 30):
        for b in range(-30, x_max + 30):
            track[(a, b)] = -1

    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "E":
                end = (x, y)
            if c != "#":
                track[(x, y)] = 0
            else:
                track[(x, y)] = 1
    o_length, o_path = find_len(track, start, end, y_max, x_max, visit=True)
    cheats = []

    dists = {}
    for i, pos in enumerate(o_path):
        dists[pos] = o_length - i

    for i, pos in enumerate(o_path):
        print(i / len(o_path))
        nearby_cheats = get_nearby_cheats(pos, o_path)
        for cheat in nearby_cheats:
            cheat_length = dists[pos] - dists[cheat] - manhattan(pos, cheat)
            cheats.append(cheat_length)
    return cheats


def solve(prob, lim = 100):
    cheats = find_cheats(prob)
    return sum([c >= lim for c in cheats])

print(solve(inp_test, 50), 285)
print(solve(inp))
