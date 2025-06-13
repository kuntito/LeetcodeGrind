# https://leetcode.com/problems/text-justification/description/

from typing import List

# i want to implement a function called `fullJustify`.
# this function takes two arguments,
# a string array, `words` and an integer `maxWidth`
# this returns a list of strings

# what we want is to take each word in the input array, `words`
# and increase it's length to `maxWidth`

# and return a list of all increased words.
# but how do we increase the length, by adding spaces.

# however, we don't just add the spaces.
# there's a pattern to the madness.

# i've misunderstood the question. we're given a list of words and want to concatenate them and turn them into a paragraph.

# a paragraph where each line is `maxWidth` in length
# consider,

# ["This", "is", "an", "example", "of", "text", "justification."]
# to turn this into a paragraph
# we need to place `n` words on a line.
#
# since we can't exceeed `maxWidth` per line
# each line can only contain words whose total length don't exceed `maxWidth`
# the total length should factor in the space between words
# there should be at least one space between each word.

# for our example
# the first line would contain "This ia an"
# the break down is

# "This" - 4
# " " - 1
# "is" - 4
# " " - 1
#  "an" - 2

# total count = 4 + 1 + 4 + 1 + 2 = 12

# TODO mistake, i've said "is" - 4 instead of `2`
# but the argument stands

# the next word would have been "example" - 7
# this would take the total count to 18
# the space and the word
# (" " + "example")

# so we know the first line only contains three words
# we do the same logic for the next words and we keep going
# till we exhaust the words in the input array

# once we have this, we'd use a helper function to justify each word
# we want to maximize the space between each word
# we can determine the total word len
# as in, the sum of all the words on a line
# and find out how much space is left

# and then divide the space accordingly between words
# consider: "This is an"
# the total word length is `8`, `maxWidth` is `8`
# and so the space is `8`

# since there are `3` words
# there would be `n-1` spaces,
# a space between each word
# it's convenient to split `8` into `2`
# so that works

# what if the total space was `9`
# and i had `2` slots
# the idea would be to do an integer division
# totalSpace//numberOfSlots

# this would tell you the minimum space between each word
# the remainder would be overflow
# we'd add the remainder to each space
# one at a time

# consider our example, 9 spaces, 2 slots
# 9 // 2 = 4

# each space would be at least `4`
# the total remainder is `1`

# while concatenating the words
# and appending the spaces, left to right,
# i'd add `1` to each space, and decrement the total remainder

# in this case, i'd have "This", followed by 4 spaces + 1 of the remainder
# i'd decrement the remainder and it'd become 0

# then i'd add "is", followed by 4 spaces
# since total remainder is exhausted, i'd add the last word


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        pass

        lines = []

        # i need the words for each line
        arr = []
        totalCount = 0
        for w in words:
            spaceCount = 1 if arr else 0
            nextLen = spaceCount + len(w)

            # if adding the next word causes overflow
            # append the line to `lines` and start a new line
            if totalCount + nextLen > maxWidth:
                lines.append(arr[::])
                arr.clear()
                totalCount = 0

                # decrement space count
                # since there's no space before the first word
                # on a new line
                nextLen -= 1

            arr.append(w)
            totalCount += nextLen

        lines.append(arr)

        res = []
        for idx, ln in enumerate(lines):
            if idx + 1 == len(lines):
                res.append(self.justifyLast(ln, maxWidth))
            else:
                res.append(self.justifyLine(ln, maxWidth))
                
        return res
            

    def justifyLast(self, words, maxWidth):
        space = " "
        
        words = space.join(words)
        
        rightPadding = maxWidth - len(words)
        
        return words + (space * rightPadding)
        


    def justifyLine(self, words, maxWidth):
        totalWordsLen = sum(len(x) for x in words)
        totalSpaces = maxWidth - totalWordsLen

        gaps = len(words) - 1
        print(words)
        # if gaps == 0:
        #     if totalSpaces:
        #         words.append(" " * totalSpaces)
        #     # print(words)
        #     return "".join(words)

        minSpace, remainder = divmod(totalSpaces, gaps)
        # print(minSpace, remainder)

        justifiedArr = []
        for w in words:
            if justifiedArr:

                extra = 1 if remainder > 0 else remainder
                if remainder:
                    remainder -= 1

                space = " " * (minSpace + extra)
                justifiedArr.append(space)

            justifiedArr.append(w)

        # print(justifiedArr)
        return "".join(justifiedArr)


arr = [
    [["This", "is", "an", "example", "of", "text", "justification."], 16],
    [["What", "must", "be", "acknowledgment", "shall", "be"], 16],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.fullJustify(foo, bar)

for x in res:
    print(x)
