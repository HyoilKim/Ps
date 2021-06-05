import sys
from bisect import bisect_left
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def post_order(start, end):
    if start > end: 
        return
    division = bisect_left(nums, nums[start], start+1, end+1) # nums[start] 보다 크고 가장 왼쪽에 있는 값
    post_order(start+1, division-1) # left child
    post_order(division, end)       # right child
    print(nums[start])              # post order

nums = []
while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break
post_order(0, len(nums)-1)
