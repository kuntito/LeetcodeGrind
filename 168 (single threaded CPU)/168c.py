
import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        pass
        # you need a way to track current time
        # and the available tasks at said time
        
        # you want to pick tasks based on the shortest processing time
        # hence, a heap that stores items based on (procTime, idx)
        
        # you pick the smallest from that heap
        # and append it to `res`
        
        # the heap should be initialized with the task with the smallest enqueue time
        # it makes sense to sort `tasks` in reverse order
        
        # since the order matters, it makes sense to pair each task with it's index
        # [enqTime, procTime, idx]
        # then sort in reverse based on enqueueTime
        
        tasksWithIndex = [[tk[0], tk[1], idx] for idx, tk in enumerate(tasks)]
        
        tasksWithIndex.sort(key=lambda a: a[0], reverse=True)
        
        # while tasksWithIndex:
        #     item = tasksWithIndex.pop()
        #     print([item[0], item[1]])
        
        res = []

        minHeap = []

        
        while tasksWithIndex or minHeap:
            if not minHeap:
                currTime = tasksWithIndex[-1][0]
                while tasksWithIndex and tasksWithIndex[-1][0] <= currTime:
                    nei = tasksWithIndex.pop()
                    neiProTime, neiIdx = nei[1], nei[2]
                    
                    heapq.heappush(minHeap, [neiProTime, neiIdx])
            
            currTask = self.getNextTask(minHeap)
            procTime, currIdx = currTask
            
            res.append(currIdx)
            
            # since current task has to end before any other task
            # update the time
            currTime += procTime
            
            # if any task has enqueueTime <= currTime
            # add to minHeap
            while tasksWithIndex and tasksWithIndex[-1][0] <= currTime:
                nei = tasksWithIndex.pop()
                neiProTime, neiIdx = nei[1], nei[2]
                
                heapq.heappush(minHeap, [neiProTime, neiIdx])
                
                
            
        
        # calculate the current time based on the new task
        # if any tasks are scheduled to start on or before the current task ends
        # add it to the heap
        
        return res
    
        
    def getNextTask(self, minHeap):
        # you want to get the task with the least processing time
        # and least index
        # in this case we know the least processing time based on the heap
    
        leastProcTime = minHeap[0][0]
        
        # gather all nodes with similar processing times into `arr`
        arr = []
        res = None
        
        while minHeap and minHeap[0][0] == leastProcTime:
            item = heapq.heappop(minHeap)
            arr.append(item)
            
            if res is None:
                res = item
            elif item[1] < res[1]:
                res = item
                
        # put all items back into the heap except the least index one
        while arr:
            item = arr.pop()
            if item == res:
                continue
            
            heapq.heappush(minHeap, item)
            
        return res
            


arr = [
    [[7,10],[7,12],[7,5],[7,4],[7,2]],
    [[1,2],[2,4],[3,2],[4,1]],
    [[46,9],[46,42],[30,46],[30,13],[30,24],[30,5],[30,21],[29,46],[29,41],[29,18],[29,16],[29,17],[29,5],[22,15],[22,13],[22,25],[22,49],[22,44]],
    [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.getOrder(foo)
print(res)