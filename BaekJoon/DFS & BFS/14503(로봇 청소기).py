import sys
input = sys.stdin.readline

direc = {0:'북', 1:'동', 2:'남', 3:'서'}
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)] 

def direc(d):
    return {
        0 : '북',
        1 : '동',
        2 : '남',
        3 : '서',
    }.get(d, -1)

def rotate(d):
    if direc(d) == '북':
        return 3
    elif direc(d)== '동':
        return 0
    elif direc(d) == '남':
        return 1
    elif direc(d) == '서':
        return 2
    else:
        return -1

def go(r, c, d):
    nr = r
    nc = c
    if direc(d) == '북':
        return nr-1, nc
    elif direc(d)== '동':
        return nr, nc+1
    elif direc(d) == '남':
        return nr+1, nc
    elif direc(d) == '서':
        return nr, nc-1
    else:
        return -1, -1

def back(r, c, d):
    nr = r
    nc = c
    if direc(d) == '북':
        nr += 1
    elif direc(d)== '동':
        nc -= 1
    elif direc(d) == '남':
        nr -= 1
    elif direc(d) == '서':
        nc += 1
    else:
        print("error")

    return nr, nc

def left_exist(room, r, c, d):
    d = rotate(d)
    r, c = go(r, c, d)
    if r >=0 and c >= 0 and r < len(room) and c < len(room[0]) and room[r][c] == 0:    
        return True
    else:
        return False

def printRoom(room):
    for i in range(len(room)):
        for j in range(len(room[0])):
            print(room[i][j], end=" ")
        print("")
    print("")
    
rotation = 0
cnt = 1
while True:
    room[r][c] = 2 

    if left_exist(room, r, c, d):
        d = rotate(d)
        r, c = go(r, c, d)
        rotation = 0
        cnt += 1
    else: 
        if rotation != 4:
            d = rotate(d)
            rotation += 1
        else:
            nr, nc = back(r, c, d)
            if room[nr][nc] != 1:
                rotation = 0
                r, c = back(r, c, d)
                continue
            else:
                break
        

print(cnt)
        
    