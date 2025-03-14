# https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}

        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1

        for idx, ch in enumerate(s):
            if char_map[ch] == 1:
                return idx
            
        return -1