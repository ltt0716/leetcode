# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0

        cur = head

        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next=head)
        last_tail = dummy

        pre = None
        cur = head

        k = 2
        while n >= k:
            n -= k

            for _ in range(k):
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

            next = last_tail.next
            next.next = cur
            last_tail.next = pre
            last_tail = next
        return dummy.next

