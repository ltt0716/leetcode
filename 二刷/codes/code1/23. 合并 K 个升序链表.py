# Definition for singly-linked list.
import math
from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pre=dummy=ListNode()
        li=[]
        id=0

        for node in lists:
            if node:
                heapq.heappush(li,(node.val,id,node))
                id+=1

        while li:
            _,_,node=heapq.heappop(li)
            pre.next=node
            pre=node
            if node.next:
                heapq.heappush(li,(node.next.val,id,node.next))
                id+=1
        return dummy.next
