# https://leetcode.com/problems/word-search-ii/description/

from typing import List

# i'm given a 2d grid of strings, `board`.
# each string is simply a character from the english alphabet.

# lowercase.

# i'm also given a list of strings, `words`
# i want to find out what strings in `words` appear on the board.

# for instance:
# board = [
#   ["o", "t", "a"],
#   ["x", "a", "e"],
#   ["h", "k", "r"],
# ]

# words = ["eat", "pan"]

# in this case, the only word from `words`
# that appears on the board is "eat"
# board = [
#   ["-", "t", "-"],
#   ["-", "a", "e"],
#   ["-", "-", "-"],
# ]

# and how would you solve this?
# well, we need to find the first character.

# so it makes sense to iterate through every character on the board
# see if it's a starting character of any word.

# if yes, start an exploration
# from that point, see if you can find the rest of the characters

# it's also mentioned we can't reuse characters on the same path
# say, we're looking for "need"
# we would need two different "e"s

# so how do you know if a character is a starting character?
# a dictionary.

# we create a word map.
# char => an array of words that begin with char

# so at board cell, where char is in `wordMap`
# we run through each word in the array, and explore.

# once, we find a word, we can remove it from the array.
# we're told all the strings in `words` are unique, so we can use a set
# instead of an array.

# i wouldn't be able to remove the word from the set during iteration.
# so i can store it somewhere..
# or better, keep it as an array of words, then change the value at the index to `None`.

# works, there might be something more optimal but let's see how it goes.

# and the recursion..
# `word` and `cellPos`
# from each cell, you're exploring cardinal directions
# with `curIdx`, when `curIdx == len(word)`
# we know we just found a word.

# at this point, we return True
# this eventually reaches the caller and we know to turn the array value to `None`

# we'd also need a global variable for results, `self.res`
# when we hit `curIdx == len(word)`

# append to `self.res`

# regarding efficiency, say you have "oath" and "oat"
# and "oath" exists.

# it would be inefficient to search for "oath" then search for "oat"
# since the existence of one demands the other.

# if there was a way to group words into one.

# a Trie fits perfectly for this use case.
# does this mean i'd have to implement one..
# it seems so..

# you know what, let me implement the inefficient one first.
# then optimize with the Trie.

# error, i didn't check to see if the cell position was out of bounds.
# an oversight, perhaps, i was too eager to write something.

# i neglected it.

# error, after implementing the check..
# i placed it after accessing the board..

# again, i'm too eager to write.. even when it's one question.
# i'm still battling myself.

# error, i ended up finding each word four times.
# what happened was, the base case for a solution
# checks if current index is equal to the length of the word.

# at which point, i should return True.
# i didn't, and it returned None by default..

# this caused the code to explore down, left and right
# reaching the base case every time.

# error, i didn't track visited cells.
# this isn't an error i found by breaking code but accidentally.
# i misdiagnosed the earlier problem as this
# but also realize..
# if i'm looking for 'need'
# and have
# ['n', 'e', 'd']
# i could go to:
#   `n` with current index 0
#   `e` with current index 1, 
# then go left to
#   `e` with current index 2,
# and from there go right
#   with current index 3

# resulting in a false positive.
# TODO address above error.

# one for the regular path..
# the others for when 

# TODO re-implement with Trie.

class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:
        self.res = []
        
        self.board = board
        wordMap = self.getWordMap(words)
        
        for rowIdx, row in enumerate(board):
            for colIdx, cellVal in enumerate(row):
                if cellVal in wordMap:
                    matchingWords = wordMap[cellVal]
                    
                    for idx, w in enumerate(matchingWords):
                        if w is None: continue
                        
                        if self.explore(0, w, rowIdx, colIdx):
                            matchingWords[idx] = None
                            
        return self.res
                        
                        
    def explore(self, curIdx, word, ri, ci):
        if curIdx == len(word):
            self.res.append(word)
            return True

        rows, cols = len(self.board), len(self.board[0])
        is_out_of_bounds = ri < 0 or ri == rows or ci < 0 or ci == cols
        if is_out_of_bounds:
            return
        
        if word[curIdx] != self.board[ri][ci]:
            return
        
        curCh = word[curIdx]
        
        
        isUp = self.explore(curIdx + 1, word, ri - 1, ci)
        if isUp:
            return True
        
        isDown = self.explore(curIdx + 1, word, ri + 1, ci)
        if isDown:
            return True
        
        isLeft = self.explore(curIdx + 1, word, ri, ci - 1)
        if isLeft:
            return isLeft
        
        isRight = self.explore(curIdx + 1, word, ri, ci + 1)
        return isRight        
            
            
        
    def getWordMap(self, words):
        wordMap = {}
        
        for w in words:
            ch = w[0]
            
            if ch not in wordMap:
                wordMap[ch] = []
                
            wordMap[ch].append(w)
        
        return wordMap
    
arr = [
    [
        [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ],
        ["oath","pea","eat","rain"],
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findWords(foo, bar)
print(res)