def solution(s):
    stack = []
    ans = 0
    tmp = 1
    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            stack.append(ch)
            tmp *= 2
        elif ch =='[':
            stack.append(ch)
            tmp *= 3
        elif ch == ')' and stack:
            if s[i-1] == '(': ans += tmp
            if stack[-1] == '(': stack.pop()
            else: return 0
            tmp //= 2
        elif ch == ']' and stack:
            if s[i-1] == '[': ans += tmp
            if stack[-1] == '[': stack.pop()
            else: return 0
            tmp //= 3
        else:
            return 0

    return ans if len(stack) == 0 else 0
 

s = input()
print(solution(s))
