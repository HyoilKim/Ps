# my solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dup = set()
            for j in range(9):
                if board[i][j] == '.': continue
                if board[i][j] in dup: return False
                dup.add(board[i][j])
              
        for i in range(9):
            dup = set()
            for j in range(9):
                if board[j][i] == '.': continue
                if board[j][i] in dup: return False
                dup.add(board[j][i])
        
        for i, j in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
            dup = set()
            for ii in range(3):
                for jj in range(3):
                    if board[i+ii][j+jj] == '.': continue
                    if board[i+ii][j+jj] in dup: return False
                    dup.add(board[i+ii][j+jj])
        
        return True

# short code
def isValidSudoku(self, board):
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(c,j),(i,c),(i/3,j/3,c)]
    return len(seen) == len(set(seen))

# clean code
def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True

def is_col_valid(self, board):
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True

def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6): # pythonic
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True
    
def is_unit_valid(self, unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit) # cool