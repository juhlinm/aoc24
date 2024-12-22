from sys import setrecursionlimit


setrecursionlimit(4000)

inp = [x.strip() for x in open("day22/inp.txt", "r").readlines()]
inp_p2 = [x.strip() for x in open("day22/inp_p2.txt", "r").readlines()]

MOD = 16777216


def secret(inp, res, max_d, d=0):
    if d == max_d:
        return res

    A = ((inp * 64) ^ inp) % MOD
    A = ((A // 32) ^ A) % MOD
    A = ((A * 2048) ^ A) % MOD
    D = A % 10
    diff = D - (inp % 10)
    return secret(A, res + ((D, diff),), max_d, d + 1)


def to_int(x, y, z, w):
    return (x + 9) * 19**3 + (y + 9) * 19**2 + (z + 9) * 19**1 + (w + 9) * 19**0


def solve(prob):
    seqs = {k: 0 for k in range(130320)}
    for j, line in enumerate(prob):
        seq = secret(
            int(line),
            ((int(line) % 10, None),),
            2000,
        )
        j_consumed = set()
        for i in range(4, len(seq)):
            s = to_int(seq[i - 3][1], seq[i - 2][1], seq[i - 1][1], seq[i][1])
            if s in j_consumed:
                continue
            seqs[s] += seq[i][0]
            j_consumed.add(s)

    return seqs[max(seqs, key=seqs.get)]


print(solve(inp_p2), 23)
print(solve(inp))
