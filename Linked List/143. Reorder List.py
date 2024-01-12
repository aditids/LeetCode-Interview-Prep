# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l2 = slow.next
        prev = None
        slow.next = None
        slow = head
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp

        l1, l2 = head, prev
        while l2:
            a, b = l1.next, l2.next
            l1.next = l2
            l2.next = a
            l1, l2 = a, b
        # Time complexity = O(n)
        # Space complexity - O(1)