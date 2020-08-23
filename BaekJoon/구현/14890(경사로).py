# count, slice, zip(*A):전치
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

def cnt_way(field):
    cnt = 0
    chk_slope = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            flag = True

            if field[i][j] == field[i][j+1]:
                continue
            else:
                # 차이가 1인 경우
                if abs(field[i][j] - field[i][j+1]) == 1:
                    # 오르막길
                    if field[i][j] < field[i][j+1]:
                        if field[i][j-L+1:j+1].count(field[i][j]) == L and True not in chk_slope[i][j-L+1:j+1]:
                            chk_slope[i][j-L+1:j+1] = [True] * L
                            continue
                        else:
                            flag = False
                            break
                    # 내리막길
                    else:
                        if field[i][j+1:j+1+L].count(field[i][j+1]) == L:
                            chk_slope[i][j+1:j+1+L] = [True] * L
                            continue
                        else:
                            flag = False
                            break
                else:
                    flag = False
                    break
        if flag:
            cnt += 1

    return cnt

cnt = cnt_way(field)
cnt += cnt_way(list(zip(*field)))
print(cnt)

