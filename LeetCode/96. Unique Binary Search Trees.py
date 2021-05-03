# my solution
# recursion + memoization
class Solution:
    def __init__(self):
        self.memo = [0]*20
        
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            if not self.memo[n]:
                total = 0
                for i in range(n):
                    total += self.numTrees(i) * self.numTrees(n-1-i)
                self.memo[n] = total
            return self.memo[n]
                
# another solution
class Solution:
    def numTrees(self, n):
        arr = [0]*(n+1)
        arr[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                arr[i] += arr[j-1] * arr[i-j]
        return arr[-1]