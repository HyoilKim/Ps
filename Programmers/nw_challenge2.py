def solution(grid):
    R, C = len(grid), len(grid[0])
    dp = [[0]*C for _ in range(R)]
    
    # 1행, 1열 초기화
    dp[0][0] = grid[0][0]
    for c in range(1, C):
        dp[0][c] = grid[0][c] + dp[0][c-1]
    for r in range(1, R):
        dp[r][0] = grid[r][0] + dp[r-1][0]
    
    for r in range(1,R):
        for c in range(1,C):
            dp[r][c] = grid[r][c] + min(dp[r][c-1], dp[r-1][c])
            
    return dp[-1][-1]