from collections import deque
def solution(places):
    def is_safe(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visited = [[False]*5 for _ in range(5)]
                    visited[i][j] = True
                    queue = deque([(i,j,0)])
                    while queue:
                        r,c,d = queue.popleft()
                        if place[r][c] == 'P' and 0 < d <= 2:
                            return 0
                        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < 5 and 0 <= nc < 5:
                                if visited[nr][nc]: continue
                                if place[nr][nc] == 'X': continue
                                queue.append((nr,nc,d+1))
                                visited[nr][nc] = True
        return 1
    
    answer = []
    for place in places:
        answer.append(is_safe(place))
                    
    return answer