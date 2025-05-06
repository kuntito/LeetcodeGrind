# https://leetcode.com/problems/buildings-with-an-ocean-view/description/
import heapq
class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        pass
    
        # we're given the an array containing the heights of buildings
        # the order of the heights represent the order of the buildings
        # to the far right is an ocean, we want to first find the buildings that have an ocean view
        
        # a building has an ocean view if there's no obstruction i.e all the buildings to it's right are shorter than itself
        
        # each building is only concerned with the tallest building to it's right
        # is there a way to know at each index what the tallest building is?
        
        # what if there was a way to track the tallest height to the right and it's index, the idea here is that every building knows the tallest building to it's right
        # 
        # the way i'd do this is with a max heap to store all the heights and their indices
        # and for each index i check the maxheap[0]
        # if the height is lower than current height and the index is to the right
        # if the index is to-
        # i think it makes sense to remove leading redundant heights
        # if the index of the height at maxHeap[0] is to the left of current index
        # remove it
        
        # else check if the height is lower, if it is, track the current index as being able to see the ocean in an array `res`
        
        heightsToRight = []
        # grab all the heights from idx = 1 till the end
        idx = 1
        dim = len(heights)
        
        # what if you only had one element in `heights`
        # this wouldn't run, it would, this is just for the heap
        for idx in range(1, dim):
            h = heights[idx]
            heapq.heappush(
                heightsToRight,
                (-1 * h, idx)
            )
        
        res = []
        for currIdx, h in enumerate(heights):
            while heightsToRight and heightsToRight[0][1] <= currIdx:
                heapq.heappop(heightsToRight)

            maxRightHeight = -1 * heightsToRight[0][0] if heightsToRight else None
            
            if not maxRightHeight or h > maxRightHeight:
                res.append(currIdx)
        
        return res
    
arr = [
    [4,2,3,1],
    [4,3,2,1],
    [1,3,2,4],
]
foo = arr[-1]
sol = Solution()
res = sol.findBuildings(foo)
print(res)