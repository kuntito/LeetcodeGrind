# https://leetcode.com/problems/task-scheduler/description/

from typing import List

# i'm given two things.
# an array of strings, `tasks`
# and an integer, `n`

# each element of `tasks` is one of A..Z

# i want to run all the tasks.
# each task takes 1 second to run.

# however, there's a caveat.
# every task has a cooldawn of `n` seconds.
# if i do a task now, i need to wait `n` seconds before i can do it again.


# consider the following:
# tasks = [A, A, B, B]
# n = 1

# in the first second, i pick task A
# i'm left with [_, A, B, B]

# in the second second, i can't pick task A
# cause it needs to cool down..
# so i pick the next available task, B
# i'm left with [_, A, _, B]

# in the third second, i can't pick A..
# it's in the first second of cooldown
# i also can't pick B, it' just started to cool down..
# so i have to chill
# in the third second, i chill
# so i'm left with [_, A, _, B]

# in the fourth second, A has cooled down for 2 seconds
# so i pick it again
# i'm left with [_, _, _, B]

# in the fifth second, B has cooled down
# so i can pick it..
# i'm left with [_, _, _, _]

# it took 5 seconds to finish all the tasks.
# the total time is what i want to return.

# how would this go in code?
# i want to pick the next available task.

# how do you know the next available task..
# how about i use a hash map to group the tasks by frequency
# then iterate through the hashmap, picking tasks..

# well you could, but how would you address the cooldown?
# i'm thinking minHeap.. and hashmap

# how would this work..
# i'd use a hashmap to map each task to it's frequency

# okay, and minHeap.. we'd append each unique task to the minHeap
# each item would be [timeAvailable, task]

# initially, all the tasks would have `timeAvailable` as `0`
# so i can pick any task..

# once, i pick a task..
# i upload it's frequency in the hashmap..
# if the frequency is greate than `0`

# i'll re-add it to the heap
# but update it's `timeAvailable`

# it'd become `timeAvaiable += n`
# then re-add to the heap..

# i'd need one more variable current time..
# current time, technically is always the time of the topmost heap item
# this way, i always pick the next available task..

# the hashmap let's me know when i'm done with the task
# so i'd return `currentTime`

# error, while pushing to the minHeap
# i didn't add `minHeap` to the push method

# i did `heapq.heappush(elem)` instead of `heapq.heappush(minHeap, elem)`

# error, i should increment current time on each iteration

# error, incrementing current time on each iteration adds an extra second
# to the entire duration..
# the condition for the while loop is if `minHeap` has values..
# when i pop the last value..

# i still increment `currentTime` by `1`
# so i should only increment, if the minHeap still has values.

# TODO doesn't work with this example
# [["B","C","D","A","A","A","A","G"], 1]
# for nextAvailableTime, my guess is i want to treat ties differently..
# there's multiple A's so i should always pick A first if available

# rewrite approach, define this problem


import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        
        for t in tasks:
            hashMap[t] = hashMap.get(t, 0) + 1
            
        minHeap = [(1, t) for t in hashMap]
        
        currentTime = 0
        while minHeap:
            availableTime, currentTask = heapq.heappop(minHeap)
            
            if availableTime > currentTime:
                currentTime = availableTime
            
            hashMap[currentTask] -= 1
            # not sure deleting adds anything to the algorithm
            if hashMap[currentTask] == 0:
                del hashMap[currentTask]
            else:
                nextAvailableTime = currentTime + n + 1
                heapq.heappush(
                    minHeap,
                    (
                        nextAvailableTime,
                        currentTask
                    )
                )
                
            if minHeap:
                currentTime += 1
                
        return currentTime
            
            
arr = [
    [["A","A","B","B"], 2],
    [["A","A","A","B","B","B"], 2],
    [["B","C","D","A","A","A","A","G"], 1]
]
foo, bar = arr[-1]
sol = Solution()

res = sol.leastInterval(foo, bar)
print(res)