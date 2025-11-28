
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head

        while cur:
            node=Node(x=cur.val,next=cur.next)
            cur.next=node

            cur=node.next

        index=0

        dummy=Node(x=-1,next=head)
        pre=dummy
        cur=dummy.next

        while cur:
            if index%2==0:
                pre.next=cur.next
            else:
                cur.random=pre.random.next

            pre = cur
            cur = cur.next
            index+=1

        return dummy.next









