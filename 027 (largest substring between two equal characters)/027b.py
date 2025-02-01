# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}
        
        # determine the first and last occurrences of each char
        for idx, ch in enumerate(s):
            if ch not in char_map:
                char_map[ch] = [idx, None]
                
            char_map[ch][1] = idx
        
        # calculate the length of the max substring
        for start, end in char_map.values():
            dist = # TODO
    
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