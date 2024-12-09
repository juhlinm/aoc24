

DOT = "."

def count_line(line):
    sum = 0
    for i, c in enumerate(line):
        if c != DOT:
            j = int(c)
            sum += j * i
    return sum


def build_value(idx, vals):
    if idx < len(vals):
        res = [str(idxs[idx])] * int(vals[idx])
        if idx < len(spcs):
            res.extend(DOT * int(spcs[idx]))
        return res
    else:
        return []
    


def get_highest_v():
    global high
    if high < 0:
        return 0
    v = high
    high -= 1
    return v



def fill_space(nums, vals):
    v = get_highest_v()
    rep = None
    found = False
    while v != 0 and not found:
        k = int(vals[v])
        l = str(idxs[v])
        if l in reps_x:
            v = get_highest_v()
            continue
        for idx, spc in enumerate(spcs):
            if k <= int(spc):
                rep = [l] * k
                found = True
                break
        else:
            v = get_highest_v()
    
    if rep:
        nums = [x if x != l else DOT for x in nums]
        iid = [DOT if x == DOT else "o" for x in nums]
        i = "".join(iid).index(DOT * int(spc))
        if i not in reps:
            nums[i:i+k] = rep
            reps.extend([x for x in range(i, i+k)])
            reps_x.append(l)
            spcs[idx] = str(int(spcs[idx]) - k)
            
    return nums, len(reps_x)
    

def defrag(line):
    global high, spcs, idxs, reps, reps_x

    vals = list(line[::2])
    spcs = list(line[1::2])
    idxs = [i for i in range(len(vals))]
    reps = []
    reps_x = []

    
    i = 0
    nums = []
    o_nums = ["-1"]
    while nums != o_nums:
        o_nums = nums.copy()
        nums.extend(build_value(i, vals))
        i += 1

    # print("".join(nums))

    o_nums = ["-1"]
    op = 0
    while nums != o_nums: 
        high = len(vals) - 1
        o_nums = nums.copy()
        nums, xp = fill_space(nums, vals)
        # print("".join(nums))
        # print(nums)
        if op % 500 == 0:
            print(xp)
        op+=1

    return nums


line = open("day9/base.txt", "r").read().strip()
assert count_line(defrag(line)) == 2858

line = open("day9/base10.txt", "r").read().strip()
assert count_line(defrag(line)) == 3200
  





# with open("day9/inp.txt", "r") as f:
#     line = f.read().strip()
# print(print(count_line(defrag(line))))



