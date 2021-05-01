def solution(enroll, referral, seller, amount):
    refer = dict()
    earn = dict()
    for e, r in zip(enroll, referral):
        refer[e] = r
    
    for i, s in enumerate(seller):
        total = 100*amount[i]
        
        if refer[s] == "-":
            earn[s] = total
        else:
            while refer[s] != "-":
                bonus = total * .1
                if bonus < 1: 
                    break
                total -= bonus
            
                if earn.get(s, 0) > 0:
                    earn[s] = earn.get(s) + total
                else:
                    earn[s] = total
    print(earn)
    result = []
    for e in enroll:
        result.append(earn.get(e, 0))
    return result


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))