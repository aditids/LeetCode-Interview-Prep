# 230. Kth Smallest Element in a BST

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        count = 0
        while curr or stack:
            while curr:               
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count+=1
            if count == k:
                return curr.val
            curr = curr.right
        return 0

# Time and Space Complexity - O(n)