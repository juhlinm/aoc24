with open("day7/inp.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def get_bin(n):
    return [bin(i)[2:].zfill(n) for i in range(2**n)]

def op(ns, op):
    if int(op) == 0:
        return ns[0] + ns[1]
    else:
        return ns[0] * ns[1]
 
sum = 0
for line in lines:
    v, x = line.split(": ")
    xs = [int(k) for k in x.split()]
    v = int(v)

    l = len(xs) - 1
    n_combs = 2**l
    bins = get_bin(l)
    lsum = [xs[0]] * n_combs
    for i in range(0, len(xs) - 1):
        for j in range(n_combs):
            lsum[j] = op((lsum[j], xs[i+1]), bins[j][i])

    if any(a == v for a in lsum):
        sum += v

print(sum)