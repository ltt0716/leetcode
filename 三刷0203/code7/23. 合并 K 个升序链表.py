# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        dummy=ListNode()
        cur=dummy
        while lists.count(None)!=n:
            min_val=math.inf
            index=0
            for i in range(n):
                if lists[i] :
                    if min_val>lists[i].val:

                        min_val=lists[i].val
                        index=i
            cur.next=lists[index]
            nxt=lists[index].next
            cur=lists[index]
            lists[index]=nxt
        
        return dummy.next
            