# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxCount = 0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            if (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            maxCount = max(maxCount, r-l+1)
        return maxCount
        # Time complexity O(26*n) -> O(n)