import sys

def solution(n, times):
    left = 1
    right = max(times)*n
    answer = sys.maxsize

    while left <= right:
        mid = (left+right)//2
        total = 0
        for i in range(len(times)):
            total += mid//times[i]

        if total < n:
            left = mid+1
        else:
            if mid < answer:
                answer = mid
            right = mid-1
    print(answer)
    return answer

n = 7
times = [8,10]
solution(n, times)