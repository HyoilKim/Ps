def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**6)

    # set input data
    # algorithm complexity O(nlogn)
    indata = nodeinfo

    # make nodeList
    nodeList = [indata[i] + [i+1] for i in range(len(indata))]
    nodeList = sorted(nodeList, key=lambda x : x[1], reverse=True)


    # make binary tree
    class node:
        def __init__(self, info):
            self.number = info[2]
            self.data = info[:2]
            self.R = None
            self.L = None

    def addnode(root, info):
        if info[0] > root.data[0]:
            if root.R == None:
                root.R = node(info)
            else:
                addnode(root.R, info)
        elif info[0] < root.data[0]:
            if root.L == None:
                root.L = node(info)
            else:
                addnode(root.L, info)
        else:
            raise ValueError('unexpected input')

    root = node(nodeList[0])
    for info in nodeList[1:]:
        addnode(root, info)


    # do preorder, postorder and sol
    def preorder(root, orderList):
        # priority root --> left --> right
        if root != None:
            orderList.append(root.number)
            preorder(root.L, orderList)
            preorder(root.R, orderList)

    preorderList = []
    preorder(root, preorderList)

    def postorder(root, orderList):
        # priority left --> right --> root
        if root != None:
            postorder(root.L, orderList)
            postorder(root.R, orderList)
            orderList.append(root.number)

    postorderList = []
    postorder(root, postorderList)

    sol = [preorderList, postorderList]
    #print('prediction : {}\nsolution : {}'.format(sol, result))
    answer = sol
    return answer