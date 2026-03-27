class Node:
    def __init__(self,val=0,end=False):
        self.val=val
        self.end=end
        self.cnt={}
class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        root=self.root
        n=len(word)

        for i in range(n):
            c=word[i]
            if c in root.cnt.keys():
                root=root.cnt[c]
            else:
                node=Node(c)
                root.cnt[c]=node
                root=node
        root.end=True

    def search(self, word: str) -> bool:
        root=self.root

        for c in word:
            if c not in root.cnt.keys():
                return False
            else:
                root=root.cnt[c]
        
        return root.end

    def startsWith(self, prefix: str) -> bool:
        root=self.root

        for c in prefix:
            if c not in root.cnt.keys():
                return False
            else:
                root=root.cnt[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)