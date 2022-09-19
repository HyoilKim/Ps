# my code
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def bfs(root, max_value):
            if not root:
                return 0

            if root.val >= max_value:
                return 1 + bfs(root.left, root.val) + bfs(root.right, root.val)
            else:
                return bfs(root.left, max_value) + bfs(root.right, max_value)
        
        return bfs(root, root.val)
