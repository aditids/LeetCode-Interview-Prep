# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return len(temp)!=len(nums)  

# Time and Space Complexity - O(n)     