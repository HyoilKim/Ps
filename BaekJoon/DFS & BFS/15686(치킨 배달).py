import itertools
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0]*n for _ in range(n)]
chicken_pos, home_pos = [], []

def data_input():
    for i in range(n):
        A[i] = list(map(int, input().split()))
        for j in range(n):
            if A[i][j] == 1:
                home_pos.append((i, j))
            elif A[i][j] == 2:
                chicken_pos.append((i, j))

def chicken_len():
    total = 0
    for h_x, h_y in home_pos:
        min_distance = 2**31
        for c_x, c_y in chicken_pos:
            min_distance = min(int(abs(h_x-c_x)+abs(h_y-c_y)),
                                min_distance)
        total += min_distance
    return total

def solution():
    remove_candidates = list(itertools.combinations(chicken_pos, len(chicken_pos)-m))
    min_len = 2**31
    for candidates in remove_candidates:
        for candidate in candidates:
            chicken_pos.remove(candidate)
            
        min_len = min(chicken_len(), min_len)
        
        for candidate in candidates:
            chicken_pos.append(candidate)
    return min_len

if __name__ == "__main__":
    data_input()
    res = solution()
    print(res)

# best solution
# combination을 쓰지 않고 푸는 방법 - dfs
# chicken_dist를 미리 구하면 시간 단축
def solution(removed_cnt, idx):
    global answer
    # 필요한 수 만큼 폐업시켰을 경우
    if(removed_cnt==len(chicken_pos)-m):
        res = min(chicken_len(), answer)
        return
    
    # 현재 폐업시킨 치킨집 이후의 치킨집들에 대해 재귀호출
    for i in range(idx+1,len(chicken)):
        removed[i] = True
        solution(removed_cnt+1, i)
        removed[i] = False


