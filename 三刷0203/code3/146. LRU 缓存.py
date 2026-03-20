class Node:
    def __init__(self,key=-1,val=-1,pre=None,nxt=None):
        self.val=val
        self.key=key
        self.pre=pre
        self.nxt=nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.maxsize=capacity
        self.cursize=0
        self.dummy=Node()
        self.dict={}
        self.last=None



    def get(self, key: int) -> int:
        if key not in self.dict.keys():
            return -1        
        else:
            self.move(key)
            return self.dict[key].val

    def put(self, key: int, value: int) -> None:
        
        if key not in self.dict.keys():
            self.add(key,value)
        else:
            self.dict[key].val=value
            self.move(key)
        return None
    
    def add(self, key: int, value: int):
        if self.cursize>=self.maxsize:
            self.dellast()

        node=Node(key,value)
        self.dict[key]=node
        
              
        if self.cursize==0:
            self.dummy.nxt=node
            node.pre=self.dummy
        else:
            nxt=self.dummy.nxt
            nxt.pre=node
            node.nxt=nxt
            node.pre=self.dummy
            self.dummy.nxt=node


        self.cursize+=1

        if self.cursize==1:
            self.last=node
        


    def dellast(self):
        last=self.last

        del self.dict[last.key]

        self.cursize-=1
        
        if self.cursize!=0:
            last.pre.nxt=None
            self.last=last.pre
        else:
            self.last=None
        
    def move(self,key):
        node=self.dict[key]
        if node.nxt==None:
            if self.cursize!=1:
                pre=node.pre
                self.last=pre
                pre.nxt=None

                fomer=self.dummy.nxt

                node.nxt=fomer
                fomer.pre=node
                self.dummy.nxt=node
                node.pre=self.dummy
        
        else:
            node.pre.nxt=node.nxt
            node.nxt.pre=node.pre

            fomer=self.dummy.nxt

            node.nxt=fomer
            fomer.pre=node
            self.dummy.nxt=node
            node.pre=self.dummy

    

