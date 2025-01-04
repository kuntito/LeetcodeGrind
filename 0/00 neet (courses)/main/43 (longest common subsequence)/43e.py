# https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        # first row
        for ci in range(cols):
            dp[0][ci] = dp[0][ci - 1]
            # comparing first char in `text1` with every char in `text2`
            if text1[0] == text2[ci]:
                dp[0][ci] = 1
    

        for ri in range(1, rows):
            chOne = text1[ri]
            for ci in range(cols):
                chTwo = text2[ci]
                isMatch = chOne == chTwo
                if ci == 0:
                    if isMatch:
                        dp[ri][ci] = 1
                    else:
                        dp[ri][ci] = dp[ri-1][ci]
                else:
                    if isMatch:
                        dp[ri][ci] = 1 + dp[ri-1][ci-1]
                    else:
                        dp[ri][ci] = max(
                            dp[ri-1][ci],
                            dp[ri][ci-1],
                        )

        return dp[-1][-1]


arr = [
    ["abc", "def"],
    ["ace", "abcde"],
    ["abc", "abc"],

]
foo, bar = arr[-1]
sol = Solution()
res = sol.longestCommonSubsequence(foo, bar)
print(res)