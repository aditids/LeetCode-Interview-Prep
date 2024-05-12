# 1318. Minimum Flips to Make a OR b Equal to c

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            if c&1:
                if not a&1 and not b&1:
                    flips+=1
            else:
                flips+= (a&1) + (b&1)
            a>>=1
            b>>=1
            c>>=1
        return flips