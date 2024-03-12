# 212. Word Search II

class TrieNode:
    def __init__(self):
        self.children = {}
        self.tail = False

    def add(self, word):
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.tail = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        visited = set()
        root = TrieNode()

        for i in words:
            root.add(i)

            def dfs(i,j,cur,word):
                if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or (i,j) in visited or board[i][j] not in cur.children:
                    return False
                visited.add((i,j))
                cur = cur.children[board[i][j]]
                word+=board[i][j]
                if cur.tail:
                    result.add(word)
                dfs(i+1,j,cur,word)
                dfs(i-1,j,cur,word)
                dfs(i,j+1,cur,word)
                dfs(i,j-1,cur,word)
                visited.remove((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root,'')

        return list(result)