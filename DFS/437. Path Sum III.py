# 437. Path Sum III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0

        def dfs(root, cSum):
            count = 0
            if not root: return count
            if cSum == root.val:
                count+=1

            print(cSum-root.val)
            count+=dfs(root.left,cSum-root.val)
            count+=dfs(root.right,cSum-root.val)
            return count

        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

# Time Complexity - O(n^2), Space complexity - O(n)        
    

    # Alternate solution - 
    
        # def dfs(node, pathSum, count):
            
        #     if not node:return 0

        #     curSum = pathSum + node.val
        #     tempSum = 0

        #     if curSum == targetSum:
        #         tempSum += 1

        #     tempSum += count[curSum-targetSum]
        #     count[curSum] += 1
        #     tempSum += dfs(node.left, curSum, count) + dfs(node.right, curSum, count)
        #     count[curSum] -= 1

        #     return tempSum
            
        # return dfs(root, 0, defaultdict(int))