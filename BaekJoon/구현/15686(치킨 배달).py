# 집을 기준으로 bfs 탐색하여 치킨거리를 모두 저장 -> sum:도시의 치킨 거리
# 치킨 집을 조합에서 최대 M개 까지 골라 없앤 후 도시의 치킨 거리를 구한다
# 최소가 되는

# 1 <= 집의 개수 < 2N
# M <= 치킨집 개수 <= 13
from queue import Queue
from itertools import combinations
import sys
input=sys.stdin.readline

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

house_pos = []
store_pos = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house_pos.append((i, j))
        elif maps[i][j] == 2:
            store_pos.append((i, j))

def chicken_len(house_pos):
    h_row = house_pos[0]
    h_col = house_pos[1]
    res = 0
    min_distance = float('inf')
    for pos in store_pos:
        c_row = pos[0]
        c_col = pos[1]
        if maps[c_row][c_col] == 2:
            distance = int(abs(h_row-c_row) + abs(h_col-c_col))

            if min_distance > distance:
                min_distance = distance

    return min_distance


def remove_store(pos_list):
    for pos in pos_list:
        row = pos[0]
        col = pos[1]
        maps[row][col] = 0

def create_store(pos_list):
    for pos in pos_list:
        row = pos[0]
        col = pos[1]
        maps[row][col] = 2

city_len = float('inf')
for pos_list in combinations(store_pos, len(store_pos)-m):
    # 치킨 집 삭제
    remove_store(pos_list)

    # 가게를 삭제 했을 경우
    # 모든 집에서 치킨 집 까지 거리 tmp에 저장
    tmp = []
    for h_pos in house_pos:
        tmp.append(chicken_len(h_pos))

    if city_len > sum(tmp):
        city_len = sum(tmp)

    # 삭제한 치킨 집 생성
    create_store(pos_list)

print(city_len)