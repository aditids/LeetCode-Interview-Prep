# 173. Binary Search Tree Iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorder(root)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.stack.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        k = self.stack.pop(0)
        return k

    def hasNext(self) -> bool:
        if len(self.stack)>0:
            return True
        return False  


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

