# https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass
        # two pointers, `idx` for iterating backwards through `word1`
        # and `tagIdx` for `word2`'s index starting from behind
        
        # a variable, `count`, that represents the "changes" made to `word1`
        
        count = 0
        tagIdx = len(word2) - 1
        # iterate backwards through `word1`
        for idx in range(len(word1)-1, -1, -1):
            # compare each char with `word2[tagIdx]`
            # if they are equal, `tagIdx -= 1`
            # if they are unqueal and `idx == tagIdx`
            # `tagIdx -= 1`

            char = word1[idx]
            if char != word2[tagIdx]:
                count += 1
                
            if char == word2[tagIdx] or idx == tagIdx:
                tagIdx -= 1
                
                
        return count if len(word1) >= len(word2) else count + len(word2) - len(word1)

arr = [
    ["horse", "ros"],
    ["intention", "execution"],
    ["", "a"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minDistance(foo, bar)
print(res)
        
        
        
        