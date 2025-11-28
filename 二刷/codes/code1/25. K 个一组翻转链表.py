# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur=head
        n=0
        while cur:
           n+=1
           cur=cur.next


        p=dummy=ListNode(next=head)
        cur=head

        while n>=k:
            n-=k
            p0=cur
            pre = None

            for _ in range(k):
                next=cur.next
                cur.next=pre
                pre=cur
                cur=next
            p0.next=cur
            p.next=pre
            p=p0

        return dummy.next


