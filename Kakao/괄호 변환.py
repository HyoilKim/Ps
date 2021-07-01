def is_balanced(s): 
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0

def divide(s):
    cnt = 0
    for i, c in enumerate(s):
        if c == '(': cnt += 1
        else: cnt -= 1
        if i > 0 and cnt == 0:
            u, v = s[:i+1], s[i+1:]
            return u, v

def solution(p):
    if p == '': 
        return ''

    u, v = divide(p)
    
    if is_balanced(u):
        return u+solution(v)
    else:
        s = '('+solution(v)+')'
        for c in u[1:-1]:
            s += ')' if c == '(' else '('
        return s
        