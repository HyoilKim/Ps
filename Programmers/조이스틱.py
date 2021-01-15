# def solution(name):
#     answer = 0
#     for x in name:
#         if x <= 'M':
#             move = ord(x)-ord('A')
#         else: # 뒤로 가는게 빠른 경우
#             move = ord('Z')-ord(x)+1
#         answer += move

#     return answer+len(name)-1

# print(solution("JZAAAAAAAZ"))

# best solution
def solution(name):
    change = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    idx = 0
    answer = 0

    while True:
        answer += change[idx]
        print(answer)
        change[idx] = 0
        if sum(change) == 0:
            return answer
        
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
            
        answer += left if left < right else right
        idx += -left if left < right else right

print(solution("JAZ"))