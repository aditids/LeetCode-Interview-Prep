# 51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        visit = set()
        positive_diagonal = set()
        negative_diagonal = set()
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                temp = [''.join(i) for i in board]
                result.append(temp)
                return
            
            for c in range(n):
                if c not in visit and r+c not in positive_diagonal and r-c not in negative_diagonal:
                    board[r][c] = 'Q'
                    visit.add(c)
                    positive_diagonal.add(r+c)
                    negative_diagonal.add(r-c)

                    backtrack(r+1)

                    board[r][c] = '.'
                    visit.remove(c)
                    positive_diagonal.remove(r+c)
                    negative_diagonal.remove(r-c)

        backtrack(0)
        return result