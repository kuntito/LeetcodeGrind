# https://leetcode.com/problems/meeting-rooms-iii/description/
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        pass
        # you need to know the current time
        # the current time determines the available meetings
        # you need to know the available rooms
        
        # at any point in time, you want to pick the next available meeting
        # and place in the next available room
        
        # i'm thinking two heaps, one to store the available rooms
        # another for the available meetings
        
        # sort the meetings in reverse order, for O(1) popping
        # the start time of last meeting determines current time
        
        # for the available rooms, you're sorting based on the current end time
        # and the current index
        
        
        heapq.heapify(meetings)

        # each element is the meeting end time, room index and the frequency
        availableRooms = [[0, i, 0] for i in range(n)]
        heapq.heapify(availableRooms)
                
        self.res = None
        while meetings:
            currMeet = heapq.heappop(meetings)
            duration = currMeet[1] - currMeet[0]

            if currMeet[0] < availableRooms[0][0]:
                currMeet[0] = availableRooms[0][0]
                currMeet[1] = currMeet[0] + duration
            
            nextRoom = self.getNextRoom(currMeet[0], availableRooms)
                
            
            nextRoom[0] = currMeet[1]
            nextRoom[2] += 1
            
            if self.res is None:
                self.res = nextRoom
            elif nextRoom[2] == self.res[2] and nextRoom[1] < self.res[1]:
                self.res = nextRoom
            elif nextRoom[2] > self.res[2]:
                self.res = nextRoom
            
            heapq.heappush(availableRooms, nextRoom)
            
        return self.res[1]
            
        
                
    def getNextRoom(self, startTime, availableRooms):
        candidates = []
        leastIndex = None
        while availableRooms and availableRooms[0][0] <= startTime:
            room = heapq.heappop(availableRooms)
            candidates.append(room)
            
            roomIdx = room[1]            
            if leastIndex is None:
                leastIndex = roomIdx
            elif roomIdx < leastIndex:
                leastIndex = roomIdx
               
        res = None 
        while candidates:
            room = candidates.pop()
            if room[1] == leastIndex:
                res = room
                continue
            
            heapq.heappush(availableRooms, room)
            
        return res
        
            
    
    
    
arr = [
    [4, [[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]],
    [2, [[0,10],[1,5],[2,7],[3,4],[8,11],[9,12]]],
    [2, [[0,10],[1,5],[2,7],[3,4]]],
    [3, [[1,20],[2,10],[3,5],[4,9],[6,8]]],
]
foo, bar = arr[-1]


sol = Solution()
res = sol.mostBooked(foo, bar)
print(res)
