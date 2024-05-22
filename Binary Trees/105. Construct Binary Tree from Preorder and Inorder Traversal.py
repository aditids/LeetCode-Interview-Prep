# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {}
        self.k = 0
        def recursion(left, right):
            if left>right:
                return
            val = preorder[self.k]
            root = TreeNode(val)
            self.k+=1
            root.left = recursion(left, indexMap[val]-1)
            root.right = recursion(indexMap[val]+1, right)
            return root

        for i, val in enumerate(inorder):
            indexMap[val] = i
        return recursion(0,len(preorder)-1)
    
    # Time complexity - O(N)