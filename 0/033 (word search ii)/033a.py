# https://leetcode.com/problems/word-search-ii/description/


class TrieNode:
    def __init__(self, ch) -> None:
        self.children = {}
        self.is_end = False
        self.ch = ch
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]

        node.is_end = True
        node.word = word
    

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        self.res = []

        trie = self.add_words(words)
        root = trie.root

        for ri, row in enumerate(board):
            for ci, ch in enumerate(row):
                if ch in root.children:
                    child = root.children[ch]
                    self.explore(child, ri, ci, board, set())

        return self.res
    

    def explore(self, child: TrieNode, ri, ci, board, visited):
        rows, cols =  len(board), len(board[0])
        if ri < 0 or ri == rows or ci < 0 or ci == cols or (ri, ci) in visited:
            return
        
        if board[ri][ci] != child.ch:
            return
        
        visited.add((ri, ci))

        if child.is_end:
            self.res.append(child.word)
            child.word = None
            child.is_end = False

        
        neighbours = (
            (ri - 1, ci),
            (ri + 1, ci),
            (ri, ci - 1),
            (ri, ci + 1),
        )

        for nei in neighbours:
            r, c = nei
            if r >= 0 and r < rows and c >= 0 and c < cols and board[r][c] in child.children:
                self.explore(
                    child.children[board[r][c]],
                    r,
                    c,
                    board,
                    visited
                )

        visited.remove((ri, ci))


    def add_words(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)

        return trie
    


arr = [
    [
        [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ],
        ["oath","pea","eat","rain"]
    ],
    # [[["a"]], ["a"]],
    # [
    #     [
    #         ["o","a","b","n"],
    #         ["o","t","a","e"],
    #         ["a","h","k","r"],
    #         ["a","f","l","v"]
    #     ],
    #     ["oa","oaa"],
    # ],
    [
        [
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
        ],
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    ],
    # [
    #     [
    #         ["o","a","a","n"],
    #         ["e","t","a","e"],
    #         ["i","h","k","r"],
    #         ["i","f","l","v"]
    #     ],
    #     ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"],
    # ],
]


board, words = arr[-1]
sol = Solution()
res = sol.findWords(board, words)

print(res)