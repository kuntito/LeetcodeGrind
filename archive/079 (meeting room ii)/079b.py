# https://leetcode.com/problems/meeting-rooms-ii/description/

# https://neetcode.io/solutions/meeting-rooms-ii
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        startTimes = sorted(x.start for x in intervals)
        endTimes = sorted(x.end for x in intervals)

        i, j = 0, 0

        maxClashes = 0
        clashes = 0
        while i < len(startTimes):
            currStartTime = startTimes[i]
            nextEndTime = endTimes[j]

            if currStartTime < nextEndTime:
                i += 1
                clashes += 1
            else:
                j += 1
                clashes -= 1
            maxClashes = max(clashes, maxClashes)

        return maxClashes
            
        
arr = [
    Interval(0, 40),
    Interval(5, 10),
    Interval(15, 20),
]

# arr=[Interval(1,5),Interval(5,10),Interval(10,15),Interval(15,20),Interval(1,20),Interval(2,6)]

sol = Solution()
res = sol.minMeetingRooms(arr)
print(res)