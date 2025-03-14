# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

class Solution:
    def minOperations(self, s: str) -> int:
        patternOne = '01'
        patternTwo = '10'

        changesOne = 0
        changesTwo = 0
        for idx, ch in enumerate(s):
            if idx % 2 == 0:
                if ch != patternOne[0]:
                    changesOne += 1
                if ch != patternTwo[0]:
                    changesTwo += 1
            else:
                if ch != patternOne[1]:
                    changesOne += 1
                if ch != patternTwo[1]:
                    changesTwo += 1

        return min(changesTwo, changesOne)


arr = [
    "10",
    "0100",
    "1"
    "1111",
]
foo = arr[-1]
sol = Solution()
res = sol.minOperations(foo)

print(res)