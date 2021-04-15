import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0, -1, 1, 1, -1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

if __name__ == '__main__':
    N = int(input())
    A = [' '.join(input()).split() for _ in range(N)]
    H = [list(map(int, input().split())) for _ in range(N)]
    num_of_house = 0
    height_list = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'P':
                sx, sy = i, j
            if A[i][j] == 'K':
                num_of_house += 1
            height_list.append(H[i][j])

    # 높이 중복제거 및 정렬
    height_set = sorted(set(height_list))
    left, right = 0, 0
    ans = sys.maxsize
    while left < len(height_set):
        visit = [[False]*N for _ in range(N)] 
        h = H[sx][sy] 
        queue = deque()
        K = 0 # 방문한 집의 개수

        if height_set[left] <= h <= height_set[right]: 
            visit[sx][sy] = True
            queue.append((sx, sy))

        while queue:
            x, y = queue.popleft()
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if visit[nx][ny]: continue
                    if height_set[left] <= H[nx][ny] <= height_set[right]:
                        visit[nx][ny] = True
                        queue.append((nx, ny))
                        if A[nx][ny] == 'K': 
                            K += 1

        if K == num_of_house:
            ans = min(ans, height_set[right] - height_set[left]) 
            left += 1 
        elif right + 1 < len(height_set): 
            right += 1
        else: 
            break
    print(ans)

# reference: https://baby-ohgu.tistory.com/20