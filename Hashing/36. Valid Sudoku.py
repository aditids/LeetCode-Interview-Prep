# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            hset = set()
            cset = set()
            for j in range(n):
                if board[i][j] in hset:
                    return False
                if board[i][j]!='.':
                    hset.add(board[i][j])
                if board[j][i] in cset:
                    return False
                if board[j][i]!='.':
                    cset.add(board[j][i])
                    
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                tset = set()
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] != '.':
                            if board[r+i][c+j] in tset:
                                return False
                            tset.add(board[r+i][c+j])
        return True