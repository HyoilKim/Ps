# my solution
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for n in course:
        all_menu = []
        for order in orders:
            if len(order) < n: continue
            menu_comb = combinations(sorted(order), n)
            for menu in menu_comb:
                all_menu.append(''.join(menu))
                
        menu_cnt = Counter(all_menu).most_common()         
        for menu, cnt in menu_cnt:
            if cnt == menu_cnt[0][1] and cnt >= 2:
                answer.append(menu)
    
    answer.sort()
    return answer

# clean code
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]