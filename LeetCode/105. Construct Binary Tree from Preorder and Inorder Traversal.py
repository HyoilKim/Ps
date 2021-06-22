# my solution - slow but easy understand
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

# another solution - fast
# 1. inor_dict 
# 2. iter(preorder)
# 3. (start, end)
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inor_dict = {}
        for i, num in enumerate(inorder):
            inor_dict[num] = i
        pre_iter = iter(preorder)
        
        def helper(start, end):
            if start > end:return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = inor_dict[root_val]
            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root
        
        return helper(0, len(inorder) - 1)