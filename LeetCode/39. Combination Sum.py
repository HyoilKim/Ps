# my solution
class Solution:
    def backtracking(self, idx, candidates, target, stack, result):
        if target < 0:
            return
        elif target == 0:
            result.append(stack)

        for i in range(idx, len(candidates)):
            self.backtracking(i, candidates, target-candidates[i], stack+[candidates[i]], result)
        
    # condidates 정렬 하지 않아도 됨
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(0, candidates, target, [], result)
        return result

# best solution
# candidates 정렬 하고 
# for에서 candidates[i] > target 인 경우에
# break 하면 성능 향상