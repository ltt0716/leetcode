# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head :
            return None
        
        slow,fast=head,head

        while fast:
            slow=slow.next
            next=fast.next
            if not next:
                return None
            fast=next.next

            if fast==slow:
                while head!=slow:
                    head=head.next
                    slow=slow.next
                return head
        
        return None
        