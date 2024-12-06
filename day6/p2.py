from copy import deepcopy

with open("day6/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

STOP = ((-1,-1), "stop")   
ESCAPE = ((-1,-1), "escape")   

y_max = len(lines)
x_max = len(lines[0])

obs = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"]
obs_y = {
    y: [x for x, c in enumerate(line) if c == "#"]
    for y, line in enumerate(lines) 
    if "#" in line
}
obs_x = {
    x: [y for y, line in enumerate(lines) if x in [i for i, c in enumerate(line) if c == "#"]]
    for x in range(x_max)
}
start = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "^"][0]



def can_move(n_pos):
    if n_pos[1] in obs_y:
        if n_pos[0] in obs_y[n_pos[1]]:
            return False
    return n_pos != n_o

def get_dirs(c):
    if c == "^":
        y = -1
        x = 0
        n_c = ">"
    elif c == ">":
        y = 0
        x = 1
        n_c = "v"
    elif c == "v":
        y = 1
        x = 0
        n_c = "<"
    elif c == "<":
        y = 0
        x = -1
        n_c = "^"
    return x, y, n_c

def move_to_next(pos, c):
    xk, yk = pos
    xd, yd, n_c = get_dirs(c)
    if xd == 0:
        try:
            l = deepcopy(obs_x[xk])
            if n_o[0] == xk:
                l.append(n_o[1])
                l.sort()
                if yd == -1:
                    l.reverse()
            n_yk = next((v for v in l if v * yd >= yk * yd))
        except (KeyError, StopIteration):
            return ESCAPE
        return (xk, n_yk - yd), n_c
    else:
        try:
            l = deepcopy(obs_y[yk])
            if n_o[1] == yk:
                l.append(n_o[0])
                l.sort()
                if xd == -1:
                    l.reverse()
            n_xk = next((v for v in l if v * xd >= xk * xd))
        except (KeyError, StopIteration):
            return ESCAPE
        return (n_xk - xd, yk), n_c
        


def move(pos, c):
    n_pos, n_c = move_to_next(pos, c)
    if c == ESCAPE[1]:
        return ESCAPE
    elif (n_pos, n_c) not in passed:
        passed.append((n_pos, n_c))
        return n_pos, n_c
    else:
        return STOP



n_os = 0
n_esc = 0
for xk in range(0, x_max):
    for yk in range(0, y_max):
        n_o = (xk, yk)

        cur_pos = start
        c = "^"
        passed = [(start, c)]

        while True:
            cur_pos, c = move(cur_pos, c)

            if c == STOP[1]:
                n_os += 1
                break
            elif c == ESCAPE[1]:
                n_esc += 1
                break

print(n_os)
