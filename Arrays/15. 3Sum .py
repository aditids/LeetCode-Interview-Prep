# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if a>0: return result
            if i>0 and a==nums[i-1]:
                continue
            b, c = i+1, len(nums)-1
         
            while b<c:                
                tsum = nums[b]+a+nums[c]
                if tsum<0:
                    b+=1
                elif tsum>0:
                    c-=1
                else:
                    result.append([nums[b],a,nums[c]])
                    b+=1
                    while b<c and nums[b]==nums[b-1]:                       
                        b+=1               
        return result
         # Time complexity  - O(n^2)
        # Space Complexity - O(1)