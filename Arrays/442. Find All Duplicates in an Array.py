# 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        duplicates = []
        for i in nums:
            if i in res:
                duplicates.append(i)
            res.add(i)
        return duplicates

    # Time and Space complexity - O(n)      