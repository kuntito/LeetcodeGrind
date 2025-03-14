# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = Node()
            temp = temp.children[ch]
        
        temp.is_end = True

    def get_prefix(self, prefix: Node):
        temp = self.root
        for ch in prefix:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]

        return temp

    def search(self, word: str) -> bool:
        res = self.get_prefix(word)
        return res.is_end if isinstance(res, Node) else False

    def startsWith(self, prefix: str) -> bool:
        res = self.get_prefix(prefix)
        return isinstance(res, Node)
