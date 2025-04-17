# https://leetcode.com/problems/distinct-subsequences/


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        # it's giving two pointer and recursion
        # two pointers, `ess` and `tee`

        # the idea is the values at `ess` and `tee` should match
        # when they match, we start another recursive call
        # and move `ess` and `tee` forwards

        # consider: `adb` and `ab`
        # initially `a` and `a` match
        # so we proceed to `d` and `b`
        # `d` doesn't match, so we move it forward
        # then get `b` and `b`

        # doing it this way reveals that `ess` pointer should constantly move forward
        # when a match is found, start a recursive call
        # the ending would be when `ess` is out of bounds and `tee` is out of bounds
        # indicating the end of a sequence

        # might benefit from memoization but not sure

        # rather than `ess` and `tee`
        # i'd use `uno` and `dos`

        uno, dos = 0, 0
        return self.explore(uno, dos, s, t, {})

    def explore(self, startUno, dos, reservoir, main_chars, memo):
        mi = (startUno, dos)
        if mi in memo:
            return memo[mi]

        dimUno = len(reservoir)
        dimDos = len(main_chars)

        # if `dos` reaches the end a subsequence has been found
        if dos == dimDos:
            return 1
        # if uno reaches the end and dos hasn't, it means we can't form a subsequence on this path
        if startUno == dimUno:
            return 0

        count = 0
        # we move uno forward
        for uno in range(startUno, dimUno):
            chUno, chDos = reservoir[uno], main_chars[dos]
            if chUno == chDos:
                count += self.explore(uno + 1, dos + 1, reservoir, main_chars, memo)

        memo[mi] = count
        return memo[mi]


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
