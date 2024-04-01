# 2542. Maximum Subsequence Score

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [(i,j) for i,j in zip(nums1,nums2)]
        nums = sorted(nums, key=lambda i:i[1], reverse=True)
        minHeap = []
        score = 0
        maxScore = 0
        for i,j in nums:
            score+=i
            heapq.heappush(minHeap,i)
            if len(minHeap)>k:
                temp = heapq.heappop(minHeap)
                score-=temp
            if len(minHeap)==k:
                maxScore = max(maxScore, score*j)
        return maxScore
    
    # Time Complexity - O(nlogn)