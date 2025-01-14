def find_shortest_path(graph, a, b):
    q = [a]
    st = set()
    checked = set()
    dct = {a: [None, 0]}
    while q:
        q_copy = q[:]
        q = []
        while q_copy:
            cur = q_copy.pop(0)
            for edge in graph[cur]:
                if edge[0] in checked:
                    continue
                if edge[0] not in st:
                    st.add(edge[0])
                    q.append(edge[0])
                if edge[0] not in dct:
                    dct[edge[0]] = [-1, float('inf')]
                if edge[1] + dct[cur][1] < dct[edge[0]][1]:
                    dct[edge[0]] = [cur, edge[1] + dct[cur][1]]
            checked.add(cur)
    path = []
    cur = b
    while cur is not None:
        path.append(str(cur))
        cur = dct[cur][0]
    path.reverse()
    return ["->".join(path), dct[b][1]]