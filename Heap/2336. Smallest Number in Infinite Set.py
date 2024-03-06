# 2336. Smallest Number in Infinite Set

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.inf_set = set()
        self.small = 1

    def popSmallest(self) -> int:
        if self.heap:
            k = heapq.heappop(self.heap)
            self.inf_set.remove(k)
            return k
        else:
            k = self.small
            self.small+=1
            return k

    def addBack(self, num: int) -> None:
        if num<self.small and num not in self.inf_set:
            heapq.heappush(self.heap,num)
            self.inf_set.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)