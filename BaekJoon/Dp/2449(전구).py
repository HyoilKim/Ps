# dp[s][e]
# s부터 e까지의 전구를 모두 같은 색으로 맞추는데 필요한 최소 횟수

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
dp = [[float('inf')]*n for _ in range(n)]

def solve(s, e):
    if s == e: return 0
    if dp[s][e] != float('inf'): return dp[s][e]
    print(s,e)
    for i in range(s, e):
        cnt = 0 if arr[s] == arr[i+1] else 1
        dp[s][e] = min(dp[s][e], solve(s, i) + solve(i+1, e) + cnt)

    return dp[s][e]

print(solve(0,n-1))