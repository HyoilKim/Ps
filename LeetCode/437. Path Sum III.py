class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
# my solution - Brute Force
# time - O(NlogN) ~ O(N^2)
# space - O(NlogN) ~ O(N^2)
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node):
            if not node: return
            path_sum(node, 0)
            dfs(node.left)
            dfs(node.right)
            
        def path_sum(node, subsum):
            if not node: 
                return
            path_sum(node.left, subsum+node.val)
            path_sum(node.right, subsum+node.val)
            if subsum+node.val == targetSum:
                self.cnt += 1
            
        self.cnt = 0    
        dfs(root)
        return self.cnt

# memorization solution
# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
# time - O(N)
# space - O(N)
class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0:1}
        self.dfs(root, target, 0, cache)
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return  

        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target

        # update result and cache
        self.result += cache.get(oldPathSum, 0)            # 과거 path 불러오기
        cache[currPathSum] = cache.get(currPathSum, 0) + 1 # 현재 path 저장
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
        