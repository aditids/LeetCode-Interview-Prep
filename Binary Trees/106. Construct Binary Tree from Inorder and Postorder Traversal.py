# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexMap = {}

        def recursion(l, r):
            if l>r:
                return
            val = postorder.pop()
            root = TreeNode(val)

            k = indexMap[val]
            root.right = recursion(k+1, r)
            root.left = recursion(l, k-1)
            return root

        for i, val in enumerate(inorder):
            indexMap[val] = i

        return recursion(0, len(postorder)-1)