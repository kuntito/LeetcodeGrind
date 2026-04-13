# https://leetcode.com/problems/meeting-rooms-iii/

from typing import List

# i'm given two things.

# an integer, `n`
# and an array, `meetings`

# each elements of `meetings` is an array, an array of integers.

# i'm given two things.
# an integer, `n`
# and a 2d array of integers, `meetings`.

# each element of `meetings` is [start, end]
# where `start` and `end` represent the  duration of a meeting.

# `end` is not inclusive 
# i.e. the meeting starts at `start` and ends at `end-1`


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        pass