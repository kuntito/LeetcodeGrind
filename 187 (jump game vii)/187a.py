# https://leetcode.com/problems/jump-game-vii/description/

# TODO TLE
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        pass
    
        return self.explore(0, s, minJump, maxJump, {})
    
    def explore(self, start_idx, chars, low, high, memo):
        if start_idx in memo:
            return memo[start_idx]
        
        if start_idx >= len(chars):
            return True
        
        if start_idx + 1 == len(chars) and chars[-1] == '0':
            return True

        if chars[start_idx] == '1':
            memo[start_idx] = False
            return memo[start_idx]
        
        dim = min(
            start_idx + high + 1,
            len(chars)
        )
        for idx in range(start_idx + low, dim):
            if self.explore(idx, chars, low, high, memo):
                memo[start_idx] = True
                return memo[start_idx]
            
            
        memo[start_idx] = False
        return memo[start_idx]

arr = [
    ["011010", 2, 3],
    ["01101110", 2, 3]
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.canReach(foo, bar, baz)
print(res)
            
            
        
        