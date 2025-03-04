# https://leetcode.com/problems/meeting-rooms-iii/description/
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        pass
        # create hashmap to store the frequency of each meeting room
        room_freq = {idx:0  for idx in range(n)}
        
        # sort meetings in reverse to get the earliest meeting
        meetings.sort(reverse=True)
        
        # create an array to store meeting rooms in descending order
        rooms = [i for i in range(n-1, -1, -1)]
        
        # create a heap, to store the (end time, meeting room)
        endTimes = []
        
        # for each meeting in `meetings`
        # check `minHeap` if the end time of the earliest meeting
        # is lower than the the start Time of the new meeting
        # if this is true, the new meeting will simply use that room
        # else if there is vacant room, the new meeting will use that vacant room
        # else the new meeting will update it's end time to 
        # the endTime of earliest meeting and use the room
        
        most_used = 0
        while meetings:
            newMeeting = meetings.pop()
            start, end = newMeeting
            
            roomIdx = None
            if endTimes and endTimes[0][0] <= start:
                roomIdx = endTimes[0][1]
                
                    
                heapq.heappop(endTimes)
                heapq.heappush(endTimes, (end, roomIdx))
            elif rooms:
                roomIdx = rooms.pop()
                
                heapq.heappush(endTimes, (end, roomIdx))
            else:
                earliestEnd, roomIdx = endTimes[0]
                end += earliestEnd
                heapq.heappop(endTimes)
                heapq.heappush(endTimes, (end, roomIdx))
                
            room_freq[roomIdx] += 1
            most_used = max(most_used, room_freq[roomIdx])
        

        print(room_freq)
        for idx in range(n):
            if room_freq[idx] == most_used:
                return idx    
    
    
    
arr = [
    [2, [[0,10],[1,5],[2,7],[3,4],[8,11],[9,12]]],
    [2, [[0,10],[1,5],[2,7],[3,4]]],
    [3, [[1,20],[2,10],[3,5],[4,9],[6,8]]],
    
    # TODO, you want to put the new meeting in the earliest room
    # not the meeting that finishes first
    # for instance, all three meetings finish before `[17, 19]`
    # the current implementation seeks the earliest room
    # and as a result places the meeting in room[2]
    # when the earliest room is in fact room[0]
    [4, [[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]],
]
foo, bar = arr[-1]


sol = Solution()
res = sol.mostBooked(foo, bar)
print(res)
