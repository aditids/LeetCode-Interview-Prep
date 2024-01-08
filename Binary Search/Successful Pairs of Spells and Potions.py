# Successful Pairs of Spells and Potions
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        
        for i in range(len(spells)):
            l = 0
            r = len(potions)-1
            k = len(potions)
            while l<=r:
                m = (l+r)//2
                if potions[m]*spells[i]<success:
                    l=m+1
                else:
                    r = m-1
                    k = m
            pairs.append(len(potions)-k)
        return pairs
