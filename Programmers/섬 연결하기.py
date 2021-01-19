def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    parent = [i for i in range(n)]
    total = 0
    count = 0
    for x in costs:
        if not is_same_parent(parent, x[0], x[1]):
            parent = union_parent(parent, x[0], x[1])
            total += x[2]
            count += 1
            if count == n-1:
                break
            
    print(total)
    return total

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return parent

def get_parent(parent, x):
    if parent[x] == x:
        return x
    else:
        return get_parent(parent, parent[x])

def is_same_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    return True if a == b else False

n = 7
costs = [[0,6,12],[0,3,28],[0,1,67],[0,4,17],
        [1,3,24],[1,4,62],[2,4,20],[2,5,37],[3,6,13],
        [4,5,45],[4,6,73]]
solution(n, costs)

# best solution
import heapq as hq

def solution(n, costs):
    answer = 0
    from_to = list(list() for _ in range(n))
    visited = [False] * n
    priority = []

    for a, b, cost in costs:
        from_to[a].append((b, cost))
        from_to[b].append((a, cost))

    hq.heappush(priority, (0, 0))
    while False in visited:
        cost, start = hq.heappop(priority)
        if visited[start]: continue

        visited[start] = True
        answer += cost
        for end, cost in from_to[start]:
            if visited[end] : continue
            else:
                hq.heappush(priority, (cost, end))

    return answer