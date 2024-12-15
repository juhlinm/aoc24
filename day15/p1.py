inp = open("day15/inp.txt", "r").read().split("\n\n")
inp_10092 = open("day15/10092.txt", "r").read().split("\n\n")
inp_2028 = open("day15/2028.txt", "r").read().split("\n\n")

def attempt(move, boxes, walls, robot):
    i = 0
    gap = False
    if move == 0:
        n_robot = (robot[0], robot[1] - 1)
        c_walls = [w for w in walls if w[0] == robot[0] and w[1] < robot[1]]
        c_boxes = sorted([b for b in boxes if b[0] == robot[0] and b[1] < robot[1]], reverse=True)
        n_boxes = [b for b in boxes if b[0] != robot[0]]
        n_boxes.extend([b for b in boxes if b[0] == robot[0] and b[1] > robot[1]])
        if c_boxes and n_robot in c_boxes:
            prev_box = c_boxes[0]
            for i in range(len(c_boxes)):
                box = c_boxes[i]
                diff = abs(box[1]-prev_box[1])
                if diff > 1:
                    gap = True
                    break
                n_boxes.append((box[0], box[1] - 1))
                prev_box = box
        else:
            n_boxes.extend(c_boxes)
    if move == 1:
        n_robot = (robot[0] + 1, robot[1])
        c_walls = [w for w in walls if w[1] == robot[1] and w[0] > robot[0]]
        c_boxes = sorted([b for b in boxes if b[1] == robot[1] and b[0] > robot[0]])
        n_boxes = [b for b in boxes if b[1] != robot[1]]
        n_boxes.extend([b for b in boxes if b[1] == robot[1] and b[0] < robot[0]])
        if c_boxes and n_robot in c_boxes:
            prev_box = c_boxes[0]
            for i in range(len(c_boxes)):
                box = c_boxes[i]
                diff = abs(box[0]-prev_box[0])
                if diff > 1:
                    gap = True
                    break
                n_boxes.append((box[0] + 1, box[1]))
                prev_box = box
        else:
            n_boxes.extend(c_boxes)
    if move == 2:
        n_robot = (robot[0], robot[1] + 1)
        c_walls = [w for w in walls if w[0] == robot[0] and w[1] > robot[1]]
        c_boxes = sorted([b for b in boxes if b[0] == robot[0] and b[1] > robot[1]])
        n_boxes = [b for b in boxes if b[0] != robot[0]]
        n_boxes.extend([b for b in boxes if b[0] == robot[0] and b[1] < robot[1]])
        if c_boxes and n_robot in c_boxes:
            prev_box = c_boxes[0]
            for i in range(len(c_boxes)):
                box = c_boxes[i]
                diff = abs(box[1]-prev_box[1])
                if diff > 1:
                    gap = True
                    break
                n_boxes.append((box[0], box[1] + 1))
                prev_box = box
        else:
            n_boxes.extend(c_boxes)
    if move == 3:
        n_robot = (robot[0] - 1, robot[1])
        c_walls = [w for w in walls if w[1] == robot[1] and w[0] < robot[0]]
        c_boxes = sorted([b for b in boxes if b[1] == robot[1] and b[0] < robot[0]], reverse=True)
        n_boxes = [b for b in boxes if b[1] != robot[1]]
        n_boxes.extend([b for b in boxes if b[1] == robot[1] and b[0] > robot[0]])
        if c_boxes and n_robot in c_boxes:
            prev_box = c_boxes[0]
            for i in range(len(c_boxes)):
                box = c_boxes[i]
                diff = abs(box[0]-prev_box[0])
                if diff > 1:
                    gap = True
                    break
                n_boxes.append((box[0] - 1, box[1]))
                prev_box = box
        else:
            n_boxes.extend(c_boxes)
    if gap:
        for j in range(i, len(c_boxes)):
            n_boxes.insert(0, c_boxes[j])

    if n_robot in c_walls:
        return boxes, robot
    elif n_boxes and n_boxes[-1] in c_walls:
        return boxes, robot
    elif n_robot not in c_boxes:
        return boxes, n_robot
    else:
        return n_boxes, n_robot

def solve(prob):
    env_raw, move_raw = prob

    walls = []
    boxes = []
    for y, line in enumerate(env_raw.split("\n")):
        for x, c in enumerate(line):
            if c == "@":
                robot = (x,y)
            if c == "#":
                walls.append((x,y))
            if c == "O":
                boxes.append((x,y))

    moves = []
    for move in move_raw.split("\n"):
        for c in move:
            if c == "^":
                moves.append(0)
            elif c == ">":
                moves.append(1)
            elif c == "v":
                moves.append(2)
            elif c == "<":
                moves.append(3)
    
    for move in moves:
        boxes, robot = attempt(move, boxes, walls, robot)

    return sum([box[0] + box[1] * 100 for box in boxes])


print(solve(inp_2028),2028)
print(solve(inp_10092),10092)
print(solve(inp))