n = input()
times = map(int, input().split(' '))
times = sorted(times)

sum = 0
waitTime = 0
for i in times:
    sum += (i + waitTime)
    waitTime += i

print(sum)

# 1 2 3 3 4