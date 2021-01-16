def solution(people, limit):
    people.sort()
    count = 0
    for i in range(len(people)):
        weight = people[i]
        if weight == 241:
            continue

        target = limit-weight
        left = 0
        right = len(people)
        while left < right:  # [40, 55, 60, 70]
            mid = (left+right)//2
            if people[mid] > target:
                right = mid
            else:
                left = mid+1
            
        if people[left-1] + weight <= limit and i != left-1: # 찾은 경우
            people[left-1] = 241    
        
        count += 1
    return count

people = [40, 50, 50, 50]
limit = 100
res = solution(people, limit)
print(res)