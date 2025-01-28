# https://leetcode.com/problems/car-fleet/description/

import heapq
# TODO i think i've misunderstood the question
# look at nav's solution
# explore what it does
# compare it to what yours does

# https://neetcode.io/solutions/car-fleet
# 09:41
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        count = 0
        
        i = 1
        while position:        
            # pair each position with it's speed
            intervals = self.get_intervals(position, speed)
            intervals.sort()
            
            # if i == 2:
            #     print(intervals)
            
            minHeap = self.drive(intervals)
            
            # if i == 2:
            #     while minHeap:
            #         print(heapq.heappop(minHeap))
            
            
            
            position, speed, incr = self.count_fleets(minHeap, target)
            count += incr
            
            # print(count)
            
            i += 1

            
        return count
        
        
                
    def count_fleets(self, minHeap, target):
        count = 0
        position, speed = [], []
        
        target_found = False
        seen = set()
        while minHeap:
            pos, sp = heapq.heappop(minHeap)
            
                    
            if pos >= target:
                # seen.add(pos)
                if pos > target:
                    count += 1
                elif target_found is False:
                    count += 1
                    target_found = True
                        # if position is empty or the new position is different from the last item in `position`
            elif not position or position[-1] != pos:
                position.append(pos)
                speed.append(sp)  

                    
        return position, speed, count# + len(seen)
    
        
    def drive(self, intervals):
        # drive all cars in reverse
        # store the new position in a `minHeap`
        minHeap = []
        for idx in range(len(intervals)-1, -1, -1):
            pos, sp = intervals[idx]
            new_pos = pos + sp
            # for the heap property to function
            # place [new_pos, sp] into the heap
            
            
            # every car that drives should not have a new position > `minHeap[0]`
            # car new position = min(newPosition, minHeapLowestPosition)
            if minHeap and new_pos >= minHeap[0][0]:
                new_pos = minHeap[0][0]
                sp = minHeap[0][1]
            
            heapq.heappush(minHeap, (new_pos, sp))
            
        return minHeap
        
    
    def get_intervals(self, pos_arr, sp_arr):
        intervals = []
        
        for pos, sp in zip(pos_arr, sp_arr):
            intervals.append(
                (pos, sp)
            )
            
        return intervals
    
    
arr = [
    [12, [10,8,0,5,3], [2,4,1,1,3]],
    [100, [0, 2, 4], [4, 2, 1]],
    [31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]],
    [10, [3], [3]],
    [21, [1,15,6,8,18,14,16,2,19,17,3,20,5], [8,5,5,7,10,10,7,9,3,4,4,10,2]],
    # TODO why does my code return `8` when the answer is `7`?
]

target, foo, bar = arr[-1]
sol = Solution()

res = sol.carFleet(target, foo, bar)
print(res)