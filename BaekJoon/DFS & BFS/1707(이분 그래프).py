from collections import deque, defaultdict
import sys

def bfs(graph, v, e):
    queue = deque()
    color = [0]*(v+1) # 디폴트 0 / set_1 : 1 / set_2 : -
    visited = [False]*(v+1)
    for i, value in graph.items():
        if visited[i]:
            continue
        queue.append(i)
        color[i] = 1
        visited[i] = True
        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if color[cur] == color[nxt]:
                    return "NO"
                if not visited[nxt]:
                    queue.append(nxt)
                    visited[nxt] = True
                    color[nxt] = 1 if color[cur] == -1 else -1
    return "YES"

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for _ in range(n):
        v, e = map(int, sys.stdin.readline().split())

        graph = defaultdict(list)
        for _ in range(e):
            v1, v2 = map(int, sys.stdin.readline().split())
            graph[v1].append(v2)
            graph[v2].append(v1)

        res=bfs(graph, v, e)
        print(res)