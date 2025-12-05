# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        slow=head

        fast=head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        cur=slow
        pre=None

        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        
        while pre :
            if head.val!=pre.val:
                return False
            
            head=head.next
            pre=pre.next

        
        return True
