# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:



        now=head

        last=None
        init = None

        while now:
            n=k
            l=now
            pre=None

            while n>0 and now:
                next=now.next
                now.next=pre
                pre=now
                now=next
                n-=1
            if n==0:
                if last:
                    last.next = pre
                if not last:
                    init = pre

                l.next = now
                last = l
            else:
                n1=None
                while n<k:
                    next=pre.next
                    pre.next=n1
                    n1=pre
                    pre=next
                    n+=1




        return init








