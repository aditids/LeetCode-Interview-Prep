# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        heap = []
        for i in nums:
            hash_table[i] = hash_table.get(i,0) + 1
        
        for i,j in hash_table.items():
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        #print(heap)
        return [i[1] for i in heap]


        # hash_table = {}
        # result = []
        # for i in nums:
        #     hash_table[i] = hash_table.get(i,0) + 1
        # while k:
        #     result.append(max(hash_table, key=hash_table.get))
        #     del hash_table[result[-1]]
        #     k-=1
        # return result