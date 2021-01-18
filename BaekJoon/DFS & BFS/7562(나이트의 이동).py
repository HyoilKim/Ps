from collections import deque

n = int(input())

for _ in range(n):
    m = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    queue = deque([[start_x, start_y, 0]])
    visited = [[False]*m for _ in range(m)]
    dx = [-2, -2, 2, 2, -1, -1, 1, 1]
    dy = [-1, 1, -1, 1, -2, 2, -2, 2]
    while queue:
        x, y, count = queue.popleft()
        if x == end_x and y == end_y:
            print(count)
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            
            queue.append((nx, ny, count+1))
            visited[nx][ny] = True
        