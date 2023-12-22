# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # i = 0
        # j = 1
        # temp = []
        # count=0
        # while i<(len(nums)-1):
        #     if nums[i]!=nums[j] and j<len(nums):
        #         return nums[i]
        #     i=i+2
        #     j=j+2
        # return nums[len(nums)-1]
        result = 0
        for i in nums:
            result = result ^ i #xor
            print(result)
        return result    
    # Time complexity - O(n)
    # Space complexity - O(1)