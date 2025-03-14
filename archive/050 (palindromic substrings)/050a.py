# https://leetcode.com/problems/palindromic-substrings/description/


class Solution:
    def countSubstrings(self, s: str) -> int:
        self.s = s

        res = 0
        for idx in range(len(s)):
            res += self.explore(idx, idx, s)

        for idx in range(1, len(s)):
            res += self.explore(idx - 1, idx, s)

        return res
    
    def explore(self, left, right, chars):
        res = 0
        while left >= 0 and right <= len(chars) - 1 and chars[left] == chars[right]:
            res += 1
            left -= 1
            right += 1

        return res

    
arr = [
    "aaa",
    'bab',
    "abc",
    "aaaaa",
]
foo = arr[-1]
sol = Solution()
res = sol.countSubstrings(foo)
print(res)