# 73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zero = set()
        cols_to_zero = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for row in rows_to_zero:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        for col in cols_to_zero:
            for i in range(len(matrix)):
                matrix[i][col] = 0

# Time Complexity - O(m * n)
# Space Complexity - O(m+n)