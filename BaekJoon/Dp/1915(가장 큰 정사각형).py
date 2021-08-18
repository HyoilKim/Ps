# my solution
# dp배열 만들 필요가 x
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[int(x) for x in input().rstrip()] for _ in range(n)]
dp = [[0]*m for _ in range(n)]

# dp init
for i in range(m): dp[0][i] = arr[0][i]
for i in range(n): dp[i][0] = arr[i][0]
    
max_len = arr[0][0]
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j]:
            if dp[i-1][j-1] and dp[i][j-1] and dp[i-1][j]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            else:
                dp[i][j] = arr[i][j]
        max_len = max(max_len, dp[i][j])

print(max_len**2) 
'''
좋은 반례
5 5
11100
11110
11111
01111
00111
'''

# simple solution
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])+1

ans = max(max(x) for x in arr)
print(ans*ans)