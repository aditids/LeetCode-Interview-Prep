# 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = [-inf]*(len(nums))
        lsum = 0
        for i in range(len(nums)):
            sumLeft[i] = lsum
            lsum+=nums[i]

        sumRight = [-inf]*(len(nums))
        rsum = 0
        for i in range(len(nums)-1,-1,-1):
            sumRight[i] = rsum
            rsum+=nums[i]

        for i in range(len(nums)):
            if sumLeft[i] == sumRight[i]:
                return i

        return -1