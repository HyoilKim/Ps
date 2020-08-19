import itertools
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split())) # + - * /
res = []

def back(add, sub, mul, div, cnt, val):
    if cnt == n:
        res.append(val)
    if add > 0:
        back(add-1, sub, mul, div, cnt+1, val+nums[cnt])
    if sub > 0:
        back(add, sub-1, mul, div, cnt+1, val-nums[cnt])
    if mul > 0:
        back(add, sub, mul-1, div, cnt+1, val*nums[cnt])
    if div > 0:
        if val < 0:
            back(add, sub, mul, div-1, cnt+1, -((-val) // nums[cnt]))
        else:
            back(add, sub, mul, div-1, cnt+1, val // nums[cnt])

back(op[0], op[1], op[2], op[3], 1, nums[0])
print(max(res))
print(min(res))