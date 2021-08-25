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

# second try
from collections import defaultdict
from itertools import combinations, permutations
def solution(orders, course):         
    # 2명 이상의 고객에게 주문된 조합이어야 한다
    # 음식 조합이 가장 높은 빈도를 우선으로 코스로 구성한다
    candi = defaultdict(int) # {메뉴구성:빈도}
    
    for order in orders:
        order = ''.join(sorted(order))
        for n in range(2, len(order)+1):
            for menu in [''.join(x) for x in combinations(order, n)]:
                candi[menu] += 1
                
    result = []
    for n in course:
        tmp = defaultdict(list)
        max_freq = 0
        for menu, freq in candi.items():
            if len(menu) == n:
                tmp[freq].append(menu)
                max_freq = max(max_freq, freq)
        if max_freq >= 2:
            result += tmp[max_freq]
    
    result.sort()
    return result