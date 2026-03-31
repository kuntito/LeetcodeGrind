# https://leetcode.com/problems/word-ladder/
from typing import List

# what am i doing here?
# i'm give three things..

# two strings and a list of strings.
# one string is `beginWord`
# the second string is `endWord`

# and the list of strings is `wordList`

# and what am i doing with these strings?

# i want to transform `beginWord` to `endWord`
# using the least amount of words from `wordList`

# what is this transformation?

# say,
# beginWord = "cat"
# endWord = "dab"

# and wordList is ["dat", "dab"]
# the way the transformation works is..
# each word can only transform into another word..

# if both words differ by one character.
# in our case, we can go from "cat" => "dat",
# the differing character is the first character 'c' & 'd'

# then we can go from "dat" to "dab",
# the differing character is "t" and "b"

# and the full transformaton is:
# cat => dat => dab
# there were three steps involved, and that's what we want to return
# the least number of transformations, it takes `beginWord` to become `endWord`

# in our case, there was only one transformation
# so our result was three by default
# but consider:

# wordList is ["dat", "dar", "dab"]
# another transformation could have been:
# cat => dat => dar => dab

# however, this would be longer than 3 steps.

# and note, the `beginWord` was not in `wordList`
# it could be.. but it doesn't have to..

# okay, so how would this go in code?
# i know it's a graph problem from last time.

# you want to create a graph of word list where
# the neighbors for each word are the words that differ by one character.

# start at begin word..
# then use a bread first search..
# what words can beginWord get to..
# are any of them `endWord`..

# keep going, tracking the steps taken until you find end word
# or run out of words.

# and how exactly would you run out of words..
# say you're at `cat`. want to get to `dab`
# but the only words in the list are [cat, mat]

# cat goes to mat, mat goes to cat, cat goes to mat..
# infinite recursion.

# okay, question says all words are unique..
# in this case, i can track the words i've seen.
# and this avoids the problem.

# and if i never find the endWord, i return `0`
# think, this'd be the default since, endWord if it exists.
# would be found within the loop

# so what variables do i need..
# `graph`, word => neighbors
# `seenWords`
# `steps`

# and how do you handle the begin word not being in the graph.
# just add it manually.. if it's there, it's no skin off your teeth
# graph is a hashmap

# i'd also need a variable to track the words in the next layer
# i'd call it `layer`

# error, the graph only creates entries for words in `wordList`
# in the event where `beginWord` is not in `wordList`
# we never get to compare it with other words in the list..
# and so the entry, while in the graph, remains, empty..

# the way around this would be add the `beginWord` to the graph..
# and add a check to ensure, you avoid a duplicate if it exists..

# this way, i no longer need to add to the graph from the jump
# i made this mistake cause i'm tired.. apparently, i can't work all day
# even if i wanted to..

# okay.. it seems to work
# and as i sorta expected, TLE
# need to rewrite.. TODO

# the limiting factor is the graph construction.


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:
        graph = self.getWordGraph(beginWord, wordList)
        
        # what's the while condition..
        # while there's cells to explore.. in layer
        
        steps = 0
        seen = set()
        layer = [beginWord]
        while layer:
            steps += 1
            # so what do you do..
            # create `nextLayer`
            # explore every word in `layer`
            # add their neighbours to next layer..
            # after iteration..
            
            # layer = nextLayer
            # how do you address finding the solution..
            # it would be during the iteration of layer
            # if any of the words is `endWord`, return steps
            
            # also, each word is added to seen during the layer iteration
            nextLayer = []
            for wd in layer:
                if wd == endWord:
                    return steps
                
                if wd in seen: continue
                
                seen.add(wd)
                
                nextLayer.extend(graph[wd])
                
            layer = nextLayer
                
        return 0
    
    def getWordGraph(self, beginWord, wordList):
        # what am i doing here..
        # for one, create the graph variable..
        
        graph = {}
        
        # add `beginWord` in case, it's not in `wordList`
        # and if it is.. add a condition in the iteration to skip the duplicate
        wordList.append(beginWord)
        
        # now what..
        # for each word, you want to find out all other words with which it differs by `1`
        
        # does this mean, i have to compare every word with every word?
        # let's do that first, if it doesn't work, make it efficient..
        
        # for each word, we'd explore every other word..
        # if they differe by 1 character, make an entry for both words in the graph
        
        # i.e. wordA => [wordB], wordB => [wordA]
        
        dim = len(wordList)
        for idxOne in range(dim):
            wdOne = wordList[idxOne]
            
            # we added `beginWord` cause it might not be in `wordList`
            # if it turns out it is.. then we should skip the duplicate..
            if wdOne == beginWord and beginWord in graph:
                continue
            
            if wdOne not in graph:
                graph[wdOne] = []
                
            for idxTwo in range(idxOne + 1, dim):
                wdTwo = wordList[idxTwo]
                if wdTwo not in graph:
                    graph[wdTwo] = []
                    
                if self.isDifferByOne(wdOne, wdTwo):
                    graph[wdOne].append(wdTwo)
                    graph[wdTwo].append(wdOne)
                    
        return graph
    
    
    def isDifferByOne(self, wdOne, wdTwo):
        diff = 0
        
        for chOne, chTwo in zip(wdOne, wdTwo):
            if chOne != chTwo:
                diff += 1
                
            if diff > 1:
                return False
            
        return diff == 1
                
            
arr = [
    [
        "hit",
        "cog",
        ["hot","dot","dog","lot","log","cog"],
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.ladderLength(foo, bar, baz)
print(res)