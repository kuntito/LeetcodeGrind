# https://leetcode.com/problems/meeting-rooms/description/


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))

        for idx in range(1, len(intervals)):
            prev = intervals[idx - 1]
            curr = intervals[idx]

            if prev.end > curr.start:
                return False

        return True
