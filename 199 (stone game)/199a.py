# https://leetcode.com/problems/stone-game/description/

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        pass
    
        # two integer variables, `alice` and `bob`
        # two pointers, `left` and `right`
        # while left <= right
        # compare the values at left and right and give the highest to alice
        # on the next turn, do the same for bob
        
        # TODO in the case, where the left and right val's are equal
        # explore both scenarios
    
arr = [
    [3,7,2,3],
    [5,3,4,5],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGame(foo)
print(res)