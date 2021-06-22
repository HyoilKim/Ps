import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewelrys = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewelrys.sort()
bags.sort()

money = 0
possible = []
for bag in bags:
    while jewelrys and bag >= jewelrys[0][0]:
        # 무게 순서로 비교하기 때문에
        # heap 에서 가치 순서로 재정렬 해야 함
        heapq.heappush(possible, (-jewelrys[0][1], jewelrys[0][1]))
        heapq.heappop(jewelrys) 
    if possible:
        money += heapq.heappop(possible)[1]
    elif not jewelrys:
        break
        
print(money)
