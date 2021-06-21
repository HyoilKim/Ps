import sys, heapq
input = sys.stdin.readline

tc = int(input())
heapl = [] # max heap
heapr = [] # min heap
res = []
for i in range(tc):
    n = int(input())
    if i % 2 == 0:
        heapq.heappush(heapl, (-n, n))
    else:
        heapq.heappush(heapr, n)

    if i > 0 and heapl[0][1] > heapr[0]:
        k = heapq.heappop(heapr)
        heapq.heappush(heapl, (-k, k))
        heapq.heappush(heapr, heapq.heappop(heapl)[1])
    res.append(heapl[0][1])
for n in res:
    print(n)