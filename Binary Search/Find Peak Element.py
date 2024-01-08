# Find Peak Element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        while l < r:
            m = l + (r - l) // 2
            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return l