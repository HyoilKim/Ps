# my solution(dfs)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.traverse(root, 0)
    
    def traverse(self, node, depth):
        if not node:
            return depth
        return max(self.traverse(node.left, depth+1), self.traverse(node.right, depth+1))

# another solution(bfs)
# 속도 빠름
def maxDepth(self, root: TreeNode) -> int:
    depth = 0
    cur = [root] if root else []
    while level:
        depth += 1
        cur = [child for node in cur for child in (node.left, node.right) if child]
    return depth