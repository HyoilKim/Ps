# my solution
# bst
import sys, bisect
from collections import defaultdict
input = sys.stdin.readline

n, h = map(int, input().split())
odd = []
even = []
for i in range(1, n+1):
    height = int(input())
    if i % 2 == 0:
        even.append(height)
    else:
        odd.append(height)
odd.sort()
even.sort()

min_crash = n+1
dic = defaultdict(int)
for i in range(1, h+1):
    odd_crash = len(odd) - bisect.bisect_left(odd, i)
    even_crash = len(even) - bisect.bisect_right(even, h-i)
    crash = odd_crash + even_crash
    dic[crash] += 1
    min_crash = min(min_crash, crash)

print(min_crash, dic[min_crash])

# another solution
# cummulative sum
n, h = map(int, input().split())

up = [0]*(h+1)    # 석순
down = [0]*(h+1)  # 종유석

min_cnt = n    # 파괴해야 하는 장애물의 최소값
range_cnt = 0        # 최소값이 나타나는 구간의 수

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

# up[i]: i 구간으로 갔을 경우 파괴되는 석순
for i in range(h-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

for i in range(1, h+1):
    if min_cnt > (down[i] + up[h-i+1]):
        min_cnt = (down[i] + up[h-i+1])
        range_cnt = 1
    elif min_cnt == (down[i] + up[h-i+1]):
        range_cnt += 1

print(min_cnt, range_cnt)