# https://leetcode.com/problems/meeting-rooms-iii/description/

from typing import List

# right, what we doing here?
# i'm given two things.

# an integer, `n`
# and a 2d integer array, `meetings`

# each meeting is represented by [start, end]
# these are the elements of `meetings`

# `n` is the number of meeting rooms available.

# so what are we doing with these?

# every meeting occurs in a meeting room.
# the way the rooms are assigned is this..

# the unused room with the lowest number
# becomes the venue for the next available meeting.

# think of the meeting rooms ordered in a row
# the rooms are numbered from `0` up till `n-1`

# if n is 2, the available rooms are
# room 0 and room 1

# when all rooms are occupied and there are still meetings..
# we wait until one of the rooms becomes available.

# following these rules, i want to return the room
# that held the most meetings.

# how would this go?

# a heap for meeting rooms?
# each heap item is the (roomNumber, meetingEnd)

# also, worth pointing out, each meeting interval, (start, end)
# is exclusive of the `end`

# in clearer terms, the meeting starts at `start` but ends just before `end`
# so if another meeting starts as the same time as `end`
# that meeting can happen in the same room.

# right, back to heap.
# a heap for meeting rooms, (roomNumber, endTime)
# initially, all end times are `0`, `0`

# so we pop from the heap to get the smallest available room
# we get roomNumber, and endTime

# we check if our next available meeting is can start at this time..
# if it can, we add the room back to the minHeap.

# this reveals one problem.. you can't place rooms in the min heap
# by (roomNumber, endTime)

# you want to always get the room whose meeting ends first
# so should priortize endTime i.e. (endTime, roomNumber)

# okay.. how do i guarantee, the first case gives me room 0
# i think Python's minHeap inherently sorts items like this..

# if you have (0, 0), (0, 1) in the minHeap
# it would sort the heap items by the second value, since the first values are equal

# so this ensures the lower room number is always preferred.
# so this way we can assign rooms to meetings..

# let's not forget the goal of the question
# we want to know what room holds the most meetings..

# we could create a map of `roomNumber => usageCount`
# and would update this every time, we add a meeting to a room.

# at the end, we could iterate through this map,
# let's call it `roomUsage` and return the highest occuring room.

# if there's a tie, we should return the room with the lower number
# to be fair, we could track this as we add items to each room.

# set a variable, `mostUsedRoom`
# and update as necessary.

# what if we have a meeting and all our rooms are occupied.
# well, the meeting would have to pick the next available room from the heap.

# in reality, the meeting would have waited but as far as the code is concerned.
# we always want to pick the room on top the heap.

# the wait time is invisble. if a meeting is (3, 5)
# and the minHeap has (8, 0)

# that is, next meeting to end, ends at `8`
# or rather, the room becomes available at `8`

# it would mean `(3, 5)` has to take that room.
# elephant in the room.. `3` is after `8`

# this would mean the meeting was delayed.
# there was only one meeting room and it was being used.

# the (3, 5) would have to be updated.
# current time is `8` and so the new meeting time
# becomes (8, 10)

# the top of the minHeap always determines the current time.
# if the next meeting has a lower time, it means the meeting was delayed.

# and we should update it's intervals.

# all the meeting start times are unique.
# i don't know what use this info serves but let's see how it goes.

# create a minHeap for the rooms..
# append each room (availableTime, roomNumber)
# initialize available time to `(0, roomNumber)`

# then-
# it's not stated if the meetings are sorted by start time but that's
# a good thing to ensure..

# create a map to store room and it's usage, `roomUsageMap`

# initialize the variable, most used room
# and update on every entry to `roomUsageMap`

# then iterate through each meeting, assigning it to a room
# update the `roomUsageMap`

# error, i didn't re-add room to minHeap
# after adding a new meeting.

# i think it happened cause i got caught up the logic
# of updating the most used room..

# and when i was done, i just wanted to submit,
# not realizing i wasn't done.

# perhaps, this is why hard questions get their reputation.
# there's several considerations one has to make in tandem.

# error, didn't sort meetings from the jump.
# even though i'd written it in the breakdown.

# again, several considerations.

# lastly, the code fails with this case..
# `[[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]`

# my code returns `2` as the most used room
# since end time, `10` is the one that finishes first.
# however, when closely inspected..

# the last meeting [18, 19] starts at time `18`
# at this point all three meetings

# [2, 13], [3, 12] and [7, 10]
# would have ended..

# and i by extension, i'd have to pick the room the lowest number
# room `0`

# my code doesn't account for this type of situation.

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)
        
        roomUsageMap = {}
        mostUsedRoomNum = 0
        
        minHeap = [(0, roomNumber) for roomNumber in range(n)]
        
        heapq.heapify(minHeap)
        
        for startTime, endTime in meetings:
            naStartTime, naRoomNumber = heapq.heappop(minHeap)
            
            # if the current meeting should have started before
            # the next available start time, we should update it's end time
            # to reflect the new duration
            if startTime < naStartTime:
                duration = endTime - startTime
                endTime = endTime + duration
                
            roomUsageMap[naRoomNumber] = roomUsageMap.get(naRoomNumber, 0) + 1
            
            newRoomUsage = roomUsageMap[naRoomNumber]
            currMostUsedRoomUsage = roomUsageMap[mostUsedRoomNum]
            
            # update most used room..
            # if the new room has a usage higher than what we have
            # update..
            if newRoomUsage > currMostUsedRoomUsage:
                mostUsedRoomNum = naRoomNumber
            
            # if the new room has the same usage as what we have
            # but has a lower room number, update
            elif newRoomUsage == currMostUsedRoomUsage and naRoomNumber < mostUsedRoomNum:
                mostUsedRoomNum = naRoomNumber
                
            
            heapq.heappush(
                minHeap,
                (
                    endTime,
                    naRoomNumber
                )
            )
                
        return mostUsedRoomNum
    
arr = [
    [
        4,
        [[18,19],[3,12],[17,19],[2,13],[7,10]],
    ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.mostBooked(foo, bar)

print(res)