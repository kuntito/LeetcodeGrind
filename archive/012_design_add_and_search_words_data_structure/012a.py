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
        node_list = [self.root]
        for ch in word:
            temp = []
            for node in node_list:
                if ch in node.children:
                    temp.append(node.children[ch])
                elif ch == '.':
                    for child_node in node.children.values():
                        temp.append(child_node)

            if not temp: return False
            node_list = temp

        return any(node.is_word_end for node in node_list)


class TrieNode:
    def __init__(self, is_word_end = False) -> None:
        self.is_word_end = is_word_end
        self.children = {}


sol = WordDictionary()
sol.addWord("but")
sol.addWord("ba")
sol.addWord("dad")
sol.addWord("mad")
print(sol.search("."))
