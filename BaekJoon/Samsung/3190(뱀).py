import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

apples = set()
for _ in range(K):
    r, c = map(int, input().split())
    apples.add((r-1,c-1))

L = int(input())
change = dict()
for _ in range(L):
    t, d = input().split()
    change[int(t)] = d

t = 0
snake = [(0,0)]
length = 1
cur_d = 'E'
turn_left = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}
turn_right = {'E':'S', 'S':'W', 'W':'N', 'N':'E'}
while True:
    t += 1
    r, c = snake[0]
    if cur_d == 'E':
        c += 1
    elif cur_d == 'S':
        r += 1
    elif cur_d == 'W':
        c -= 1
    elif cur_d == 'N':
        r -= 1
    
    # 자기자신/벽과 부딪히는 경우 종료
    head = (r,c)
    # print(head)
    if head in snake or r < 0 or r >= N or c < 0 or c >= N:
        print(t)
        break

    snake.insert(0, head) # 앞부분만 이동해서 추가
    if head in apples:
        apples.remove(head)
    else: # 사과 없으면 꼬리 당기기
        snake.pop()        

    if t in change: # 방향 변환
        d = change[t]
        if d == 'D':
            cur_d = turn_right[cur_d]
        else:
            cur_d = turn_left[cur_d]