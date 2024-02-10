# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxc = max(candies)
        for i in candies:
            if i+extraCandies>=maxc:
                result.append(True)
            else:
                result.append(False)
        return result