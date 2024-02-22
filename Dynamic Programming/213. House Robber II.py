# 213. House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        def calc(arr):
            a,b = 0,0
            for i in arr:
                temp = max(a+i,b)
                a = b
                b = temp
            return b

        return max(nums[0],calc(nums[1:]), calc(nums[:-1]))