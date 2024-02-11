# 76. Minimum Window Substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if m<n: return ""

        tCount = Counter(t)
        sCount = {}
        minCount = float("inf")
        minWindow = [-1,-1]
        l, a = 0, 0
        b = len(tCount)

        for r in range(m):
            temp = s[r]
            sCount[temp] = 1+sCount.get(temp,0)
            if temp in tCount and tCount[temp]==sCount[temp]:
                a+=1
            while a==b:
                if r-l+1<minCount:
                    minCount = r-l+1
                    minWindow = [l,r]
                sCount[s[l]]-=1
                if s[l] in tCount and sCount[s[l]]<tCount[s[l]]:
                    a-=1
                l+=1
            
        i,j = minWindow
        return s[i:j+1] if minCount<float("inf") else ""