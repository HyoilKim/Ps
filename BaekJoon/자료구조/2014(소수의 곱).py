# 정렬을 반복해서 해야 된다면? -> priority queue를 떠올려 보자
# pq에서 최솟값을 꺼내어 각 소수들과 곱하여 pq에 다시 넣는다

import sys, heapq
input = sys.stdin.readline

k, n = map(int, input().split())
primes = list(map(int, input().rstrip().split()))
pq = list(primes)
heapq.heapify(pq)

for _ in range(n):
    head = heapq.heappop(pq)
    for prime in primes:
        heapq.heappush(pq, head*prime)
        print(head, prime)
        if head % prime == 0: # 중복처리
            break
        
print(head)
