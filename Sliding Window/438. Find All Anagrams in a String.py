# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p): return []
        l = 0
        r = 0
        pcount = Counter(p)
        result = []
        i = 0
        tcount = {}
        while r<len(s):           
            while r<len(s) and i<len(p):
                tcount[s[r]] = tcount.get(s[r],0)+1
                i+=1
                r+=1
            if tcount==pcount:
                result.append(l)               
            
            if tcount[s[l]]>1:
                tcount[s[l]]-=1
            else:
                del tcount[s[l]]
            i-=1
            l+=1
        return result  