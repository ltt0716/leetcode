# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        h1=headA
        h2=headB

        while True:
            if h1==h2:
                return h1
            
            h1=h1.next
            h2=h2.next

            if not(h1 or h2):
                return None
            else:
                if not h1:
                    h1=headB
                if not h2:
                    h2=headA
            

