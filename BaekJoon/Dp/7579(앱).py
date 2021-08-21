import sys
input = sys.stdin.readline


n, m = map(int, input().split())
bytes = list(map(int, input().split()))
costs = list(map(int, input().split()))

# dp[i][j]: i번째 까지의 앱과 j의 코스트를 가지고, 
#            부분적으로 앱을 비활성화 했을 때,
#            확보 할 수 있는 최대 메모리 값
# 메모리 기준이 아니라 cost 기준으로 dp배열을 만들어야 메모리 초과가 나지 않음
dp = [[0]*(sum(costs)+1) for _ in range(n+1)]
result = sum(costs)

for i, (byte,cost) in enumerate(zip(bytes, costs)):
    for j in range(1, sum(costs)+1):
        # cost: 현재 메모리를 비활성화 했을 때 드는 비용
        # j가 cost보다 작으니 비활성화 하지 못하고
        # 이전 앱의 최대 메모리 값을 가져옴
        if j < cost: 
            dp[i][j] = dp[i-1][j]
        # 현재 cost로 해당 메모리를 비활성화 할 수 있음
        # 단 비활성화 하는 것이 효율적인지 판단
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost]+byte)
        
        if dp[i][j] >= m:
            result = min(result, j)

print(result)
