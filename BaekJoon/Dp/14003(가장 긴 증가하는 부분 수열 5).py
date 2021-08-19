import sys, bisect
input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))
arr, lis_len = [], []
for num in nums:
    idx = bisect.bisect_left(arr, num)
    lis_len.append(idx+1)
    if idx == len(arr):
        arr.append(num)
    else:
        arr[idx] = num

result = []
length = max(lis_len)
for i in range(len(lis_len)-1, -1, -1):
    if lis_len[i] == length:
        result.append(nums[i])
        length -= 1

print(len(result))
for i in reversed(result):
    print(i, end=' ')