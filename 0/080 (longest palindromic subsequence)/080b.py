# https://leetcode.com/problems/longest-palindromic-subsequence/description/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sTwo = s[::-1]

        dim = len(s)
        rowAbove = [0 for _ in range(dim)]
 
        for ri in range(dim):
            chOne = s[ri]
            curr = [0 for _ in range(dim)]
            for ci in range(dim):
                chTwo = sTwo[ci]
                if chOne == chTwo:
                    diag = rowAbove[ci - 1] if (ci - 1 >= 0) else 0
                    curr[ci] = 1 + diag
                else:
                    curr[ci] = max(
                        curr[ci - 1] if (ci - 1 >= 0) else 0,
                        rowAbove[ci]
                    )

            rowAbove = curr

        return rowAbove[-1]


arr = [
    "abcdef",
    "bbbab",
    "cbbd",
]
foo = arr[-1]
sol = Solution()
res = sol.longestPalindromeSubseq(foo)
print(res)