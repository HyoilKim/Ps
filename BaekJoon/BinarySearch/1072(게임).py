import math

def bst(x, y):
    l = 1; r = x
    while l <= r:
        mid = (l+r)//2
        nz = math.floor((y+mid)*100/(x+mid)) # y*100/x != y/x*100
        if nz == z:
            l = mid+1
        else:
            r = mid-1
    return r+1


if __name__ == "__main__":
    x, y = map(int, input().split())
    z = math.floor(y*100 / x)
    if z >= 99:
        print(-1)
    else:
        print(bst(x, y))