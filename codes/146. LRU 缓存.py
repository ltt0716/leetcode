class ListNode:
    def __init__(self,key="-1",val=0,pre=None,next=None):
        self.key=key
        self.val=val
        self.pre=pre
        self.next=next


class LRUCache:

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.size=0
        self.mp = {}
        self.dummy=ListNode(val=-1)
        self.dummy.pre=self.dummy
        self.dummy.next=self.dummy

    def get(self, key: int) -> int:
        if key  in self.mp.keys():
            node=self.mp[key]
            self._put_front(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp.keys():
            node=self.mp[key]
            node.val=value
            self._put_front(node)
        else:
            if self.size<self.maxsize:
                self._add(key=key,val=value)
            else:
                self._del(self.dummy.pre)
                self._add(key=key, val=value)

    def _put_front(self,node):
        key=node.key
        self._del(node)
        node.next=self.dummy.next
        node.pre=self.dummy
        node.pre.next.pre=node
        node.pre.next=node
        self.mp[key]=node
        self.size+=1


    def _del(self,node):
        key=node.key
        node.pre.next=node.next
        node.next.pre=node.pre
        del self.mp[key]
        self.size-=1

    def _find(self,key):
        # 保证存在
        cur=self.dummy.next

        while cur :
            if cur.key==key:
                return cur
            else:
                cur=cur.next

        return cur

    def _add(self,key,val):
        node=ListNode(key=key,val=val)
        node.pre=self.dummy
        node.next=self.dummy.next
        node.pre.next.pre=node
        node.pre.next=node
        self.size+=1
        self.mp[key]=node





