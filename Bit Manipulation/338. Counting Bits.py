# 338. Counting Bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        signed = 1
        for i in range(1,n+1):
            if i&(i-1) == 0:
                signed = i
            result.append(1+result[i-signed])
        return result
        
    # Time Complexity - O(n)

        # dp = [0]
        # offset = 1
        # for i in range(1,n+1):
        #     if offset*2==i:
        #         offset = i
        #     dp.append(1+dp[i-offset])
        # return dp


        # alternate solution
        # dp = [0]
        # for i in range(1,n+1):
        #     dp.append(dp[i//2]+(i&1))
        # return dp