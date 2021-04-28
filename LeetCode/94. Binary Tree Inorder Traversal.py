# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution - recursive
# time complexity: O(N)
# space complexity: worst-O(N), avg-O(logN)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans
    
    def inorder(self, node, ans):
        if node:
            self.inorder(node.left, ans)
            ans.append(node.val)
            self.inorder(node.right, ans)

# another solution - stack
# time complexity: O(N)
# space complexity: O(logN)
public class Solution {
    public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        Stack < TreeNode > stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}