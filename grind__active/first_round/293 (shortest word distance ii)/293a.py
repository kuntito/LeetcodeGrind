# https://leetcode.com/problems/shortest-word-distance-ii/description/

# we want to create a data structure that is initialized with a group of strings
# we want to implement a method that takes two string arguments
# these strings are elements of the array the object is initialized with
# we want to find the shortest distance between these two strings

# the problem arises from string duplications
# consider the initial array, [cat, dog, rabbit, cat]
# if our two strings are "cat" and "dog"
# there's two ways to go about it but one is shorter than the other
# cat->dog
# OR
# dog->rabbit->cat

# i'd argue, we should note the indices of every word
# the shortest distance would be the two closest indices of any two words

# given a list of two integers, how do i find which ones are the closest?
# [2, 3]
# [4, 8]

# off the dome, i'd say explore every number in the smaller list??
# what if i put all the numbers in a list and denote them with start and end and i want to find the smallest window...

# i think i might be overcomplicating things here
# i'd start with exploring the shorter indices list
# for every number in there, explore forward till you hit another number
# so for [2, 3]
# i'd start with `2` and explore the next array [4, 8]
# the closest number is `4`, i'd track the distance
# then move to `3` and move forward

# this would work for this example, but what if it's just for this example
# for what it's worth, one index has to come first
# we don't know which so do we explore all of them
# well, we'd have to

# but what's the argument against moving leftwards, you only seem to be moving rightwards
# since we're iterating ltr, any number we can meet leftwards would have already been parsed
from collections import defaultdict


class WordDistance:
    def __init__(self, wordsDict: list[str]):
        self.wordMap = defaultdict(list)
        for idx, w in enumerate(wordsDict):
            self.wordMap[w].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        lsOne, lsTwo = self.wordMap[word1], self.wordMap[word2]

        smallest = float("inf")
        for idxOne in lsOne:
            for idxTwo in lsTwo:
                smallest = min(smallest, abs(idxTwo - idxOne))

        return smallest


arr = [
    ["practice", "makes", "perfect", "coding", "makes"],
]
foo = arr[-1]
sol = WordDistance(foo)

words = [
    ["makes", "coding"],
    ["coding", "practice"],
]
uno, dos = words[-1]
res = sol.shortest(uno, dos)
print(res)
