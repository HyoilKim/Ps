# 1st try
n = input()
times = map(int, input().split(' '))
times = sorted(times)

sum = 0
waitTime = 0
for i in times:
    sum += (i + waitTime)
    waitTime += i

print(sum)

# 2nd try
import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()

total = 0
pre_sum = 0
for t in time:
    total += t + pre_sum
    pre_sum += t

print(total)
