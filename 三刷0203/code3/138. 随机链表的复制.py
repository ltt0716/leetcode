"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        val_id={}
        id_val={}

        cur=head

        i=0
        while cur:
           val_id[cur]=i

           node=Node(cur.val)
           id_val[i]=node
           cur=cur.next
           i+=1

        val_id[None]=i
        id_val[i]=None


        h=id_val[0]
        cur=head
        i=0
        while cur:
            nxt=id_val[i+1]
            random=id_val[val_id[cur.random]]
            h.next=nxt
            h.random=random

            h=nxt
            cur=cur.next
            i+=1

        return id_val[0]
