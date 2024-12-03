import re

with open("day3/inp.txt", "r") as f:
    lines = f.readlines()

txt = "".join(lines)
muls = []


def get_index_of_last(pattern, txt):
    matches = list(iter(re.finditer(pattern, txt)))
    if len(matches):
        return matches[-1].end()
    else:
        return -1


matches = list(iter(re.finditer(r"mul\(([\d]+),([\d]+)\)", txt)))
muls.append((matches[0].group(1), matches[0].group(2)))
do = True
for i in range(len(matches) - 1):
    s = matches[i].end()
    e = matches[i + 1].start()
    l_do = get_index_of_last(r"do\(\)", txt[s:e])
    l_dont = get_index_of_last(r"don't\(\)", txt[s:e])
    if l_dont > l_do:
        do = False
    elif l_do > l_dont:
        do = True

    if do:
        muls.append((matches[i + 1].group(1), matches[i + 1].group(2)))

sum = 0
for m in muls:
    sum += int(m[0]) * int(m[1])
print(sum)
