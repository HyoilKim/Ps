# brute force - O(2^(n+m))
class Solution:
    def __init__(self):
        self.answer = 0
        
    def uniquePaths(self, m: int, n: int) -> int:
        self.dfs(0, 0, m, n)
        return self.answer
    
    def dfs(self, x, y, m, n):
        if x == m-1 and y == n-1:
            self.answer += 1
            return
        if x >= m or y >= n:
            return
        
        self.dfs(x+1, y, m, n)
        self.dfs(x, y+1, m, n)
    
# Memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
    
        for i in range(n): dp[0][i] = 1
        for i in range(m): dp[i][0] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]