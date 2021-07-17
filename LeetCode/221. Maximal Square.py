# my solution
# time - O(n*m) / n: len(matrix), m: len(matrix[0])
# space - O(n*m)
class Solution:
    def maximalSquare(self, matrix):
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        max_len = 0
        
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            max_len = max(max_len, dp[i][0])
            
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
            max_len = max(max_len, dp[0][i])
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_len = max(max_len, dp[i][j])
                
        return max_len**2

    # clean code 1
    def maximalSquare(self, matrix):
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]        
        max_len = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_len = max(max_len, dp[i][j])
                
        return max_len**2

    # clean code 2(easy)
    def maximalSquare(self, matrix):
        dp = [[0]*(len(matrix[0])) for _ in range(len(matrix))]        
        max_len = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_len = max(max_len, dp[i][j])
                
        return max_len**2

# better solution
# time - O(nm)
# space - O(n)
class Solution:
    def maximalSquare(self, matrix):
        dp = [0]*(len(matrix[0])+1)
        max_len = 0
        prev = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(prev, dp[j-1], dp[j]) + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0
                prev = tmp

        return max_len**2