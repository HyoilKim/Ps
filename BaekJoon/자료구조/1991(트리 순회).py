# dictionary를 사용한 tree
class Node:
    def __init__(self, val, left, right):
        self.val = val 
        self.left = left
        self.right = right
    
def pre_order(node):
    print(node.val, end="")
    if node.left != '.': pre_order(root[node.left])
    if node.right != '.': pre_order(root[node.right])

def in_order(node):
    if node.left != '.': in_order(root[node.left])
    print(node.val, end="")
    if node.right != '.': in_order(root[node.right])

def post_order(node):
    if node.left != '.': post_order(root[node.left])
    if node.right != '.': post_order(root[node.right])
    print(node.val, end="")

n = int(input())
root = {}
for _ in range(n):
    val, left, right = input().split()
    root[val] = Node(val, left, right)

pre_order(root['A'])
print()
in_order(root['A'])
print()
post_order(root['A'])

# class를 활용한 tree
# None -> '.'
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left  == None : self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inorderTraversal(node.right)
    
    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node

