# https://leetcode.com/problems/find-the-town-judge/

from typing import List

# i'm given two things, an integer, `n`
# and a 2d array of integers, `trust`

# i'm told the number, `n` represent distinct people in a town.
# each person is numbered between `1` and `n`, `n` inclusive.

# a rumour exists, of all the towspeople, one of them is a judge.
# we want to find this judge and return his number.

# but how? that's where the 2d array comes in, `trust`

# what is `trust`, a 2d array of integers.
# yes, but what does it represent?

# each element of trust is like [a, b]
# `a` represents the number of someone in the town
# `b` represents another person.

# the element [a, b] indicates that person `a` trusts person `b`
# okay.. so how does this help us find the judge?

# the judge trusts no one.
# also, the judge is trusted by everyone.

# okay.. that helps simplifies things.
# so, we want to find the guy that trusts no one but is trusted by everyone.

# we'd need some way to collate all the trusted relationships.
# an dictionary, where the key is the persons number.

# the value is an array of trustees

# as an optimization, i'd create a set of every one, `candidates`.
# while populating the trustees dictionary, 
# i'd remove each person that has trustee from candidates

# why? if they trust someone, they can't be the judge
# okay, so whoever is left in `candidates` must be the judge

# not quite, whoever is left, is then filtered for who is trusted by everybody.
# sounding like another dictionary is in order, `clout`

# what's this, for each trusted person, i want to increase their clout by `1`
# so at the end of the populating, candidates.

# i'd know the people that have no trustees and i can check their clout.
# if their clout == n, voila.. else return `-1`

# to be fair, i don't even need a `trustees` dict
# i just need `candidates` and `clout`

# made an error with this check `if their clout == n, voila.. `
# the judge is trusted by everyone but himself, so their clout should be `n-1` not `n`

# another error, it's possible a candidate has zero clout
# in this case

# when we check, `clout[c] == n-1`, we'd get a key error
# a default dict simply solves this? or `dict.get()` method

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        clout = {}
        candidates = set(range(1, n + 1))
        
        for arr in trust:
            a, b = arr
            
            if a in candidates:
                candidates.remove(a)
                
            clout[b] = clout.get(b, 0) + 1
            
        for c in candidates:
            cloutCount = clout.get(c, 0)
            if cloutCount == n - 1:
                return c
        
        return -1

arr = [
    [2, [[1, 2]]]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findJudge(foo, bar)
