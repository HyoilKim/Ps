from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
graph = [graph]+[[[False]*m for _ in range(n)]]


def bfs(graph):
    queue = deque([[0, 0, 1]]) # x, y, distance
    graph[0][0][0] = -1 # 지나 왔는가

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y, distance = queue.popleft()
        if x == n-1 and y == m-1:
            return distance

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[0][nx][ny]==-1:
                continue

            status, crash = graph[0][nx][ny], graph[1][x][y]
            if status == 0:
                queue.append((nx, ny, distance+1))
                graph[0][x][y] = -1
                graph[1][nx][ny] = crash
            elif status == 1 and not crash:
                print(nx,ny)
                queue.append((nx, ny, distance+1))
                graph[1][nx][ny] = True
        
    return -1

res = bfs(graph)
print(res)

