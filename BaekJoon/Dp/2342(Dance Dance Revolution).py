# dp + dfs
import sys
sys.setrecursionlimit(10**6)
def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(b-a)%2 == 0:
        return 4
    else:
        return 3
    
def solve(n, l, r):
    global dp
    if n >= len(arr)-1:
        return 0
    if dp[n][l][r] != -1:
        return dp[n][l][r]
    dp[n][l][r] = min(solve(n+1, arr[n],r) + move(l, arr[n]), solve(n+1, l, arr[n]) + move(r, arr[n]))
    return dp[n][l][r]
 
arr = list(map(int, sys.stdin.readline().split()))
dp = [[[-1]*5 for _ in range(5)] for _ in range(100000)]
 
print(solve(0, 0, 0))

# hash
def solution():
    costs = {
        (0,1):2,(0,2):2,(0,3):2,(0,4):2,
        (1,1):1,(1,2):3,(1,3):4,(1,4):3,
        (2,1):3,(2,2):1,(2,3):3,(2,4):4,
        (3,1):4,(3,2):3,(3,3):1,(3,4):3,
        (4,1):3,(4,2):4,(4,3):3,(4,4):1,
    }
    arr = list(map(int,input().split()[:-1]))
    dp = {(0,0):0}

    for num in arr:

        next_dp = {}

        for l,r in dp:

            # 왼발 이동
            if (num,r) in next_dp:
                next_dp[(num,r)] = min(next_dp[(num,r)], dp[(l,r)]+costs[(l,num)])
            else:
                next_dp[(num, r)] = dp[(l,r)]+costs[(l,num)]

            # 오른발 이동
            if (l,num) in next_dp:
                next_dp[(l, num)] = min(next_dp[(l, num)], dp[(l, r)]+costs[(r,num)])
            else:
                next_dp[(l, num)] = dp[(l, r)] + costs[(r,num)]

        dp = next_dp
    
    return min(dp.values())

result = solution()
print(result)

    