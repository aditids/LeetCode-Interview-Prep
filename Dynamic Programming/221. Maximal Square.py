# 221. Maximal Square

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for j in range(m+1)]
        l = 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])+1
                    l = max(l,dp[i][j])
        #print(dp)   
        return l*l