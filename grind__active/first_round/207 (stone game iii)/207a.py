# https://leetcode.com/problems/stone-game-iii/description/

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        pass
        # TODO
        # i'd say explore all possibilties
        # at the end of each possibility, save the winner in a set
        # if alice wins any of the possibilities, immediately return True
        # else add "Bob" to the set OR add "tie" to the set if it happens to be the case
        # if at the end, a "tie" is possible, return "tie"
        
        # to explort all possibilities
        # use a boolean to indicate whose turn it is, `currTurn`
        # if positive, alice, else bob
        # for each turn iterate through the stone possibilities
        # for i in range(1, 4):
        #   the person would take their respective stones
        #   save the stone score
        #   then start another recursive function
        #   where the turn is negated and the start idx
        #   is the next index after the stones taken
        
        #   at the end of each recursive function, we want to return the 
        #   number of stones that had the best score
        #   did candidate have best score when they picked 1, 2, or 3 stones
        
        self.res = set()
        # use an array to track the current scores of alice and bob respectively
        aliceWin = self.explore(True, 0, [0, 0], stoneValue)
        if aliceWin:
            return "Alice"
        
        return "Tie" if "Tie" in self.res else "Bob"
    
        
    def explore(self, currTurn, startIdx, scoreBoard, stones):
        dim = len(stones)
        if startIdx == dim:
            pass
        
        endRange = min(startIdx + 3, dim)
        totalAdded = 0
        for idx in range(startIdx, endRange):
            stone = stones[idx]
            # alice's turn, add the stone values
            if currTurn:
                scoreBoard[0] += stone
                if self.explore(not currTurn, idx + 1, scoreBoard, stones):
                    return True
            else:
                scoreBoard[1] += stone
                if self.explore(not currTurn, idx + 1, scoreBoard, stones):
                    return True
            
            totalAdded += stone
            
        if currTurn:
            scoreBoard[0] -= totalAdded
        else:
            scoreBoard[1] -= totalAdded
        
        
    
arr = [
    [1,2,3,-9],
    [1,2,3,6],
    [-1,-2,-3],
    [1,2,3,7],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGameIII(foo)
print(res)