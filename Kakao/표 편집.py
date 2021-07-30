def solution(n, k, cmd):
    prev = [0] + [i for i in range(n-1)]
    nxt = [i for i in range(1, n)] + [n-1]
    stack = []
    last = n-1
    
    for c in cmd:
        c = c.split()
        if c[0] == 'D':
            for _ in range(int(c[1])):
                k = nxt[k]
        elif c[0] == 'C':
            stack.append((k, nxt[k], prev[k])) 
            if k == last:
                last = k = prev[k]
            else:
                nxt[prev[k]] = nxt[k]
                prev[nxt[k]] = prev[k]
                k = nxt[k]
        elif c[0] == 'U':
            for _ in range(int(c[1])):
                k = prev[k]
        elif c[0] == 'Z':
            _k, _nxt, _prev = stack.pop()
            if _k > last: 
                last = _k
            else:
                prev[_nxt] = _k            
                nxt[_prev] = _k
                prev[_k] = _prev
                nxt[_k] = _nxt

    answer = ['O']*n
    for x in stack:
        answer[x[0]] = 'X' 
    return ''.join(answer)