# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        while r<len(nums):
            count = 1
            while r<len(nums)-1 and nums[r]==nums[r+1]:
                count+=1
                r+=1
            for i in range(min(count,2)):
                nums[l] = nums[r]
                l+=1
            r+=1
        return l