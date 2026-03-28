# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        fast=dummy
        pre=dummy
        slow=dummy.next

        for _ in range(n):
            fast=fast.next

        while fast.next:
            fast=fast.next
            pre=slow
            slow=slow.next
        
        pre.next=slow.next

        return dummy.next
        