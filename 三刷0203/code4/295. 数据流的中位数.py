import heapq
class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        if len(self.left)==len(self.right):
            if len(self.left)==0:
                heapq.heappush(self.left,-num)
                return
            
            r=self.right[0]
            if r<num:
                heapq.heappushpop(self.right,num)
                heapq.heappush(self.left,-r)
            else:
                heapq.heappush(self.left,-num)
        
        else:
            l=-self.left[0]
            if l>num:
                heapq.heappushpop(self.left,-num)
                heapq.heappush(self.right,l)
            else:
                heapq.heappush(self.right,num)


    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            return (self.right[0]-self.left[0])/2
        else:
            return -self.left[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()