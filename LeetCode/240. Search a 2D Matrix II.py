# my solution(terrible)
# time - O(NMlog(NM))
# space - O(N if N > M else M)
from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix, target):
        # row, col에 대하여 bst 해서 사각형 범위를 줄임
        # 값이 안나왔으면 row+1, col+1해서 다시 반복
        R, C = len(matrix), len(matrix[0])
        r, c = 0, 0
        
        while r < R and c < C:
            rows = []
            cols = []
            
            # O(N)
            for i in range(c, C):
                cols.append(matrix[r][i])
            for i in range(r, R):
                rows.append(matrix[i][c])
            
            R = bisect_left(rows, target)+r
            C = bisect_left(cols, target)+c
            
            if 0 <= R < len(matrix) and matrix[R][c] == target: return True
            if 0 <= C < len(matrix[0]) and matrix[r][C] == target: return True
        
            r += 1
            c += 1
            
        return False
                
    # time - O(NM)
    # space - O(1)
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True

# best solution
# time - O(N+M)
# space - O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        r, c = 0, len(matrix[0])-1          # top-right
        while c >= 0 and r < len(matrix):
            if matrix[r][c] > target:       # to left
                c -= 1
            elif matrix[r][c] < target:     # to bottom
                r += 1
            else:
                return True
        return False

# another solution
# time - O(NlogM)
# space - O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        h, w = len(matrix), len(matrix[0])
        for row in matrix:
            left, right = 0, w-1
            i = bisect_left(row, target, lo=left, hi=right)
            if row[i] == target:
                return True
        return False