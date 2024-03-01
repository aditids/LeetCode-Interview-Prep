# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        f=0
        mcount = 0
        for r in range(len(nums)):
            if nums[r]==0:
                f+=1
            if f>1:               
                while nums[l]!=0:
                    l+=1
                l+=1
                f-=1  
            mcount = max(mcount, r-l)
        return mcount   