# my solution
from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    info = [i.split() for i in info]
    info_dict = defaultdict(list)
    for _info in info:
        data, score = _info[:-1], int(_info[-1])
        for i in range(5):
            for j in combinations([0,1,2,3], i):
                _data = data[:]
                for k in j:
                    _data[k] = '-'
                info_dict[''.join(_data)].append(score)
                
    for k in info_dict:
        info_dict[k].sort() 
        
    answer = []
    for q in query:
        q = q.replace(" and", "").split()
        _q, score = ''.join(q[:-1]), int(q[-1])
        if info_dict[_q]:
            idx = bisect_left(info_dict[_q], score)
            answer.append(len(info_dict[_q]) - idx)
        else:
            answer.append(0)
    
    return answer

# second try fail