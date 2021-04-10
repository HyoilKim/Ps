class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.perm(nums, [], result, dict())
        return result
        
    def perm(self, nums, s, result, dic):
        if len(nums) == len(s):
            result.append(s)
        
        for i in range(len(nums)):
            if dic.get(nums[i], 0) == 0:
                dic[nums[i]] = 1
                self.perm(nums, s+[nums[i]], result, dic)
                del dic[nums[i]]
                
# best solution
# parameter에 slicing 결과를 넘기면 시간 복잡도는 동일 하지만,
# 재귀 호출이 점점 줄어들어서 dictionary를 만드는 것 보다 빨라짐
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        