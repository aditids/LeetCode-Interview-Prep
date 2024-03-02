# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            k^=i
        return k