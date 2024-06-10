# 918. Maximum Sum Circular Subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 0
        minsum = nums[0]
        total = sum(nums)
        curmin = 0
        for i, num in enumerate(nums):
            cur = max(cur,0)+num
            res = max(res, cur)  
            curmin = min(curmin, 0) + num
            minsum = min(minsum, curmin)   
        if total == minsum:
            return res   
        return max(res, total-minsum)