from collections import deque, defaultdict

n, k = map(int, input().split())

def bfs(n, k):
    queue = deque([[n, 0]])
    visited = defaultdict(int)
    while True:
        pos, count = queue.popleft()
        print(pos, end=' ')
        if pos == k:
            return count
        if not visited[pos] and 0 <= pos:
            queue.append((pos+1, count+1))
            queue.append((pos-1, count+1))
            queue.append((pos*2, count+1))
            visited[pos] = 1

print(bfs(n, k))