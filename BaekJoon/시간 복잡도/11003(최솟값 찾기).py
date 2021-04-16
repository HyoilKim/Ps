# best solution
# deque
# O(N)
from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
for i in range(len(arr)):
    if dq and dq[0][1] <= i-L:
        dq.popleft()
    while dq and dq[-1][0] > arr[i]:
        dq.pop()
    
    dq.append((arr[i], i))
    print(dq[0][0], end=' ')
    
# my solution
# sliding window, binary search
# O(NlogN) - 시간초과
from bisect import bisect_left
window = []
for i in range(len(arr)):
    if i >= L:
        del window[bisect_left(window, arr[i-L])]

    num = arr[i]
    index = bisect_left(window, num)
    window.insert(index, num)
    print(window[0], end=' ')