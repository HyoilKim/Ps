def curv_path(d, g):
    if g == 0 : return [d]
    ret = curv_path(d, g-1)
    return ret + [(i+1)%4 for i in ret[::-1]]

def dragon_path(cord, x, y, d, g):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    cord[x][y] = 1
    for w in curv_path(d, g):
        x, y = x+dx[w], y+dy[w]
        cord[x][y] = 1

def count_square(cord):
    ret = 0
    for i in range(100):
        for j in range(100): ret += sum([cord[i+x//2][j+x%2] for x in range(4)])==4
    return ret

cord = [[0 for _ in range(101)] for _ in range(101)]
for param in [map(int, input().split()) for _ in range(int(input()))]: dragon_path(cord, *param)
print(count_square(cord))