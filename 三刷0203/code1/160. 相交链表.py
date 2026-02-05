# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1,h2=headA,headB

        while h1 and h2:
            if h1==h2:
                return True
            nxt1,nxt2=h1.next,h2.next

            if nxt1 is None and nxt2 is None:
                return None

            if  nxt1 is None:
                h1=headB
            else:
                h1=nxt1

            if nxt2 is None :
                h2=headA
            else:
                h2=nxt2

        return None