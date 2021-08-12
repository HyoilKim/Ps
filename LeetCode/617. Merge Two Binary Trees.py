class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# my solution(dfs)
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None
        
        # node = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0)
        val1, val2 = 0, 0
        if root1: val1 = root1.val
        if root2: val2 = root2.val
        node = TreeNode(val1+val2)    
        
        # node.left = merge(root1 and root1.left, root2 and root2.left)
        if root1 and root2:
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            node.left = self.mergeTrees(root1.left, root2)
            node.right = self.mergeTrees(root1.right, root2)
        elif root2:
            node.left = self.mergeTrees(root1, root2.left)
            node.right = self.mergeTrees(root1, root2.right)
            
        return node
        
# clean code
class Solution:
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans

class Solution():
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

# bfs solution
from collections import deque
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not (t1 and t2):
            return t1 or t2
        queue1, queue2 = deque([t1]), deque([t2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return t1
