# https://leetcode.com/problems/word-ladder-ii/description/

from collections import defaultdict
from typing import List

# i want to implement a function called `findLadders`.
# the function takes three arguments, 
# two strings and one string array, and returns a 2d array of strings.
# 
# the two strings are called `beginWord` and `endWord`
# and the string array is `wordList`

# i want to transform `beginWord` into `endWord`
# by changing one character at a time until i arrive at `endWord`

# for example,
# `beginWord = cat`
# `endWord = bag`

# one possible transformation is "cat => bat => bag"
# we want to return all the words involved in the transformation

# i.e. ["cat", "bat", "bag"]

# but all words involved must exist in `wordList`
# the only exception is `beginWord`
# `beginWord` is the only word that can be part of the transformation
# and not in `wordList`

# this can be reworded for clarity but... i've gotten the message
# it's looking like a graph problem

# where every word is a node and has edges to other words that differ by one character
# at this point, it becomes a path exploration problem
# given a graph of words, find and return the different ways you can get from `beginWord` to `endWord`


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        pass
    
        graph = self.getGraph(wordList)
        
        
    def getGraph(self, wordList):
        pass
        graph = defaultdict(list)
        
        # now, how to get the graph?
        # i think for each word, i'd have to explore every other word
        # except itself and check if they differ by one character
        # memoization could help speed things up here
        
        for idxOne, wordOne in enumerate(wordList):
            for idxTwo, wordTwo in enumerate(wordList):
                if idxOne == idxTwo: continue
                
                if self.isDifferByOne(wordOne, wordTwo):
                    graph[wordOne].append(wordTwo)
                    graph[wordTwo].append(wordOne)
                    
        return graph
                    
    def isDifferByOne(self, wordOne, wordTwo):
        diff = 0
        
        for chOne, chTwo in zip(wordOne, wordTwo):
            if chOne != chTwo:
                diff += 1
                
            if diff == 2:
                return False
            
        return diff == 1