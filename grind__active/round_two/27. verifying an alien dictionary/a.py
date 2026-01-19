# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List

# i'm given two things, a array of words and a string.
# the array, `words`, well, contains words..

# the string however, contains 26 characters
# the lowercase english alphabet, albeit in a different order..

# the ask is, are the words in `words` sorted lexicographically.
# that word, lexicographically, is where the problem lies.

# what does that mean?

# let's consider the natural order of the alphabet
# `abc..`

# and consider the words, [ap, ad]
# are they sorted in lexicographical order?

# it essence, it means on the first character where two words differ..
# do they follow the order of the alphabet..

# what do you mean..
# in english, `a` comes before `b` and `b` comes before `c`..
# you can drive this to it's natural conclusion..

# when we compare `ap` and `ad`
# we want to find out if the sorting of these words follows that order..
# we start from their first letters..

# `a` and `a`, for this, we can't determine any order.. since they're the same
# so we move to the next characters..
# `p` and `d`,  now, we got a situation..

# `p` doesn't come before `d` in the alphabet, ergo, the words aren't sorted lexicographically..
# the correct order would be `ad`, `ap`

# off, the dome, i'd say run through `words`
# picking two words at a time..

# the current word and the next, be careful for the last index..
# since there's no word after it..

# an optimization would be to start iteration from the first index..
# this way i'd compare the current word and previous word..

# so i never get the out of bounds error or have to rewrite the code
# to accomodate this..

# alreet.. then, how'd this work..
# for each two words, i'd use a helper function to compare lexicographical order

# if the following are words [jay, nas, em]
# if `jay and nas` are ordered, we check `nas and em`

# if all checks return positive, we'd return True after iteration
# else, return False on the first False check..

# how exactly would you check if one character is before the other
# that's where a dictionary comes in, we map each character to a number.. `0..25`
# and use the nunmber for comparison..

# is it optimal? we'd find out..

# well, at test case 120/125
# i get this.. ["apple","app"]
# my logic dictates that this is ordered but it isn't
# while the first differing characters does not exist..
# because, after exhausting the similarities between "apple" and "app"
# i'm left with "le" and ""
# and this isn't lexicographically ordered..

# new amendment, if we run out of charaters, the prev word must be shorter or equal
# to the next word..

# hence return case should be `len(prev) <= len(curr)`
# it works and is optimal.. we ball
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pass
    
        orderDict = {ch: i for i, ch in enumerate(order)}

        dim = len(words)
        for idx in range(1, dim):
            prev = words[idx - 1]
            curr = words[idx]
            
            if not self.isLexi(prev, curr, orderDict):
                return False
            
        return True
    
    def isLexi(self, prev, curr, orderDict):
        # you want to do this for the first differing character
        # and only the first differing character
        # how do you find the first differing character
        for chOne, chTwo in zip(prev, curr):
            if chOne != chTwo:
                return orderDict[chOne] <= orderDict[chTwo]
            
        return len(prev) <= len(curr)
