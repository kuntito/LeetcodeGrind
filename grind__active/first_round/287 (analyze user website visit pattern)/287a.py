# https://leetcode.com/problems/analyze-user-website-visit-pattern/description/

class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        pass
        # can i take a moment to understand the question
        
        # we're given two arrays, they both contain strings
        # and are the same length
        
        # we have users that visit websites
        # not entirely sure how this connects to the two arrays but...
        
        # there's patterns with which websites are visited
        # i.e. a -> b -> c
        # means a user visited websites `a`, `b` and `c` in order
        
        # from what i can gather, we want to order the websites visited by each user in order
        
        # once we have the website order for each user, we need to observe the distinct patterns
        
        # then return the most frequent of said patterns
        # and if there's a tie, we should return the lexicographically smaller pattern
        
        