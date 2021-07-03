# my solution
# eval - so slow
import math
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                n1, n2 = stack.pop(), stack.pop()
                n = eval(n2+token+n1)
                if token == '/':
                    n = math.ceil(n) if n < 0 else math.floor(n)
                stack.append(str(n))
            else:
                stack.append(token)
        return stack.pop()

# another solution
# more readable
class Solution:
    def evalRPN(self, tokens):
        stack = []
        def f(a, b, c):
            if c == "+": return a+b
            if c == "-": return b-a
            if c == "*": return a*b
            if c == "/": return int(b/a)
            
        for token in tokens:
            if token in "*/+-":
                stack.append(f(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))
        return stack[-1]