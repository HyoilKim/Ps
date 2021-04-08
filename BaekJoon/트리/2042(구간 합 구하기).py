import sys
input = sys.stdin.readline

def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i &= i-1
        # i -= (i & -i)
    return result

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

n, m, k = map(int, input().split())
data = [0]+[int(input()) for _ in range(n)]
tree = [0]*(n+1)

for i in range(1, n+1):
    update(i, data[i])
    
for _ in range(m+k):
    a, b ,c = map(int, input().split())
    if a == 1:
        update(b, c-data[b])
        data[b] = c
    else:
        print(interval_sum(b, c))