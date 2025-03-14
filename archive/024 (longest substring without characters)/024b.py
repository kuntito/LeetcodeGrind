# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0

        res = 0
        for end, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[start])
                start += 1

            res = max(
                res,
                end - start + 1
            )

            seen.add(ch)

        return res
