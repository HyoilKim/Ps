def solution(maps, p, r):    
    N = len(maps)
    answer = 0
    for x in range(-1,N+1):
        for y in range(-1,N+1):
            cnt = 0
            for _x in range(r//2): 
                _r = r-(2*_x)
                # 오른-노랑
                for _y in range(1, _r//2): 
                    if 0 <= x-_x < N and 0 <= y+_y < N and maps[x-_x][y+_y] <= p: cnt += 1
                    if 0 <= x+_x+1 < N and 0 <= y+_y < N and maps[x+(_x+1)][y+_y] <= p: cnt += 1
                # 오른-파랑    
                if 0 <= x-_x < N and 0 <= y+(_r//2) < N and maps[x-_x][y+(_r//2)] <= p/2: cnt += 1
                if 0 <= x+_x+1 < N and 0 <= y+(_r//2) < N and maps[x+(_x+1)][y+(_r//2)] <= p/2: cnt += 1
                # 왼-노랑
                for _y in range(_r//2-1):
                    if 0 <= x-_x < N and 0 <= y-_y < N and maps[x-_x][y-_y] <= p: cnt += 1
                    if 0 <= x+_x+1 < N and 0 <= y-_y < N and maps[x+(_x+1)][y-_y] <= p: cnt += 1
                # 왼-파랑
                if 0 <= x-_x < N and 0 <= y-(_r//2-1) < N and maps[x-_x][y-(_r//2-1)] <= p/2: cnt += 1
                if 0 <= x+_x+1 < N and 0 <= y-(_r//2-1) < N and maps[x+(_x+1)][y-(_r//2-1)] <= p/2: cnt += 1

            answer = max(answer, cnt)
    return answer

maps = [[47, 8, 99, 9, 85, 3, 8], [90, 93, 8, 25, 98, 15, 97], [9, 95, 91, 87, 8, 81, 9], [98, 88, 82, 89, 79, 81, 97], [97, 35, 31, 97, 81, 2, 92], [32, 16, 49, 9, 91, 89, 17], [53, 6, 35, 12, 13, 98, 5]]
p = 78
r = 6
print(solution(maps,p,r))