# my solution
# time - O(N^2)
# space - O(1)
class Solution:
    def countSubstrings(self, s):
        def palindrome_nums(l, r):
            cnt = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]: 
                    return cnt
                cnt += 1
                l -= 1
                r += 1
            return cnt
        
        result = 0
        for i in range(len(s)):
            result += palindrome_nums(i, i+1)
            result += palindrome_nums(i, i)
        return result

# dp solution
# time - O(N^2)
# space - O(N^2)
class Solution:   
    def countSubstrings(s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = True
            count += 1
            for j in range(i+1, len(s)):
                if j == i+1 and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
                if j>i+1 and dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
        return count

# brute force
# time - O(n^3)
# space - O(N^2)
class Solution:
    def countSubstrings(self, s):
        return sum(s[i:j] == s[i:j][::-1] for j in range(len(s) + 1) for i in range(j))