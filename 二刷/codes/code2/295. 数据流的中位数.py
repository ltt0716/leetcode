import heapq


class MedianFinder:

    def __init__(self):
        self.leftheap = []
        self.rightheap = []

    def addNum(self, num: int) -> None:
        if len(self.leftheap) == 0:
            heapq.heappush(self.leftheap, -num)
            return

        if len(self.leftheap) == len(self.rightheap):
            x = heapq.heappushpop(self.rightheap, num)
            heapq.heappush(self.leftheap, -x)

        else:
            x = heapq.heappushpop(self.leftheap, -num)
            heapq.heappush(self.rightheap, -x)

    def findMedian(self) -> float:
        if len(self.leftheap) == len(self.rightheap):
            return (self.rightheap[0] - self.leftheap[0]) / 2
        else:
            return -self.leftheap[0]


