# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}
        
        for idx in range(len(s) - 1, -1, -1):
            ch = s[idx]
            # including the last occurrence of each character
            if ch in char_map: continue
            char_map[ch] = idx

        res = None
        for idx, ch in enumerate(s):
            if ch not in char_map: continue
            
            # if the last index of ch has been determined
            if char_map[ch] > idx:
                diff = char_map[ch] - (idx + 1)
                res = diff if res is None else max(res, diff)
                del char_map[ch]


        return -1 if res is None else res
    
arr = [
    "abca",
    "cbzxy",
    "mgntdygtxrvxjnwksqhxuxtrv",
    "aa",
]
foo = arr[-1]
sol = Solution()
res = sol.maxLengthBetweenEqualCharacters(foo)
print(res)