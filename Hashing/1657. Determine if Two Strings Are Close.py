# 1657. Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2): 
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        if sorted(c1.values())!=sorted(c2.values()):
            return False
        if set(c1.keys()) != set(c2.keys()):
            return False
        return True