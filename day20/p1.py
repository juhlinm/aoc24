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


def is_valid_wall(p, map):
    if map[p] in [0, -1]:
        return False
    return (map[(p[0] + 1, p[1])] == 0 and map[(p[0] - 1, p[1])] == 0) or (
        map[(p[0], p[1] + 1)] == 0 and map[(p[0], p[1] - 1)] == 0
    )

def find_len(track, start, end, max_y, max_x):
    distances = {}
    heap = [(0, start)]

    unexplored = {}
    for y in range(max_y):
        for x in range(max_x):
            if track[(x, y)] == 0:
                unexplored[(x, y)] = float("inf")

    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue
        distances[node] = dist
        for path in get_paths(unexplored, node):
            if path not in distances:
                hq.heappush(heap, (dist + 1, path))

    return distances[end]

def find_cheats(prob):
    track = {}
    for a in range(-2, len(prob) + 2):
        for b in range(-2, len(prob[0]) + 2):
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
    o_length = find_len(track, start, end, len(prob), len(prob[0]))
    o_track = track.copy()
    cheats = []

    walls = [k for k in track.keys() if is_valid_wall(k, track)]
    for wall in walls:
        track[wall] = 0
        length = find_len(track, start, end, len(prob), len(prob[0]))
        if length:
            cheats.append(o_length - length)
        track[wall] = 1
    return cheats


def solve(prob):
    cheats = find_cheats(prob)
    return sum([c >= 100 for c in cheats])


print(find_cheats(inp_test))
print(solve(inp))
