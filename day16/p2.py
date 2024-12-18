inp = open("day16/inp.txt", "r").readlines()
inp_11048 = open("day16/inp_11048.txt", "r").readlines()
inp_7036 = open("day16/inp_7036.txt", "r").readlines()
inp_21148 = open("day16/inp_21148.txt", "r").readlines()
inp_4013 = open("day16/inp_4013.txt", "r").readlines()
inp_5078 = open("day16/inp_5078.txt", "r").readlines()

def get_paths(unexplored, explore):
    paths = []
    for dir, diff in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
        n_pos = (explore[0] + diff[0], explore[1] + diff[1])
        if n_pos in unexplored:
            paths.append((n_pos, dir))
    return paths

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def traverse(maze, start, end, y_max, x_max):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (x_max - 1) or node_position[0] < 0 or node_position[1] > (y_max - 1) or node_position[1] < 0:
                continue

            if maze[(node_position[0],node_position[1])] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            
            if sum(o.position == child.position for o in open_list) > 1000:
                return None  # How to break A* loop if no way
            else:
                open_list.append(child)


def solve(prob):
    walls = []
    for y, line in enumerate(prob):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == "#":
                walls.append((x, y))
            if c == "E":
                end = (x, y)
    y_max = y + 1
    x_max = x + 1

    maze = {}
    for y in range(y_max):
        for x in range(x_max):
            if (x, y) in walls:
                maze[(x, y)] = 1
            else:
                maze[(x, y)] = 0
                

    o_path = traverse(maze, start, end, y_max, x_max)
    poses = set(o_path)
    for i in range(0, len(o_path)-1):
        maze[o_path[i+1]] = 1
        path = traverse(maze, o_path[i], end, y_max, x_max)
        if path:
            poses.update(path)
        maze[o_path[i+1]] = 0

    return len(poses)



print(solve(inp_7036), 45)
print(solve(inp_11048), 64)
print(solve(inp_21148), 149)
print(solve(inp_4013), 14)
print(solve(inp_5078), 413)
# print(solve(inp))
