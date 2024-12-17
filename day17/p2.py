inp = open("day17/inp.txt", "r").read().split("\n\n")

def execute(A):
    return ((A//2**((A%8)^5)) ^ (((A%8)^5)^6)) % 8 

def find(A, ops, col=0):
    global As
    if execute(A) != ops[-(col + 1)]:
        return

    if col == len(ops) - 1:
        As.append(A)
    else:
        for B in range(8):
            find(A * 8 + B, ops, col + 1)

def solve(prob):
    global As
    _, ops = prob
    ops = ops.split(": ")[1]
    ops = list(map(int, ops.split(",")))
    
    As = []
    for a in range(8):
        find(a, ops)
    return As[0]

print(solve(inp))
