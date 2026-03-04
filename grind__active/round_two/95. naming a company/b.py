# https://leetcode.com/problems/naming-a-company/description/

from typing import List

# follow-up from a.py..
# for each word, check if it's valid..
# if both words are valid, increment the counter.

# error, for the slice of the second word..
# i passed `wordTwo[2:]` instead of `wordOne[1:]`
# perhaps, it's because i'm tired?
# perhaps, a cog in my thinking..

# either way, it's fixed but still TLE
# TODO need to find another way..

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideaSet = set(ideas)
        
        self.newWordCache = {}
        
        
        counter = 0
        dim = len(ideas)
        for idxOne in range(dim):
            wordOne = ideas[idxOne]
            for idxTwo in range(idxOne + 1, dim):
                wordTwo = ideas[idxTwo]
                
                isWordOneValid = self.isValid(wordTwo[0], wordOne[1:], ideaSet)
                if not isWordOneValid:
                    continue
            
                isWordTwoValid = self.isValid(wordOne[0], wordTwo[1:], ideaSet)
                if isWordTwoValid:
                    counter += 1

        return counter * 2

    def isValid(self, ch, restOfWord, ideaSet):
        mitem = (ch, restOfWord)
        if mitem in self.newWordCache:
            return self.newWordCache[mitem]
        
        newWord = ch + restOfWord
        self.newWordCache[mitem] = newWord not in ideaSet
        
        return self.newWordCache[mitem]
    

    
    
    
arr = [
    ["coffee","donuts","time","toffee"],
]
foo = arr[-1]
sol = Solution()
res = sol.distinctNames(foo)
print(res)