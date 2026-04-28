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
            # now, what do i want to do?
            # i want to check if a collision can occur
            # if yes, collide and see if another can occur
            self.ifCanCollideCollide(arr, idx)
            
        return [
            healths[idx] for idx in arr
        ]
            
    def ifCanCollideCollide(self, arr, idx):
        if arr:
            prevElemIdx = arr[-1]
            prevElemDir = self.directions[prevElemIdx]
            currElemDir = self.directions[idx]
            
            if prevElemDir != currElemDir:
                # here, i want to collide the elements
                maybeWinningIdx = self.collide(prevElemIdx, idx)
                if maybeWinningIdx == idx:
                    arr.pop()
                    self.healths[idx] -= 1
                    self.ifCanCollideCollide(arr, idx)
                elif maybeWinningIdx == prevElemIdx:
                    self.healths[prevElemIdx] -= 1
                else:
                    arr.pop()
            else:
                arr.append(idx)
        else:
            arr.append(idx)
            
    def collide(self, leftIdx, rightIdx):
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
    ],
    # [
    #     [3,47],
    #     [46,26],
    #     "LR",
    # ]
]
foo, bar, zad = arr[-1]
sol = Solution()
res = sol.survivedRobotsHealths(foo, bar, zad)
print(res)