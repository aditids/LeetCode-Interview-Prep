# 211. Design Add and Search Words Data Structure

class TrieNode:
    def __init__(self):
        self.children = {}
        self.tail = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.tail = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    for c in cur.children.values():
                        if dfs(i+1,c): return True
                    return False
                else:
                    if word[i] not in cur.children:               
                        return False
               
                    cur = cur.children[word[i]]
            return cur.tail
        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)