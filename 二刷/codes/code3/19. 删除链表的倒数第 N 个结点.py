# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m=0
        cur=head

        while cur:
            m+=1
            cur=cur.next

        dummy=ListNode(next=head)

        pre=dummy
        cur=head

        k=m-n+1

        while k>1:
            pre=cur
            cur=cur.next
            k-=1

        pre.next=cur.next
        return dummy.next
