# https://leetcode.com/problems/word-pattern-ii/

# i want to implement a function that takes two string arguments
# `pattern` and `s`

# i want to find out if it's possible to map each character in `pattern`
# to specific substrings in `s`

# for instance,
# pattern = "aba"
# s = "dogbatdog"

# in this case "a => dog" and "b => bat"

# pattern = "aba"
# s = "dogbatdo"

# in this case, "a => dog", "b => bat"
# but "a => do" would negate the arrangement
# each character in `pattern` should map to the same substring in `s`
# and vice versa

# if "a => dog", you can't map "dog" to any other character
# that said, we'd need a two way mapping system

# for mapped character, we'd have two hashmaps
# charToStr and strToChar

# i'd use a recursive approach
# where i attempt to map the first character in `pattern` to `n` chars in `s`
# after a mapping it, i'd explore the rest of `pattern` and the rest of `s`
# in another recursive loop and repeat until i hit the base case where
# pattern == "" and s == ""

# if either pattern or s becomes an empty string while the other contains characters
# i'd return False
# and remove any mappings it took to get there

# it's a recursive backtracking solution 
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        charToStr = {}
        strToChar = {}
        return self.explore(pattern, s, charToStr, strToChar)
    
    def explore(self, pattern, chars, charToStr, strToChar):
        if pattern == "" and chars == "":
            return True
        
        if pattern == "" or chars == "":
            return False
        
        firstPat = pattern[0]
        
        # now we want to explore mapping `firstPat` with `n` consecutive characters in `chars`
        # where `n < len(chars)`
        # but what if `firstPat` is already mapped?
        # well, we should check that and proceed to the next recursive call
        
        if firstPat in charToStr:
            # and if the slice is what starts `chars`
            slice = charToStr[firstPat]
            if slice == chars[:len(slice)]:
                return self.explore(pattern[1:], chars[len(slice):], charToStr, strToChar)
            return False
        
        dim = len(chars)
        for idx in range(dim):
            slice = chars[:idx + 1]
            # we need to make sure the slice hasn't been mapped
            # if it is, return False
            # since getting here, we know for a fact, it wasn't mapped to `firstPat`
            if slice in strToChar:
                continue
            
            # getting here, means we create a mapping and test it
            charToStr[firstPat] = slice
            strToChar[slice] = firstPat
            
            if self.explore(
                pattern[1:],
                chars[len(slice):],
                charToStr,
                strToChar
            ):
                return True

            # remove the mapping if it doesn't work out
            del charToStr[firstPat]
            del strToChar[slice]
            
            
        return False
    
arr = [
    ["aaaa", "asdasdasdasd"],
    ["abab", "redblueredblue"],
    ["ab", "aa"],
    ["aabb", "xyzabcxzyabc"],
    ["aba", "aaaa"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordPatternMatch(foo, bar)
print(res)
            
            