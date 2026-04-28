from typing import List


class Solution:
    def survivedRobotsHealths(
        self,
        positions: List[int],
        healths: List[int],
        directions: str
    ) -> List[int]:
        # and how do i want to do this?
        
        # well iterate through indices
        # from `0` till len(anyOne)
        
        self.positions = positions
        self.healths = healths
        self.directions = directions
        
        dim = len(positions)
        
        arr = []
        for idx in range(dim):
            # now, at each index what do i want to do?
            # if i have an L, i want to check if the previous element is an R
            self.ifShouldCollideCollide(arr, idx)
            
        return [healths[idx] for idx in arr]

                    
    def ifShouldCollideCollide(self, arr, curIdx):
        currentDir = self.directions[curIdx]
        
        if self.isPrevR(arr) and currentDir == 'L':
            prevIdx = arr[-1]
            maybeWinningIdx = self.collideRobotsAtIndices(
                prevIdx,
                curIdx
            )
            
            if maybeWinningIdx == prevIdx:
                self.healths[prevIdx] -= 1
            elif maybeWinningIdx == curIdx:
                self.healths[curIdx] -= 1
                # remove the right one if it loses..
                arr.pop()
                # then compare again
                self.ifShouldCollideCollide(arr, curIdx)
            else:                
                # if neither wins
                # simply remove the last element
                arr.pop()
        else:
            arr.append(curIdx)
        
            
            
    def isPrevR(self, arr):
        if arr:
            prevElemIdx = arr[-1]
            return self.directions[prevElemIdx] == 'R'
        
        return False
    
    
    def collideRobotsAtIndices(self, leftIdx, rightIdx):
        leftHealth = self.healths[leftIdx]
        rightHealth = self.healths[rightIdx]
        
        if leftHealth > rightHealth:
            return leftIdx
        elif leftHealth < rightHealth:
            return rightIdx
        
        return None
    
arr = [
    [
        [5,4,3,2,1],
        [2,17,9,15,10],
        "RRRRR",
    ],
    [
        [3,5,2,6],
        [10,10,15,12],
        "RLRL",
    ],
    [
        [1,2,5,6],
        [10,10,11,11],
        "RLRL",
    ],
    [
        [13,3],
        [17,2],
        "LR",
    ]
]
foo, bar, zad = arr[-1]
sol = Solution()
res = sol.survivedRobotsHealths(foo, bar, zad)
print(res)