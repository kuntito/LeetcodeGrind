# https://leetcode.com/problems/edit-distance/description/

# given two strings, i want to find the minimum number of operations i can perform on the first string to turn it into the second string.

# an operation is of three types:

# insertion
# deletion
# replacement

# insertion means you insert a character anywhere in the string
# deletion, delete a character anywhere in the string
# replacement, replace any character in the string

# given these rules, what's the least amount of operations
# i'd need to perform on the first string to turn it into the second string

# take "horse" and "ros"

# my first intuition is find the longest common subsequence between
# words, then find out what you need to remove or replace.

# my previous write up suggests my intuition is wrong but i have long since
# forgotten why and so, i'd try again..

# let's go..
# longest common subsequence, this is a leetcode problem
# and i do not recall how to solve it but let's walk through it

# "horse"
# "ros"

# since i'm pitting the first string against the second, it makes sense to see...

# hold up, what exactly is a sequence
# inside a string, a sequence is set of characters that follow each other
# but not necessarily after one another

# so how do i find the longest common sequence between two strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass