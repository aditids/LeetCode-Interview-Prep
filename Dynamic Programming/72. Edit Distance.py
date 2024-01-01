# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        cache = [[float("inf")] * (w2+1) for i in range(w1+1)]
        for i in range(w2+1):
            cache[w1][i] = w2-i
        for i in range(w1+1):
            cache[i][w2] = w1-i
        for i in range(w1-1, -1, -1):
            for j in range(w2-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1+min(cache[i][j+1],cache[i+1][j],cache[i+1][j+1]) # insert/delete/replace
        return cache[0][0]
        # Time and Space complexity - O(n^2)