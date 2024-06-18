# 373. Find K Pairs with Smallest Sums

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in nums1:
            for j in nums2:
                if len(heap)<k:
                    heapq.heappush(heap,[-(i+j),[i,j]])
                else:
                    if i + j < -heap[0][0]:
                        heapq.heappushpop(heap, [-(i+j),[i,j]])
                    else:
                        break        
            
        result = []
        for i in range(len(heap)):
            _, pair = heapq.heappop(heap)
            result.append(pair)
        return result