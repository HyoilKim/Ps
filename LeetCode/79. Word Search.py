# my solution - dfs
class Solution:
    def __init__(self):
        self.dx = [1,0,-1,0]
        self.dy = [0,1,0,-1]
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.back((i,j), board, word[1:], visited):
                        return True
                    visited[i][j] = False
        return False
    
    def back(self, pos, board, word, visited):
        if word == '': 
            return True
        
        for i in range(4):
            nx = pos[0]+self.dx[i]
            ny = pos[1]+self.dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if visited[nx][ny]: continue
                if word[0] == board[nx][ny]:
                    visited[nx][ny] = True
                    if self.back((nx,ny), board, word[1:], visited):
                        return True
                    visited[nx][ny] = False
        return False

# for 다른 표현방식 1
#  res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
#   or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])

# for 다른 표현방식 2
# if i > 0 and self.back(board, word[1:], i-1, j):
#     return True
# if i < len(board)-1 and self.back(board, word[1:], i+1, j):
#     return True
# if j > 0 and self.back(board, word[1:], i, j-1):
#     return True
# if j < len(board[0])-1 and self.back(board, word[1:], i, j+1):
#     return True