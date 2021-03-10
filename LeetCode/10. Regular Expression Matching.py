# backtracking
# ...

# dp
# 1. s[i] == p[i] and p[j] == '.'
# dp[i][j] = dp[i-1][j-1] 

# 2. p[j] == '*' 
# if s[i] == p[j-1] or p[j-1] == '.' 
#   dp[i][j] = dp[i][j-2] || dp[i-1][j] (이전 문자열 1번 이상 반복)
# else
#   dp[i][j] = dp[i][j-2](이전 문자열 0번 반복)

# 3. else
# dp[i][j] = False

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2] 
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = False

        return dp[-1][-1]
