# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen = {}

        longest, end = 0, 0
        while end < len(s):
            ch = s[end]
            if ch in seen:
                longest = max(
                    longest,
                    end - start
                )

                foo = seen[ch]
                while start <= foo:
                    del seen[s[start]]
                    start += 1

            seen[ch] = end
            end += 1
        
        return max(
            longest,
            end - start,
        )
    

arr = [
    "abcabcbb",
    "abba",
    "abcabcbb",
]
foo = arr[-1]
sol = Solution()

res = sol.lengthOfLongestSubstring(foo)
print(res)