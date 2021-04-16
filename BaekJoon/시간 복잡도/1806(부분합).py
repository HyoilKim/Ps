N, M = map(int, input().split())
arr = list(map(int, input().split()))

def solution():
    left = 0; right = 0
    min_len = N+1
    sub_sum = arr[left]
    while left < N and right < N:
        if sub_sum >= M:
            min_len = min(min_len, right-left+1)
            sub_sum -= arr[left]
            left += 1
        else:
            right += 1
            if right == N:
                break
            sub_sum += arr[right]

    if min_len == N+1:
        return 0
    return min_len
    
print(solution())