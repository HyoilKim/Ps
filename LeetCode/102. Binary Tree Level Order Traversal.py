# my solution - so slow
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        self.traverse(root, nodes, 0)
        if not nodes:
            return []
        
        nodes.sort(key=lambda x:x[1])
        result = []
        for i in range(nodes[-1][1]+1):
            level = []
            for val, depth in nodes:
                if i == depth:
                    level.append(val)
            result.append(level)
            
        return result
    
    def traverse(self, node, nodes, depth):
        if not node:
            return
        nodes.append((node.val, depth))
        self.traverse(node.left, nodes, depth+1)
        self.traverse(node.right, nodes, depth+1)

# while 을 사용하여 bfs 탐색 - so fast
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans, cur = [], [root]
        while cur:
            ans.append([node.val for node in cur])
            child = []
            for node in cur:
                child.extend([node.left, node.right])
            cur = [node for node in child if node]
        return ans

    # list comprehension
    def levelOrder(self, root):
        ans, cur = [], [root]
        while root and cur:
            ans.append([node.val for node in cur])            
            cur = [child for node in cur for child in (node.left, node.right) if child]
        return ans