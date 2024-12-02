with open("day2/inp.txt", "r") as f:
    lines = f.readlines()

l1 = []
for l in lines:
    l1.append([int(x) for x in l.split(" ")])

sum = len(l1)
for ln in l1:
    o_asc = ln[1] > ln[0]
    for i in range(0, len(ln) - 1):
        asc = ln[i+1] > ln[i]
        diff = abs(ln[i+1] - ln[i])
        if asc != o_asc or diff not in [1,2,3]:
            sum -= 1
            break

print(sum)