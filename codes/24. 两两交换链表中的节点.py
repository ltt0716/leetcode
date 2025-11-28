from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(-1)
        dummy.next=head

        if dummy.next==None or dummy.next.next==None :
            return dummy.next

        l=dummy
        m=l.next
        r=m.next

        while l and m and r:
            l.next=r
            m.next=r.next
            r.next=m

            m,r=r,m
            if r.next==None or r.next.next==None:
                break
            l,m,r=r,r.next,r.next.next

        return dummy.next
