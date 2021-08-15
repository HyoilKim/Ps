# max heap solution
# time - O(N*n) / n is cool-off period
# space - O(1) / O(26)
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks, n):        
        order = []
        for task, freq in Counter(tasks).items():
            heapq.heappush(order, (-freq, (task,freq)))
        
        time = 0
        while order:
            i, tmp = 0, []
            while i <= n:
                time += 1
                if order:
                    freq, item = heapq.heappop(order)
                    if freq != -1: # 2번 이상 나온 task만 저장
                        tmp.append((freq+1, item))
                if not order and not tmp:
                    break    
                i += 1
            for item in tmp:
                heapq.heappush(order, item)
                
        return time

# math solution
# time - O(N)
# space - O(1)
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)