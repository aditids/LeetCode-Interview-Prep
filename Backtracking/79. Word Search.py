# 79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        uniquePath = set()
        def dfs(i,j,index):
            if index == len(word): return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or (i,j) in uniquePath or word[index]!=board[i][j]:
                return False
            uniquePath.add((i,j))
            result = dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1)
            uniquePath.remove((i,j))
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False