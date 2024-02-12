# 417. Pacific Atlantic Water Flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        result = []

        def dfs(row, col, prev, visited):
            if (row, col) in visited or row<0 or col<0 or row>=rows or col>=cols or heights[row][col]<prev:
                return

            visited.add((row,col))

            dfs(row+1, col, heights[row][col], visited)
            dfs(row-1, col, heights[row][col], visited)
            dfs(row, col+1, heights[row][col], visited)
            dfs(row, col-1, heights[row][col], visited)
        
        for row in range(rows):
            dfs(row,0,heights[row][0],pacific)
            dfs(row,cols-1,heights[row][cols-1],atlantic)

        for col in range(cols):
            dfs(0,col,heights[0][col],pacific)
            dfs(rows-1,col,heights[rows-1][col],atlantic)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in atlantic and (row, col) in pacific:
                    result.append([row, col])

        return result

# Time and Space Complexities - O(rows * cols)