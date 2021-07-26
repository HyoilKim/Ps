# my solution(recursion)
# time - O(N)
# space - O(N)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        
        return root if left and right else left or right

# iterative solution
# time - O(N)
# space - O(N)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None} # child:parent
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q