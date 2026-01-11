# https://leetcode.com/problems/stone-game/description/

from collections import deque

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        pass
        # try all possibilities
        # if there's one where alice win's return True
        
        # you need to know who's turn it is,
        # use a boolean, `True` for Alice, `False` for Bob
        # and you'd start a recursive call for each end of `piles`
        # use pointers, `left` and `right` to indicate what section of `piles`
        # add variables, `aliceScore, bobScore`
        # you can explore
        left, right = 0, len(piles) - 1
        self.piles = piles
        return self.explore(True, left, right, 0, 0, {})
        
    def explore(self, currTurn, left, right, aliceScore, bobScore, memo):
        if left > right:
            return aliceScore > bobScore

        mi = (left, right, aliceScore, bobScore)
        if mi in memo:
            return memo[mi]
        
        
        if currTurn:
            if self.explore(
                not currTurn,
                left + 1,
                right,
                aliceScore + self.piles[left],
                bobScore,
                memo
            ):
                memo[mi] = True
                return True

            if self.explore(
                not currTurn,
                left,
                right-1,
                aliceScore + self.piles[right],
                bobScore,
                memo
            ):
                memo[mi] = True
                return True
                    
        else:
            if self.explore(
                not currTurn,
                left + 1,
                right,
                aliceScore,
                bobScore + self.piles[left],
                memo
            ):
                memo[mi] = True
                return True

            if self.explore(
                not currTurn,
                left,
                right-1,
                aliceScore,
                bobScore + self.piles[right],
                memo
            ):
                memo[mi] = True
                return True
        
        memo[mi] = False
        return memo[mi]
        
    
arr = [
    [3,2,10,4],
    [5,3,4,5],
    [3,7,2,3],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGame(foo)
print(res)