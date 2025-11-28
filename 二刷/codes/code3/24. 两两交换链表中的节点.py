# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def findhead_tail_next(head, k):
            cur = head

            while k > 1:
                k -= 1
                cur = cur.next

                if cur is None:
                    return head, None, None

            return head, cur, cur.next

        def reversehead_tail_next(head, k):

            pre = None
            cur = head
            while k:
                k -= 1
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

            return pre, head

        k = 2
        dummy = ListNode(next=head)
        pre = dummy
        cur = head
        while cur:
            curhead, curtail, curnext = findhead_tail_next(cur, k)

            if curtail is None:
                pre.next=curhead
                return dummy.next

            newhead, newtail = reversehead_tail_next(curhead, k)
            pre.next = newhead
            pre = newtail
            cur = curnext
        return dummy.next







