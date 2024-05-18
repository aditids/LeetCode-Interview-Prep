# 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums)-1
        if r==0:
            return True
        l = r-1
        while l>=0:
            if nums[l]+l>=r:
                r=l
            l-=1
        return True if r==0 else False