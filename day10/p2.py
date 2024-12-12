twotwoseven = list(map(lambda x: x.strip(), open("day10/twop2.txt", "r").readlines()))
three = list(map(lambda x: x.strip(), open("day10/threep2.txt", "r").readlines()))
thirteen = list(map(lambda x: x.strip(), open("day10/four.txt", "r").readlines()))
eightyone = list(map(lambda x: x.strip(), open("day10/threesix.txt", "r").readlines()))
inp = list(map(lambda x: x.strip(), open("day10/inp.txt", "r").readlines()))


def get_starts(lines):
    xs = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "0":
                xs.append((x, y))
    return xs

def get_heightmap(lines):
    hs = {}
    for y in range(-1, len(lines) + 1):
        for x in range(-1, len(lines[0]) + 1):
            hs[(x,y)] = -2
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            try:
                hs[(x,y)] = int(c)
            except ValueError:
                hs[(x,y)] = -2
    return hs

def is_next(a, b, h_map):
    return h_map[b] - h_map[a] == 1

def solve(prob):
    height_map = get_heightmap(prob)
    x0s = get_starts(prob)
    return sum(walk(x0, height_map) for x0 in x0s)

def walk(pos, h_map, h=0):
    sum = 0
    if is_next(pos, (pos[0]+1, pos[1]), h_map):
        sum += walk((pos[0]+1, pos[1]), h_map, h+1)
    if is_next(pos, (pos[0]-1, pos[1]), h_map):
        sum += walk((pos[0]-1, pos[1]), h_map, h+1)
    if is_next(pos, (pos[0], pos[1]+1), h_map):
        sum += walk((pos[0], pos[1]+1), h_map, h+1)
    if is_next(pos, (pos[0], pos[1]-1), h_map):
        sum += walk((pos[0], pos[1]-1), h_map, h+1)
    if h == 9:
        return 1
    return sum

print(solve(three),3)
print(solve(thirteen),13)
print(solve(eightyone),81)
print(solve(twotwoseven),227)
print(solve(inp))
