# 572. Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot: return True
    if not root: return False
    if self.sameTree(root,subRoot):
        return True
    return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

def sameTree(self,a,b):
    if not a and not b:
        return True
    if a and b and a.val==b.val:
        return self.sameTree(a.left,b.left) and self.sameTree(a.right,b.right)
    return False