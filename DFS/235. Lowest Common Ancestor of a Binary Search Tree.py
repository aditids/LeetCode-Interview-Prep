#235. Lowest Common Ancestor of a Binary Search Tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return
        
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        return root
        
# Time and Space Complexity - O(n)