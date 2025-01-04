# https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass
        # two pointers, `sIdx` and `tIdx`
        # both represents the current index in the respective strings
        
        # recursively iterate from `sIdx,` to `len(s)`
        # if the character at `sIdx` matches the charactaer at `tIdx`
        # start another recursive call `explore(sIdx+1, s, tIdx + 1, t)`
        
        # if `tIdx == len(t)`, return 1
        # if `sIdx == len(s)` return 0
        
        # TODO, it's taking too long
        
        return self.explore(0, s, 0, t, {})
        
    def explore(self, s_idx, s, t_idx, t, memo):
        foo = (s_idx, t_idx)
        if foo in memo:
            return memo[foo]
        
        if t_idx == len(t):
            memo[foo] = 1
            return 1
        if s_idx == len(s):
            memo[foo] = 0
            return 0
        
        res = 0
        for idx in range(s_idx, len(s)):
            if s[idx] == t[t_idx]:
                res += self.explore(idx+1, s, t_idx+1, t, memo)
                
        
        memo[foo] = res
        return memo[foo]
    
arr = [
    ["babgbag", "bag"],
    ["raat", "rat"],
    ["rabbbit", "rabbit"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numDistinct(foo, bar)
print(res)