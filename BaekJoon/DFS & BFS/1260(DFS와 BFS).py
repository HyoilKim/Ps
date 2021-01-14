from collections import deque

def dfs(graph, v, path):
    path.append(v)

    for next_v in range(1, n+1):
        if graph[v][next_v] == 1 and next_v not in path:
            dfs(graph, next_v, path)

    return path

def bfs(graph, v):
    queue = deque([v])
    path = [v]
    while queue:
        cur = queue.popleft()
        for next_v in range(1, n+1):
            if graph[cur][next_v] == 1 and next_v not in path:
                queue.append(next_v)
                path.append(next_v)

    return path


n, m, start = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1


dfs_res = dfs(graph, start, [])
bfs_res = bfs(graph, start)
print(' '.join(map(str, dfs_res)))
print(' '.join(map(str, bfs_res)))