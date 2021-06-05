import heapq
import sys
input = sys.stdin.readline

heap = []
tc = int(input())
for _ in range(tc):
    n = int(input())
    if n == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-n, n)) # (priority, value)
