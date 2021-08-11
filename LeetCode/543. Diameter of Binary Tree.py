# my solution
# time - O(N)
# space - O(logN)
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        def dfs(node): # readable name is depth or height
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.result = max(self.result, left+right)
            return max(left, right)+1
        
        self.result = 0
        dfs(root)
        return self.result

# don't use global variable
class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.depth(root, diameter)
        return diameter[0]

    def depth(self, root, diameter):
        if not root:
            return 0
        left_height = self.depth(root.left, diameter)
        right_height = self.depth(root.right, diameter)
        diameter[0] = max(diameter[0], left_height + right_height)
        return 1 + max(left_height, right_height)

# if inner function's name is depth, 'return 0' is contradiction
# single node's depth is 1
# so change to return -1
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def height(p):
            # it's custom to define the height of an empty tree to be -1. This also fixes the off-by-one error I mentioned.
            if not p: return -1       
                            
            left, right = height(p.left), height(p.right)
            
            # the "2+" accounts for the edge on the left plus the edge on the right. This change is required to account for 
            # the fact that we updated the height of an empty tree to be -1. 
            self.ans = max(self.ans, 2+left+right)   
            
            return 1+max(left, right)
            
        self.ans = 0
        height(root)
        return self.ans