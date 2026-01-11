# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from typing import List

# i want to implement a function that returns a string array.
# this function takes two string arguments, `s` and `p`.

# my job is to return an integer array.
# each element in the array represents the starting indices of an anagram of `p`

# it is possible that `p` or it's anagrams are a substring of `s`
# i.e. 
# s = "abc"
# p = "bc"

# in this case, `p` is a substring of `s`
# and the substring starts at index `1`

# it's possible multiple substrings exist
# consider when s = "abcb" and p = "bc"

# in this situation, two anagrams of `p` exist
# "bc" and "cb"
# and they each start at index `1` and index `2` in `p`

# now that we're on the same page
# how do i solve this joint?

# i'm thinking a sliding window of length `p`
# i'd also have a Counter to keep track of character count

# i'd intialize the Counter with the first len(p) characters
# and keep track if i match `p`s character length

# since the substring is contiguous, while building the sliding window
# i need to ensure the sliding window charCount matches p's charCount
# which means, if i encounter a char count in `s` that exceeds it's charCount in `p`
# i'd move the left pointer forward until the window is valid

# also, while building the window, if i find a character in `s` that is not in `p`
# i'd move the left pointer forward until the window is valid, in this case, i'd move it to the next character after currentChar
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pass