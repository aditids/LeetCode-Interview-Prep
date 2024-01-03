# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]> nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]
        # Time complexity - O(log n)
        # Space complexity - O(1)