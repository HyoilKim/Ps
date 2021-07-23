# best solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        length = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    length = i-stack[-1]
                    max_length = max(length, max_length)
                else:
                    stack.append(i)
        return max_length

# clean code
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans, stack = 0, [-1]
        for i, c in enumerate(s):
            if c == ")":
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                    continue
            stack.append(i)
        return ans

# another solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def solution(s, direction):
            max_length = 0
            left = 0
            right = 0
            for ch in s:
                if ch == '(':
                    left += 1
                else:
                    right += 1
                    
                if left == right:
                    max_length = max(left+right, max_length)
                else:
                    if direction == "r" and right > left: 
                        left = right = 0
                    elif direction == "l" and left > right:
                        left = right = 0
            return max_length

        return max(solution(s, "r"), solution(s[::-1], "l"))

# another solution(dp)
class Solution(object):
    def longestValidParentheses(self, s):
        dp = [0]*len(s)
        max_len = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2] if dp[i-1] > 0 else 0
                max_len = max(max_len, dp[i])
        return max_len