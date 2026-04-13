# https://leetcode.com/problems/meeting-rooms-iii/

from typing import List

# i have some meeting rooms.
# and have some meetings to assign to these rooms.

# the meeting rooms are ordered from zero upwards.

# starting at room zero, i want to assign meetings
# starting with the earliest meeting.

# if i run out of rooms.
# i wait till a meeting ends so the next available meeting is held in that room.

# this goes on until all meetings have been held.

# my job is to return the room that held the most meetings.

# and the code?
# for one, `i need to sort the meetings by start time`.
# then allocate each meeting one by one.

# and if i run out rooms?
# i wait for the next available room.

# for this, `i need to know what meeting ends next`

# and when done, how do i know which room held the most meetings?

# hashmap.

# i'd call it `roomUsage`

# notes:
# i'm given two variables.
# an integer,`n`, representing the total number of rooms.
# a 2d integer array, `meetings`, 
#   where each element represents the `start` and `end` intervals for each meeting

# the meeting starts at `start` and ends at `end-1`

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomUsage = {}
        
        # sorting meeting by start time.
        meetings.sort(key=lambda x: x[0])
        
        # what would i initialize the min heap as..
        # each element is when (timeRoomIsAvailable, roomNumber)
        
        # at the start, all the rooms are available..
        # how do i denote this? 0?
        
        # yeah, that works.
        # since every meeting starts at zero or after it.
        roomHeap = [(0, roomNumber) for roomNumber in range(n)]
        
        # do i need to heapify this or (0, 0) stays on top?
        # why not be safe?
        heapq.heapify(roomHeap)
        
        for mt in meetings:
            startTime, end = mt
            
            # now i want to assign this meeting a room
            # i need to know the next available room
            # how do i know that?
            
            # a heap lends itself nicely to this problem.
            # a min heap, where each element is (timeRoomIsAvailable, roomNumber)
            
            # so i need a heap.
            # a min heap that stores every room.
            
            # now the topmost element in `roomHeap` is the next available room.
            # what do i want to do with this?
            
            # i'd grab the next available room.
            # however, there's a problem i found on my last attempt.
            
            # the next available room isn't the only condition.
            # if two rooms are available, i want to pick the room with the smaller number.
            
            # consider a situation where the next meeting starts at `7`
            # and the roomHeap contains two items [(5, 1), (6, 0)]
            
            # room 1 is available at time 5
            # room 0 is available at time 6
            
            # both rooms are available before `7`, the next meeting start time.
            
            # in this case, i'd want to pick room 0 because it has the smaller number.
            # but the way, i've described my approach.
            
            # i'd be picking room 1 first.
            # since it's at the top of the heap.
            
            # the revision, 
            # the next available room is a function of the time of the next meeting.
            
            # this should be it's own function.
            # and it should take meeting `startTime` as an argument.
            # it should also take `roomHeap` as an argument.
            
            nextMeetingStartTime, nextAvailableRoom = self.getNextAvailableRoom(startTime, roomHeap)
            
            # now, i update the room's usage..
            roomUsage[nextAvailableRoom] = roomUsage.get(nextAvailableRoom, 0) + 1
            
            # then what..
            # i want to note when the room next becomes available..
            # and how do i do that?
            
            # i'd add to the heap,
            # (timeMeetingStarts + duration, roomNumber)
            
            # and how do i get the time the meeting starts?
            # startTime? not always.
            
            # consider a situation.
            # one meeting room
            # two meetings.
            # the first meeting starts at 2, ends at 4
            # the second meeting starts at 3 ends at 5
            
            # the only room is room0
            
            # based on the current logic,
            # i'd note when the room next becomes available..
            # in this case, the room next becomes available at time `4`
            
            # at this point, the next meeting can start.
            # however, the next meeting should have started at `3`
            # but starts at `4` since we had to wait for an available room.
            
            # so the start time of the next meeting is the time the room becomes available.
            # not the start time of the meeting.
            
            # and how do we know the time the room next becomes avaialable?
            
            # `getNextAvailableRoom` should return two things..
            # the time the room is available, and the room number
            
            # now, we can update the `roomHeap`
            # with when the room next becomes available..
            
            meetingDuration = end - startTime
            heapq.heappush(
                roomHeap,
                (
                    nextMeetingStartTime + meetingDuration,
                    nextAvailableRoom
                )
            )
            
    def getNextAvailableRoom(self, startTime, roomHeap):
        pass
        # based on the room availabilities in `roomHeap`
        # what's the smallest roomNumber a meeting that starts at `startTime` can use?
        # TODO start here..
