with open("day6/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

y_max = len(lines)
x_max = len(lines[0])

obs = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"]
start = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "^"][0]


def can_move(n_pos, n_o):
    return n_pos != n_o and n_pos not in obs


passed = [start]


def move(pos, c, n_o):
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

    n_pos = (pos[0] + x, pos[1] + y)
    if can_move(n_pos, n_o):
        passed.append(n_pos)
        return n_pos, c
    else:
        return pos, n_c


n_os = []
i_max = 10000
for xk in range(0, x_max):
    print(xk / x_max)
    for yk in range(0, y_max):
        n_o = (xk, yk)
        i = 0
        cur_pos = start
        c = "^"

        while True:
            i += 1
            if i > i_max:
                n_os.append(n_o)
                break

            if cur_pos[0] not in range(0, x_max) or cur_pos[1] not in range(0, y_max):
                break

            cur_pos, c = move(cur_pos, c, n_o)


print(len(n_os))
