# Definition for singly-linked list.
from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur=head
        index=0
        heap=[]
        while cur:
            next=cur.next
            cur.next=None
            heapq.heappush(heap,(cur.val,index,cur))
            index+=1
            cur=next

        dummy=ListNode()
        pre=dummy

        while heap:
            _,_,node=heapq.heappop(heap)

            pre.next=node
            pre=node
        return dummy.next

