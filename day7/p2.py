with open("day7/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def get_tern(n):
    ls = []
    for i in range(n):
        lsx = []
        for j in range(3**n):
            if i == 0:
                lsx.append(str(j % 3))
            else:
                lsx.append(str((j // 3**(i)) % 3))
        ls.append(lsx)
    return sorted([''.join(chars) for chars in zip(*ls)])

def op(ns, op):
    if int(op) == 0:
        return ns[0] + ns[1]
    elif int(op) == 1:
        return ns[0] * ns[1]
    else:
        return int(str(ns[0]) + str(ns[1]))
 
sum = 0
for line in lines:
    print(lines.index(line) / len(lines))
    v, x = line.split(": ")
    xs = [int(k) for k in x.split()]
    v = int(v)

    l = len(xs) - 1
    n_combs = 3**l
    terns = get_tern(l)
    lsum = [xs[0]] * n_combs
    for i in range(0, len(xs) - 1):
        for j in range(n_combs):
            lsum[j] = op((lsum[j], xs[i+1]), terns[j][i])

    if any(a == v for a in lsum):
        sum += v

print(sum)