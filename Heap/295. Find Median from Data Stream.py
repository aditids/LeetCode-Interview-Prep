# 295. Find Median from Data Stream

class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1, -1*num)
        if self.heap1 and self.heap2 and -1*self.heap1[0]>self.heap2[0]:
            temp = heapq.heappop(self.heap1)*-1
            heapq.heappush(self.heap2, temp)

        if len(self.heap1)>len(self.heap2)+1:
            temp = heapq.heappop(self.heap1)*-1
            heapq.heappush(self.heap2, temp)

        if len(self.heap2)>len(self.heap1)+1:
            temp = heapq.heappop(self.heap2)*-1
            heapq.heappush(self.heap1, temp)

        # Time complexity -> Add/remove - O(1) and Sorting - O(logn)

    def findMedian(self) -> float:
        if len(self.heap1)>len(self.heap2):
            return self.heap1[0]*-1
        if len(self.heap2)>len(self.heap1):
            return self.heap2[0]
        return ((self.heap1[0]*-1)+(self.heap2[0]))/2
    # Time complexity -> O(1)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()