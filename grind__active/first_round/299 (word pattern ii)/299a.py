# https://leetcode.com/problems/word-pattern-ii/description/

# it seems to me, i have a tendency to jump straight to code.
# you like to code, we get it but this isn't about you
# not really, the company wants an employee and they want someone who can communicate their thinking

# and that's who you want to become, yes, you want to solve the problem and are concerned you wou;dn't solve the problem within the time constraints. while that may be true, jumping directly into code is not in your best interests.

# you can code. there's evidence to that. what you struggle with is taking the time to write out your thoughts before coding.

# you have a question
# explain it in your own words
# what arguments are you dealing with
# what are you returning
# is it a function, is it a design problem

# write in english
# then code
# code after the lines you've written in english
# you don't want to write a long paragraph then code underneath
# let the code reflect the content of your writing
# do this and repeat until the message sinks in
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pass
        # first, what do you understand by the question? what is the question asking? what's the challenge?
        
        # we are to implement a function and return a boolean.
        # the function takes two arguments, `pattern` and `s`, two strings
        
        # `pattern` eponymously means a pattern
        # each string in pattern maps to a set of unique string
        
        # `s` is a sequence of characters
        # our job is to determine if `pattern` matches `s`
        
        # this is an interesting problem
        # i'd say we need to know what the pattern represents, what does each character mean
        
        # let's consider
        # pattern = "abab"
        # s = "redblueredblue"
        
        # how do i know what `a` represents?
        # `a` could reprsent the first `n` characters in `s`
        # where `n >= 1`
        
        # would this be a bruteforce approach?
        # where we pair a -> with every character until something sticks
        
        # a -> r
        # a -> re
        # a -> red
        
        # for every pairing we make, we'd add to a hashmap
        # and explore the rest of the string the same way
        # if we get to the end of the string and have exhausted all characters in `pattern`
        # we'd have our answer and if not, we return False
        
        # say you explore `r` and realize that's not the case, what do you do?
        # we explore `re` and replace the mapping
        
        # if we're working with a -> re
        # and encounter another `a`, if it already exists in the mapping, we should stop exploring
        
        # so a recursive backtracking function
        # it takes the current pattern, the string, it also needs a hashmap
        # and would return True, if we get to the end
        return self.explore(pattern, s, {})
    
    def explore(self, pattern, chars, patternMap):
        # what is the base case here? since `pattern` and `chars`
        # is what's left of our pattern and the characters, if we exhaust both
        # we have our result
        if pattern == "" and chars == "":
            return True
        
        # if we exhaust one and not the other, we return False
        # it means we can't form the pattern with chars
        if pattern == "" or chars == "":
            return False

        firstPat = pattern[0]
        # now we explore pairing pattern[0]
        # with `n` first characters in `chars`
        for idx in range(len(chars)):
            # we take a slice from `chars`
            slice = chars[:idx + 1]
            # map it to the first character in pattern
            # but first check if that pattern exists
            # if it does `TODO`
            patternMap[firstPat] = slice
            # and continue the exploration, if it returns True
            # return True
            
            if self.explore(
                pattern[1:],
                chars[idx + 1:]
            ):
                return True
            
            # if not, remove the mapping
            # do we need to remove the mapping since it would be replaced in the next iteration?
            
            # well, since before adding a new pattern, we want to check if the pattern is present then yes
            
            # if we have a -> r
            # next iteration, we'd have a -> re
            # if we check that `a` is in the map....
        