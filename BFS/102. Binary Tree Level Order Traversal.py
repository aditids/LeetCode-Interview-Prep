# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = [root]
        while queue:
            n = len(queue)
            lvl = []
            for i in range(n):
                k = queue.pop(0)
                lvl.append(k.val)
                if k.left:
                    queue.append(k.left)
                if k.right:
                    queue.append(k.right)
            result.append(lvl)
        return result