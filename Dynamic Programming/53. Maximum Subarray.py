# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tsum = 0
        msum = -inf
        for i in nums:
            tsum+=i
            msum = max(msum,tsum)
            if tsum<0:
                tsum=0
        return msum