import math
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        dummy=ListNode(val=-1)
        cur=dummy

        heads=[]
        unique_id=0
        for head in lists:
            if head!=None:
                heapq.heappush(heads,(head.val,unique_id,head))
                unique_id+=1

        while len(heads):
            val,_,node=heapq.heappop(heads)
            cur.next=node
            cur=node
            if node.next:
                heapq.heappush(heads,(node.next.val,unique_id,node.next))
                unique_id+=1


        return dummy.next




