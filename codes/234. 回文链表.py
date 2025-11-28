from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def ptr_half(head: Optional[ListNode]) -> Optional[ListNode]:
            fast, slow = head, head

            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

            return slow

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            pre=None
            while head:
                tem=head.next
                head.next=pre
                pre=head
                head=tem
            return pre

        half=ptr_half(head)
        last=reverse(half.next)


        while head and last and head!=last:
            if (head.val!=last.val):
                return False
            head=head.next
            last=last.next

        return True


