# https://leetcode.com/problems/time-taken-to-cross-the-door/description/

import heapq
class Solution:
    def timeTaken(self, arrival: list[int], state: list[int]) -> list[int]:
        pass
    
        # you want to know:
        # the current time
        # how many people want to use the door at the current time
        # sort these people based on indices
        # maintain two lists, one for entry
        # another for exit
        
        # you need to track the door history
        # use a hashmap to track the time the ith person crossed the door
        
        movementMap = {}
        doorHistory = []
        currTime = arrival[0]
        entryHeap = []
        exitHeap = []
        
        dim = len(arrival)
        i = 0
        while i < dim or entryHeap or exitHeap:            
            if i < dim:
                # update time if there are no more heap items
                # or the lowest arrival time is greater than current time
                lowestArrival = self.getLowestArrivalTime(entryHeap, exitHeap, arrival)
                if len(entryHeap) + len(exitHeap) == 0 or (lowestArrival and currTime < lowestArrival):
                    currTime = arrival[i]
                
                availState = state[i]
                
                if availState:
                    heapq.heappush(exitHeap, i)
                else:
                    heapq.heappush(entryHeap, i)
                
            # for the current time, you want to put every one in the heap
            while i + 1 < dim and arrival[i + 1] <= currTime:
                i += 1
                availState = state[i]
                
                if availState:
                    heapq.heappush(exitHeap, i)
                else:
                    heapq.heappush(entryHeap, i)
                    
            # at this point we have all the people who want to enter at this time
            
            # if two or more persons want to enter
            if len(entryHeap) + len(exitHeap) >= 2:
                if not doorHistory:
                    # if door not used, the person who wants to exit goes first
                    currPersonIdx = self.explorePreference(exitHeap, entryHeap)
                elif doorHistory[-1] == 0: # door used for entry
                    # preference is entry
                    currPersonIdx = self.explorePreference(entryHeap, exitHeap)
                elif doorHistory[-1]: # door used for exit
                    currPersonIdx = self.explorePreference(exitHeap, entryHeap)
            elif entryHeap:
                currPersonIdx = self.explorePreference(entryHeap, None)
            else:
                currPersonIdx = self.explorePreference(exitHeap, None)

            
            movementMap[currPersonIdx] = currTime
            doorHistory.append(state[currPersonIdx])
            currTime += 1
            
            i += 1
            
        
        return [movementMap[i] for i in range(dim)]
    
    def getLowestArrivalTime(self, heapOne, heapTwo, arrival):
        if not heapOne and not heapTwo:
            return None
        
        if heapOne and heapTwo:
            idxOne = heapOne[0]
            idxTwo = heapTwo[0]
            
            return min(arrival[idxOne], arrival[idxTwo])
        
        if heapOne:
            return arrival[heapOne[0]]
        
        return arrival[heapTwo[0]]
            
    def explorePreference(self, mostPreferred, lessPreferred):
        currPersonIdx = heapq.heappop(mostPreferred) if mostPreferred else heapq.heappop(lessPreferred)
        return currPersonIdx


arr = [
    [[0,1,1,2,4], [0,1,0,0,1]],
    [[0,0,0], [1,0,1]],
    [[0,5,6,6,7,9,9,9,10,10,10,10,10,15,16,17,17,17], [1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0]],
    [[0,0,6,9,10,10,11,11,11,12,14,14,15,15,15,15,15,16,18,18], [0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.timeTaken(foo, bar)
print(res)
