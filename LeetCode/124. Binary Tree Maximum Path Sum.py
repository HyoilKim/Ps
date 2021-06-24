class Solution:        
    def maxPathSum(self, root: TreeNode) -> int:
        def max_path(node):
            nonlocal max_num
            if not node:
                return 0
            left = max_path(node.left)
            right = max_path(node.right)
            max_num = max(max_num, left+node.val +right)
            return max(node.val + max(left, right), 0)
        
        max_num = float('-inf')
        max_path(root)
        return max_num