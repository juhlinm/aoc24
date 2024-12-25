inp = open("day25/inp.txt", "r").read().split("\n\n")
inp_test = open("day25/inp_test.txt", "r").read().split("\n\n")


def fits(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True


def solve(prob):
    keys = []
    locks = []
    for data in prob:
        split = data.split("\n")
        transposed = ["".join(s) for s in zip(*split)]
        elem = tuple()
        for trans in transposed:
            elem = elem + (trans.count("#") - 1,)
        if all(c == "#" for c in split[0]):
            locks.append(elem)
        else:
            keys.append(elem)

    s = 0
    for lock in locks:
        for key in keys:
            s += fits(lock, key)

    return s


print(solve(inp_test), 3)
print(solve(inp))
