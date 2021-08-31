# 90도 회전
# 회전 후 배열의 X 인덱스 == 회전하기 전 배열의 Y 인덱스
# 회전 후 배열의 Y 인덱스 == (배열 크기 - 1) - 회전하기 전 배열의 X 인덱스
# (x, y) -> (y, len(arr)-1-x)
def rotate(key):
    n = len(key)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = key[i][j]
    return ret

# 자물쇠가 열리는지 check
def check(ei, ej, key, lock):
    key_len, lock_len = len(key), len(lock)
    expand_len = lock_len + 2*(key_len-1)
    expend_list = [[0]*expand_len for _ in range(expand_len)]

    # expend list에 key 추가
    for i in range(key_len):
        for j in range(key_len):
            expend_list[ei+i][ej+j] += key[i][j]
            
    # key와 lock의 1이어야 True
    for i in range(lock_len):
        for j in range(lock_len):
            if expend_list[i+key_len-1][j+key_len-1]+lock[i][j] != 1:
                return False    
    return True

def solution(key, lock):
    key_len, lock_len = len(key), len(lock)
    for _ in range(4):
        for i in range(lock_len+key_len-1):
            for j in range(lock_len+key_len-1):
                if check(i, j, key, lock):
                    return True
        key = rotate(key)        
    return False

# Refer: https://johnyejin.tistory.com/127

# second try fail