# bfs solution
# time - O(N) (branch: sqrt(N), depth: sqrt(N))
from collections import deque
import math
class Solution:
    def numSquares(self, n):
        psnums = [x**2 for x in range(1, int(math.sqrt(n))+1)]
        queue = deque([(0,0)])
        visited = set([0])      # 같은 숫자 재방문 방지
        
        while queue:
            num, level = queue.popleft()
            for psnum in psnums:
                if num+psnum in visited: continue
                if num+psnum == n: return level+1
                if num+psnum < n: 
                    queue.append((num+psnum, level+1))
                    visited.add(num+psnum)