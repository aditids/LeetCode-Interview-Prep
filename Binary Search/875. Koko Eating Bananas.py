# 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): return max(piles)
        l = 1
        r = max(piles)
        mink = float('inf')
        while l<=r:
            k = (l+r)//2
            hrs = 0
            for i in piles:
                hrs+=math.ceil(i/k)
            if hrs>h:
                l = k+1
            else:
                r = k-1
                mink = min(mink, k)
        return mink
        