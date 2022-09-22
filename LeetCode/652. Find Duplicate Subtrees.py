# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = defaultdict(int)
        res = []
        def pre_order(root, tree):
            if not root:
                return "null"
            tree += '%s %s %s' % (root.val, pre_order(root.left, tree), pre_order(root.right, tree))
            trees[tree] += 1
            if trees[tree] == 2:
                res.append(root)
            return tree
        
        pre_order(root, '')
        return res
