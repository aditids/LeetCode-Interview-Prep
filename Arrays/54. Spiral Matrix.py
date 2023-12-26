# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])
        row, col = 0,0
        while row<m and col<n:
            for i in range(col, n):
                result.append(matrix[row][i])
            
            row+=1
            for i in range(row, m):
                result.append(matrix[i][n-1])

            n-=1

            if row<m:
                for i in range(n-1, col-1,-1):
                    result.append(matrix[m-1][i])

            m-=1
            if col<n:
                for i in range(m-1, row-1, -1):
                    result.append(matrix[i][col])
            col+=1
        
        return result
        
        # Time and Space Complexity -  O(m * n)