"""
# Definition for a Node.

"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        mp={}

        cur=head

        while cur:
            node=Node(cur.val)
            mp[cur]=node
            cur=cur.next


        cur=head
        while cur:

            newnode=mp[cur]
            newnode.next=mp.get(cur.next)
            newnode.random=mp.get(cur.random)
            cur=cur.next
        return mp.get(head)
