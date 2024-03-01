# 2352. Equal Row and Column Pairs

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r = Counter(tuple(row) for row in grid)
        transposed_grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        c = Counter(tuple(col) for col in transposed_grid)
        count = 0
        for k,v in r.items():
            if k in c:
                count+=v*c[k]
        return count