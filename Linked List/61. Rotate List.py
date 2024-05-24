# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        temp = head
        count = 1
        while temp.next:
            temp = temp.next
            count+=1
        
        k = k%count
        temp.next = head       
        prev = head
        for i in range(count-k-1):
            prev = prev.next

        res = prev.next
        prev.next = None
        return res