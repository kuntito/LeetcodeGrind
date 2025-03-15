# https://leetcode.com/problems/stone-game-iii/description/

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        pass
        # TODO
        # this looks like a dp problem
        # iterate from behind, determine the best score
        # any body can get at each `idx`
        # once all this is sorted
        # play alice and bob through the array
        # each player compares their first, second and third indices
        # for the highest score and picks that
    
arr = [
    [1,2,3,-9],
    [1,2,3,6],
    [1,2,3,7],
    [-1,-2,-3],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGameIII(foo)
print(res)