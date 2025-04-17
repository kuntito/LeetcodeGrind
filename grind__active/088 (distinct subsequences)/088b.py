# https://leetcode.com/problems/distinct-subsequences/description/

# https://neetcode.io/solutions/distinct-subsequences
# TODO compare with 088a.py
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass
        if len(t) > len(s):
            return 0
        
        memo = {}
        
        def dfs(uno, dos):
            foo = (uno, dos)
            
            if dos == len(t):
                return 1
            if uno == len(s):
                return 0
            if foo in memo:
                return memo[foo]
            
            # skip the current char at `i`
            res = dfs(uno + 1, dos)
            
            # only continue if the chars are equal
            if s[uno] == t[dos]:
                res += dfs(uno + 1, dos + 1)
                
            memo[foo] = res
            return res

        return dfs(0, 0)
    
arr = [
    ["babgbag", "bag"],
    ["raat", "rat"],
    ["rabbbit", "rabbit"],
    ["", "a"],
    ["a", ""],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numDistinct(foo, bar)
print(res)