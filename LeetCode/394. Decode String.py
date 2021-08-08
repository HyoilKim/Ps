# time - O(N)
# space - O(N)
class Solution(object):
    def decodeString(self, s):
        # stack 의 마지막에 지금까지 계산한 string을 저장
        stack = [["", 1]] # (str, num)
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]