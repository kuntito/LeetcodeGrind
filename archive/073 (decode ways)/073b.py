# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        # you can either take one or two elements
        
        return self.explore(0, s, {})

    def explore(self, start, s, memo):
        foo = start
        if foo in memo:
            return memo[foo]
        
        dim = len(s)
        if start == dim:
            return 1
        
        res = 0

        end = start + 1
        if end <= dim and self.is_valid(start, end, s):
            res += self.explore(end, s, memo)

        end = start + 2
        if end <= dim and self.is_valid(start, end, s):
            res += self.explore(end, s, memo)

        memo[foo] = res
        return memo[foo]
    
    
    def is_valid(self, start, end, s):
        ch = s[start : end]
        if ch[0] == '0': return False

        num = int(ch)
        return num >= 1 and num < 27


arr = [
    "121",
    "16",
    "11106",
    "226",
    "111111111111111111111111111111111111111111111",
]
foo = arr[-1]
sol = Solution()
res = sol.numDecodings(foo)
print(res)
