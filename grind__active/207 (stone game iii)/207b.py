# https://leetcode.com/problems/stone-game-iii/description/

# https://neetcode.io/solutions/stone-game-iii
# 08:37
# TODO how does this work?
class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        pass
        # what does it mean to play optimally?
        
        # we'd explore each position
        # for i in range(1, 4)
        
        
        res = self.explore(0, stoneValue, {})
        if res > 0:
            return "Alice"
        elif res == 0:
            return "Tie"
        
        return "Bob"
    
    def explore(self, start_idx, stones, memo):
        if start_idx in memo:
            return memo[start_idx]
        
        dim = len(stones)
        if start_idx == len(stones):
            return 0
        
        endRange = min(start_idx + 3, dim)
        maxHere = float("-inf")
        picks = 0
        for idx in range(start_idx, endRange):
            picks += stones[idx]
            # `res` represents the highest score at `idx + 1`
            res = self.explore(idx + 1, stones, memo)
            maxHere = max(
                maxHere,
                picks - res
            )
            
        memo[start_idx] = maxHere
        return memo[start_idx]
    
arr = [
    [-1,-2,-3],
    [1,2,3,7],
    [1,2,3,-9],
    [1,2,3,6],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGameIII(foo)
print(res)