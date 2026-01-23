# https://leetcode.com/problems/merge-strings-alternately/

# i'm given two strings, `word1`, and `word2`
# and want to merge them together into a new string, `combined`

# the merge instructions is like this.
# starting from the begining of both strings..
# i'd pick the first char from `word1`, add it to combined
# pick the first char from `word2`, add it to combined..

# keep doing this till i run out of both or one of the strings..
# if i run out of both, merge complete..

# if i run out of only one, i'd simply append the rest of the remaining string to `combined`
# return combined.

# for example, if i merge 'nas' and 'jay'
# i'd have 'njaasy'

# if i merged 'nasir' and 'jay', i'd run out of 'jay' first, then be left with 'ir' and ''
# i'd have 'njaasyir'

# okay so how would you implement this..
# two indices
# one for each word..

# i'd use a while loop, while both indices are valid
# add each character to combined in the order of `word1`s char then `word2`s char
# once you run out..

# check with each index, which word still has characters
# add said characters to `combined`.
# then we done..

# also, make `combined` an array then convert to a string.

# this is more efficient, since strings are immutable
# having to add each character on the go creates a new string
# as opposed to having an array and the joining it.

# but isn't concatenation doing the same thing..
# might be more optimal.. since they know they're concatenating from the jump.

# made an error, 
# i didn't update the iterator in the while loop checking which
# string didn't run out..

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = []
        
        idxOne, idxTwo = 0, 0
        dimOne, dimTwo = len(word1), len(word2)
        
        while idxOne < dimOne and idxTwo < dimTwo:
            combined.append(word1[idxOne])
            combined.append(word2[idxTwo])
            
            idxOne += 1
            idxTwo += 1
            
        while idxOne < dimOne:
            combined.append(word1[idxOne])
        
        while idxTwo < dimTwo:
            combined.append(word2[idxTwo])
            
        return ''.join(combined)
    
arr = [
    ["ab", "pqrs"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.mergeAlternately(foo, bar)