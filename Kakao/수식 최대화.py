import re
from itertools import permutations

def solution(expression):
    ops = [x for x in ['*','+','-'] if x in expression]
    ops_list = list(permutations(ops))
    ex = re.split(r'(\D)',expression)
    
    answer = 0
    for ops in ops_list:
        _ex = ex[:]
        for op in ops:
            while op in _ex:
                idx = _ex.index(op)
                val = str(eval(_ex[idx-1] + _ex[idx] + _ex[idx+1]))
                _ex = _ex[:idx-1] + [val] + _ex[idx+2:]
        answer = max(answer, abs(int(_ex[0])))
        
    return answer