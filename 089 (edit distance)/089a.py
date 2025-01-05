# https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass
        # since the words can be of different sizes
        # if they're equal lengths, we'd possibly replace in `word1`
        # if `word1` is longer, we'd remove and/or replace from `word1`
        # if `word2` is longer, we'd add and/or replace to `word1`
        
        # LIS is longest common substring??
        
        # find LIS between the two strings
        # using the position of the LIS in `word2`

        # count += max(
        #   determine the number of characters before the LIS in `word2`,
        #   determine the number of characters before the LIS in `word1`
        # )

arr = [
    ["horse", "ros"],
    ["intention", "execution"],
    ["", "a"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minDistance(foo, bar)
print(res)
        
        
        
        