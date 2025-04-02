# https://leetcode.com/problems/stone-game/description/

from collections import deque

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        # the reason this works is.. at each point the game
        # the participants can either pick the leftmost element or
        # the rightmost element
        # depending on the list size, there could be innumerable choices
        # that emerge from each choice, `left` or `right`
        # but how ever many those choices are, one of the them would result in
        # a better strategy
        
        # we can conclude, that whatever the answer is
        # it'd have to be by picking `left` or picking `right`
        # since alice can pick either, it's safe to say that she would always win the game
        return True
        
    
arr = [
    [3,2,10,4],
    [5,3,4,5],
    [3,7,2,3],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGame(foo)
print(res)