# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid(root, float('-inf'), float('inf'))
    
    def is_valid(self, root, min_val, max_val):
        if not root:
            return True
        if not min_val < root.val < max_val:
            return False
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.is_valid(root.left, min_val, root.val) \
                and self.is_valid(root.right, root.val, max_val)
       