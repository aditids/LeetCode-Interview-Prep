# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        def postorder(root):
            if not root: return
            postorder(root.left)
            postorder(root.right)
            self.result.append(root.val)
        #postorder(root)

        if not root: return 
        stack = []
        r = []
        while True:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.right and stack and stack[-1]==root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                r.append(root.val)
                root = None

            if len(stack)==0: break

        return r