# my solution
# 316ms, 19.5MB
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def make_bit_tree(cur, bits, dic):
            if not cur: return
            dic[bits] = cur.val
            if cur.left: make_bit_tree(cur.left, bits+'0', dic)
            if cur.right: make_bit_tree(cur.right, bits+'1', dic)
            
        dic = dict()
        make_bit_tree(root, '', dic)
        return dic
        
    def deserialize(self, data):
        def make_tree(node, bit, val):
            if not bit:
                node.val = val
                return
            
            if bit[0] == '0':
                if not node.left: node.left = TreeNode(None)
                make_tree(node.left, bit[1:], val)
            else:
                if not node.right: node.right = TreeNode(None)
                make_tree(node.right, bit[1:], val)
                
        if not data: 
            return
        root = TreeNode(data[''])
        for bit in data:
            make_tree(root, bit, data[bit])
        return root

# best solution
# 92ms, 18.8MB
class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals) # 배열 메모리 > 문자열 메모리

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()