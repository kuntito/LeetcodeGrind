# https://leetcode.com/problems/meeting-rooms-iii/description/
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        pass
        # create a hashmap to store the number of times a meeting room was used
        room_freq = {}
        for i in range(n):
            room_freq[i] = 0
        self.res = (0, 0)
            
        # create an array, `meetingRooms` of size `n` representing all the meeting rooms
        # initialize it's values to `None`
        rooms = [None for _ in range(n)]
        
        
        # heapify `meetings`, to order by the earliest starting time
        heapq.heapify(meetings)
        
        endTimes = []
                
        # go through each room placing the earliest meeting in each room
        # store the ending times of each meeting in another heap, `endTimes`
        earliestEnd = 0
        while meetings:
            self.add_new_meetings(rooms, meetings, endTimes, room_freq)
            
            # TODO the earliest end is also a factor of the time passed before it
            if endTimes:
                earliestEnd = heapq.heappop(endTimes)
                self.update_end_times(rooms, earliestEnd)
        
        print(room_freq)
        return self.res[0]
            
    
        # pop the earliest end time from `endTimes`
        # and all end Times with the same value
        
        # go through each room again, updating each meeting's start time to the earliest end Time
        # if startTime == endTime, that meeting has ended
        # set room[idx] = None
        
        # repeat the cycle till you run out of meetings
        # return the most used room
        
    def add_new_meetings(self, rooms, meetings, endTimes, room_freq):
        for idx, occupant in enumerate(rooms):
            if not meetings: break
            
            if occupant is None:
                start, end = heapq.heappop(meetings)
                
                rooms[idx] = [start, end]
                heapq.heappush(endTimes, end)
                room_freq[idx] += 1
                
                if room_freq[idx] > self.res[1]:
                    self.res = [idx, room_freq[idx]]
        
            
    def update_end_times(self, rooms, earliestEnd):
        for idx, occupant in enumerate(rooms):
            if occupant is None: continue
            
            start, end = occupant
            start = earliestEnd
            
            if start == end:
                rooms[idx] = None
            else:
                rooms[idx] = [start, end]
    
    
    
arr = [
    [3, [[1,20],[2,10],[3,5],[4,9],[6,8]]],
    [2, [[0,10],[1,5],[2,7],[3,4],[8,11],[9,12]]],
    [2, [[0,10],[1,5],[2,7],[3,4]]],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.mostBooked(foo, bar)
print(res)
