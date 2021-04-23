from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def is_tree(tree, root, set_child):
    queue = deque([root])
    visited = [False]*100000
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if visited[child]:
                return False
            else:
                visited[child] = True
                queue.append(child)
    
    # 방문하지 않은 자식 노드가 있으면 
    # root에서 도달하지 못하는 자식이 있다는 것
    for child in set_child:
        if not visited[child]:
            return False

    return True
        
if __name__ == "__main__":
    k = 1
    while True:
        tree = defaultdict(list)
        set_all = set()
        set_child = set()
        iuput_flag = system_flag = False
        while True:
            for pair in input().rstrip().split("  "):
                if not pair:            # 빈 입력 처리
                    continue
                u, v = map(int, pair.split())
                if u == 0 and v == 0:   # input 종료
                    iuput_flag = True 
                    break
                elif u < 0 and v < 0:   # system 종료
                    system_flag = True
                    break
                tree[u].append(v)       # tree 생성
                set_all.add(u)          # 모든 node 저장
                set_all.add(v)          # 
                set_child.add(v)        # child node 저장
            if iuput_flag or system_flag:
                break
        if system_flag:
            break

        try:                            # child가 아닌 root node 필수
            root = (set_all-set_child).pop()
        except:
            root = None
            
        if is_tree(tree, root, set_child):
            print("Case {} is a tree.".format(k))
        else:
            print("Case {} is not a tree.".format(k))
        
        k += 1