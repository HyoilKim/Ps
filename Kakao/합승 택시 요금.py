# dijkstra + heap
import heapq
from collections import defaultdict
def solution(n, s, a, b, fares):
    def dijkstra(start):
        dist = [float('inf')]*(n+1)
        heap = [(start,0)]
        dist[start] = 0
        while heap:
            cur, d = heapq.heappop(heap)
            if dist[cur] < d:          # 인접 노드 생략 (이미 구한 거리 < 현재 까지 거리)
                continue 
            for nxt in adj[cur]:
                nd = d+adj[cur][nxt]
                if nd <= dist[nxt]:
                    heapq.heappush(heap, (nxt, nd))
                    dist[nxt] = nd
        return dist
    
    adj = defaultdict(dict)
    for i,j,c in fares:
        adj[i][j] = c
        adj[j][i] = c

    answer = float('inf')
    dp = [[]]+[dijkstra(i) for i in range(1, n+1)]
    for i in range(1, n+1):
        answer = min(answer, dp[s][i]+dp[i][a]+dp[i][b])
    return answer

# clean code (no dijkstra)
def solution(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv