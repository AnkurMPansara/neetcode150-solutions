class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        if self.smallHeap and -self.smallHeap[0] > num:
            heapq.heappush(self.smallHeap, -num)
        else:
            heapq.heappush(self.largeHeap, num)
        if len(self.smallHeap) - len(self.largeHeap) > 1:
            heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))
        if len(self.largeHeap) - len(self.smallHeap) > 1:
            heapq.heappush(self.smallHeap, -heapq.heappop(self.largeHeap))

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        elif len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        else:
            return (self.largeHeap[0]-self.smallHeap[0])/2