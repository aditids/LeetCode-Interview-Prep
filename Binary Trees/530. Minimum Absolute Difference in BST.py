# 530. Minimum Absolute Difference in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mink = inf
        def dfs(root,a,b):
            if root:
                x = root.val
                self.mink = min(self.mink, x-a, b-x)
                dfs(root.left,a,x)
                dfs(root.right,x,b)
        dfs(root,-inf,inf) 
        return self.mink     