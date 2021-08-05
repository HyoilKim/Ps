# my solution
# time - O(NlogN)
# space - O(N)
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        # dic = Counter(nums)

        arr = [(k,v) for k,v in dic.items()]
        arr.sort(key=lambda x: x[1], reverse=True)
        result = [arr[i][0] for i in range(k)]
        return result
        
# clean and short solution
# time - O(NlogN)
# space - O(N)
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        most_common = Counter(nums).most_common()
        res = [most_common[i][0] for i in range(k)]
        return res
    
# heap solution
# time - O(NlogK)
# space - O(N+K)
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k): 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 

# buckets solution(best)
# time - O(N)
# space - O(N)
'''
chain()
첫 번째 이터러블에서 소진될 때까지 요소를 반환한 다음 이터러블로 넘어가고, 
이런 식으로 iterables의 모든 이터러블이 소진될 때까지 진행하는 이터레이터를 만듭니다. 
여러 시퀀스를 단일 시퀀스처럼 처리하는 데 사용됩니다.
'''
from collections import chain
class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]