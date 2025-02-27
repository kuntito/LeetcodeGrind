# https://leetcode.com/problems/single-threaded-cpu/description/

import heapq
# TODO solve it!
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        pass
        # you want to select the task with the shortest processing time
        # that can start at the current time `t`
        
        # if there are clashes, pick the one with the smallest index
        
        # you need to know what tasks are available at what time
        
        # one heap where the tasks are sorted by enqueueTime, `startHeap`
        # the start time is the time of the first element
        
        # select that heap and append it's index to `res`
        # currTime = enqueue time of that element
        # calculate the end time as currTime += processingTime
        
        # for every element in `startHeap` who's start time is less than `currTime`
        # append to a newHeap, `processHeap`
        # the key of this heap would be the process time
        
        # subsequent selections would be from this heap
        # as the indices are appended to `res`
        # and `currTime` is updated
        
        # once you run out of `processHeap` items
        # currTime becomes the enqueueTime of the first item in `startHeap`
        # and the process repeats till you run out of elements