import sys
input = sys.stdin.readline


def solution(rings):
    # 각 지점마다 가장 가까운 1의 위치를 N*K만에 파악가능?
    sums = [sum(row) for row in rings]
    
    max_rows = []
    max_sum = max(sums)
    for row, row_sum in enumerate(sums):
        if row_sum == max_sum:
            max_rows.append(row)
    
    result = float('inf')
    # for mrow in max_rows:
    mrow = max_rows[len(max_rows)//2]
    cnt = 0
    for col in range(C):
        for row in range(R//2+1):
            if rings[(mrow+row)%R][col] == 1:
                cnt += row
                break
            if rings[mrow-row][col] == 1:
                cnt += row
                break
    # print(mrow, cnt)
    result = min(result, cnt)
    return result
    

tc = int(input())
for i in range(tc):
    C, R = map(int, input().split())
    rings = []
    for _ in range(R):
        ring = []
        for n in input().rstrip():
            ring.append(int(n))
        rings.append(ring)
    print('#{0} {1}'.format(i+1, solution(rings)))
'''

def solution(rings, N, K, dpl, dpr, dp):
    for i in range(N*3*K):
        r, c = i // N, i % N
        if rings[r][c] == 1:
            dpl[i] = 0
        elif i >= N:
            dpl[i] = dpl[i-N] + 1
            
    for i in range(N*3*K-1, -1, -1):
        r, c = i // N, i % N
        if rings[r][c] == 1:
            dpr[i] = 0
        elif i < N*3*K-N:
            dpr[i] = dpr[i+N] + 1

    for i in range(N*K):
        dp[i] = min(dpl[i], dpr[i])
            
    min_sum = float('inf')
    for i in range(K):
        # print(dp[r])
        min_sum = min(min_sum, sum(dp[i*N:(i+1)*N]))
    return min_sum
            

def main():
    tc = int(input())
    dpl = [float('inf')]*3000000
    dpr = [float('inf')]*3000000
    dp = [float('inf')]*1000000
    for i in range(tc):
        N, K = map(int, input().split())
        rings = [[int(n) for n in input().rstrip()] for _ in range(K)]
        print('#{0} {1}'.format(i+1, solution(rings*3, N, K, dpl, dpr, dp)))

main()
    '''