from copy import deepcopy

inp = list(map(lambda x: x.strip(), open("day14/inp.txt", "r").readlines()))

def has_base(robots):
    base_w = 1
    rob_ps = [r[0] for r in robots]
    for r_i in range(len(robots)):
        p, _ = robots[r_i]
        x0, y0 = p
        a = all((x0-base_w+i, y0) in rob_ps for i in range(base_w * 2 + 1))
        b = all((x0-base_w+i, y0-1) in rob_ps for i in range(base_w * 2 + 1))
        c = all((x0-base_w+i, y0+1) in rob_ps for i in range(base_w * 2 + 1))
        if a and b and c:
            return True
    return False

def draw(robots, bg, x_max, y_max, t):
    if has_base(robots):
        bg = deepcopy(bg)
        for robot in robots:
            p, _ = robot
            bg[p] = "1"
        show = ""
        for y in range(y_max):
            for x in range(x_max):
                show += bg[(x,y)]
            show += "\n"

        with open("day14/out.txt", "w") as f:
            f.write("="*(x_max-len(str(t))) + str(t) + "\n\n" + show)
        return True
    return False

def drive(robot, x_max, y_max):
    p, v = robot
    p_x, p_y = p
    v_x, v_y = v
    n_x = p_x + v_x
    n_y = p_y + v_y

    if n_x < 0:
        n_x = x_max + n_x
    if n_y < 0:
        n_y = y_max + n_y
    if n_x > x_max - 1:
        n_x = n_x - x_max
    if n_y > y_max - 1:
        n_y = n_y - y_max

    return ((n_x, n_y), v)

def simulate(robots, x_max, y_max):
    return [drive(robot, x_max, y_max) for robot in robots]

def solve(prob, x_max, y_max):
    robots = []
    for line in prob:
        p_raw, v_raw = line.split()
        p_raw = p_raw.split("=")[1]
        p_x, p_y = map(int, p_raw.split(","))
        v_raw = v_raw.split("=")[1]
        v_x, v_y = map(int, v_raw.split(","))
        robots.append(((p_x, p_y), (v_x, v_y)))

    bg = {}
    for y in range(y_max):
        for x in range(x_max):
            bg[(x,y)] = "."

    with open("day14/out.txt", "w") as f:
        f.write("")

    t = 0
    while t < 10**5:
        robots = simulate(robots, x_max, y_max)
        t += 1
        if draw(robots, bg, x_max, y_max, t):
            break
    return t

print(solve(inp, 101, 103))
