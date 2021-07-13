# bfs
# time - O(n)
from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                right_val = node.val
                if node.left:
                    queue.append(node.left)
                    right_val = node.val
                if node.right:
                    queue.append(node.right)
                    right_val = node.val
            res.append(right_val)
            
        return res        
        
            