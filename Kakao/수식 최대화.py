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

# recursion
from itertools import permutations
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = (list(permutations(['*','-','+'], 3)))
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer