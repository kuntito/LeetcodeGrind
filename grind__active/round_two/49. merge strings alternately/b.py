# https://leetcode.com/problems/merge-strings-alternately/

# as a follow up from `a.py`
# i can check handle the situation for the string that runs out in the main loop

# i'd create a loop that lasts as long as the longest string..
# i'd iterate through that loop with the index.

# the trick happens inside the loop
# the index would point to the current position in both strings..

# so what happens when you run out of one word
# that's where the if condition comes in..

# before adding any char to `combined`
# you check to see that index is valid in said string..

# neat..

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = []
        
        dimOne, dimTwo = len(word1), len(word2)
        longer = max(dimOne, dimTwo)
        
        for idx in range(longer):
            if idx < dimOne:
                combined.append(word1[idx])
                
            if idx < dimTwo:
                combined.append(word2[idx])
            
        return ''.join(combined)
    
arr = [
    ["ab", "pqrs"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.mergeAlternately(foo, bar)