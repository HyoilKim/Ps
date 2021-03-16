# NUM X : apppend(X)
# POP : pop()
# INV : append(-1*pop())
# DUP : append(peek())
# SWP : a=pop(), b=pop(), append(b), append(a)
# ADD : "", append(a+b)
# SUM : "", append(a-b)
# MUL : "", append(a*b)
# DIV : "", append(b//a)
# MOD : "", append(abs(b)%abs(a)) * -개수 
# pop() == None, 0으로 나눌 때, res > 10**9 -> Error
import sys
input = sys.stdin.readline

def gostack(cmd_list, n):
    stack = [n]
    for cmd in cmd_list:
        # print(cmd[0], stack)
        try:
            if cmd[0] == "NUM":
                num = int(cmd[1])
                stack.append(num)
            elif cmd[0] == "POP":
                stack.pop()
            elif cmd[0] == "INV":
                stack[-1] *= -1
            elif cmd[0] == "DUP":
                stack.append(stack[-1])
            elif cmd[0] == "SWP":
                stack[-2], stack[-1] = stack[-1], stack[-2]
            elif cmd[0] == "ADD":
                stack.append(stack.pop()+stack.pop())
            elif cmd[0] == "SUB":
                stack.append(-1*stack.pop()+stack.pop())
            elif cmd[0] == "MUL":
                stack.append(stack.pop()*stack.pop())
            elif cmd[0] == "DIV":
                sign = 1 if stack[-1]*stack[-2] else -1
                a = abs(stack.pop())
                b = abs(stack.pop())
                stack.append((b // a) * sign)
            elif cmd[0] == "MOD":
                sign = 1 if stack[-1]*stack[-2] else -1
                a = abs(stack.pop())
                b = abs(stack.pop())
                stack.append((b % a) * sign)
        except:
            return "ERROR"
        finally:
            if len(stack) > 0 and abs(stack[-1]) > 10**9:
                return "ERROR"

    if len(stack) != 1:
        return "ERROR"
    else:
        return stack[-1]

cmd_list = []
while True:
    cmd = input().split()
    if cmd[0] == "QUIT":
        break
    else:
        cmd_list.append(cmd)
        if cmd[0] == "END":
            tc = int(input())
            for _ in range(tc):
                n = int(input())
                print(gostack(cmd_list, n))
            cmd_list = []
            input()
