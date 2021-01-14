from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0 , 0, 1, -1]
    
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count
            
dangi_num = 0
house_num = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dangi_num += 1
            house_num.append(bfs(i, j))

print(dangi_num)
house_num.sort()
for i in house_num:
    print(i)
            



