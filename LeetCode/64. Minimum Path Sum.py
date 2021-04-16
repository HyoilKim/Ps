class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0]
        
        for i in range(1, len(grid[0])):
            for j in range(1, len(grid)):
                grid[j][i] += min(grid[j-1][i], grid[j][i-1])
            
        return grid[-1][-1]