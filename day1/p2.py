with open("day1/inp.txt", "r") as f:
    lines = f.readlines()

l1 = []
l2 = []
for l in lines:
    l = l.strip()
    l1.append(int(l.split(" ")[0]))
    l2.append(int(l.split(" ")[-1]))

l1 = sorted(l1)
l2 = sorted(l2)

sum = 0
for x, y in zip(l1, l2):
    sum += x * l2.count(x)

print(sum)