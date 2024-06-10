# 148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        next = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(next)
        return self.dnc(left,right)
        
    def dnc(self, l, r):
        if not l:
            return r
        if not r: 
            return l
        dummy = ListNode()
        temp = dummy
        while l and r:
            if l.val<r.val:
                temp.next = ListNode(l.val)
                l = l.next
            else:
                temp.next = ListNode(r.val)
                r = r.next
            temp = temp.next
        if l:
            temp.next = l
        if r:
            temp.next = r
        return dummy.next