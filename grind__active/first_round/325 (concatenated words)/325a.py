# https://leetcode.com/problems/concatenated-words/

from typing import List

# what's the situation?

# i'm given a list of strings.
# every string in the list is unique.

# from the list,
# i want to find and return the concatenated words

# but what is a concatenated word?
# it's a word in the list that's made up two or more smaller words

# i.e. ["pep", "si", "pepsi"]
# "pepsi" is a concatenated word, it's made from "pep" and "si"

# the smaller words can be repeated
# i.e. ["pa", "papa"]
# "papa" is a concatenated word that's made up of two "pa"'s

# now, that i understand the question
# how do i solve it?

# how do i find out a word can be made up of two smaller words
# i've got an idea

# consider the "pepsi" example
# i'd explore every starting substring in "pepsi"

# i.e. "p", "pe", "pep"...
# the idea here is every starting substring can represent a word in the array
# to find out if the word is in the array, i'd beforehand place the words in a set
# the moment i find a word in the array,

# i'd restart the process, this is giving recursion
# for the "pepsi" example, the first word that'd be in the array would be "pep"

# at this point, i'd restart the process with the rest of the word i.e. "si"
# i'd explore every starting substring, "s" and then "si"
# i'd find out "si" is in the array, and explore the rest of the word

# in this case, i'd end up with ""
# meaning i've explored the entire word
# and return False

# this should work but the base case looks dodgy.
# let's say the main word i explored was "pep" not "pepsi"

# i'd check every starting substring
# "p", "pe" and "pep"
# at "pep" i'd find a word in the array and check the rest of the words
# in which case, i'd end up with a blank string indicating the base case
# but i would be wrong, since a concatenated word requires two or more smaller words
# and in this case, i've only explored one


# i think every recursive call should have a count
# the number of subwords so far
# the edge case that returns true is a blank string and a count > 1

# this works well enough for the test cases and on submission runs into TLE
# quite understandably. how to optimize?

# for one, i could memoize seen words
# write in another file...
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.allWords = set(words)

        res = []
        for w in words:
            if self.explore(0, w):
                res.append(w)

        return res

    def explore(self, count, word):
        if count > 1 and word == "":
            return True

        dim = len(word)

        count += 1
        for idx in range(dim):
            endIdx = idx + 1
            substr = word[:endIdx]
            if substr in self.allWords:
                if self.explore(count, word[endIdx:]):
                    return True

        return False


arr = [
    [
        "cat",
        "cats",
        "catsdogcats",
        "dog",
        "dogcatsdog",
        "hippopotamuses",
        "rat",
        "ratcatdogcat",
    ],
    # ["pep", "si", "pepsi"],
]
foo = arr[-1]
sol = Solution()
res = sol.findAllConcatenatedWordsInADict(foo)
print(res)
