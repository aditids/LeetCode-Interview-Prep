# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highestAltitude = 0
        altitude = 0
        for i in gain:
            altitude+=i
            highestAltitude = max(highestAltitude, altitude)
        return highestAltitude