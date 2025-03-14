# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        dim = len(s)
        memo = {dim: 1}

        for idx in range(dim-1, -1, -1):
            oneDig = s[idx]
            if oneDig == "0":
                memo[idx] = 0
            else:
                memo[idx] = memo[idx + 1]

                if idx + 1 < dim and self.is_valid(s[idx:idx+2]):
                    memo[idx] += memo[idx + 2]
        
        return memo[0]

    def is_valid(self, chars):
        return 1 <= int(chars) <= 26


arr = [
    "121",
    "16",
    "11106",
    "226",
    "9",
    "111111111111111111111111111111111111111111111", 
]
foo = arr[-1]
sol = Solution()
res = sol.numDecodings(foo)
print(res)
