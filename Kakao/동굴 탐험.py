from collections import defaultdict
def solution(n, path, order):
    before = defaultdict(int)   # x:y -> x 이후에 y를 방문해야 하는 경우
    after = defaultdict(int)
    nodes = defaultdict(list)

    for v1,v2 in path:
        nodes[v1].append(v2)
        nodes[v2].append(v1)
    
    for v1,v2 in order:
        if v2 == 0:      # root를 나중에 탐색해야 하는 경우
            return False
        before[v2] = v1
    stack = [0]
    visited = [False]*n
    
    ### 탐색
    while stack:
        cur = stack.pop()
        if cur in before and not visited[before[cur]]: # 이전에 방문해야 할 것이 있지만, 방문 하지 않은 경우
            after[before[cur]] = cur
            continue
        elif cur in after:           # 현재 노드 이후에 방문해야 할 곳이 있으면
            stack.append(after[cur]) # 바로 방문하기(기다리고 있었음)
            
        visited[cur] = True
        for adj in nodes[cur]:
            if not visited[adj]:
                stack.append(adj)
        
    return True if False not in visited else False