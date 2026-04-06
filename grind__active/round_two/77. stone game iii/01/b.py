# https://leetcode.com/problems/stone-game-iii/

from typing import List

# i'm following up from the breakdown in `a.py`
# i want to add memoization by passing current index in every recursive call

# and i've learned i should still explore the stone values
# even when there's at most three stones because the stone values
# could be negative..

# error, currentVal isn't the value at the current index
# but the sum of all picks up till that point..

# you missed this cause you were rushing to implement
# seeing that the first iteration worked, you were on auto pilot
# and didn't think this through, do better.

# error, 
# you cached based on `idx` and not `startIdx`
# again, you were rushing..

# third, a mere pointer..
# yes, you do need to check if the start idx goes out of bounds..
# consider [1, 2, 3] at the point when you pick three stones..

# your next call is `self.explore(idx + 1, ...)`
# at this point, `idx + 1` would be out of bounds..

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        firstIdx = 0
        
        aliceScore, bobScore = self.explore(firstIdx, stoneValue, memo)
        
        if aliceScore > bobScore:
            return "Alice"
        
        if bobScore > aliceScore:
            return "Bob"
        
        return "Tie"
    
    def explore(self, startIdx, stoneValue, memo):
        dim = len(stoneValue)
        # TODO i don't think this ever executes..
        if startIdx == dim:
            return 0, 0
        
        if startIdx in memo:
            return memo[startIdx]
        
        # what we doing, iterate from startIdx to endRange
        endRange = min(
            startIdx + 3,
            dim
        )
        
        bestPlay = None
        
        for idx in range(startIdx, endRange):
            
            currentVal = sum(stoneValue[startIdx:idx + 1])
            
            oppBestPlay, myBestPlayAfterOpp = self.explore(
                idx + 1,
                stoneValue,
                memo
            )
            
            myBestPlayAtPick = currentVal + myBestPlayAfterOpp
            
            if bestPlay is None:
                bestPlay = (
                    myBestPlayAtPick,
                    oppBestPlay
                )
            else:
                diffCurr = bestPlay[0] - bestPlay[1]
                diffAtPick = myBestPlayAtPick - oppBestPlay
                
                if diffAtPick > diffCurr:
                    bestPlay = (
                        myBestPlayAtPick,
                        oppBestPlay
                    )
                    
        memo[idx] = bestPlay
        return memo[idx]