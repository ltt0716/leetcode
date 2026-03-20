class Node:
    def __init__(self,val,end=False,nxt=None):
        self.end=end
        self.val=val
        self.nxt={}

class Trie:

    def __init__(self):
        self.nxt={}

    def insert(self, word: str) -> None:
        n=len(word)
        nxt=self.nxt
        for index,val in enumerate(word):
            if val not in nxt.keys():
                if index==n-1:
                    node=Node(val,True)
                    nxt[val]=node
                else:
                    node=Node(val)
                    nxt[val]=node
                    nxt=node.nxt
            else:
                if index==n-1:
                    nxt[val].end=True
                nxt=nxt[val].nxt

    def search(self, word: str) -> bool:
        nxt=self.nxt
        n=len(word)
        for index,val in enumerate(word):
            if val not in nxt.keys():
                return False
            else:
                if index==n-1:
                    return nxt[val].end
            nxt=nxt[val].nxt

    def startsWith(self, prefix: str) -> bool:
        nxt=self.nxt
        n=len(prefix)
        for index,val in enumerate(prefix):
            if val not in nxt.keys():
                return False
            nxt=nxt[val].nxt
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)