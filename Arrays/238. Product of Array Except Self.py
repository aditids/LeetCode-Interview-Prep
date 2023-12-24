# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        flag = 0
        result = []
        for i in nums:
            if i!=0: total*=i
            else: flag += 1
        
        for i in nums:
            if i !=0 and flag >= 1: 
                result.append(0)
            elif i!=0 and flag!=1:
                result.append(total//i)
            elif i==0 and flag > 1:
                result.append(0)
            else:
                result.append(total)
        return result

        # Time and Space Complexity - O(n)      