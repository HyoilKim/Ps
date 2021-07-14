# my solution
# bfs
from collections import deque
class Solution:
    def numIslands(self, grid):
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    queue = deque([(i,j)])
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in [(0,-1),(0,1),(1,0),(-1,0)]:
                            nr = r+dr
                            nc = c+dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                                if grid[nr][nc] == '1':
                                    grid[nr][nc] = '0'
                                    queue.append((nr,nc))
        return cnt

# another solution
# dfs
def numIslands(self, grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1
    return count

def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)