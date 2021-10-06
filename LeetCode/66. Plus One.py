# my solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [x for x in str(int(''.join(map(str, digits)))+1)]