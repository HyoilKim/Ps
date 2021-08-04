# dfs solution
class Solution(object):
    def rob(self, root):
        def superrob(node):
            # returns tuple of size two (now, later)
            # now: max money earned if input node is robbed
            # later: max money earned if input node is not robbed
            
            # base case
            if not node: return (0, 0)
            
            # get values
            left, right = superrob(node.left), superrob(node.right)
            
            # rob now(cur now + left later + right later)
            now = node.val + left[1] + right[1]
            
            # rob later(left max(now, later) + right max(now, later))
            later = max(left) + max(right)
            
            return (now, later)
            
        return max(superrob(root))


'''
my solution - time over
don't understand

class Solution:
    def rob(self, root: TreeNode) -> int:
        def cal_rob(root):
            if not root: return 0
            
            left = cal_rob(root.left)
            if not flag:
                left = max(left, cal_rob(root.left, flag))
                
            right = cal_rob(root.right, not flag)
            if not flag:
                right = max(right, cal_rob(root.right, flag))
                
            cur = left+right
            if flag: cur += root.val
                
            return cur
        
        return max(cal_rob(root))
'''