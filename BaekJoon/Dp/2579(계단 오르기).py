import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0]*n

for i in range(n):
    if i == 0:
        dp[0] = arr[0]
    elif i == 1:
        dp[i] = arr[0]+arr[1]
    elif i == 2:
        dp[i] = max(dp[i-2]+arr[i], arr[i-1]+arr[i])
    else:
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(dp[-1])