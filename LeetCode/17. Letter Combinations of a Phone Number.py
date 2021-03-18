class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        buttons = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []

        def backtracking(idx, letters):
            if len(letters) == len(digits):
                result.append(letters)
                return

            for i in range(idx+1, len(digits)):
                for ch in buttons[digits[i]]:
                    backtracking(i, letters+ch) 

        backtracking(-1, "")
        return result