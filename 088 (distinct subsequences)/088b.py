# https://leetcode.com/problems/distinct-subsequences/description/

# https://neetcode.io/solutions/distinct-subsequences
# TODO compare with 088a.py
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass
        if len(t) > len(s):
            return 0
        
        memo = {}
        
        def dfs(i, j):
            foo = (i, j)
            
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if foo in memo:
                return memo[foo]
            
            # skip the current char at `i`
            res = dfs(i + 1, j)
            
            # only continue if the chars are equal
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
                
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