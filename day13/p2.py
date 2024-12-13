inp = list(map(lambda x: x.strip(), open("day13/inp.txt", "r").read().split("\n\n")))
test = list(map(lambda x: x.strip(), open("day13/test.txt", "r").read().split("\n\n")))


def add(v1, v2):
    return tuple([v1[0] + v2[0], v1[1] + v2[1]])


def determinant(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


def press(A, B, prize):
    det = determinant(A, B)
    if det == 0:
        return None
    else:
        a = (prize[0] * B[1] - prize[1] * B[0]) / det
        b = (prize[1] * A[0] - prize[0] * A[1]) / det

        if a % 1 == 0.0 and b % 1 == 0.0:
            return (a, b)
        else:
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
            sum += int(3 * res[0] + 1 * res[1])
    return sum


print(solve(test), 875318608908)
print(solve(inp))
