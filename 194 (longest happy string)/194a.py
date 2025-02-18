# https://leetcode.com/problems/longest-happy-string/description/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pass
        # you can take at most two of each character
        # before adding the next one
        # it makes sense to start with the most popular characters
        
        # sort a, b, c in decreasing order of frequency
        # create an array, `res`
        
        # iterate from most_frequent to the least
        # grab at most two of each
        
        lst = [
            ["a", a],
            ["b", b],
            ["c", c],
        ]
        

