def step1(s):
    return s.lower()

def step2(s):
    result = ""
    for ch in s:
        if ord('a') <= ord(ch) <= ord('z') or ch.isdigit() or ch == '_' or ch == '-' or ch == '.':
            result += ch
    return result

def step3(s):
    i = 0
    result = ""
    while i < len(s):
        if s[i] == '.':
            while i < len(s)-1 and s[i+1] == '.':
                i += 1
            result += '.'
        else:
            result += s[i]
        i += 1
    return result

def step4(s):
    result = s
    if len(s) == 0:
        return result
    else:
        if result[0] == '.': 
            result = result[1:]
        if s[-1] == '.': 
            result = result[:-1]
    return result

def step5(s):
    if s == "":
        return 'a'
    return s

def step6(s):
    result = s
    if len(s) >= 16:
        if s[14] == '.':
            result = s[:14]
        else:
            result = s[:15]
    return result

def step7(s):
    if len(s) <= 2:
        return s+s[-1]*(3-len(s))
    return s

def solution(new_id):
    answer = ''
    answer = step4(step3(step2(step1(new_id))))
    answer = step7(step6(step5(answer)))
    return answer

print(solution(input()))


# second try
def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    tmp = ''
    for ch in new_id:
        if ch.isdigit() or ch.isalpha() or ch in '-_.':
            tmp += ch
    new_id = tmp
    
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # 4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    # 5단계
    if new_id == '':
        new_id = 'a'
        
    # 6단계
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <= 2:
        new_id += new_id[-1]*(3-len(new_id))
    
    return new_id