# 567. Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c1 = Counter(s1)
        k = len(s1)
        l = 0
        c2 = Counter(s2[0:k])
        for i in range(k,len(s2)):
            if c1 == c2:
                return True
            c2[s2[l]]-=1
            l+=1
            c2[s2[i]] = c2.get(s2[i],0)+1
        return c1 == c2