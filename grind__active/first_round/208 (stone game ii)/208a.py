# https://leetcode.com/problems/stone-game-ii/description/


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        pass
        # at the start, M = 1
        # we can take at most 2M stones
        
        # we'd explore all the possibilities
        # we need a recursive function that knows
        # M
        # has access to piles
        # knows the current start index
        # knows whose turn it is
        # keeps track of alice's score
        # can update alice's score
        
        self.piles = piles
        self.dim = len(piles)
        self.aliceScore = 0
        
        currIdx = 0
        M = 1
        currTurn = True # True is Alice, False is Bob
        currAliceScore = 0
        
        self.explorePicks(currIdx, M, currTurn, currAliceScore)
        
        return self.aliceScore
    
        
    def explorePicks(self, startIdx, M, currTurn, currAliceScore):
        maxPicks = 2 * M
        
        # if the current player can pick all the stones then do so
        if startIdx + maxPicks >= self.dim:
            if currTurn:
                currAliceScore += sum(self.piles[startIdx:])
            startIdx = self.dim


        if startIdx == self.dim:
            self.aliceScore = max(
                self.aliceScore,
                currAliceScore
            )
            return
        
        
        
        # from current index to min(currIdx + maxPicks, dim)
        endRange = min(
            startIdx + maxPicks,
            self.dim
        )
        
        for idx in range(startIdx, endRange):
            val = self.piles[idx]
            if currTurn:
                currAliceScore += val
                
            newM = (idx - startIdx) + 1
            self.explorePicks(idx + 1, newM, not currTurn, currAliceScore)
            
            
arr = [
    [2,7,9,4,4],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGameII(foo)
print(res)