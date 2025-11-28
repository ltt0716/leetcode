class Node:
    def __init__(self,val=''):
        self.val=val
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root=Node()


    def insert(self, word: str) -> None:
        root=self.root
        n=len(word)
        for i in range(n):

            ch=word[i]

            flag=False

            if ch in root.children.keys():
                flag=True
                root=root.children[ch]
            
            if not flag:
                newnode=Node(val=ch)
                print(ch,newnode.val)
                root.children[ch]=newnode
                root=newnode
     
            if i==n-1:
                root.is_end=True


    def search(self, word: str) -> bool:
        root=self.root
        n=len(word)
        for i in range(n):
            ch=word[i]

            flag=False

            if ch in root.children.keys():
                flag=True
                root=root.children[ch]
            
            if not flag:
                return False
                
            if i==n-1:
                return root.is_end


    def startsWith(self, prefix: str) -> bool:
        root=self.root
        n=len(prefix)
        for i in range(n):
            ch=prefix[i]

            flag=False

            if ch in root.children.keys():
                flag=True
                root=root.children[ch]
            
            
            if not flag:
                return False
            
        return True

