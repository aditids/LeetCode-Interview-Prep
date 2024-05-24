# 138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        temp = head
        dummy = ListNode(0)
        cur = dummy
        while temp:
            node = ListNode(temp.val)
            next = temp.next
            temp.next = node
            node.next = next
            temp = next

        temp = head
        while temp:
            if temp.random:           
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp = temp.next.next

        temp = head
        while temp:
            cur.next = temp.next
            cur = cur.next
            temp.next = cur.next
            temp = temp.next

        return dummy.next