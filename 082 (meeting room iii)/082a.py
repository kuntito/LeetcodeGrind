# https://leetcode.com/problems/meeting-rooms-iii/description/
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        pass
        # create a hashmap to track the amount of times a room was used
        freq = { i : 0 for i in range(n) }
        
        meetings.sort()

        # explore each room in sequence
        # if the room is vacant, place the earliest meeting
        # to aid easy retrieval of the earliest meetings
        # sort meetings
        
        # go through each meeting in `meetings`
        # place each meeting in the first vacant room
        # track the meetings in order of completion
        
        # this heap is initialized as (endTime, roomIdx) where endTime = 0 since no meeting has started
        # and `roomIdx` is every available room
        
        heap = [(0, i) for i in range(n)]
        heapq.heapify(heap)
        # heap? where you store the end of the meeting (endTime, roomIdx)
        # this would be the location for the next meeting
        
        most_used = 0
        for meet in meetings:
            pass
            earliestEnd, room_idx = heapq.heappop(heap)
            
            _, end = meet
            # start += earliestEnd
            # the next meeting's end times are incremented by the endTime of the last meeting
            end += earliestEnd
            
            freq[room_idx] += 1
            
            heapq.heappush(
                heap,
                (end, room_idx)
            )
            
            if freq[room_idx] > freq[most_used]:
                most_used = room_idx
            
            if freq[room_idx] == freq[most_used] and room_idx < most_used:
                most_used = room_idx
                
        return most_used
        
    
    
    
arr = [
    [2, [[0,10],[1,5],[2,7],[3,4],[8,11],[9,12]]],
    [2, [[0,10],[1,5],[2,7],[3,4]]],
    [3, [[1,20],[2,10],[3,5],[4,9],[6,8]]],
    [4, [[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]],
    # TODO, it's not the earliest room per se
    # it's the earliest room before the startTime of the next meeting
]
foo, bar = arr[-1]


sol = Solution()
res = sol.mostBooked(foo, bar)
print(res)
