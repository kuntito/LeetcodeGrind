# https://leetcode.com/problems/single-threaded-cpu/description/

import heapq
# TODO solve it!
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        pass
        # put all tasks into a `minHeap` based on (processTime, enqueueTime)
        
        # get the task with the smallest processing time such that
        # it's enqueueTime > time
        # if no such time exists, set time to the enqueueTime of the smallest
        # task
        
        # twoHeaps, the second heap would store any `processTime` with `enqueueTime < time`
        
        minHeap = []
        for enTime, procTime in tasks:
            heapq.heappush(minHeap, (procTime, enTime))
            
        time = 1