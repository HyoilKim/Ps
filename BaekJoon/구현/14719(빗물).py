import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, len(arr)-1
left_max, right_max = 0, 0
total = 0

while l < r:
    left, right = arr[l], arr[r]
    left_max = max(left_max, left)
    right_max = max(right_max, right)

    if left_max < right_max:
        total += left_max-arr[l]
        l += 1
    else:
        total += right_max-arr[r]
        r -= 1

print(total)
