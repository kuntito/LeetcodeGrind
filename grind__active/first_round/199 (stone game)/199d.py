# https://leetcode.com/problems/stone-game/description/


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        # the reason `return True` works is
        # at any point, the participants can pick stones from either end of the piles
        
        # but whichever choice, left or right
        # leads to another set of left or right choices
        # and whichever of those is picked, leads to more left and right choices
        
        # depending on the array size, the decision tree could grow very large with numerous paths including the optimal path(s)
        
        # however, one thing stands true
        # the optimal path can be traced up to the first left or the first right decision
        # since we know alice starts first, we don't need to do the work to determine the optimal path.
        # 
        # if it emerges from a left choice, that's what alice would pick
        # if it emerges from a right choice, that's also what alice would pick
        # 
        # since the problem insists that alice and bob play optimally
        # the first player ALWAYS wins
        
        
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