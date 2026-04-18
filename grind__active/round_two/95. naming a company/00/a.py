# https://leetcode.com/problems/naming-a-company/description/

from typing import List

# i'm given a list of strings, `ideas`
# i want to explore all the distinct ways 
# i can pick two words from the list of strings.

# from each two-word selection
# i want to create two new words.

# the two new words are formed by swapping 
# the first letters of the original two words.
# if both new words don't exist in the list, `ideas`

# i should note this.
# my job is to count how many times this situation occurs.

# and return that value.

# my first trial is to explore every combination of two items.
# form the two new words, check if both new words do not exist in `ideas`
# increment the counter accordingly.

# for this, i'd need a set for `ideas`
# the question guarantees every word in `ideas` is unique.
# this way, i can check for the existence of the two new words.

# seems simple enough but i have a feeling
# the real question is about making this efficient.

# error, turns out the word pairs in each combination aren't unique.
# (apple, oranges) and (oranges, apple) are classed as two different combinations.

# in this case, i can keep my code as is, and just multiply the result by `2`
# since the order of every combination can be swapped.

# i didn't realize this from the jump because i didn't take the time to read the examples.
# i assumed i understood the question, i didn't. i should've looked at the examples.

# right, time limit exceed as expected.
# what's the limiting factor? how can i make this faster?

# i do have to check every combination
# don't i? it seems so. Claud agrees.

# then the check must be the issue..
# is there a way to premtively check?

# what do we do when we check?
# we swap the first characters of both strings.
# then ensure the new strings don't exist in the set.

# consider two pairs.

# (apple, mango)
# (apple, maple)

# both pairs result in:
# (mpple, aango)
# (mpple, aaple)

# in both cases, `mpple` is formed twice.
# no need to recreate the string.
# one approach is to cache this..
# the first time we create the string..

# what are we caching? the created string?
# that would defeat the point, since we have to recreate it
# to check if it's in the cache.

# on first instance, we create the string..
# then store a tuple as cache (firstChar, restOfChar) => boolean
# this way we can have the parts that make up the new string and the result
# this saves us from having to.. form the new string everytime.
# so this might save time..
# let's try it out.

# TODO best i rewrite this.


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideaSet = set(ideas)
        
        counter = 0
        dim = len(ideas)
        for idxOne in range(dim):
            wordOne = ideas[idxOne]
            for idxTwo in range(idxOne + 1, dim):
                wordTwo = ideas[idxTwo]
                
                print(wordOne, wordTwo)
                
                newWordOne, newWordTwo = self.getNewWords(
                    wordOne,
                    wordTwo,
                )
                
                if newWordOne in ideaSet or newWordTwo in ideaSet:
                    continue
                
                counter += 1
                
        return counter * 2
    
    def getNewWords(self, wordOne, wordTwo):
        newWordOne = wordTwo[0] + wordOne[1:]
        newWordTwo = wordOne[0] + wordTwo[1:]
        
        return newWordOne, newWordTwo
    
    
    
arr = [
    ["coffee","donuts","time","toffee"],
]
foo = arr[-1]
sol = Solution()
res = sol.distinctNames(foo)
# print(res)