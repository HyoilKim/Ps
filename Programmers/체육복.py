def solution(n, lost, reserve):
    intersection = list(set(lost) & set(reserve))
    for i in intersection:
        lost.remove(i)
        reserve.remove(i)
    
    borrow = 0
    for i in lost:
        if i-1 in reserve:
            borrow +=1
            reserve.remove(i-1)
        elif i+1 in reserve:
            borrow += 1
            reserve.remove(i+1)
    
    return n-len(lost)+borrow

n = 5
lost = [1,2,3,4,5]
reserve = [1,2,3,4,5]
print(solution(n, lost, reserve))

# best solution
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)