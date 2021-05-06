from collections import deque
def solution(board):
    dx = [1,0,-1,0] # 남,동,북,서
    dy = [0,1,0,-1]
    q = deque([(0,0,0,-1)])

    N = len(board)
    dp = [[1000000]*N for _ in range(N)]
    dp[0][0] = 0

    while q:
        x, y, c, d = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0:
                    if d == -1 or d == i:
                        if c+100 <= dp[nx][ny]:
                            dp[nx][ny] = c+100
                            q.append((nx, ny, c+100, i))
                    elif d != i:
                        if c+600 <= dp[nx][ny]:
                            dp[nx][ny] = c+600
                            q.append((nx, ny, c+600, i))
    return dp[-1][-1]

