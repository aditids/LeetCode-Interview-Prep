# 86. Partition List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        prev = ListNode(0)
        ptemp = prev
        next = ListNode(0)
        ntemp = next
        temp = head
        while temp:
            if temp.val<x:
                ptemp.next = temp
                ptemp = ptemp.next
            else:
                ntemp.next = temp
                ntemp = ntemp.next
            temp = temp.next
        
        ntemp.next = None
        ptemp.next = next.next
        return prev.next