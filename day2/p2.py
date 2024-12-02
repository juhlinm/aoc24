with open("day2/inp.txt", "r") as f:
    lines = f.readlines()

l1 = []
for l in lines:
    l1.append([int(x) for x in l.split(" ")])

def is_safe(ln):
    o_asc = ln[1] > ln[0]
    for i in range(0, len(ln) - 1):
        asc = ln[i+1] > ln[i]
        diff = abs(ln[i+1] - ln[i])
        if asc != o_asc or diff not in [1,2,3]:
            return False
    return True

sum = len(l1)
for ln in l1:
    if not is_safe(ln):
        can_be_safe = False
        for i in range(len(ln)):
            ln_m = ln.copy()
            ln_m.pop(i)
            if is_safe(ln_m):
                can_be_safe = True
                break
        if not can_be_safe:
            sum -= 1

print(sum)