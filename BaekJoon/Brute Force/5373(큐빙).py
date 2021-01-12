import sys
input=sys.stdin.readline


def rotate(cube, cmd):


n = int(input())
for i in range(n):
    m = int(input())
    cmd = []
    for j in range(m):
        cmd = input().split()
    
    # rotate(cube, cmd)



# 3차원 데이터 각 value는 3개 or 2개 data가짐
# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
# 윗:흰색, 아랫:노란색, 앞:빨간색, 뒷:오렌지, 왼:초록, 오른:파란색
# 