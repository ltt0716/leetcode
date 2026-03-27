# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        h1=head
        while h1:
            n+=1
            h1=h1.next
        
        dummy=ListNode(0,head)
        pre=dummy
        lasttail=dummy
        newhead=head
        while n>=k:
            n-=k
            m=k
            h1=newhead
            while m>0:
                nxt=h1.next
                h1.next=pre
                pre=h1
                h1=nxt
                m-=1
            lasttail.next=pre
            newhead.next=h1
            lasttail=newhead
            newhead=h1
        
        return dummy.next
                    