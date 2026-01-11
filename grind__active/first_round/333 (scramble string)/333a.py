# https://leetcode.com/problems/scramble-string/description/

# i want to implement a function, `isScramble`
# this function takes two string arguments and returns a boolean.

# the two string arguments are `s1` and `s2`
# we want to scramble string `s1` to get `s2`

# if the length of the `s1` is `1`, we stop
# if the length is greater than `1`, we do the following:

# we split `s1` into two non-empty substrings, `uno` and `dos`
# then combine the substrings however you please

# you could do `uno + dos` which would result back into `s1`
# or do `dos + uno` which would result in a different string

# right, the OG explanation was a bit long winded but i get it now
# we're give two strings, `s1` and `s2`

# we want to find out, if we can scramble `s1` to form `s2`
# the scrambling works like this

# we split the string, `s1`
# into two non-empty strings, `uno` and `dos`

# then we may or may not swap the order
# but that isn't relevant now

# when we obtain our splits, `uno` and `dos`
# we further split each one into two non-empty substrings

# and repeat the process on each substring

# say our word was "live"
# and we choose to split into "li" and "ve"
# we would eventually combine the words
# but first want to see the different ways we can split and combine the substrings, "li" and "ve"

# for "li", we can split "l" and "i"
# at this point, we can no longer split the substrings
# so we have to recombine and return the combinations
# we can combine like "l" + "i" or "i" + "l"
# so we'd return "li" and "il"

# we can do the same for "ve"
# where we return "ve" and "ev"

# going back to the first recursive call, where we obtained
# "li" and "ve"

# we would want to combine the words "li" + "ve"
# or "ve" + "li"

# but recall,
# "li" can be scrambled to "li" and "il"
# and 
# "ve" can be scrambled to "ve" and "ev"

# so we can combine each scramble of "li"
# with each scaramble of "ve"

# and have:
# "li, ve"
# "li, ev"
# "il, ve"
# "il, ev"

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        pass
        self.explore(s1)
        
    def explore(self, chars):
        # for 
        pass