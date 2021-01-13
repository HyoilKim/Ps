from collections import defaultdict 

def dfs(tickets, end_len, key, path):
    if len(path) == end_len:
        return path

    for idx, country in enumerate(tickets[key]):
        tickets[key].pop(idx)
        ret = dfs(tickets, end_len, country, path+[country])
        tickets[key].insert(idx, country)
        if ret:
            return ret

def solution(tickets):
    answer = []
    dict_tickets = defaultdict(list)
    end_len = len(tickets)+1

    for ticket in tickets:
        dict_tickets[ticket[0]].append(ticket[1])
        dict_tickets[ticket[0]].sort()

    answer = dfs(dict_tickets, end_len, "ICN", ["ICN"])

    return answer

# tickets = [["ATL", "SFO"], ["ICN", "ATL"], ["ICN", "ATL"], ["ATL", "ICN"], ["SFO","ATL"]]
# res = solution(tickets)
# print(res)

# 나의 dfs
# 정렬 오류
# 백트래킹 오류