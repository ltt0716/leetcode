# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()

        cur=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                nxt1=list1.next

                cur.next=list1
                cur=list1

                list1=nxt1
            else:
                nxt2=list2.next
                cur.next=list2
                cur=list2

                list2=nxt2
                
        if not list2:
            cur.next=list2
        else:
            cur.next=list1
        
        return dummy.next


