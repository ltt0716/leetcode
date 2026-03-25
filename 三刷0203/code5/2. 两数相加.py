# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode()
        pre=dummy
        add=0
        while l1 or l2:
            cur=0
            if l1 :
                cur+=l1.val
                l1=l1.next
            if l2:
                cur+=l2.val
                l2=l2.next
            
            cur+=add
            add=cur//10
            cur=cur%10

            node=ListNode(cur)
            pre.next=node
            pre=node

        if add:
            pre.next=ListNode(add)
            
        return dummy.next