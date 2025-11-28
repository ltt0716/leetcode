# class ListNode:
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)

        pre=cur=dummy

        for _ in range(left):
            pre=cur
            cur=cur.next

        init=cur
        pre0=None
        for _ in range(right-left+1):
            next=cur.next
            cur.next=pre0
            pre0=cur
            cur=next

        pre.next=pre0
        init.next=cur

        return dummy.next










