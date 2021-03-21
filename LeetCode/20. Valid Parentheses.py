class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '[':']', '{':'}'}
        
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif stack and dic[stack[-1]] == ch:
                stack.pop()
            else:
                return False

        # 같은 문법이지만 가독성이 좋음
        # return stack == []       
        if len(stack) > 0:
            return False
        else:
            return True
