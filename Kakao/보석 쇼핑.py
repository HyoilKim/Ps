# my solution
# two pointers
from collections import defaultdict
def solution(gems):
    jewelry_num = len(set(gems))
    cand = defaultdict(int)
    l = r = 0
    ans_l = 0; ans_r = len(gems)
    
    while l < len(gems) and r < len(gems):
        if len(cand.keys()) < jewelry_num:
            cand[gems[r]] += 1
            r += 1
        while len(cand.keys()) == jewelry_num:
            if r-l < ans_r-ans_l:
                ans_l, ans_r = l, r
            cand[gems[l]] -= 1
            if cand[gems[l]] == 0: del cand[gems[l]]
            l += 1
    return [ans_l+1, ans_r]
    