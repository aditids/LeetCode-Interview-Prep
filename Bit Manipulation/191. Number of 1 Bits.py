# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count+=1
        return count

        # count = 0
        # while n:
        #     count+=n%2
        #     n = n >> 1
        # return count

        # Time complexity - O(32) -> O(1)