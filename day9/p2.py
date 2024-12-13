base = open("day9/base.txt", "r").read().strip()
base10 = open("day9/base10.txt", "r").read().strip()
fourtwenty = open("day9/base420.txt", "r").read().strip()
inp = open("day9/inp.txt", "r").read().strip()

def count_line(line):
    sum = 0
    for i, c in enumerate(line):
        if c:
            j = int(c)
            sum += j * i
    return sum

def defrag(line):
    n_line = []
    spaces = []
    file_cnt = 0
    file_lens = {}
    file_poss = {}
    pos = 0
    for i, c in enumerate(line):
        c = int(c)
        if i % 2 == 0:
            n_line[pos:pos+c] = [file_cnt] * c
            file_lens[file_cnt] = c
            file_poss[file_cnt] = pos
            file_cnt += 1
        else:
            n_line[pos:pos+c] = [None] * c
            spaces.append((pos, pos+c))
        pos = pos + c
    o_line = n_line.copy()

    for file in range(file_cnt - 1, 0, -1):
        file_len = file_lens[file]
        file_pos = file_poss[file]
        to_remove = []
        to_change = []
        to_append = []
        for space in sorted(spaces):
            if space[0] < file_pos and file_len <= (space[1] - space[0]):
                n_line[space[0]:space[0] + file_len] = [file] * file_len
                if file_len == space[1] - space[0]:
                    to_remove.append(space)
                else:
                    to_change.append((space, (space[0] + file_len, space[1])))
                n_line[file_pos:file_pos+file_len] = [None] * file_len
                to_append.append((file_pos, file_pos+file_len))
                break
        for rm in to_remove:
            spaces.remove(rm)
        for ch in to_change:
            spaces.remove(ch[0])
            spaces.append(ch[1])
        for ap in to_append:
            spaces.append(ap)

    assert len(o_line) == len(n_line)
    print(n_line[0:100])
    return count_line(n_line)


print(defrag(base), 2858)
print(defrag(base10), 3208)
print(defrag(fourtwenty), 132)
print(defrag(inp))

