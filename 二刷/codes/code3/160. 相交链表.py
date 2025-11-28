# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1,h2=headA,headB

        while h1 and h2:
            if h1==h2:
                return h1
            if not h1.next and not h2.next:
                return None
            if h1.next:
                h1=h1.next
            else:
                h1=headB
            if h2.next:
                h2=h2.next
            else:
                h2=headA


