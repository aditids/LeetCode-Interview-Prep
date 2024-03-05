# 1161. Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        cur_level = 1
        max_sum = -inf
        max_level = 0
        while q:
            cur_sum = 0
            for i in range(len(q)):
                k=q.pop(0)
                cur_sum+=k.val
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
            if max_sum<cur_sum:
                max_sum = cur_sum
                max_level = cur_level
            cur_level+=1
        return max_level