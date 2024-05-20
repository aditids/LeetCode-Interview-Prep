# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s)!=len(pattern):
            return False
        
        hmap = {}
        visit = set()
        for i in range(len(s)):
            if pattern[i] not in hmap:
                if s[i] in visit:
                    return False
                visit.add(s[i])
                hmap[pattern[i]] = s[i]

            elif hmap[pattern[i]]!=s[i]:
                return False
        return True