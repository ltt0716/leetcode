import bisect
import heapq

class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        if len(self.left)==len(self.right):
            newnum=heapq.heappushpop(self.right,num)
            heapq.heappush(self.left,-newnum)
        else:
            newnum=heapq.heappushpop(self.left,-num)
            heapq.heappush(self.right,-newnum)
    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            return (self.right[0]-self.left[0])/2
        else:
            return -self.left[0]

