# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for i, num in enumerate(nums):
            if num in hmap and abs(i-hmap[num])<=k:
                        return True
                                       
            hmap[num] = i
        return False