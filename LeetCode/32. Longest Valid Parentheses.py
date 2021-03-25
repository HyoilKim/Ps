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
