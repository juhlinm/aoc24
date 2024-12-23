inp = [x.strip() for x in open("day23/inp.txt", "r").readlines()]
inp_test = [x.strip() for x in open("day23/inp_test.txt", "r").readlines()]


def dfs(graph, start, node, visited):
    if visited[node]:
        if node == start:
            return sorted([k for k in visited if visited[k]])
        else:
            return None
    visited[node] = True
    for child in graph[node]:
        return dfs(graph, start, child, visited)


def find_circuits(graph):
    circs = []
    for k in graph.keys():
        visited = {k: False for k in range(677)}
        circuit = dfs(graph, k, k, visited)
        if circuit:
            circs.append(circuit)

    return None


def encode(id):
    return (ord(id[0]) - 97) * 26 + ord(id[1]) - 96


def decode(e_id):
    e_id -= 1
    return chr((e_id // 26) + 97) + chr(e_id % 26 + 97)


def get_interconnected(graph, node, visited):
    o_visited = [v for v in visited if v != node]
    if all([v in graph[node] for v in o_visited]):
        visited.append(node)
    else:
        return
    for neib in graph[node]:
        if neib not in visited:
            get_interconnected(graph, neib, visited)


def get_inter(prob):
    conn = {}
    for line in prob:
        a, b = list(map(encode, line.split("-")))
        if a in conn:
            conn[a].append(b)
        else:
            conn[a] = [b]
        if b in conn:
            conn[b].append(a)
        else:
            conn[b] = [a]

    circs = set()
    for k in conn.keys():
        visited = []
        get_interconnected(conn, k, visited)
        if visited:
            circs.add(tuple(sorted(visited)))

    return sorted(circs, key=lambda x: len(x))[-1]


def solve(prob):
    inter = get_inter(prob)
    return ",".join([decode(x) for x in inter])


print(solve(inp_test), "co,de,ka,ta")
print(solve(inp))
