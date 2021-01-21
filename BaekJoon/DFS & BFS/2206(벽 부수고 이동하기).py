from collections import deque

def bfs(graph):
    queue = deque([[0, 0, 0, 1]]) # x, y, crash, distance
    visited[0][0][0] = 1
    while queue:
        x, y, crash, distance = queue.popleft()
        if x == n-1 and y == m-1:
            return distance
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny][crash]:
                continue
            visited[nx][ny][crash] = 1
            if graph[nx][ny] == 0:
                queue.append((nx, ny, crash, distance+1))
            elif graph[nx][ny] == 1 and crash == 0:
                queue.append((nx, ny, 1, distance+1))
                
    return -1

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]  # 벽을 깨고 가는 경우 / 벽을 깨지 않은 경우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = bfs(graph)
print(res)

'''
0000
1110
0000
1111
0111
0000
'''