#448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for num in nums:
            i = abs(num) - 1           
            nums[i] = -abs(nums[i])

        result = [i + 1 for i, num in enumerate(nums) if num > 0]
        return result

# Time Complexity - O(n)   
# Space Complexity - O(1) 

# Alternate solution - 

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:        
#         temp = set(nums)
#         n = len(nums)
#         result = []
#         for i in range(1,n+1):
#             if i not in temp:
#                 result.append(i)

#         return result

# Time Complexity - O(n^2)   
# Space Complexity - O(n) 