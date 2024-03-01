# 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [inf]*(len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i]+min(dp[i-1],dp[i-2])

        return min(dp[len(dp)-1],dp[len(dp)-2])