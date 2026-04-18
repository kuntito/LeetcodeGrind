from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dim = len(ideas)
        validNameCount = 0
        self.ideaSet = set(ideas)
        self.memo = {}
        
        for idxOne in range(dim):
            wdOne = ideas[idxOne]
            for idxTwo in range(idxOne + 1, dim):
                wdTwo = ideas[idxTwo]
                
                # i don't need to make the swaps
                # and return both new strings.
                
                # both strings are doing the same thing.
                # take one character, combine it with a string
                # does the combination exist in the `ideaSet`
                if self.is_combo_valid(wdOne, wdTwo[0]) and \
                    self.is_combo_valid(wdTwo, wdOne[0]):
                        validNameCount += 1
                        
        return validNameCount * 2
    
    def is_combo_valid(self, word, ch):
        mitem = (word, ch)
        if mitem in self.memo:
            return self.memo[mitem]
        
        new_word = ch + word[1:]
        is_exist = new_word not in self.ideaSet
        
        self.memo[mitem] = is_exist
        return self.memo[mitem]
    
arr = [
    ["coffee","donuts","time","toffee"],
]
foo = arr[-1]
sol = Solution()
res = sol.distinctNames(foo)
print(res)