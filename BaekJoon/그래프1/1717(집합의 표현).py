import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    elif cmd == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
