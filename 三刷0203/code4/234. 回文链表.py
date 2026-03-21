# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        h1=head
        s1=""

        while h1:
            s1+=h1.val
            h1=h1.next
        
        h2=head
        s2=""
        pre=None
        while h2:
            nxt=h2.next
            h2.next=pre
            pre=h2
            h2=nxt
        