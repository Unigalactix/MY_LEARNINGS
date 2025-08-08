"""BFS and DFS on an undirected graph using adjacency list
"""
from collections import deque, defaultdict


def build_graph(edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g


def bfs_order(g, start):
    seen = {start}
    q = deque([start])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return order


def dfs_order(g, start):
    seen = set()
    order = []

    def dfs(u):
        seen.add(u)
        order.append(u)
        for v in g[u]:
            if v not in seen:
                dfs(v)

    dfs(start)
    return order


def shortest_path_unweighted(g, src, dst):
    # BFS to reconstruct path
    from collections import deque
    q = deque([src])
    parent = {src: None}
    while q:
        u = q.popleft()
        if u == dst:
            break
        for v in g[u]:
            if v not in parent:
                parent[v] = u
                q.append(v)
    if dst not in parent:
        return []
    # reconstruct
    path = []
    cur = dst
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]


def _test():
    edges = [(1,2),(2,3),(1,4),(4,5),(5,3)]
    g = build_graph(edges)
    b = bfs_order(g, 1)
    d = dfs_order(g, 1)
    sp = shortest_path_unweighted(g, 1, 3)
    assert b[0] == 1 and set(b) == {1,2,3,4,5}
    assert d[0] == 1 and set(d) == {1,2,3,4,5}
    assert sp[0] == 1 and sp[-1] == 3
    print("graphs bfs/dfs OK")


if __name__ == "__main__":
    _test()
