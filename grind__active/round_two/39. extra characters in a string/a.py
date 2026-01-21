# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List

# i'm given two things..

# a string, `s` and an array of strings, `strArr`
# i want to return an integer, but what does that integer represent?

# let's start with a back story.. the list, `strArr`, may contain words
# that exist in the string, `s`, let's call these words, `presentWord`s

# for instance:
# s = "applebee"
# strArr = ["apple", "mango"]

# there's only one `presentWord` here, "apple"
# it exists in `strArr` and also in `s`

# our way to describe our job is to return the number of characters left in `s`
# after we remove all the `presentWord`s

# more, accurately, we want to return the minimum number of characters left in `s`
# after we remove the non-overlapping `presentWord`s..

# but what does this mean? let's start with non-overlapping.
# consider:

# s = "obscene"
# strArr = ["scene", "obsc"]

# now, in this case, both words in `strArr` are `presentWord`s
# they both exist in `s`, however, they overlap.

# in this case, i can only remove one of them.

# if i remove `obsc` from `obscene`, i'm left with `ene` (3 characters)
# if i remove `scene` from `obscene`, i'm left with `ob` (2 characters)

# it's apparent, removing `scene` gives us the lower number of characters
# so in this case, our answer is `2`.

# so that's the task.

# but how do we solve it. off the dome, i'd say..
# every character in `s` represents the start of a word, but which one..
# we'd just have to check innit?

# what, for each character, check if every word in `strArr`?
# well, we could, but intuition is screaming suboptimal..

# another way is.. recursion..
# why recursion?

# consider:
# s = "leetscode"
# strArr = ["lee", "leet", ...]

# there's two `presentWord`s that begin `s`
# but we don't know which one leads to the minimum characters left
# so we'd have to try both..

# say we track characters from the get go, moment we find `lee`
# we start a recursive call with the rest of `s`, i.e. `tscode`
# now, we're back to the starting point.. repeat the same logic
# track characters from the start of `s`

# i mean, i see the point.. in the parent call, we hit `lee`, start recursive call
# we hit `leet` start recursive call..


# how do you address the .. what if the words don't start at the beginning of `s`
# consider:
# s = "aleetscode"
# strArr = ["lee", "leet", ...]

# how would you address this.. 

# this is crazy.

# sounding like the first iteration is over every character
# from the start of every character, we track all characters, if we find a match in `strArr`
# start recursive call..

# also, `strArr` should be turned into a set, question says the words are distinct,
# and the set allows us check in O(1) time..

# nonethess, start from every char
# if find word, start recursion, but how do you calculate the minimum chars left after exploration
# i think you can track the length of every found word..
# sum it up along each path
# and return to the parent..

# so the parent knows how many characters were found along this path

# let's try it out with

# s = "aleetscode"
# strArr = ["lee", "leet", ...]

# we run through every character in `s`
# starting with `a`
# we do:

# `a`
# `al`
# `ale`
# `alee..`
# we keep going and find no hits.. so we move to 

# `l`
# `le`
# `lee`, our first hit, the we start recursion
#     now, s = `tscode`
#         then we do what we did at the start
#         every character in `tscode`, 
#         we find nothing until we hit `c`, which ends up being `code`

#     this the most clunky algorithm, i ever wrote..
#     would we benefit from memoization?

#     well, yes..
    
# since at every character we want to find the same thing.
# track every substring starting with the first character
# and every other character after..

# i.e if word is "apple"
# check, `a`, `ap`, `app`

# technically, we could just do this without recursion, at least for a start.
# the first task is for every character, find out how many words start here..

# once, we have that we can now use recursion
# say we did that for `aleetscode`
# and we had the mapping, each char => words that begin there..

# we'd immediately know at `a`, there are no words that begin here.
# and so, we can disregard it.

# at `l`, we know there's two words that start here..
# `lee` and `leet`

# now, this is where it gets interesting.
# using the length of `lee`
# we immediately know the next substring to address is `tscode`
# but because we've cached each character to number of words..

# we know the words that begin with `t`.. if there's none, proceed to..


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        pass