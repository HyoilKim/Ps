# 136ms
# time - O(2^2N*N)
# space - O(N)
class Solution:
    def generateParenthesis(self, n: int):
        def generate(i, strs):
            if i == 2*n:
                if valid(strs):
                    result.append(strs)
                return
            generate(i+1, strs+"(")
            generate(i+1, strs+")")
      
        def valid(strs):
            stack = []
            for i in strs:
                if i == '(':
                    stack.append(i)
                elif i == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return len(stack) == 0
        
        result = []
        generate(0, "")      
        return result

# 44ms
# time - O(2^2N/sqrt(N))
# space - O(N)
class Solution:
    def generateParenthesis(self, n: int):
        def backtracking(i, strs, stack):
            if i == 2*n:
                if len(stack) == 0:
                    result.append(strs)
                return

            backtracking(i+1, strs+"(", stack+['('])
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
                backtracking(i+1, strs+")", stack)
        
        result = []
        backtracking(0, "", [])
        return result

# best solution(36ms)
class Solution:
    def generateParenthesis(self, n):
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        ans = []
        backtrack()
        return ans