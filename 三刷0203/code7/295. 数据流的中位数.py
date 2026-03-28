import heapq

class MedianFinder:

    def __init__(self):
        self.size=0
        self.heap1=[]
        self.heap2=[]


    def addNum(self, num: int) -> None:
        self.size+=1
        if len(self.heap1)==len(self.heap2):
            num=heapq.heappushpop(self.heap2,num)
            heapq.heappush(self.heap1,-num)
        else:
            num=heapq.heappushpop(self.heap1,-num)
            heapq.heappush(self.heap2,-num)

    def findMedian(self) -> float:
        if self.size%2==1:
            return -self.heap1[0]
        else:
            return (self.heap2[0]-self.heap1[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()