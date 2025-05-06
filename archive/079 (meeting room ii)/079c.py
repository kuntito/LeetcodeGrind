# https://leetcode.com/problems/meeting-rooms-ii/description/

# https://neetcode.io/solutions/meeting-rooms-ii
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        pass
        # to clarify, we're given a set of meeting intervals
        # start and end times
        
        # it's not stated so i'd ask, can each conference room host more than one meeting?
        
        # is there a limit to conference rooms?
        # not really, when they say minimum, the idea is that we don't want to use more conference rooms than is necessary
        
        # if certain meetings occur at the same time or clash, they'd have to have different conference rooms
        
        # the way i'd go about this, is to sort the meetings by start time
        # i want to start the earliest meeting first and keep track of how many conference rooms i've used so far
        
        # i'd also keep track of the end time of the meeting
        # moving to the next meeting, can it use the current room, well we compare it's start time to the current meeting's end time
        
        # and if there's a clash, we use another room.
        # else we use the same room and keep track of that meeting's end time
        
        # two scenarios now, one where we use the same room and another where we use another room
        
        # if we use the same room, it's essentially the same state but a different current end time
        
        # but if we use a different room, we now have to keep track of two different end times, but which is important, we want to use the least conference rooms as possible so if a meeting has ended, we want to use that same room
        
        # i suggest a heap based on endTimes, this way we know the earliest end time
        # and can compare next meetings to it
        
        # i think if we track the largest size of the heap `endTimes`, we know the most rooms used at once
        
        intervals.sort()
        endTimes = []
        
        minRooms = 0
        for start, et in intervals:
            # et = meet.end
            # start = meet.start
            pass
            # if this meeting starts after the least end time, 
            # remove that end time and add this meeting's end time
            # also add this meeting's end time, if heap is empty
            
            # i'm not clear on the logic
            # if endTimes is empty, add new end time
            if not endTimes:
                heapq.heappush(endTimes, et)
            elif start >= endTimes[0]:
                heapq.heappop(endTimes)
                heapq.heappush(endTimes, et)
            else:
                heapq.heappush(endTimes, et)
            
            minRooms = len(endTimes)
            # if this meeting starts before the least end time, add the meeting's end time
            
        return minRooms
        
arr = [
    Interval(0, 40),
    Interval(5, 10),
    Interval(15, 20),
]

# arr=[Interval(1,5),Interval(5,10),Interval(10,15),Interval(15,20),Interval(1,20),Interval(2,6)]

sol = Solution()
res = sol.minMeetingRooms(arr)
print(res)