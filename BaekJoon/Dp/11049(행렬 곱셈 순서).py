# dp + memoization + dfs
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')]*n for _ in range(n)]

def dfs(s, e):
    if dp[s][e] != float('inf'): return dp[s][e]
    if s == e: return 0

    for i in range(s, e):
        total = dfs(s,i)+dfs(i+1,e)+arr[s][0]*arr[i][1]*arr[e][1] # 점화식
        dp[s][e] = min(dp[s][e], total)
    return dp[s][e]

print(dfs(0, n-1))