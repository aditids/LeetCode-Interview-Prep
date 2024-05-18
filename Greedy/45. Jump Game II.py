# 45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJump = 0
        curEnd = 0
        count = 0
        for i in range(len(nums)-1):
            maxJump = max(maxJump,i+nums[i])
            if i == curEnd:
                count+=1
                curEnd = maxJump

                if curEnd >= len(nums)-1:
                    return count
        return count