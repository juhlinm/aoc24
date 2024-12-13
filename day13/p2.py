import math

inp = list(map(lambda x: x.strip(), open("day13/inp.txt", "r").read().split("\n\n")))
test = list(map(lambda x: x.strip(), open("day13/test.txt", "r").read().split("\n\n")))

press_max = 10**12


def add(v1, v2):
    return tuple([v1[0] + v2[0], v1[1] + v2[1]])


def subtract(v1, v2):
    return tuple([v1[0] - v2[0], v1[1] - v2[1]])


def multiply(v, k):
    return tuple([v[0] * k, v[1] * k])


def distance(v1, v2):
    diff = subtract(v1, v2)
    return math.sqrt(diff[0] ** 2 + diff[1] ** 2)


def press(A, B, prize):
    for i in range(1, press_max + 1, 10**9):
        print(i)
        for j in range(1, press_max + 1, 10**9):
            p1 = add((0, 0), multiply(B, j))
            p2 = subtract(prize, multiply(A, i))
            if distance(p1, p2) < 10**12:
                break
    print(i, j, p1, p2)
    for i in range(i, press_max + 1):
        for j in range(j, press_max + 1):
            if add((0, 0), multiply(B, j)) == subtract(prize, multiply(A, i)):
                return (i, j)
    return None


def solve(machines):
    sum = 0
    for machine in machines:
        lines = machine.split("\n")
        A = tuple(map(int, (lines[0].split("+")[1].split(",")[0], lines[0].split("+")[-1])))
        B = tuple(map(int, (lines[1].split("+")[1].split(",")[0], lines[1].split("+")[-1])))
        prize = tuple(map(int, (lines[2].split("=")[1].split(",")[0], lines[2].split("=")[-1])))
        prize = add(prize, (10**13, 10**13))
        res = press(A, B, prize)
        if res:
            sum += 3 * res[0] + 1 * res[1]

    return sum


print(solve(test), 480)
# print(solve(inp))
