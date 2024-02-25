# 199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        res = []
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                k = q.pop(0)
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
                if i==n-1:
                    res.append(k.val)
        return res