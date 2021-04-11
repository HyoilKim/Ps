# my solution
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            x, y = i, i
            n = len(matrix) - (2*i)
            for _ in range(n-1):
                tmp = matrix[x][y]
                for j in range(1, n):
                    matrix[x+(j-1)][y] = matrix[x+j][y]
                    
                for j in range(1, n):
                    matrix[x+n-1][y+(j-1)] = matrix[x+n-1][y+j]
                    
                for j in range(n-1, 0, -1):
                    matrix[x+j][y+n-1] = matrix[x+(j-1)][y+n-1]

                for j in range(n-1, 0, -1):
                    matrix[x][y+j] = matrix[x][y+(j-1)]
                    if j == 1:
                        matrix[x][y+j] = tmp

# best solution 1
# 1칸씩 rotate 하는 것이 아니라
# rotate된 결과로 바로 결정지음
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


# best solution 2
# Rotated = Transposed + Reversed
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]