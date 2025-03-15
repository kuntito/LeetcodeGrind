# https://leetcode.com/problems/last-stone-weight-ii/description/

# TODO compare with asteroid collision

# TODO https://neetcode.io/solutions/last-stone-weight-ii
# 11:40
# TODO write your version
import heapq
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        pass
        # the aim is to have two piles who's sum is closest
        # to half of the total piles
        
        # find total piles, `sum(stones)`
        
        # explore all possible pile combinations
        # and select the one that's closest to `totalPiles/2`
        
        # once you have that, smash the stones in the piles together
        # TODO do you just subtract that value from the remainder of total??
        
        total = sum(stones)
        target = total // 2
        
        self.explore(target, stones, 0, 0)
        
    def explore(self, target, stones, start_idx, total):
        pass
        if total > target:
            return
        
        # TODO am i storing all the `total`s that don't exceed target?
        
        dim = len(stones)
        for idx in range(start_idx, dim):
            item = stones[idx]
            total += item
        

        
        

arr = [
    [2,7,4,1,8,1],
    [31,26,33,21,40],
]
foo = arr[-1]
sol = Solution()
res = sol.lastStoneWeightII(foo)
print(res)