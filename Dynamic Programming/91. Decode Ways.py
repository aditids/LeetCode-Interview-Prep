# 91. Decode Ways
class Solution:
    def numDecodings(self, s: str) -> int:
        b, c = 1, 1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                a = 0
            else:
                a = b
            if(i+1<len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456')):
                a+=c
            c = b
            b = a
        return a
        # Time complexity - O(n)
        # Space complexity - O(1)