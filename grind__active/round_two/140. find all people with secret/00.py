from typing import List

import heapq

class Solution:
    def findAllPeople(
        self,
        n: int,
        meetings: List[List[int]],
        firstPerson: int
    ) -> List[int]:
        # each meeting id described (personNumber, personNumber, meetingTime)
        # i can throw all the meetings in a minHeap
        # to pick them in order.
        # i'd have a set of who knows the secret.
        # and pass it around.
        
        meetingHeap = self.getMeetingHeap(meetings)
        knowsSecret = {0, firstPerson}
        
        while meetingHeap:
            # grab meetings happening now
            currentMeetings = self.grabCurrentMeetings(meetingHeap)
            allAttendees = self.getAllAttendees(currentMeetings)
            if any(person in knowsSecret for person in allAttendees):
                for person in allAttendees:
                    knowsSecret.add(person)
                    
        return list(knowsSecret)
            
            
    def getAllAttendees(self, currentMeetings):
        attendees = set()
        for _, a, b in currentMeetings:
            attendees.add(a)
            attendees.add(b)
            
        return attendees
            
    # TODO start here, this is the bottle neck.
    # you don't want meetings that start at the same time.
    # you want meetings that overlap attendees
    # (tunde, joshua) and (matthew, tunde) overlap at tunde
    # (tunde, joshua) and (matthew, mark) don't overlap
    # if they happen at the same time, the secret doesn't reach both meetings.
    
    def grabCurrentMeetings(self, meetingHeap):
        now = meetingHeap[0][0]
        curr = []
        while meetingHeap and meetingHeap[0][0] == now:
            meetingItem = heapq.heappop(meetingHeap)
            curr.append(
                meetingItem
            )
            
        return curr
            
        
        
    def getMeetingHeap(self, meetings):
        minHeap = []
        for a, b, meetingTime in meetings:
            heapq.heappush(minHeap, (meetingTime, a, b))
            
        return minHeap
    
arr = [
    [
        6,
        [[0,2,1],[1,3,1],[4,5,1]],
        1
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.findAllPeople(foo, bar, baz)
print(res)