# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node,good):
            if not node: return
            if node.val>=good: 
                good = node.val
                self.count+=1
            dfs(node.left,good)
            dfs(node.right,good)
        dfs(root,float('-inf'))
        return self.count