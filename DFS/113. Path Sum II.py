# 113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        path = []

        def dfs(root, cSum):
            if not root: return
            path.append(root.val)
            cSum+=root.val
            if not root.left and not root.right and cSum == targetSum:
                paths.append(path.copy())
            else:
                dfs(root.left, cSum) 
                dfs(root.right, cSum)
            path.pop()

        dfs(root,0)
        return paths

# Time and Space Complexity - O(n)