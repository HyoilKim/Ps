import sys
input = sys.stdin.readline
arr1 = input().rstrip()
arr2 = input().rstrip()

dp = [[0]*len(arr2) for _ in range(len(arr1))]
result = 0

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            if i > 0 and j > 0 and arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        result = max(result, dp[i][j])
print(result)

# simple code
for i in range(1, len(arr1)+1):
    for j in range(1, len(arr2)+1):
        if arr1[j - 1] == arr2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        ans = max(ans, dp[i][j])