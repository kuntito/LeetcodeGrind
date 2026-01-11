# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/description/

import math

class Solution:
    def minimumTime(self, jobs: list[int], workers: list[int]) -> int:
        pass
        # i'm thinking what job takes the longest to finish
        # the worker with the most capacity should attend to this job
        
        jobs.sort()
        workers.sort()
        
        maxDays = 0
        for jobTime, workerCapacity in zip(jobs, workers):
            days = 1 if workerCapacity >= jobTime else math.ceil(jobTime/workerCapacity)
                
            maxDays = max(days, maxDays)
        
        return maxDays
       
        
arr = [
    [[3,18,15,9], [6,5,1,3]],
    [[5,2,4], [1,7,5]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minimumTime(foo, bar)


print(res)