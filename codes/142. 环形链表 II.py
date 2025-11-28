# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        if head.next.next==None:
            return None

        slow,fast = head,head.next.next

        while fast:
            if slow==fast:
                return slow

            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

        return None
