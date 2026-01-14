# https://leetcode.com/problems/implement-trie-prefix-tree/description/


# want to implement a Trie. what is this a Trie.

# a data structure, a tree like data structure, with a root node
# and several or no children.

# { i did some deep thought... }

# a Trie is essentially a recursive node.
# each node contains, a set of Trie's

# however, a Trie's node is made up of two parts.
# the head and the children.

# and each child has it's own head, and it's children

# let's make it clearer, consider this Trie node

#      a
#     ...

# this is the minimum Trie node. the head is `a`
# and the `...` represent the absence of children.

# let's give it some children

#      a
#     fhg
#     ...

# now the Trie `a`, has three children, `f`, `g` and `h`.
# and each of the chilren is it's own Trie, hence the `...` indicating each child Trie does not have any children.

# i have some sense of the concept, now to implement this..
# from experience, i know to use a dictionary to represent a Trie Node..

# it works cleanly since the head is the key
# and the values are the children..

# i don't think it's a must that the child heads of a Trie are unique..
# but the usage of the data structure seems to demand it..

# a Trie can be used to store words, like a real life dictionary..

# consider the earlier example

#      a
#     fhg
#     ...

# based on this, i can find out if the Trie contains a sequence, `af`
# if i had a multiple `f`s within the child node, it wouldn't stop it's operation
# but it wouldn't be very efficient either, since i'd only need one `f`

#      a
#     ffhg
#      ..

# the above would be overkill if i simply wanted to check if `af` existed in the Trie.
# it's a way to store words..

# so back to this:

#      a
#     fhg
#     ...

# if i wanted to add another word, say `agi`
# i'd start from the root, check if the first character in `agi` exists in the Trie..
# yes it does, so i don't need to add an `a`

# now, i'm with `gi`, i check the next layer `fhg`
# does `g` exist, yes

# next layer, `...`, does `i` exist?
# no, add `i`


#      a
#     fhg
#     ..i

# also worth pointing out i've said layers, which is technicall correct, but i'm exploring a tree path
# as i progress through layers, i started at a -> g -> ?
# saw there was no `i`, created it and the exploration stopped there.. since i only wanted to add `agi`

# how about adding `bad`
# how would that work, in my case, the root node is `a`

# i understand that the root node in this case would need some abstraction
# if i were to accomodate the a new starting character, `b`

# the way the OGs suggest is to rewrite the root node..
# the root should be Trie where the value is unused..
# and the first characters in any word would be this children of this root node

# in my case, it'd look like

#    "root"
#      a
#     fhg
#     ..i

# this way, if i want to add `bad`
# i'd simply check `root`s children, if it has a `b`
# it doesn't so, i'd add a b


#    "root"
#      ab
#     fhg
#     ..i

# then continue the path traversal, does that `b` have an `a` child,
# in our case, obviously no, since we just added the `b`
# so, we'd have to create the `a` child...


#    "root"
#      ab
#     fhga
#     ..i

# we keep going and we eventually have:

#    "root"
#      ab
#     fhga
#     ..id

# and this is how the insertion would work, you'd basically traverse until you insert the word.
# what if the word exists, you'd still have to traverse to verify..

# okay, how do you search, search is basically the same as insert
# without the insert.. you traverse along a path
# and if you run out of Trie's before you run out of the search term
# you return False

# one subtle problem is knowing when a word exists..
# i know the problem exists cause i've solved this before..

# consider, the Trie:
#    "root"
#      ab
#     fhga
#     ..id

# say i'm searching for `ba`, looking at the Trie, it exists...
# but does it? i never inserted `ba`, i inserted `bad`

# and so a search operation should return False..
# how do i prevent this false positive..
# you want to somehow note, if a character is the end of a word..

# in this case, i'd have done it at letter `d` in `bad` and not at `a`
# so if i search for `ba`, technically those characters exist in the Trie..
# but they aren't actually an inserted word, so i'd return False..

# okay.. how about startswith.. this is essentially a search but i don't care
# if the character ends the word, all i want to know is if the search path exists somewhere in the Trie..

# okay, so how would you represent this Trie..
# i've said dictionary, but how do i represent the end of word character..

# "root" -> {a, b, c}

# two abstractions, a Trie class and the children as dictionaries

# class Trie
#     value
#     children
#     is_end

# so the root would be 
# class Trie
#     value = root
#     children = {...of child value => child Tries}
#     is_end = False

# so if i add `a`

# i check if `a` is the root.children..
# if it is, `a`s Trie becomes the root in the recursive exploration..
# and so on...

# don't do this in Python, `children={}`
# def __init__(self, val, children={}, is_end=False):
# what it does is re-use the same dictionary for all instances
# creating unintended consequences

# if you want to default to a mutable type do something like
# def __init__(self, val, children=None, is_end=False):
#   self.children = {} if children is None else children


class TrieNode:
    def __init__(self, val, is_end=False):
        self.val = val
        self.children = {}
        self.is_end = is_end

class Trie:
    def __init__(self):
        self.root = TrieNode(
            val="root"
        )

    def insert(self, word: str) -> None:
        self.insertRec(0, word, self.root)
        
    def insertRec(self, idx, word, root):
        if idx == len(word):
            return True
        
        newCh = word[idx]
        
        # we wanna check if `newCh` exists in `root.children`
        # if it does, start new recursive call with `root.children[newCh]` as `root`
        # increase idx by 1
        
        # if `newCh` doesn't exist in `root.children`
        # create the Trie, and add it to `root.children`
        # then start new recursive call with `root.children[newCh]` as `root`
        # increase idx by 1
        
        if newCh not in root.children:
            root.children[newCh] = TrieNode(newCh)
            
        if self.insertRec(
            idx + 1,
            word,
            root.children[newCh]
        ):
            root.children[newCh].is_end = True
        
        # and at what point does this recursion end..
        # it ends when idx == len(word)
        # in which case, the last node added sets `is_end = True`
        
        # how do you know to do this? well, we can return True
        # when idx == len(word), this way we tell the parent
        # you are the last node

    def search(self, word: str) -> bool:
        idx = 0
        root = self.root
        return self.searchRec(idx, word, root)
    
    def searchRec(self, idx, word, root):
        if idx == len(word):
            return False
        
        searchCh = word[idx]
        if searchCh not in root.children:
            return False
        elif idx == len(word) - 1 and root.children[searchCh].is_end:
            return True
        
        return self.searchRec(
            idx + 1,
            word,
            root.children[searchCh]
        )
        

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithRec(0, prefix, self.root)
        
    def startsWithRec(self, idx, word, root):
        if idx == len(word):
            return False
        
        currCh = word[idx]
        if currCh not in root.children:
            return False
        elif idx == len(word) - 1:
            return True
        
        return self.startsWithRec(
            idx + 1,
            word,
            root.children[currCh]
        )


t = Trie()

print(t.startsWith("a"))