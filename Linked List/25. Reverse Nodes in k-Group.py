# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head
        count = 0
        temp = head
        while temp:
            count+=1
            temp = temp.next
        count = count//k
        cur = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while count:
            count-=1           
            cur = prev.next
            next = cur.next
            for i in range(k-1):
                cur.next = next.next
                next.next = prev.next
                prev.next = next
                next = cur.next
            prev = cur
        return dummy.next