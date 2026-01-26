# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List

# following from `a.py`
# you want to reverse iterate through `s`
# at each index, you want to note all the words that start there..

# once done..
# start an iteration from the first..
# for each point where there's a word..
# explore all the words.. this'd probably be recursive..

# for every word.. you explore if a word occurs after it.. or the indices after it..
# to be more explicit..
# if you're at index = 0, you find a word `lee`

# you want ot check from `index + len("lee")` onwards..
# do other words start here...

# in essence, you want to optimize for ...
# how about, what question are we asking at each point during the iteration..
# what's the best way i can remove words from the rest of the string
# that i'd have the least amount of characters left

# nother attempt,
# i'm saying, at this point, i want to remove words from the rest of the string.
# i want words in a way that reduces the rest of the string

# say i have "apple"
# ideally, if i remove "apple".. the rest of the string becomes ""
# so i'd have no more characters left..

# this isn't the best explanation..
# let's go again..

# i have a string.. `s`
# i have a list of words, `wordList`,
# some of those words exist in `s`.. let's call each one, `existingWord`
# i want to remove one or more `existingWord`s from `s`

# but i want to find the right combination, such that when removed from `s`
# `s` becomes as small as possible..

# for example:
# s = "jaynas"
# wordList = ["ayna", "nas", "jay"]

# all the words of `wordList` exist in `s`
# but which combination do i remove..

# for starters, if i remove "ayna"
# i'm left with `s = js`

# i can no longer remove any words..
# i can't get "nas" or "jay" from here..
# ergo, removing "ayna" would reduce the length of `s` to `2`

# okay, what if i remove "nas"
# i'm left with `s = "jay"`
# okay, i can then remove "jay"
# and be left with ""

# i thinking removing "nas" and "jay" is the best approach..
# also, does the question mention removing the same word more than once..
# it doesn't say, but i should assume it's the case..

# if i had "nasnas" with the same word list, i can remove "nas" twice..
# that said..you don't know which word to remove first until you do..

# hence, why the iteration from the start is useful..
# restarting the example:
# s = "jaynas"
# wordList = ["ayna", "nas", "jay"]

# from the details in `a.py`, 
# i said i'd start with a loop to cache words that start at each position

# so, if i ran the loop on "jaynas"

# i'd have:
# 0 => ["jay"]
# 1 => ["ayna"]
# 2 => []
# 3 => ["nas"]
# 4 => []
# 5 => []

# then start another iteration, this way when i hit index `0`
# i immediately have access to the words that start at `0`
# in this case, `jay`
# i know `jay` exists, if i remove `jay`, i'm left with the words in index `3` onwards..

# this is now the recursive step, at index `3`
# i'm doing the exact same thing as `index 0`
# what words start here..
# i'd find `nas`
# if i remove `nas`, need to find words from `index 6` onwards..
# this is out of bounds, and so, i can deduce, i remove six chars, "jay" and "nas" from "s"
# i'd be left with `0` chars in `s`.. this is the best case and i can end the iteration here..

# but imagine `s` was "jaynasir"
# and word list was "jay", "nas" and "nasir"
# 
# it would mean after removing "jay" and exploring "nas", s would be "ir"
# i'd still end the loop there cause no word starts at "i" or "r"

# but going back to `index 3`, there's another word.. "nasir"
# so i'd explore "nasir" too..
# in essence, i'm exploring every word at each index..

# yes.. but are you moving forward too..
# what do you mean..
# say you had "jayxnas"
# and wordList = [jay, nas]
# you remove `jay`, jump to `index 3`, you're at character `x`
# you see there's no words in `x`.. what do you do..
# you continue the iteration.. right..
# it's the same pattern on every step..
# iterate from starting index to the end of `s`
# any point with words, explore to the last.. store the length of all words removed..

# this would benefit from caching.. definitely..
# so what is each recursive function needing..

# startIdx
# memo
# lenSoFar
# wordCache
# a global variable for least found..


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        startIdx = 0
        wordCache = self.getWordCache(s, dictionary)
        lenSoFar = 0
        memo = {}
        
        self.leastExtraChars = len(s)
        
        self.explore(startIdx, lenSoFar, wordCache, memo)
        
        return self.leastExtraChars
    
    def getWordCache(self, chars, wordList):
        pass
        # what am i doing here.. 
        # for each index, i want to know the words that exist there..
        
        # i don't know if there's a clever way to do this..
        # seems for each character, i'd have to check every substring that can form
        # and see if they exist in `wordList`
        
        # that's a rather tedious approach..
        # another one is..
        
        # map every letter of the alphabet to the existing words..
        # wordList = [az, busta]
        
        # charMap = { a => [az], b => [busta] }
        # this way for each character in `s`
        # if i see an `a`, i know the only word i have is `az`
        # so it becomes, a substring slice problem..
        # what substring would i need for az, s[idx: idx + 2]
        # is that slice == az.. if yes..
        # move forward..
        
        