# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = max(nums)
        cmax, cmin = 1, 1
        for i in nums:
            temp = cmax
            cmax = max(cmax*i, cmin*i, i)
            cmin = min(temp*i, cmin*i, i)
            maxProduct = max(cmax, maxProduct)
        return maxProduct