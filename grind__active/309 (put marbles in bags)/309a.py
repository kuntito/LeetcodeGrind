# https://leetcode.com/problems/put-marbles-in-bags/

from typing import List

# what's the crack? we want to implement a function that takes two arguments
# a integer array, `weights` and and integer `k`

# the elements of `weights` represent the individual weight of each marble
# we want to divide the marbles into `k` bags according to the following rules

# no bag is empty, every bag should have at least one marble

# if the ith and jth marble are in a bag, then all marbles with indexes between the ith and jth indices should also be in that bag
# in english, if a bag contains more than one marble, the indices of the marbles should be consecutive.

# and lastly, if a bag consists of all the marbles with an index from `i` to `j` inclusively, then the cost of the bag is `weights[i] + weights[j]`
# in english, if the above rules are followed, any bag with more than one marble should cost weights[i] + weights[j], where `i` is the lowest indexed marble in the bag and `j` the highest indexed marble in the bag

# scratch that, even if the bag contains one marble,
# the score remains weights[i] + weights[j]
# where `i` and `j` are the lowest and highest indices respectively

# after said and done, we want to sum up the score of each bag
# and return the difference between the highest scores and the lowest scores

# in case, it wasn't said, we want to distribute the marbles such that we'd have the highest absolute difference

# we know that `k <= len(weights)`
# so we want to find the best way to distribute these marbles into `k` bags

# what really determines a high score? is that what we want?
# for maximum absolute difference, we want to find out the score of the largest bag
# after we've excluded the smallest bag

# check this,
# [1,3,5,1], k=2

# the smallest bag is definitely the smallest weight, i don't think there's a way around that
# the biggest bag would be the biggest thing outside of that
# biggest doesn't necessarily mean the widest range, you just need the largest `i` and `j`
# elements

# what if we determined the width of the largest bag
# and use a shrinking sliding window to parse through `weights`
# say the width of the largest bag is `3`

# we'd start with a window of `3`, calculate the score
# not too sure about this one

# what if we started with an elastic sliding window of size `1`
# we determine the score of that bag, our aim is to expand this window
# if we can have a higher score

# since we start at size `1`
# we can only expand the right pointer
# if the score is higher, we track the new score

# and expand once more, we keep expanding till we hit the maximum bag size
# once we do this we start shrinking

# do we shrink to size `1` or shrink one step at a time?
# the thing is.. a bigger score can exist inside the window
# so if we shrink one at a time, we can track the score?
# TODO not too sure about the shrinking, might need an example to illustrate the potential flaws in this logic..


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pass