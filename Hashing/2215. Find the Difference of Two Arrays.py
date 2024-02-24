# 2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        d1 = list(n1-n2)
        d2 = list(n2-n1)
        return [d1,d2]
        
        
        # result = []
        # distinct = set()
        # for i in nums1:
        #     if i not in nums2:
        #         distinct.add(i)

        # result.append(distinct)

        # distinct = set()
        # for i in nums2:
        #     if i not in nums1:
        #         distinct.add(i)

        # result.append(distinct)
        # return result   