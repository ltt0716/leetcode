# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(-1)
        h=head
        dot=0
        while l1 and l2:
            node=ListNode((l1.val+l2.val+dot)%10)
            dot=(l1.val+l2.val+dot)//10

            h.next=node
            h=node

            l1=l1.next
            l2=l2.next
        if l1:
            while l1:
                node = ListNode((l1.val + dot) % 10)
                dot = (l1.val +dot) // 10

                h.next = node
                h = node

                l1 = l1.next
        else:
            while l2:
                node = ListNode((l2.val + dot) % 10)
                dot = (l2.val +dot) // 10

                h.next = node
                h = node

                l2 = l2.next

        if dot==1:
            node = ListNode(1)


            h.next = node
            h = node


        return head.next