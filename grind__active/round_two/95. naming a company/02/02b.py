from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dim = len(ideas)
        validNameCount = 0
        ideaSet = set(ideas)
        
        for idxOne in range(dim):
            wdOne = ideas[idxOne]
            for idxTwo in range(idxOne + 1, dim):
                wdTwo = ideas[idxTwo]
                
                # now, i have to swap the first letters
                # i'm creating a new string here.
                
                newStrOne, newStrTwo = self.swapFirstLetters(
                    wdOne,
                    wdTwo
                )
                
                if newStrOne in ideaSet or newStrTwo in ideaSet:
                    continue
                
                validNameCount += 1
                
        # 'pparently, (cat, bar) and (bar, cat) are to be treated as distinct.
        # and is why i simply multiplied by `2`
        # if the new words after swapping are valid.
        # they'd remain valid even if the order was swapped.
        # hence, every valid company name has a twin.
        return validNameCount * 2
                
    def swapFirstLetters(self, wdOne, wdTwo):
        newStrOne = wdTwo[0] + wdOne[1:]
        newStrTwo = wdOne[0] + wdTwo[1:]
        
        return newStrOne, newStrTwo
    
arr = [
    ["coffee","donuts","time","toffee"],
]
foo = arr[-1]
sol = Solution()
res = sol.distinctNames(foo)
print(res)