# recursive inorder traversal
# time - O(N)
# space - O(N)
class Solution:
    def kthSmallest(self, root, k):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return inorder(root)[k-1]

'''
# iterative inorder traversal
# time - O(H+k), H: tree height
-> balanced tree - (logN+k)
-> unbalnced tree - (N+k)
# space - O(H)
-> balanced tree - (logN)
-> unbalnced tree - (N)
'''
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)  
                root = root.left    # bst는 왼쪽에 더 작은 값이 있기 때문에
            root = stack.pop()      # 작은 순서대로 값이 나옴
            k -= 1
            if not k:
                return root.val
            root = root.right

'''
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?

Insert and delete in a BST: O(H)
Hence without any optimisation insert/delete + search: O(2H+k) 

optimisation: 각 노드 값을 double linked list로 구현

time-complexity
- best: O(logN+k)
- wrost: O(N+k)
space-complexity
- O(N)
'''


'''
[Segment Tree]
Can probably do search in O(H) time, but need O(N) additional storage.
For each node in the tree, we precompute how many are to the left and how many are to the right. 
Then at each node, we will know whether the k-th smallest is at the left or the right branch. 
Search, insert, delete are all O(H).
'''