class Solution:
    def totalFruit(self, tree):
        count, i = {}, 0
        res = 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
            res = max(res, j-i+1)
        return res
      
"""
Problem
"Start from any index, we can collect at most two types of fruits. What is the maximum amount"


Translation
Find out the longest length of subarrays with at most 2 different numbers?


Explanation
Solve with sliding window,
and maintain a hashmap counter,
which count the number of element between the two pointers.
Find more infinite similar prolems in the end.


Complexity
Time O(n)
Space O(1)
"""
