# https://leetcode.com/problems/decode-ways/description/

# TODO `https://neetcode.io/solutions/decode-ways`
class Solution:
    def numDecodings(self, s: str) -> int:
        # you can either take one or two elements
 
        return self.explore(0, 1, s, {})

    def explore(self, start, end, s, memo):
        foo = (start, end)
        if foo in memo:
            return memo[foo]

        dim = len(s)
        if end > dim:
            return 0
        
        res = 0
        if self.isValid(start, end, s):
            if end == dim:
                memo[foo] = 1
                return memo[foo]
            res += self.explore(end, end + 1, s, memo)

        twoDigitEnd = end + 1
        if self.isValid(start, twoDigitEnd, s):
            if twoDigitEnd == dim:
                memo[foo] = res + 1
                return memo[foo]
            res += self.explore(twoDigitEnd, twoDigitEnd + 1, s, memo)

        memo[foo] = res
        return memo[foo]

        
    def isValid(self, start, end, s):
        slice = s[start:end]
        if slice[0] == '0': return False

        num = int(slice)
        return num >= 1 and num < 27
    

arr = [
    "16",
    "226",
    "11106",
    "121",
    "111111111111111111111111111111111111111111111",
]
foo = arr[-1]
sol = Solution()
res = sol.numDecodings(foo)
print(res)