# https://leetcode.com/problems/count-the-number-of-k-free-subsets/description/

from typing import List


# what's the situation? i want to implement a function that takes two arguments,
# and returns an integer.

# the two arguments are an integer, `k` and an integer array, `nums`

# all the elements of `nums` are unique. our job is to count the number of subsets
# of `nums` that meet a given criteria.

# for all subsets, the criteria is no two elements in said subset can have an absolute
# difference equal to `k`

# what is a subset? any combination of integers from `nums`
# consider, [1, 2, 3]
# the following are subsets, {1}, {}, {1, 3}

# so how would this work? for starters, we know an empty set is part of the subset
# we know all single digits are part of the subset.

# so we are only concerned with subsets, rather, we only need to check subsets
# with two or more elements.
class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        pass