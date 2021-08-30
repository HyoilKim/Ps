def solution(s):
    min_len = len(s)
    for n in range(1,(len(s)//2)+1):
        length = 0
        i = 0
        while i < len(s):
            token = s[i:n+i]
            iter = -1
            while token == s[i:n+i]:
                i += n
                iter += 1
                
            if iter > 0:
                length += n+len(str(iter+1))
            else:
                length += len(token)
        min_len = min(min_len, length)
    return min_len

# second try fail