# 200. Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!="1":
                return False
            grid[i][j] = "0"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if dfs(i,j):
                        count+=1

        return count