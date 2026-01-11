# https://leetcode.com/problems/implement-trie-ii-prefix-tree/description/

# we want to implement a Trie
# Trie's store words in a tree structure

# every letter of a word is a node
# each letter serves as the parent node of the next

# each node has potentially 26 children
# for instance "ant" and "act"
# both have the same parent node ("a")
# but ("a") has two children ("n") and ("c")

# the root node would be the starting point for all words

# in this Trie, a word can be inserted multiple times
# i think the way to address this is to have a count associated with each node
# this way if i insert "act" twice

# the nodes ("a"), ("c") and ("t") would have a count of 2
# and the wordEnd would be at ("t")

# what would each node look like
# i need
# node character
# node count
# hashmap for it's children
# a boolean to indicate the last char in the word
class TrieNode:
    def __init__(self, ch) -> None:
        self.ch = ch
        self.count = 0
        
        # each element is `ch => TrieNode`
        self.children = {}
        self.isEnd = False
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.ch})'


# TODO don't work, trie again
# TODO might be the erase function
class Trie:
    def __init__(self):
        self.root = TrieNode("root")

    def insert(self, word: str) -> None:
        currNode = self.root
        # to insert word, you'd go through every character
        # creating it's node or grabbing if it already exists
        # increase the count
        
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TrieNode(ch)
            
            newNode = currNode.children[ch]
            newNode.count += 1
            
            currNode = newNode
            
        currNode.isEnd = True

    def countWordsEqualTo(self, word: str) -> int:
        pass
        currNode = self.root
        
        minCount = float("inf")
        for ch in word:
            if ch not in currNode.children:
                return 0
            currNode = currNode.children[ch]
            minCount = min(currNode.count, minCount)
            
        return minCount if currNode.isEnd else 0
            

    def countWordsStartingWith(self, prefix: str) -> int:
        currNode = self.root
        
        minCount = float("inf")
        for ch in prefix:
            if ch not in currNode.children:
                return 0
            currNode = currNode.children[ch]
            minCount = min(currNode.count, minCount)
            
        return minCount

    def erase(self, word: str) -> None:
        currNode = self.root
        
        for ch in word:
            currNode = currNode.children[ch]
            currNode.count -= 1
    
    
sol = Trie()
sol.insert("abc")
sol.insert("abc")
res = sol.countWordsStartingWith("ab")
print(res)

sol.erase("abc")
res = sol.countWordsStartingWith("ab")
print(res)