# 494. Target Sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i,t):
            if i == len(nums):
                return 1 if t == target else 0
            if (i,t) in dp:
                return dp[(i,t)]
            dp[(i,t)] = backtrack(i+1,t+nums[i])+ backtrack(i+1,t-nums[i])
            print("dp[",i,",",t,"]",dp[(i,t)])
            return dp[(i,t)]
        return backtrack(0,0)       