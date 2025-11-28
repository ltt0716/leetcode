# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=None

        l1=l11=ListNode()
        l2=l22=ListNode()

        for i in range(len(list1)):
            temp=ListNode(list1[i])

            if i==0:
                l1=l11=temp
            else:
                l1.next=temp
        for i in range(len(list2)):
            temp = ListNode(list2[i])

            if i == 0:
                l2 = l22 = temp
            else:
                l2.next = temp



        if l11.val>l22.val:
            head=l22
            l22=l22.next
        else:
            head=l11
            l11=l11.next
        head1=head
        while l11 and l22:
            if l11.val > l22.val:
                head.next = l22
                l22 = l22.next
            else:
                head.next = l11
                l11 = l11.next
            head=head.next

        return head1
