# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

class Solution:
    def minOperations(self, s: str) -> int:
        return min(
            self.explore('10', s),
            self.explore('01', s)
        )
    
    def explore(self, pattern, s):
        dim = len(s)
        idx = 0
        count = 0
        while idx < dim:
            if s[idx] != pattern[0]:
                count += 1
            if idx + 1 < dim and s[idx+1] != pattern[1]:
                count += 1

            idx += 2

        return count


arr = [
    "1111",
    "10",
    "0100",
    "1"
]
foo = arr[-1]
sol = Solution()
res = sol.minOperations(foo)

print(res)