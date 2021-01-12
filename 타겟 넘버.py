answer = 0

def dfs(arr, idx, target, total):
    if idx == len(arr):
        if total == target:            
            global answer
            answer += 1
        return 
    dfs(arr, idx+1, target, total+arr[idx])
    dfs(arr, idx+1, target, total-arr[idx])
    
def solution(numbers, target):
    dfs(numbers, 0, target, 0)
    return answer

'''
다른 풀이

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''