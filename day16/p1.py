from functools import cache

inp = open("day16/inp.txt", "r").readlines()
inp_11048 = open("day16/inp_11048.txt", "r").readlines()
inp_7036 = open("day16/inp_7036.txt", "r").readlines()

@cache
def find_paths(walls, end, walked, rotated, pos, dir):
    global min_score
    if pos == end:
        return walked, rotated, True

    poses = [(pos[0], pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1])]

    found = False
    r_found = False
    r_walked = tuple()
    r_rotated = tuple()
    for i, p in enumerate(poses):
        if abs(dir - i) == 2:
            continue

        if p not in walls and p not in walked:
            o_walked = walked
            o_rotated = rotated

            walked = walked + (p,)
            
            if abs(dir-i) in [1,3]:
                rotated = rotated + ((p, i),)
         
            walked, rotated, found = find_paths(walls, end, walked, rotated, p, i)
            if found:
                score = 1000 * len(rotated) + len(walked)
                if score < min_score and end in walked:
                    min_score = score
                    r_walked = walked
                    r_rotated = rotated
                r_found = True
            walked = o_walked
            rotated = o_rotated
            
    return r_walked, r_rotated, r_found

def solve(prob):
    global min_score
    walked = tuple()
    rotated = tuple()
    walls = tuple()
    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "#":
                walls = walls + ((x, y),)
            if c == "E":
                end = (x, y)

    dir = 1
    pos = start
    min_score = 10**9
    find_paths(walls, end, walked, rotated, pos, dir)
    return min_score


print(solve(inp_7036), 7036)
print(solve(inp_11048), 11048)
print(solve(inp))
