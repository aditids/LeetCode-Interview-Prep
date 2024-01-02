# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxd = 0

        while(l<r):
            maxd = max(maxd, (min(height[l],height[r])*(r-l)))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxd
        # Time Complexity - O(n)
        # Space Complexity - O(1)