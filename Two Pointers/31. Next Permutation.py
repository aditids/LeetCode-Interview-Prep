# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = n-2
        while r>=0 and nums[r]>=nums[r+1]:
            r-=1
        if r>=0:
            j = n-1
            while nums[r]>=nums[j]:
                j-=1
            nums[r], nums[j] = nums[j], nums[r]
        j = n-1
        r+=1
        while r<j:
            nums[r],nums[j] = nums[j],nums[r]
            r+=1
            j-=1