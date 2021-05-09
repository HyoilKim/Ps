from collections import deque, defaultdict
def solution(t, r):
    answer = []
    c_info = defaultdict(list)              # 손님 정보
    for cid, time in enumerate(t):    
        c_info[time].append((cid, r[cid]))  # 도착시간: (손님id, 손님등급) 
        
    rq = []                                 # 대기중인 손님들
    for time in range(10001):
        if len(c_info[time]) > 0:           # 해당 시간에 대기 손님
            for c in c_info[time]:
                rq.append(c)
            rq.sort(key = lambda x: x[1])   # 손님 등급에 따라 순서 교체
        if rq:                              # 대기 중인 손님이 있으면
            answer.append(rq[0][0])         # 탑승
            del rq[0]
    
    return answer