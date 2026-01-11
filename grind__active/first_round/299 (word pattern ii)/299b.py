# https://leetcode.com/problems/word-pattern-ii/description/

# what's the challenge?
# i'm to implement a function that takes two string arguments
# `pattern` and `s`

# both strings contain lowercase english characters
# we want to find out if each character in `pattern` can accurately map onto substrings in `s`
# i.e.
# pattern = "aba"
# s = "peabodypea"

# in this case, it maps
# a => pea
# b => body

# pattern = "aba"
# s = "peabodyped"
# this doesn't match
# there's no way to structure the patterns that we find a valid mapping

# the examples make the question simple
# but really when we compare a character in `pattern`
# we don't know how much of `s` it maps to
# so we'd have to experiment

# for each character in pattern, we'd explore `n` starting characters in `s`
# where `n <= len(s)`
# we'd do this recursively and track the patterns we found
# if `a` => `pea`, we'd put it in a hashmap
# if we explore the rest of the strings i.e. pattern[1:], s[?:]
# and we find out `a` => `pea` doesn't give a final answer
# we remove it from the hashmap and try another combination

# TODO i understand the problem but my implementation is false
# when you have a => red
# if you encounter a again, you want to check if it maps to the current entry in `patternMap`

# TODO it fails the last test case, you need to handle the bijection
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # i think i'm doing this wrong, the only time i should loop
        # is the starting point, i want to know how much of `s` maps to `pattern[0]`
        # this might be wrong too
        
        patternMap = {}
        res =  self.explore(pattern, s, patternMap)
        # print(patternMap)
        return res
            
    def explore(self, pattern, chars, patternMap):
        if pattern == "" and chars == "":
            return True
        if pattern == "" or chars == "":
            return False
        
        first = pattern[0]
        if first in patternMap:
            slice = patternMap[first]
            currSlice = chars[:len(slice)]
            if slice == currSlice:
                return self.explore(
                    pattern[1:],
                    chars[len(slice):],
                    patternMap
                )
            else:
                return False
        
        dim = len(chars)
        
        for idx in range(dim):
            addedHere = False
            slice = chars[:idx + 1]
            
            if first in patternMap and patternMap[first] != slice:
                return False
    
            if first not in patternMap:
                patternMap[first] = slice
                addedHere = True
            
            if self.explore(
                pattern[1:],
                chars[idx + 1:],
                patternMap
            ):
                return True
            
            # i want to delete the pattern, only if it was added in the current recursive call
            if addedHere:
                del patternMap[first]
            
        return False
        
        
arr = [
    ["aabb", "xyzabcxzyabc"], # TODO
    ["aaaa", "asdasdasdasd"],
    ["abab", "redblueredblue"],
    ["ab", "aa"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordPatternMatch(foo, bar)
print(res)

# a = "aa"
# print(a[5:])
