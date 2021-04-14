from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
A = []; B = []
C = []; D = []
for i in range(n):
    a,b,c,d = map(int, input().split())
    A.append(a); B.append(b)
    C.append(c); D.append(d)

AB = defaultdict(int)
CD = defaultdict(int)
for i in range(n):
    for j in range(n):
        AB[A[i]+B[j]] += 1
        CD[C[i]+D[j]] += 1

total = 0    
for i in AB:
    total += CD[-i]
print(total)
