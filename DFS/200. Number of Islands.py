# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        def dfs(r, c):
            if r<0 or c<0 or r>=n or c>=m or grid[r][c]=="0":
                return 0
            grid[r][c]="0"
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
            return 1
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    count+=dfs(i,j)
        return count

# Time and Space complexity - O(n*m)