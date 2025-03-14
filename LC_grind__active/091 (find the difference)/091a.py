# https://leetcode.com/problems/find-the-difference/description/

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        pass
        # define a counter for `s`    
        counter = Counter(s)
        
        # iterate through `t`
        # if the character is not in `counter` or the character count == 0
        # return False
        # else decrement the character count
        
        for ch in t:
            if ch not in counter or not counter[ch]:
                return ch
            
            counter[ch] -= 1

            
arr = [
    ["abcd", "abcde"],
    ["a", "aa"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findTheDifference(foo, bar)

print(res)