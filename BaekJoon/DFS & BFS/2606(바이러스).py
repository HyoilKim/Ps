n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(int(input())):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

def dfs(graph, v, path):
    path.append(v)
    for next_v in range(1, n+1):
        if graph[v][next_v] == 1 and next_v not in path:
            dfs(graph, next_v, path)
    return

path = []
dfs(graph, 1, path)
print(len(path)-1)