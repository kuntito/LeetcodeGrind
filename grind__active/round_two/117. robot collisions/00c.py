from typing import List


# TODO solved, but rewrite this joint.
class Solution:
    def survivedRobotsHealths(
        self,
        positions: List[int],
        healths: List[int],
        directions: str
    ) -> List[int]:
        combo = []
        dim = len(positions)
        
        for idx in range(dim):
            combo.append([
                positions[idx],
                healths[idx],
                directions[idx],
                idx
            ])
            
        # now, i have combo
        combo.sort(key=lambda x: x[0])
        self.combo = combo
        
        # sorted by position
        
        arr = []
        for modIdx in range(dim):
            self.ifCanCollideCollide(arr, modIdx)
            
        
        arr = [combo[idx] for idx in arr]
        
        arr.sort(key=lambda x: x[-1])
        
        return [x[1] for x in arr]
    
    def ifCanCollideCollide(self, arr, curIdx):
        if arr:
            if self.isPrevR(arr) and self.combo[curIdx][2] == 'L':
                prevIdx = arr[-1]
                maybeWinIdx = self.collide(prevIdx, curIdx)
                
                if maybeWinIdx == prevIdx:
                    self.combo[prevIdx][1] -= 1
                elif maybeWinIdx == curIdx:
                    arr.pop()
                    self.combo[curIdx][1] -= 1
                    
                    self.ifCanCollideCollide(arr, curIdx)
                else:
                    arr.pop()
                
            else:
                arr.append(curIdx)
        else:
            arr.append(curIdx)
            
    def isPrevR(self, arr):
        if arr:
            prevElemIdx = arr[-1]
            elem = self.combo[prevElemIdx]
            return elem[2] == 'R'
        
        return False
    
    def collide(self, leftIdx, rightIdx):
        leftElem = self.combo[leftIdx]
        rightElem = self.combo[rightIdx]
        
        leftHealth = leftElem[1]
        rightHealth = rightElem[1]
        
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
    # [
    #     [3,5,2,6],
    #     [10,10,15,12],
    #     "RLRL",
    # ],
    # [
    #     [1,2,5,6],
    #     [10,10,11,11],
    #     "RLRL",
    # ],
    # [
    #     [13,3],
    #     [17,2],
    #     "LR",
    # ],
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