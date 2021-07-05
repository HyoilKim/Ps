# readable solution
class Solution(object):
    def wordBreak(self, s, wordDict): 
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]

# short solution
# speed: += value > append(value) > +=[value]
# ok[i] tells whether s[:i] can be built.
class Solution:                    
    def wordBreak(self, s, words):
        ok = [True]
        words = set(words)
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)), # ',' value to tuple -> extends array
        return ok[-1]

    # not pythonic
    def wordBreak(self, s, words):
        ok = [True]
        words = set(words)
        for i in range(1, len(s)+1):
            for j in range(i):
                flag = False
                if ok[j] and s[j:i] in words:
                    flag = True
                    break
            if flag:
                ok += [True]
            else:
                ok += [False]
        return ok[-1]

# dfs/bfs
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        seen = set() 
        while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False

# brute force
# Time-Complexity: O(2^n)
# T(N) = T(N-1) + T(N-2) + ... + T(0)
# T(N-1) = T(N-2) + ... + T(0)
# T(N) - T(N-1) = T(N-1)
# T(N) = 2*T(N-1))
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s, word_set):
            if len(s) == 0:
                return True
            
            for i in range(1,len(s)+1):
                if s[:i] in word_set and dfs(s[i:], word_set):
                    return True
            return False
            
        word_set = set(wordDict)
        return dfs(s, word_set)


