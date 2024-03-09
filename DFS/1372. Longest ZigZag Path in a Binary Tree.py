# 1372. Longest ZigZag Path in a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def maxZigZag(node, l, r):
            if not node: return 0

            self.res = max(self.res, l, r)
            maxZigZag(node.left, r+1, 0)
            maxZigZag(node.right, 0, l+1)

            return self.res
        
        return maxZigZag(root,0,0)        