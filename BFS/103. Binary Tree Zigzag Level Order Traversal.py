
# 103. Binary Tree Zigzag Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        rev = 0
        while q:
            cur = []
            n = len(q)
            #print(q)
            for i in range(n):
                k = q.pop(0)
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
                cur.append(k.val)
            #print(cur)
            if rev%2 == 0:
                res.append(cur)
            else:
                res.append(reversed(cur))
            rev+=1
        return res