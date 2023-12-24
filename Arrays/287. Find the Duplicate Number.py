# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i in res:
                return i
            res.add(i)
        return 0

    # Time and Space Complexity - O(n)