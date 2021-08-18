import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cumsum = [0]*(n+1)
for i in range(1, n+1):
    cumsum[i] = arr[i-1]+cumsum[i-1]
    
for _ in range(m):
    s, e = map(int, input().split())
    print(cumsum[e]-cumsum[s-1])