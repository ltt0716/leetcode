# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # 返回链表长度
    def getlength(self,head):

        ans=0
        while head:
            head=head.next
            ans+=1

        return ans

    # 返回划分后的链表
    def getspiltlist(self,head,size):
        cur=head

        for _ in range(size-1):
            if cur==None:
                break
            cur=cur.next

        if cur==None or cur.next==None:
            return None

        nxt=cur.next
        cur.next=None

        return nxt

    def merge(self,head1,head2):
        dummy=ListNode(-1)

        cur=dummy
        while head1 and head2:
            if head1.val<head2.val:
                cur.next=head1
                head1=head1.next
            else:
                cur.next=head2
                head2=head2.next
            cur=cur.next


        if head1:
            cur.next=head1
        if head2:
            cur.next=head2

        pre=None
        while cur:
            pre=cur
            cur=cur.next

        return dummy.next,pre


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1,next=head)
        length=self.getlength(head)
        size=1


        while size<length:
            new_list_tail=dummy
            cur=dummy.next

            while cur:
                head1=cur
                head2=self.getspiltlist(head1,size)
                next_head=self.getspiltlist(head2,size)

                head,tail=self.merge(head1,head2)
                new_list_tail.next=head
                new_list_tail=tail

                cur=next_head
            size *= 2




        return dummy.next





