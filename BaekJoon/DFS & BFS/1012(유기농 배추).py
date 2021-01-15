from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    worm = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                worm += 1
                queue = deque([[x,y]])
                graph[y][x] = 0

                while queue:
                    _x, _y = queue.popleft()
                    for k in range(4):
                        nx = _x+dx[k]
                        ny = _y+dy[k]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if graph[ny][nx] == 1:
                            graph[ny][nx] = 0
                            queue.append((nx, ny))
    print(worm)