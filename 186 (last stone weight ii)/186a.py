# https://leetcode.com/problems/last-stone-weight-ii/description/

# TODO compare with asteroid collision

import heapq
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        pass
        # since we're optimizing for the smallest stone
        # it makes sense to smash the largest two stones
        # use a maxHeap, while len(maxHeap) > 2:
        # grab the top two stones
        # smash them, if there's a remainder, heappush the remainder
        
        # FIXME correction, we smash the closest two stones
        # the stones with the least absolute difference
        
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            pass
            uno = -1 * heapq.heappop(maxHeap)
            dos = -1 * heapq.heappop(maxHeap)
            
            rem = abs(uno-dos)
            if rem > 0:
                heapq.heappush(maxHeap, -rem)
        
        
        return -1 * maxHeap[0] if maxHeap else 0

arr = [
    [2,7,4,1,8,1],
    [31,26,33,21,40],
]
foo = arr[-1]
sol = Solution()
res = sol.lastStoneWeightII(foo)
print(res)