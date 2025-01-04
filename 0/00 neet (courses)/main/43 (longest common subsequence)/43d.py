# https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)

        rowAbove = [0 for _ in range(cols)]

        for ri in range(rows):
            charOne = text1[ri]
            curRow = [0 for _ in range(cols)]
            for ci in range(cols):
                charTwo = text2[ci]
                isMatch = charOne == charTwo

                # for each position, if `isMatch`, line[ci] = rowAbove[ci-1]
                if isMatch:
                    curRow[ci] = 1 + (rowAbove[ci - 1] if ci - 1 >= 0 else 0)
                else:
                # if is not isMatch, line[ci] = max(line[ci-1], rowAbove[ci])
                    curRow[ci] = max(
                        curRow[ci-1] if ci - 1 >= 0 else 0,
                        rowAbove[ci]
                    )

            rowAbove = curRow


        return rowAbove[-1]



arr = [
    ["abc", "def"],
    ["ace", "abcde"],
    ["abc", "abc"],

]
foo, bar = arr[-1]
sol = Solution()
res = sol.longestCommonSubsequence(foo, bar)
print(res)