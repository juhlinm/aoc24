inp = list(map(lambda x: x.strip(), open("day14/inp.txt", "r").readlines()))
twelve = list(map(lambda x: x.strip(), open("day14/12.txt", "r").readlines()))

def is_inside(robot, x_min, x_max, y_min, y_max):
    p, _ = robot
    p_x, p_y = p
    return p_x >= x_min and p_x <= x_max and p_y >= y_min and p_y <= y_max

def count(robots, x_max, y_max):
    result = 1
    mid_x = x_max // 2
    mid_y = y_max // 2
    for i in range(4):
        if i == 0:
            x_mi = 0
            x_ma = mid_x -1
            y_mi = 0
            y_ma = mid_y -1
        if i == 1:
            x_mi = mid_x + 1
            x_ma = x_max
            y_mi = 0
            y_ma = mid_y -1
        if i == 2:
            x_mi = 0
            x_ma = mid_x -1
            y_mi = mid_y + 1
            y_ma = y_max
        if i == 3:
            x_mi = mid_x + 1
            x_ma = x_max
            y_mi = mid_y + 1
            y_ma = y_max
        s = sum([is_inside(robot, x_mi, x_ma, y_mi, y_ma) for robot in robots])
        print(s)
        if s > 0:
            result *= s
    return result

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
    max_t = 100

    robots = []
    for line in prob:
        p_raw, v_raw = line.split()
        p_raw = p_raw.split("=")[1]
        p_x, p_y = map(int, p_raw.split(","))
        v_raw = v_raw.split("=")[1]
        v_x, v_y = map(int, v_raw.split(","))
        robots.append(((p_x, p_y), (v_x, v_y)))

    for _ in range(max_t):
        robots = simulate(robots, x_max, y_max)

    return count(robots, x_max, y_max)

print(solve(twelve, 11, 7), 12)
print(solve(inp, 101, 103))