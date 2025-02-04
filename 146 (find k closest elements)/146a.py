# https://leetcode.com/problems/find-k-closest-elements/

import heapq
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        pass
        # use binary search to find x's index, `idx`
        # if x does not exist search all indices `[idx: ]`
        # and `[:idx-1]` and store k values on both sides in a heap
        
        # if `x` does exist, search `[idx+1: ]` and [:idx-1]
        
    
arr = [
    [[1, 2, 3, 4, 5], 4, 3],
    [[1,1,2,3,4,5], 4, -1],
    [[1,1,1,10,10,10], 1, 9],
]
foo, bar, zar = arr[-1]
sol = Solution()
res = sol.findClosestElements(foo, bar, zar)
print(res)