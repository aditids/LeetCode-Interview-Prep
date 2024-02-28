# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r1 = [1]*n
        for i in range(m-1):
            r2 = [1]*n
            for j in range(n-2,-1,-1):
                r2[j] = r2[j+1]+r1[j]
            r1 = r2
        return r1[0]

        # Time complexity - O(m*n)
        # Space complexity - O(n)