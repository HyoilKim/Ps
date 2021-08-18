import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+arr[i][j])
        elif j < i:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+arr[i][j], dp[i-1][j]+arr[i][j])
        elif j == i:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+arr[i][j])
            
print(max(dp[-1]))