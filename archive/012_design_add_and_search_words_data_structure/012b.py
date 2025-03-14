# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word_end = True
            

    def search(self, word: str) -> bool:
        root = self.root

        return self.dfs(0, root, word)
        

    def dfs(self, start_idx, root, word):
        for idx in range(start_idx, len(word)):
            ch = word[idx]
            if ch in root.children:
                root = root.children[ch]
            elif ch == '.':
                for child_node in root.children.values():
                    res = self.dfs(
                        idx + 1,
                        child_node,
                        word
                    )
                    if res:
                        return True
                return False
            else:
                return False

        return root.is_word_end



class TrieNode:
    def __init__(self, is_word_end = False) -> None:
        self.is_word_end = is_word_end
        self.children = {}



sol = WordDictionary()
sol.addWord("but")
sol.addWord("b")
sol.addWord("dad")
sol.addWord("mad")
print(sol.search(".ad"))