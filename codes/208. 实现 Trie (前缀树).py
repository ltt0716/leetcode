class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False


class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for letter in word:
            if letter not in node.child:
                node.child[letter]=TrieNode()
            node=node.child[letter]
        node.end=True

    def search(self, word: str) -> bool:
        node=self.root
        for letter in word:
            if letter not in node.child:
                return False
            node=node.child[letter]
        return  node.end

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for letter in prefix:
            if letter not in node.child:
                return False
            node=node.child[letter]
        return  True
