class Node:
    def __init__(self,key=0,val=0):
        self.val=val
        self.key=key
        self.next=None
        self.pre=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dir={}
        self.size=0
        self.dummy_head=Node()
        self.dummy_tail=Node()
        self.dummy_head.next=self.dummy_tail
        self.dummy_tail.pre=self.dummy_head

    def get(self, key: int) -> int:
        if key in self.dir.keys():
            val,node=self.dir[key]
            self.movehead(node)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dir.keys():
            
            _,node=self.dir[key]
            node.val=value
            self.movehead(node)

    
    def addnode(self,key,val):
        node=Node(key,val)
        next=self.dummy_head.next

        self.dummy_head.next=node
        node.next=next
        next.pre=node
        node.pre=self.dummy_head
        self.size+=1
        self.dir[key]=(val,node)
        if self.size>self.capacity:
            self.removetail()

    def movetohead(self,cur):
        pre=cur.pre
        next=cur.next
        pre.next=next
        next.pre=pre

        headnext=self.dummy_head.next
        self.dummy_head.next=cur
        cur.pre=self.dummy_head
        cur.next=headnext
        headnext.pre=cur

    
    def removetail(self):
        self.dir[self.dummy_tail.pre.key]
        pre=self.dummy_tail.pre.pre
        pre.next=self.dummy_tail
        self.dummy_tail.pre=pre
        self.size-=1
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)