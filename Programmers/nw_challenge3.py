def dfs(arr, sorted_arr, k, cnt):
    if arr == sorted_arr:
        global min_cnt
        min_cnt = min(min_cnt, cnt)
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if j-i <= k and arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                dfs(arr, sorted_arr, k, cnt+1)
                arr[j], arr[i] = arr[i], arr[j]

min_cnt = 0 
def solution(arr, k):
    global min_cnt
    min_cnt = len(arr) ** 2
    sorted_arr = sorted(arr)
    dfs(arr, sorted_arr, k, 0)
    return min_cnt