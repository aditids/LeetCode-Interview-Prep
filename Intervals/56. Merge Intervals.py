# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = [intervals[0]]
        for s,e in intervals[1:]:
            topEnd=result[-1][1]
            if s<=topEnd:
                result[-1][1]=max(topEnd,e)
            else:
                result.append([s,e])
        return result
    # Time Complexity - O(nlogn)