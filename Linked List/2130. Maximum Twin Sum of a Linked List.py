# 2130. Maximum Twin Sum of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        temp = head
        while temp:
            n+=1
            temp=temp.next
        if n==2:
            return head.val+head.next.val
        cur = head
        i = 0
        while i<n//2:
            cur = cur.next
            i+=1
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        a = head
        b = prev
        maxSum = 0
        
        while b:
            maxSum = max(maxSum,a.val+b.val)
            a = a.next
            b = b.next
        return maxSum