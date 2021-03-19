import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
while left <= right:
    height = (left+right)//2
    total = 0
    for i in trees:
        if i > height:
            total += i-height
    if total < M:
        right = height-1
    else:
        left = height+1

print(left-1)