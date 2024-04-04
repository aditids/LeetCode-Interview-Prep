# 120. Triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0]*(len(triangle)+1)
        for i in triangle[::-1]:
            for k, val in enumerate(i):
                dp[k] = val + min(dp[k],dp[k+1])
            #print(dp)
        return dp[0]