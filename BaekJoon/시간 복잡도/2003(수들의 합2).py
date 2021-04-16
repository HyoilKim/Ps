N, M = map(int, input().split())
A = [x for x in map(int, input().split())]
l, r = 0, 0
count = 0
total = A[0]
while l < len(A) and r < len(A):
    if total == M:
        count += 1
    if total <= M:
        r += 1
        if r == len(A):
            break
        total += A[r]
    else:
        total -= A[l]
        l += 1
print(count)

# best solution
# 가독성이 뛰어남
count = 0
end = 0
interval_sum = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += data[end]
        end += 1
    if interval_sum == M:
        count += 1
    interval_sum -= data[start]

