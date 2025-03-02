# https://leetcode.com/problems/single-threaded-cpu/description/

# TODO solve it!
import heapq
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        pass
        indexedTasks = self.get_indexed_tasks(tasks)
        # sort based on enqueueTime since that's the first element in each tuple
        indexedTasks.sort(reverse=True)
        
        # the queue stores tasks based on processing time
        _, procTime, idx = indexedTasks.pop()
        queue = [(procTime, idx)]
        
        res = []
        currTime = 1
        while indexedTasks or queue:
            if not queue:
                newEnqTime, newProcTime, newIdx = indexedTasks.pop()
                currTime = newEnqTime + newProcTime
                heapq.heappush(queue, (newProcTime, newIdx))
                
            
            procTime, idx = heapq.heappop(queue)
            currTime += procTime
            res.append(idx)

            while indexedTasks and currTime >= indexedTasks[-1][0]:
                _, newProcTime, newIdx = indexedTasks.pop()
                heapq.heappush(queue, (newProcTime, newIdx))
        
        
        return res
        
    def get_indexed_tasks(self, tasks):
        arr = []
        for idx, item in enumerate(tasks):
            enqTime, procTime = item
            arr.append((enqTime, procTime, idx))
            
        return arr
        

        
        
        
        
arr = [
    [[1,2],[2,4],[3,2],[4,1]],
    [[7,10],[7,12],[7,5],[7,4],[7,2]],
]
foo = arr[-1]
sol = Solution()
res = sol.getOrder(foo)
print(res)