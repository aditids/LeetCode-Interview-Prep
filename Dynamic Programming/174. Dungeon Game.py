# 174. Dungeon Game

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r, c = len(dungeon), len(dungeon[0])
        dp = [[inf]*(c+1) for i in range(r+1)]
        dp[r][c-1] = 1
        dp[r-1][c] = 1
        print(dp)
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                min_health = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, min_health)
        return dp[0][0]