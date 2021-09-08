from itertools import combinations
def solution(relation):
    answer = []
    clen = len(relation[0])
    for n in range(1, 1+clen): 
        for idxs in sorted(combinations(range(clen), n)): 
            flag = False
            for cand in answer:
                cnt = 0
                for i in cand:
                    if i in idxs:
                        cnt += 1
                if cnt == len(cand):
                    flag = True
                    break
            if flag: 
                continue
                
            candidate = True
            dup = set()
            for row in relation:
                data = ''.join([row[idx] for idx in idxs])
                if data in dup:
                    candidate = False
                    break
                else:
                    dup.add(data)
                    
            if candidate:
                answer.append(idxs)
            
    return len(answer)