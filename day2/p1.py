with open("day2/inp.txt", "r") as f:
    lines = f.readlines()

l1 = []
for l in lines:
    l1.append([int(x) for x in l.split(" ")])

sum = len(l1)
for ln in l1:
    o_asc = ln[1] > ln[0]
    diff = abs(ln[1] - ln[0])
    if diff < 1 or diff > 3:
        sum -= 1
        continue
    for i in range(1, len(ln) - 1):
        asc = ln[i+1] > ln[i]
        if asc != o_asc:
            sum -= 1
            break
        diff = abs(ln[i+1] - ln[i])
        if diff < 1 or diff > 3:
            sum -= 1
            break

print(sum)