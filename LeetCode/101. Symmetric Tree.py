# my solution 1
# traverse all nodes
class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        
    def isSymmetric(self, root: TreeNode) -> bool:
        self.left_traverse(root.left)
        self.right_traverse(root.right)
        return self.left == self.right
    
    def left_traverse(self, node):
        if not node: 
            self.left.append('')
            return
        self.left.append(node.val)
        self.left_traverse(node.left)
        self.left_traverse(node.right)
        
    def right_traverse(self, node):
        if not node:
            self.right.append('')
            return
        self.right.append(node.val)
        self.right_traverse(node.right)
        self.right_traverse(node.left)

# my solution 2
class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        
    def isSymmetric(self, root: TreeNode) -> bool:
        self.traverse(root.left, root.right)
        return self.left == self.right
    
    def traverse(self, node1, node2):
        if not node1: self.left.append('')
        else: self.left.append(node1.val)
            
        if not node2: self.right.append('')
        else:self.right.append(node2.val)
        
        if not node1 or not node2: 
            return
        else:
            self.traverse(node1.left, node2.right)
            self.traverse(node1.right, node2.left)

# recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val and self.is_mirror(node1.left, node2.right) \
                                        and self.is_mirror(node1.right, node2.left)

# simple solution
def isSymmetric(self, root):
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)