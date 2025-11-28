# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1,node2=headA,headB

        while 1:
            if node1==node2:
                return node1
            else:
                node1,node2=node1.next,node2.next

            if node1==None and node2==None:
                return None
            elif node1==None:
                node1=headB
            elif node2==None:
                node2=headA
