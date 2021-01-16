def solution(number, k):
    answer = []
    num_len = len(number)

    while len(answer) < num_len-k:
        # 짤린 number 길이 - 앞으로 구해야 하는 길이
        c_idx = len(number) - (num_len-k-len(answer)) + 1
        candidate = number[:c_idx]

        max_num = max(candidate)
        max_idx = number.index(max_num)
        number = number[max_idx+1:]

        answer.append(max_num)
        
        if len(number) == num_len-k-len(answer):
            answer += number

    answer = ''.join(answer)
    return answer

number = "1231234"
k = 3
res = solution(number, k)
print(res)

# best solution 1
def solution(number, k):
    answer = []
    count = 0
    for i in number:
        if count == k:
            answer.append(i)
        else:
            if not answer:
                answer.append(i)
            else:
                while answer:
                    if i <= answer[-1] or count == k: 
                        break
                    if i > answer[-1]: # i보다 작은 수를 k개 만큼 제거
                        answer.pop()
                        count += 1
                answer.append(i)
    
    while count != k: # 크기순으로 정렬되어 있어, k개를 빼지 못한 경우
        answer.pop()
        count += 1
    return ''.join(answer)

# best solution2
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
