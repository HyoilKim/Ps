# 1부터 bfs 0이면 지나가고 -1로 바꿈
# 시작이 여러개 -> 하나의 큐로 해결
# 리턴 값 출력 할 때 
# bfs 횟수 만큼 return
# 처음에 0인 토마토가 없으면 return 0
# bfs 끝나고 안익은 토마토 있으면 -1

from collections import deque

def find_raw(graph):
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                return True
    return False
    
def bfs(graph):
    if not find_raw(graph):
        return 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                queue.append((i, j, 0))

    res = -1
    while queue:
        x, y, count = queue.popleft()
        graph[x][y] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = -1
                queue.append((nx, ny, count+1))
                if res < count+1:
                    res = count+1
    return res

n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

count = bfs(graph) 

if find_raw(graph): # 덜 익은 경우
    print(-1)
else:               # 모두 익었은 경우 
    print(count)