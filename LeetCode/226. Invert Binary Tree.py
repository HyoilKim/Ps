# my solution
class Solution:
    def invertTree(self, root):
        def invert_tree(root):
            if not root.left and not root.right:
                return
            
            if root.left: invert_tree(root.left)
            if root.right: invert_tree(root.right)
            root.left, root.right = root.right, root.left
        
        if not root: return
        invert_tree(root)
        return root

# short solution
def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# iteratively(DFS)
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right # stack.extend([node.left, node.right])
    return root

# iteratively(BFS)
from collections import deque
def invertTree2(self, root):
    queue = deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root