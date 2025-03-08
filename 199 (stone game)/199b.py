# https://leetcode.com/problems/stone-game/description/

from collections import deque

# TODO look at solution, your assumption is wrong
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        pass
        # this is a bruteforce backtracking problem
        # where you explore alice picking from the left and right
        # and bob picking from the left and right
        
        # track alice's highest scores on all paths
        # track bob's highest scores on all paths
        # return alice - bob >= 0
        # since alice plays first
        
        # turn piles into a deque
        # `turn` is an integer indicating whose turn it is
        # when it's even, it's alice else bob
        turn = 0
        pilesQueue = deque(piles)
        
        self.maxAlice = 0
        self.aliceScore = 0
        
        self.maxBob = 0
        self.bobScore = 0
        
        self.explore(turn, pilesQueue)
        

        return self.maxAlice >= self.maxBob
    
    
    def explore(self, turn, pilesQueue: deque):
        if not pilesQueue:
            return
        
        # bob's turn
        if turn % 2:
            leftItem = pilesQueue.popleft()
            self.updateBob(leftItem)
            
            self.explore(turn+1, pilesQueue)
            
            self.updateBob(-leftItem)
            pilesQueue.appendleft(leftItem)
            
            rightItem = pilesQueue.pop()
            self.updateBob(rightItem)
            
            self.explore(turn+1, pilesQueue)
            
            self.updateBob(-rightItem)
            pilesQueue.append(rightItem)
        # alice's turn
        else:
            pass
            leftItem = pilesQueue.popleft()
            self.updateAlice(leftItem)
            
            self.explore(turn+1, pilesQueue)
            
            self.updateAlice(-leftItem)
            pilesQueue.appendleft(leftItem)
            
            rightItem = pilesQueue.pop()
            self.updateAlice(rightItem)
            
            self.explore(turn+1, pilesQueue)
            
            self.updateAlice(-rightItem)
            pilesQueue.append(rightItem)
            

    def updateAlice(self, item):
        self.aliceScore += item
        self.maxAlice = max(
            self.aliceScore,
            self.maxAlice
        )

    def updateBob(self, item):
        self.bobScore += item
        self.maxBob = max(
            self.bobScore,
            self.maxBob
        )
        
        
    
arr = [
    [3,2,10,4],
    [5,3,4,5],
    [3,7,2,3],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGame(foo)
print(res)