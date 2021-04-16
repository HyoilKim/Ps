# my solution
# dp
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[-1]

# worst solution
# brute force
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            ans = dfs(i+1) + dfs(i+2)
            return ans
        return dfs(0)
    
# another solution
# recursion + memoization + dp
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if memo[i] > 0:
                return memo[i]

            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]
        
        memo = [0]*(n+1)
        return dfs(0)

# best solution
# fibonacci formula
public class Solution {
    public int climbStairs(int n) {
        double sqrt5=Math.sqrt(5);
        double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
        return (int)(fibn/sqrt5);
    }
}