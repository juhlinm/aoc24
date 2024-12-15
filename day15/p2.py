inp = open("day15/inp.txt", "r").read().split("\n\n")
inp_10092 = open("day15/10092.txt", "r").read().split("\n\n")
inp_p2 =  open("day15/p2.txt", "r").read().split("\n\n")

def box_clash(boxes, walls):
    boxs = boxes.copy()
    boxs.extend([(box[0] + 1, box[1]) for box in boxs])
    b = set(boxs)
    wals = walls.copy()
    wals.extend([(w[0] + 1, w[1]) for w in wals])
    w = set(wals)
    return b & w

def robot_clash(robot, other):
    o1 = other
    o2 = [(o[0] + 1, o[1]) for o in other]
    return robot in o1 or robot in o2

def get_pushed(x, d, direction, c_boxes, boxes):
    bxs = [b for b in boxes if b[1] == d]
    for b in bxs:
        if b in c_boxes:
            continue
        if b[0] == x:
            c_boxes.append(b)
            get_pushed(x, d+direction, direction, c_boxes, boxes)
        elif b[0] - 1 == x:
            c_boxes.append(b)
            get_pushed(x+1, d+direction, direction, c_boxes, boxes)
        elif b[0] + 1 == x:
            c_boxes.append(b)
            get_pushed(x-1, d+direction, direction, c_boxes, boxes)
    return

def attempt(move, boxes, walls, robot):
    i = 0
    gap = False
    c_boxes = []
    ch_boxes = []
    x0 = -1
    if move == 0:
        n_robot = (robot[0], robot[1] - 1)

        if (robot[0], robot[1] - 1) in boxes:
            x0 = robot[0]
        if (robot[0] - 1, robot[1] - 1) in boxes:
            x0 = robot[0] - 1
        if x0 != -1:
            c_boxes.append((x0, robot[1] - 1))
            get_pushed(x0, robot[1] - 2, -1, c_boxes, boxes)

        n_boxes = [b for b in boxes if b not in c_boxes]
        u_boxes = n_boxes.copy()
        if c_boxes:
            for box in c_boxes:
                ch_boxes.append((box[0], box[1] - 1))
                n_boxes.append((box[0], box[1] - 1))
        else:
            n_boxes.extend(c_boxes)
    if move == 1:
        n_robot = (robot[0] + 1, robot[1])
        c_boxes = sorted([b for b in boxes if b[1] == robot[1] and b[0] > robot[0]])
        n_boxes = [b for b in boxes if b[1] != robot[1]]
        n_boxes.extend([b for b in boxes if b[1] == robot[1] and b[0] < robot[0]])
        u_boxes = n_boxes.copy()
        if c_boxes and robot_clash(n_robot, c_boxes):
            prev_box = c_boxes[0]
            for i in range(len(c_boxes)):
                box = c_boxes[i]
                diff = abs(box[0]-prev_box[0])
                if diff > 2:
                    gap = True
                    break
                n_boxes.append((box[0] + 1, box[1]))
                ch_boxes.append((box[0] + 1, box[1]))
                prev_box = box
        else:
            n_boxes.extend(c_boxes)
    if move == 2:
        n_robot = (robot[0], robot[1] + 1)

        if (robot[0], robot[1] + 1) in boxes:
            x0 = robot[0]
        if (robot[0] - 1, robot[1] + 1) in boxes:
            x0 = robot[0] - 1
        if x0 != -1:
            c_boxes.append((x0, robot[1] + 1))
            get_pushed(x0, robot[1] + 2, 1, c_boxes, boxes)

        n_boxes = [b for b in boxes if b not in c_boxes]
        u_boxes = n_boxes.copy()
        if c_boxes:
            for box in c_boxes:
                ch_boxes.append((box[0], box[1] + 1))
                n_boxes.append((box[0], box[1] + 1))
        else:
            n_boxes.extend(c_boxes)
    if move == 3:
        n_robot = (robot[0] - 1, robot[1])
        c_boxes = sorted([b for b in boxes if b[1] == robot[1] and b[0] < robot[0]], reverse=True)
        n_boxes = [b for b in boxes if b[1] != robot[1]]
        n_boxes.extend([b for b in boxes if b[1] == robot[1] and b[0] > robot[0]])
        u_boxes = n_boxes.copy()
        if c_boxes and robot_clash(n_robot, c_boxes):
            prev_box = c_boxes[0]
            for i in range(len(c_boxes)):
                box = c_boxes[i]
                diff = abs(box[0]-prev_box[0])
                if diff > 2:
                    gap = True
                    break
                n_boxes.append((box[0] - 1, box[1]))
                ch_boxes.append((box[0] - 1, box[1]))
                prev_box = box
        else:
            n_boxes.extend(c_boxes)
    if gap:
        for j in range(i, len(c_boxes)):
            n_boxes.insert(0, c_boxes[j])

    if robot_clash(n_robot, walls):
        return boxes, robot
    elif box_clash(n_boxes, walls):
        return boxes, robot
    elif box_clash(ch_boxes, u_boxes):
        return boxes, robot
    elif not robot_clash(n_robot, c_boxes):
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
                robot = (2*x,y)
            if c == "#":
                walls.append((2*x,y))
            if c == "O":
                boxes.append((2*x,y))

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

solve(inp_p2)
print(solve(inp_10092), 9021)
print(solve(inp))