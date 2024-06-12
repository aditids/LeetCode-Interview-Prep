# 130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        j = 0

        def edge(r,c):
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!='O':
                return
            board[r][c] = -1
            edge(r+1,c)
            edge(r-1,c)
            edge(r,c+1)
            edge(r,c-1)

        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!='O':
                return
            board[r][c] = 'X'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(m):
            if board[i][j] == 'O':
                edge(i,j)
            if board[i][n-1] == 'O':
                edge(i,n-1)

        i = 0
        for j in range(n):
            if board[i][j] == 'O':
                edge(i,j)
            if board[m-1][j] == 'O':
                edge(m-1,j)

        for i in range(1,m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 'O'