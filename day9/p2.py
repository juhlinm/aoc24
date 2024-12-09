from line_profiler import profile
import sys
sys.setrecursionlimit(10**6)

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


# @profile
def fill_space(nums, vals):
    v = get_highest_v()
    rep = None
    found = False
    while v != 0:
        k = int(vals[v])
        l = str(idxs[v])

        # jj = None
        # print(nums)
        # jj = nums.index(l)
        for i in range(len(nums)):
            if nums[i] == l and nums[i+k-1] == l:
                jj = i
                break

        if l in reps_x:
            v = get_highest_v()
            continue
        for idx, spc in enumerate(spcs):
            if k <= int(spc):
                for i in range(len(nums)):
                    if nums[i] == DOT and nums[i+int(spc)-1] == DOT:
                        kk = i
                        break 
                if jj and kk < jj:
                    rep = [l] * k
                    found = True
                    break
        else:
            v = get_highest_v()
        if found:
            break
    
    if rep:
        for klp in range(k):
            nums[jj+klp] = DOT
        if kk not in reps:
            nums[kk:kk+k] = rep
            reps.extend([x for x in range(kk, kk+k)])
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

    print("".join(nums))

    o_nums = ["-1"]
    op = 0
    while nums != o_nums: 
        high = len(vals) - 1
        o_nums = nums.copy()
        nums, xp = fill_space(nums, vals)
        print("".join(nums))
        # print(nums)
        if op % 500 == 0:
            print(xp)
        op+=1

    return count_line(nums)


line = open("day9/base.txt", "r").read().strip()
assert defrag(line) == 2858

line = open("day9/base10.txt", "r").read().strip()
print(defrag(line))
  
line = open("day9/base420.txt", "r").read().strip()
assert defrag(line) == 132





# with open("day9/inp.txt", "r") as f:
#     line = f.read().strip()
# print(defrag(line))



