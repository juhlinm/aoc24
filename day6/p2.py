with open("day6/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

STOP = ((-1,-1), "stop")   
ESCAPE = ((-1,-1), "escape")   

y_max = len(lines)
x_max = len(lines[0])

obs = sorted([(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"])
start = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "^"][0]


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

def move(pos, c, n_o):
    xk, yk = pos
    xd, yd, n_c = get_dirs(c)

    if xd == 0:
        yobs = [p[1] for p in obs if p[0] == xk]
        yobs.append(yk)
        if n_o[0] == xk:
            yobs.append(n_o[1])
        yobs.sort()
        n_ind = yobs.index(yk) + yd
        if n_ind >= len(yobs) or n_ind < 0:
            return ESCAPE
        n_y = yobs[n_ind] - yd
        return (xk, n_y), n_c
    else:
        xobs = [p[0] for p in obs if p[1] == yk]
        xobs.append(xk)
        if n_o[1] == yk:
            xobs.append(n_o[0])
        xobs.sort()
        n_ind = xobs.index(xk) + xd
        if n_ind >= len(xobs) or n_ind < 0:
            return ESCAPE
        n_x = xobs[n_ind] - xd
        return (n_x, yk), n_c
        

nnos = []
for xk in range(0, x_max):
    print(xk / x_max)
    for yk in range(0, y_max):
        n_o = (xk, yk)
        if n_o in obs:
            continue

        passed = [(start, "^")]
        res = passed[0]

        while True:
            res = move(*res, n_o)
            
            if res in passed:
                nnos.append(n_o)
                break
            elif res == ESCAPE:
                break

            passed.append(res)

print(len(nnos))

with open("day6/out.txt", "w") as f:
    o_lines = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (x,y) in nnos:
                line = line[:x] + 'O' + line[x+1:]
        o_lines.append(line+"\n")
    f.writelines(o_lines)

