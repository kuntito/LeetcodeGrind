# https://leetcode.com/problems/meeting-rooms-ii/description/

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals = [(i.start, i.end) for i in intervals]
        intervals.sort()

        count = 0
        seen = set(intervals)

        while seen:
            start_idx = self.get_first_meeting_idx(seen, intervals)
            prevMeeting = intervals[start_idx]

            idx = start_idx + 1
            while idx < len(intervals):
                currMeeting = intervals[idx]

                if currMeeting in seen and prevMeeting[1] <= currMeeting[0]:
                    seen.remove(prevMeeting)
                    prevMeeting = currMeeting
                idx += 1

            seen.remove(prevMeeting)
            count += 1

        return count


    def get_first_meeting_idx(self, seen, intervals):
        for idx in range(len(intervals)):
            if intervals[idx] in seen:
                return idx
            
        
arr = [
    Interval(0, 40),
    Interval(5, 10),
    Interval(15, 20),
]

arr=[Interval(1,5),Interval(5,10),Interval(10,15),Interval(15,20),Interval(1,20),Interval(2,6)]

sol = Solution()
res = sol.minMeetingRooms(arr)
print(res)