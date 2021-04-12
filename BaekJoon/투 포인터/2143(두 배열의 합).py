from collections import defaultdict
import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dic = defaultdict(int)
ans = 0

for i in range(n):
    t = 0
    for j in range(i, n):
        t += A[j]
        dic[t] += 1

for i in range(m):
    t = 0
    for j in range(i, m):
        t += B[j]
        ans += dic[target - t]

print(ans)

# another solution 1
# dicA와 dicB를 key 값으로 정렬하고
# 투 포인터를 사용해서 합이 target인 경우

# another solution 2
# target - dicA 값을 dicB의 key를 정렬한 이후
# binary search로 탐색 이후 value 조회
