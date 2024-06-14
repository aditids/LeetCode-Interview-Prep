# 289. Game of Life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbors = [(0,-1),(0,1),(1,0),(1,1),(-1,0),(-1,-1),(-1,1),(1,-1)]

        for i in range(m):
            for j in range(n):
                count = 0
                for r,c in neighbors:
                    row = i+r
                    col = j+c
                    
                    if (row<m and row>=0) and (col<n and col>=0) and abs(board[row][col]) == 1:
                        count+=1
                if board[i][j] == 1 and (count<2 or count>3):
                    board[i][j] = -1

                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0