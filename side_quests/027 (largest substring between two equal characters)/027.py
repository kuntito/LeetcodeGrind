# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}
        res = None
        for idx in range(len(s) - 1, -1, -1):
            ch = s[idx]
            if ch not in char_map:
                char_map[ch] = idx

        for idx, ch in enumerate(s):
            if ch in char_map and char_map[ch] > idx:
                diff = char_map[ch] - (idx + 1)
                res = diff if res is None else max(res, diff)
                del char_map[ch]


        return -1 if res is None else res
    
arr = [
    "abca",
    "aa",
    "cbzxy",
    "mgntdygtxrvxjnwksqhxuxtrv",
]
foo = arr[-1]
sol = Solution()
res = sol.maxLengthBetweenEqualCharacters(foo)
print(res)