from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, x, y):
    queue = deque([[x,y,1]])
    while queue:
        x, y, count = queue.popleft()
        graph[x][y] = 0
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny,count+1))
            if nx == n-1 and ny == m-1:
                return count+1

    return -1   
    
print(bfs(graph, 0, 0))