from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs(cur, d):
            if not cur:
                return
            level_sum[d] += cur.val 
            if cur.left: bfs(cur.left, d+1)
            if cur.right: bfs(cur.right, d+1)
                
        level_sum = defaultdict(int) # level : total
        bfs(root, 1)
        max_num = max(level_sum.values())
        for i, v in enumerate(level_sum.values()):
            if max_num == v:
                return i+1
