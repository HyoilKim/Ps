# bfs solution(dfs timeover)
# 728ms, 15.2MB
from collections import deque
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        queue = deque([(0, 0)])
        visited = set()
        while queue:
            cur, cnt = queue.popleft()
            if cur == amount: 
                return cnt
            for nxt in coins:
                if cur+nxt <= amount and cur+nxt not in visited:
                    queue.append((cur+nxt, cnt+1))
                    visited.add(cur+nxt)
        
        return -1

# dp solution
# 1608ms, 14.8MB
'''
Assume dp[i] is the fewest number of coins making up amount i, 
then for every coin in coins, dp[i] = min(dp[i - coin] + 1).

The time complexity is O(amount * coins.length) and 
the space complexity is O(amount)
'''
class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]