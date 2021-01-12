# sys.readline 주의
# split을 붙이지 않으면 개행까지 받음
import sys
input=sys.stdin.readline

wheel_1 = ''.join(input().split())
wheel_2 = ''.join(input().split())
wheel_3 = ''.join(input().split())
wheel_4 = ''.join(input().split())
n = int(input())

def rotate(wheel, direc):
    if direc == 1:
        wheel = wheel[-1] + wheel[:-1]
    elif direc == -1:
        wheel = wheel[1:] + wheel[0]
    else:
        print("invalid direction")
    return wheel

score = 0
for i in range(n):
    wheel_num, direc = map(int, input().split())
    flag1 = flag2 = flag3 = flag4 = False
    direc1 = direc2 = direc3 = direc4 = 0
    
    if wheel_num == 1:
        flag1 = True
        direc1 = direc
        if wheel_1[2] != wheel_2[6]:
            flag2 = True
            direc2 = -1 if direc1 == 1 else 1
            if wheel_2[2] != wheel_3[6]:
                flag3 = True
                direc3 = -1 if direc2 == 1 else 1
                if wheel_3[2] != wheel_4[6]:
                    flag4 = True
                    direc4 = -1 if direc3 == 1 else 1
        
        if flag1: wheel_1 = rotate(wheel_1, direc1)
        if flag2: wheel_2 = rotate(wheel_2, direc2)
        if flag3: wheel_3 = rotate(wheel_3, direc3)
        if flag4: wheel_4 = rotate(wheel_4, direc4)
    # wheel_2 
    elif wheel_num == 2:
        flag2 = True
        direc2 = direc
        if wheel_2[6] != wheel_1[2]:
            flag1 = True
            direc1 = -1 if direc2 == 1 else 1
        if wheel_2[2] != wheel_3[6]:
            flag3 = True
            direc3 = -1 if direc2 == 1 else 1
            if wheel_3[2] != wheel_4[6]:
                flag4 = True
                direc4 = -1 if direc3 == 1 else 1

        if flag1: wheel_1 = rotate(wheel_1, direc1)
        if flag2: wheel_2 = rotate(wheel_2, direc2)
        if flag3: wheel_3 = rotate(wheel_3, direc3)
        if flag4: wheel_4 = rotate(wheel_4, direc4)
    # wheel_3 
    elif wheel_num == 3:
        flag3 = True
        direc3 = direc
        if wheel_2[2] != wheel_3[6]:
            flag2 = True
            direc2 = -1 if direc3 == 1 else 1
            if wheel_1[2] != wheel_2[6]:
                flag1 = True
                direc1 = -1 if direc2 == 1 else 1
        if wheel_3[2] != wheel_4[6]:
            flag4 = True
            direc4 = -1 if direc3 == 1 else 1

        if flag1: wheel_1 = rotate(wheel_1, direc1)
        if flag2: wheel_2 = rotate(wheel_2, direc2)
        if flag3: wheel_3 = rotate(wheel_3, direc3)
        if flag4: wheel_4 = rotate(wheel_4, direc4)
    # wheel_4 
    elif wheel_num == 4:
        flag4 = True
        direc4 = direc
        if wheel_3[2] != wheel_4[6]:
            flag3 = True
            direc3 = -1 if direc4 == 1 else 1
            if wheel_2[2] != wheel_3[6]:
                flag2 = True
                direc2 = -1 if direc3 == 1 else 1
                if wheel_1[2] != wheel_2[6]:
                    flag1 = True
                    direc1 = -1 if direc2 == 1 else 1

        if flag1: wheel_1 = rotate(wheel_1, direc1)
        if flag2: wheel_2 = rotate(wheel_2, direc2)
        if flag3: wheel_3 = rotate(wheel_3, direc3)
        if flag4: wheel_4 = rotate(wheel_4, direc4)
    else:
        print("Invalid input")
    
if wheel_1[0] == str(1): score += 1
if wheel_2[0] == str(1): score += 2
if wheel_3[0] == str(1): score += 4
if wheel_4[0] == str(1): score += 8
print(score)
    

