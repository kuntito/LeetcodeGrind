# https://leetcode.com/problems/excel-sheet-column-title/

# so, following up from `d.py`

# i'm thinking in terms of buckets..
# each bucket can hold no more than 26 digits..

# once you hit 26.. you're at capacity..
# any additional number means you first have to address the max capacity
# you summarize all 26 digits into the next bucket..
# the next bucket is always to the left..

# the problem with this approach is it doesn't entirely map the truth..
# the first bucket is the one with a capacity of 26..

# the next bucket's capacity is 26x26..
# but each unit of 26 is mapped to `1`

# and subsequent buckets move in that direction too..
# the first bucket treats each unit as `1`
# the second bucket treats each unit of `26` as `1`
# the third bucket treats each unit of `26x26` as `1`

# each bucket increases to the power of `26` leftwards..
# so with this question.. how should i address this?

# when they give you a number, they're asking you to represent it using this split..
# yes, but what determines the split..

# do we start by deducting 26s?

# consider `27`.. how would you address this..
# i try to fit the whole thing into the first bucket..
# but this can't take more than `26`.. so what happens?

# it says, give the `26` to the next bucket, i'd take the `1`
# this example is too simple..


# how about `53`..
# first bucket says, this is more than i can handle..
# move `26` to the next bucket..
# we do that and we're left with `27`
# i still can't handle that.. 
# move another `26` to the next bucket..

# now, we're left with `1`
# okay, i can handle that.. so it takes the `1`

# hm.. the fog is lifing..

# problem

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        pass