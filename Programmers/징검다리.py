def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.append(distance)
    rocks.sort()

    while left <= right:
        mid = (left+right)//2
        prev = 0
        remove_count = 0
        diff_min = float('inf')
        
        for i in range(len(rocks)):
            if rocks[i]-prev < mid:
                remove_count += 1
            else:
                diff_min = min(diff_min, rocks[i]-prev)
                prev = rocks[i]
                
        # '최대' diff_min을 찾기 때문에 '<=' 조건에서 answer 할당
        # 입국심사 문제는 '최소'를 찾기 때문에 '>=' 조건에서 할당
        if remove_count <= n: 
            left = mid+1
            answer = diff_min
        else:
            right = mid-1

    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
solution(distance, rocks, n)
