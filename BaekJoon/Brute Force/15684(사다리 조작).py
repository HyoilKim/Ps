# 1. 전체 탐색 중 정답인 경우 일 때 멈춤(backtraking)
# 2. dfs 종료 조건에 주의

# 다리는 가운데에서 양쪽에 두는 것이 아니라 한 방향만 두어야 함

import sys
import copy
input=sys.stdin.readline

N, M, H = map(int, input().split())
down = -1
ladder = [[-1 for _ in range(N)] for _ in range(H)]
bridge = []

def destination(col):
    row = -1
    while True:
        row += 1
        # 마지막에서 이동하기 때문에 H까지
        if row == H:
            return col
        # ladder 값은 이동할 사다리의 번호(col)
        right = col+1
        left = col-1
        direc = ladder[row][col]
        if direc == down:
            continue
        elif direc == right:
            col = col+1
        elif direc == left:
            col = col-1
        else:
            print("invalid direction")   
    

def is_answer():
    for col in range(N):
        if col != destination(col):
            return False
    return True

def put_bridge(idx, cnt):
    global result
    if result <= cnt:
        return

    if is_answer():
        result = min(result, cnt)
        return 
        
    if cnt == 3:
        return
    
    for row in range(idx, H):
        for col in range(0, N-1):
            cur_direc = ladder[row][col]
            right_direc = ladder[row][col+1]
            # 다리는 오른쪽에만 둠
            if cur_direc == down and right_direc == down:
                # print("right", row, col)
                ladder[row][col] = col+1
                ladder[row][col+1] = col
                put_bridge(row, cnt+1)
                ladder[row][col] = -1
                ladder[row][col+1] = -1
  

for _ in range(M):
    row, col = map(int, input().split())
    row -= 1 # index 0부터
    col -= 1
    ladder[row][col] = col+1
    ladder[row][col+1] = col

result = float('inf')
put_bridge(0, 0)

print(-1) if result == float('inf') else print(result)