# best solution
# 접근방법
# 1. 먼저 recursion으로 해결
# 2. memoization 추가
# 이 문제는 recursion으로 푸는 방법이 생각이 안남
# 전체를 한 번에 해결하려고 하지 말고 문제를 쪼개어 생각하기
# 문자열을 하나씩 비교하면서 3가지 속성을 실행 했을 때를 반복
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistance2(word1, word2, 0, 0, {})
        
    def minDistance2(self, word1, word2, i, j, memo):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance2(word1, word2, i + 1, j + 1, memo)
            else: 
                insert = 1 + self.minDistance2(word1, word2, i, j + 1, memo)
                delete = 1 + self.minDistance2(word1, word2, i + 1, j, memo)
                replace = 1 + self.minDistance2(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]