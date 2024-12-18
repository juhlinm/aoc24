inp_test = open("day18/inp_test.txt", "r").readlines()
inp = open("day18/inp.txt", "r").readlines()


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


def solve(prob, bytes, end):
    corrupted = []
    for line in prob[:bytes]:
        x, y = map(int, line.split(","))
        corrupted.append((x, y))

    unexplored = {}
    for y in range(end[1] + 1):
        for x in range(end[0] + 1):
            if (x, y) not in corrupted:
                unexplored[(x, y)] = float("inf")
    start = (0, 0)
    unexplored[start] = 0
    while len(unexplored) != 0:
        explore = minimum(unexplored)
        if explore == end:
            break
        else:
            for path in get_paths(unexplored, explore):
                time = unexplored[explore] + 1
                if time < unexplored[path]:
                    unexplored[path] = time
        del unexplored[explore]

    return unexplored[explore]


print(solve(inp_test, 12, (6, 6)), 22)
print(solve(inp, 1024, (70, 70)))
