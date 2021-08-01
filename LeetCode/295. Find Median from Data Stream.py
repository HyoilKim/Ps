# addNum time - O(logN)
# findMedian time - O(1)
# space - O(N)
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            # small의 pushpop 결과는 큰 중간값이다
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num)) # -num or (num, -num) -> max heap
        else:
            # large의 pushpop 결과는 작은 중간값이다
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return self.large[0]