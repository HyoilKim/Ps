from collections import deque

def solution(n, computer):
    def bfs(x, computer):
        queue.append(x)
        computer[x][x] = 0
        while queue:
            x = queue.popleft()
            for y in range(len(computer[x])):
                if computer[x][y] == 1:
                    computer[x][y] = 0
                    bfs(y, computer)
                    
    queue = deque()
    answer = 0
    for i in range(len(computer)):
        if sum(computer[i]) != 0:
            answer += 1
            bfs(i, computer)
    return answer

n = 3
computer = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
res = solution(n, computer)
print(res)

'''
101
010
101

110
110
001

110
111
011
'''