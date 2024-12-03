import re

with open("day3/inp.txt", "r") as f:
    lines = f.readlines()

muls = []
for line in lines:
    muls.extend(re.findall(r"mul\(([\d]+),([\d]+)\)", line))

sum = 0
for m in muls:
    sum += int(m[0]) * int(m[1])
print(sum)
