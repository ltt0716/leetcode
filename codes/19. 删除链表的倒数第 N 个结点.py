# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy=ListNode(-1)
        dummy.next=head
        l=r=dummy

        num=n

        while num>0:
            next=r.next
            r=next
            num-=1

        while r.next:
            next1,next2=l.next,r.next
            l,r=next1,next2

        l.next=l.next.next
        return dummy.next




