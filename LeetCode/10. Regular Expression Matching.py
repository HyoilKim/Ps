# best solution
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

# recursion(no kleene star)
def match(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])

'''
If a star is present in the pattern, it will be in the second position pattern[1]. 
Then, we may ignore this part of the pattern, or delete a matching character in the text. 
If we have a match on the remaining strings after any of these operations, then the initial inputs matched.
'''
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or # 이전 문자열 0번 반복(first_match 와 관계없이 실행)
                    first_match and self.isMatch(text[1:], pattern)) # first_match인 경우, 이전 문자열 n번 반복
        else:
            return first_match and self.isMatch(text[1:], pattern[1:]) # *없는 경우