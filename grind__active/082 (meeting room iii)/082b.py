# https://leetcode.com/problems/meeting-rooms-iii/description/
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        pass
        # you want to pick the next available meeting
        # and place it the smallest available room
    
        # start with the first meeting
        # find a room for it
        # does the meeting finish in time for the next meeting
        # if yes, put the next meeting in that same room
        
        # a heap to store (endTime, roomIdx)
        
        # as you iterate through the meetings
        meetings.sort()
        
        
        usedRooms = [0 for i in range(n)]
        
        availableRooms = [i for i in range(n)]
        heapq.heapify(availableRooms)
        
        ongoing = []
        
        currTime = meetings[0][0]
        for idx, meet in enumerate(meetings):
            startTime, endTime = meet
            
            # if any of the current meetings finish in time for this
            # meeting, free up the room
            maxEnd = self.free_rooms(startTime, ongoing, availableRooms)
            if isinstance(maxEnd, int):
                currTime = maxEnd
                
            # TODO how do you keep track of the current time
                
            duration = endTime - startTime
            endTime = currTime + duration
        
            # this picks the smallest available room
            roomIdx = heapq.heappop(availableRooms)
            usedRooms[roomIdx] += 1

            
            
            heapq.heappush(ongoing, (endTime, roomIdx))
        
            # if the current meeting ends in time for the next meeting
            # free the room
            
        print(usedRooms)
            
    def free_rooms(self, nextStart, ongoing, availableRooms):
        maxEndTime = None
        
        while ongoing and ongoing[0][0] <= nextStart:
            endTime, roomIdx = heapq.heappop(ongoing)
            
            heapq.heappush(availableRooms, roomIdx)
            if maxEndTime is None:
                maxEndTime = endTime
            else:
                maxEndTime = max(endTime, maxEndTime)
                
        return maxEndTime

            
    
    
    
arr = [
    [2, [[0,10],[1,5],[2,7],[3,4]]],
    [4, [[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]],
    [3, [[1,20],[2,10],[3,5],[4,9],[6,8]]],
    [2, [[0,10],[1,5],[2,7],[3,4],[8,11],[9,12]]],
]
foo, bar = arr[-1]


sol = Solution()
res = sol.mostBooked(foo, bar)
print(res)
