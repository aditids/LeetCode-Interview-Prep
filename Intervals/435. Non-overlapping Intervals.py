# 435. Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        prev = intervals[0][1]
        for i,j in intervals[1:]:
            if i>=prev:
                prev = j
            else:
                count+=1
                prev=min(prev,j)
        return count
    # Time complexity - O(nlogn)