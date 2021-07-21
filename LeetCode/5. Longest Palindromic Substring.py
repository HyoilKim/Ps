from collections import defaultdict
import time
class Solution:
    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            for j in range(i+1 ,len(s)):
                if (j-i) > (end-start) and self._is_palindrome(s, i, j):
                    start, end = i, j

        return s[start:end+1]

    def _is_palindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# best solution
class Solution:
    def longestPalindrome(self, s):
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) < 2 or s==s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result, 
                        expand(i-1,i+1),
                        expand(i, i+1),
                        key=len)

        return result

# another solution(dp)
# example s = 'babad' -- > dp[2][3] = s[2:3] = ba
class Solution:
    def longestPalindrome(self, s): 
        ans_l = ans_r = 0
        dp = [[False]*len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j] and (j-i == 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if ans_r-ans_l < j-i:
                        ans_l, ans_r = i, j

        return s[ans_l:ans_r+1]