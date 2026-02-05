# https://leetcode.com/problems/task-scheduler/description/

from typing import List

# i'm given two things.
# an array of strings and an integer.

# the array of strings is called `tasks`
# the integer is named `n`

# every element of `tasks` is an uppercase english letter, A..Z

# what's happening is, i want to execute each task in `tasks`
# but there's a condition.

# every task has a cooldown.

# if i have:
#   `tasks = [A, A]`
#   `n=2`
# if i do the first `A`
# i need to chill for `n` seconds before i can do the second `A`

# it would take me 4 seconds to complete these tasks.

# this is what i want to find. the minimum time, it would take me to complete the tasks.

# how do i approach this?
# well, we'd start by picking one task..
# picking the next available task..
# if none, we'd wait for the next available task..

# while this would allow me complete all the tasks
# it doesn't guarantee minimum time..

# check this out:
# tasks = [B, A, A]
# n = 1

# at time=1s, i start with `B`, the array remains [A, A]
# at time=2s, i pick `A`, the array becomes [A]
# at time=3s, i can't do nun', i need to wait one second 'fore i can pick `A` again
# at time=4s, i can pick the second `A` and i'm done.

# however, 4s is not the minimum time.
# if i'd started with task `A`, i'd have had a quicker time.
# pay attention:
# tasks = [B, A, A]
# n = 1

# at time=1s, i pick `A`, the array becomes [B, A]
# at time=2s, i pick `B`, the array becomes [A]
# at time=3s, i can pick the second `A`, since it cooled down while i picked `B`

# and i'd have completed the tasks in `3s`

# why was it necessary to pick A over B?
# because A occurred twice, B occurs once.

# when two tasks are available,
# it makes sense to pick the one with the higher frequency
# it ensures the minimum time.. because, since it occurs, the most..
# it would have the most total cooldown time..

# so when we pick it first, we get a headstart on that total cooldown.
# and how would you write this in code?

# how would you even address the cooldowns?
# i solved the cooldown problem using a min heap and a dictionary

# i stored each task as (timeAvailable, Task)
# and i'd pick the next available task from the minHeap
# update current time..
# then check the dictionary, 
# "after this task, are there more of the same?"

# if yes, i re-add the task to the min heap
# but update it's timeAvailable += cooldown

# this way, the heap accurately tracks the next available task.
# but what about frequency?

# i could have three tasks with the same `timeAvailable`
# but how do i tell which one has the higher frequency?

# apparently, when the element of a min heap
# is a tuple with more than one child..
# the min heap sorts by the first child of the tuple
# and if there's a tie..
# it sorts by the second element of the tuple..

# i.e.
# if (2, 3) and (2, 1) were in the min heap
# it would pop (2, 1) first.

# this is all i need to resolve this.
# each heap item would be (timeAvailable, -frequency, task)

# i'm using negative frequency cause it's a min heap..
# if A occurs, twice and there's a tie..
# you want to pop A first, so you use `-2` over B's `-1`

# if you added the frequency as is `1` and `2`
# you'd pop B first

# so, a dictionary for frequency
# then min heap..

# how do you deal with time..
# well all elements of the dictionary would be added to the heap
# with timeAvailable set to `1`

# and we'd update as it comes.
# we'd set the time tracker, `duration` to `0`
# when we pop the first item, we check if `timeAvailable > duration`

# if yes, `duration` becomes time available.

# two errors
# one, need to increment duration by `1` on every iteration
# two, the next available time is `currentTime` plus `n` plus `1`

# if we at time=3 and cooldown is `1`, the next available time is `5`
# 3 + 1(n) + 1

# TODO figure this one out
# [["B","C","D","A","A","A","A","G"], 1],

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskGraph = {}
        for t in tasks:
            taskGraph[t] = taskGraph.get(t, 0) + 1
            
        minHeap = [(1, -freq, t) for t, freq in taskGraph.items()]
        heapq.heapify(minHeap)
        
        duration = 0
        while minHeap:
            duration += 1
            
            timeAvailable, _, task = heapq.heappop(minHeap)
            print(task)
            
            if timeAvailable > duration:
                duration = timeAvailable
                
            taskGraph[task] -= 1
            if taskGraph[task] == 0:
                del taskGraph[task]
            else:
                heapq.heappush(
                    minHeap,
                    (
                        duration + n + 1,
                        -taskGraph[task],
                        task
                    )
                )
                
        return duration
    
arr = [
    [["A","A","B","B"], 2],
    [["A","A","A","B","B","B"], 2],
    [["B","C","D","A","A","A","A","G"], 1],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.leastInterval(foo, bar)
print(res)