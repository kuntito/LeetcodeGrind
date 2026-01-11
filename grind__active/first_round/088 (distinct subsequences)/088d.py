# https://leetcode.com/problems/distinct-subsequences/


# TODO explore the dp solution?
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass
        # TODO can you explore all possible combinations of `(i, j)`



arr = [
    ["babgbag", "bag"],
    ["rabbbit", "rabbit"],
    [
        "adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc",
        "bcddceeeebecbc",
    ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numDistinct(foo, bar)
print(res)
