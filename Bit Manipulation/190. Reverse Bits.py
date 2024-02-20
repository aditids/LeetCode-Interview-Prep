# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        i = 0
        while n:
            bit = n&1
            rev = rev | bit<<(31-i) 
            i+=1
            n >>= 1
        return rev
    