# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# this one is a different one.

# i want to implement a data structure that stores words
# and can be queried to find words..

# the query is where the problem lies..
# say i add `bad` to my structure, `WordDictionary`

# a query can be `bad`, at which case, i'd simply.. return True
# however the query can have dots, `.`, and these dots match any character..

# so a query `.ad` can match `bad`, or `cad`
# `...` can match any three letter word..

# i thought about using a Trie, but i'm not too sure about it.
# let me paint the problem, see what emerges..

# when you get a character, you need to know if it exists in your dictionary..
# to be fair, a Trie would still do wonders here..

# the difference would be when we get a dot.. we don't know which character to pick
# so we try everything..

# it would be a multi branch recursion whenever there's a dot
# and we'd return the first one we find..

# do these homies actually expect me to implement a Trie then solve this..
# it seems like it..

# kay, how do i build a Trie again.. you need a node, a Trie node..
# it contains the character, it's dictionary of children, is_word_end


# the Trie should be able to add words.. that's it..
# let's implement the Trie then take it from there..
class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode("root")

    def addWord(self, word: str) -> None:
        # so what's adding word like, you use a recursive approach
        # each recursive call addresses each character of the word..
        # what you want to do is see if that character exists in the children of the root Trie node
        # if yes, start another recursive call with the character in `word` and it's corresponding Trie node
        # what's the base case.. when we run out of characters
        # at which point, we simply set `is_word_end = True`

        # self.addWordRec(0, word, self.root)

        # why does it have to be recursion
        # why not a while loop...
        # i'm listening, iterate through word
        # for each character, check if it exists in roots children..
        # if no, add the character and move forward..
        # update root..
        # keep doing till you reach the end, at which point, root should point to the last character in word
        # set `is_word_end = True`
        # what inspired this? i was struggling figuring out how to write the base case for the recursive approach
        # since i want to set `is_word_end` at the last character
        # but i don't have access to the last character when curIdx == len(word)..
        # see your first implementation of this.. but yes, while loop can work
        
        # yeah, saw the implementation, what i did was return True
        # at the base case, so once i returned to the parent call
        # i know the current Trie node is the last..
        
        root = self.root
        
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode(ch)
                
            root = root.children[ch]
            
        root.is_end = True
        
    # okay, how would this go, say i'm searching for `.ad`
    # once i see the character is a period, i'd grab all the children..
    # i'd iterate through each child..

    # perhaps, recursion, sounds better..
    # or is easier to write, is what my intuition tells me

    # so each character, you check if it exists in roots child
    # for non-dots, the route is simple, start another call
    # with said character and it's TrieNode, move current index forward..

    # however, once we hit a dot, what do we do..
    # start a recursive call with every child in root
    # move current index forward..

    # what's the base case..
    # when ch is not dot and doesn't exist in `root.children`

    # when ch is last character
    #     if root.children contains ch, and 
    #     if root.children does not 

    # not sure you need all that consider the search `b`
    # if `b` exists in root.children, we start a rec call
    # in rec call, we'd realize we're out of bounds, but `b`s node is word end..
    # so we can return True..
    # or even simpler `b.is_end`

    # the moment we get our first True, we break
    def search(self, word: str) -> bool:
        curIdx = 0
        root = self.root
        return self.searchRec(curIdx, word, root)
        
    def searchRec(self, curIdx, word, root: TrieNode):
        if curIdx == len(word):
            return root.is_end
        
        ch = word[curIdx]
        if ch != '.':
            if ch not in root.children:
                return False
            else:
                return self.searchRec(
                    curIdx + 1,
                    word,
                    root.children[ch]
                )
                
        # at this point ch is '.'
        # so we explore every child trie node
        for trie in root.children.values():
            if self.searchRec(
                curIdx + 1,
                word,
                trie
            ):
                return True
            
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
