import math
def solution(lottery):
    lottery.sort(key=lambda x:x[0])  # 유저 별로 정렬
    user = lottery[0][0]             # 첫 유저 설정
    buy_num = 0                      # 구매 횟수
    is_win = False                   # 당첨 여부
    dic = dict()                     # {user:최초 당첨시 복권구매 횟수}
    
    for info in lottery:
        if user == info[0]:          # 같은 유저
            if is_win: continue      # 당첨됐으면 no count
            buy_num += 1
            if info[1] == 1:         # 당첨
                dic[user] = buy_num
                is_win = True
        else:                        # 새로운 유저
            user = info[0]           # 재설정
            buy_num = 1              # 초기화
            is_win = False
            if info[1] == 1:         # 한 번에 당첨
                dic[user] = buy_num
                
    total = length = 0
    for user in dic:        
        total += dic[user]
        length += 1
    
    # 당첨된 유저가 있으면 평균값 반환
    if dic:  
        return math.floor(total/length)
    else:
        return 0