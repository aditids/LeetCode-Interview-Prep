# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s)==Counter(t)

        if len(s)!= len(t):
            return False
        scount, tcount= {}, {}
        for i in range (len(s)):
            scount[s[i]] = 1 + scount.get(s[i],0)
            tcount[t[i]] = 1 + tcount.get(t[i],0)

        for i in scount:
            if scount[i] != tcount.get(i,0):
                return False
        return True