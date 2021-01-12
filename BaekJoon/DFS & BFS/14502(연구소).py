def print_lab(lab):
    print("")
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            print(lab[i][j], end=" ")
        print("")

from itertools import combinations
import queue
import copy

# 입력
n, m = map(int, input().split())
lab = [[int(x) for x in input().split()] for _ in range(n)]

# 바이러스 위치
virus_pos = []
safe_pos = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus_pos.append((i, j))
        if lab[i][j] == 0:
            safe_pos.append((i, j))

safe_filed = -1

for (r1,c1),(r2,c2),(r3,c3) in list(combinations(safe_pos, 3)):
    if lab[r1][c1] != 0: continue
    if lab[r2][c2] != 0: continue
    if lab[r3][c3] != 0: continue 

    # 벽 세우기
    tmp_lab = copy.deepcopy(lab)
    tmp_lab[r1][c1] = tmp_lab[r2][c2] = tmp_lab[r3][c3] = 1

    # 바이러스 퍼트리기(bfs)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    Q = queue.Queue()
    for pos in virus_pos:
         Q.put(pos)
         while Q.qsize() > 0:
             pos = Q.get()
             for i in range(4):
                    r = dx[i] + pos[0]
                    c = dy[i] + pos[1]
                    if r < 0 or c < 0 or r >= n or c >= m or tmp_lab[r][c] != 0: continue
                    else:
                        Q.put((r, c))
                        tmp_lab[r][c] = 2
    # 0의 개수 체크
    cnt = 0
    for i in tmp_lab:
        cnt += i.count(0)

    if safe_filed < cnt:
        safe_filed = cnt

print(safe_filed)


# import itertools
# import sys
# input=sys.stdin.readline

# n, m = map(int, input().split())
# arr = []
# L=[]
# virusList = []
# d=[[1,0],[-1,0],[0,1],[0,-1]]

# for i in range(n):
#     arr.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(m):
#         if arr[i][j]==0:
#             L.append([i,j])
#         if arr[i][j] == 2:
#             virusList.append([i,j])

# def safearea(arr):
#     sum=0
#     for i in arr:
#         sum+=i.count(0)
#     return sum

# def spread(x, y):
#     for i in range(4):
#         nx = x + d[i][0]
#         ny = y + d[i][1]
#         if 0 <= nx and nx < n and 0 <= ny and ny < m:
#             if cp[nx][ny] == 0:
#                 cp[nx][ny] = 2
#                 spread(nx, ny)


# max=0
# for (r1,c1),(r2,c2),(r3,c3) in list(itertools.combinations(L,3)):
#     cp=[arr[i][:] for i in range(n)] #deepcopy보다 빠르다
#     cp[r1][c1],cp[r2][c2],cp[r3][c3]=1,1,1
#     for x,y in virusList:
#         spread(x,y)
#     safe=safearea(cp)
#     if max<safe:
#         max=safe
# print(max)