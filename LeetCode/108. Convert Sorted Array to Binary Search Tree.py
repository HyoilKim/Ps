# my solution
# time - O(N)
# space - O(N)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def make_tree(nums):
            if not nums: return None
            n = len(nums)//2
            node = TreeNode(nums[n])
            node.left = make_tree(nums[:n])
            node.right = make_tree(nums[n+1:])
            return node
        
        n = len(nums)//2
        root = TreeNode(nums[n])
        root.left = make_tree(nums[:n])
        root.right = make_tree(nums[n+1:])
        return root
    
    # simplify
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root