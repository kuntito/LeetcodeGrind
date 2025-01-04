# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_freq = None
        char_map = {}
        best_len = 0

        start, end = 0, 0
        while end < len(s):

            ch = s[end]
            char_map[ch] = char_map.get(ch, 0) + 1

            if most_freq is None:
                most_freq = ch
            
            slots = end - start + 1
            if (slots - char_map[most_freq]) == k:
                char_map[s[start]] -= 1
                most_freq = self.get_most_frequent_char(char_map)
                start += 1
            
            
            if char_map[ch] > char_map[most_freq]:
                most_freq = ch


            end += 1

            best_len = max(slots, best_len)
        return best_len
    

    def get_most_frequent_char(self, char_map: dict):
        most_freq = None
        for ch in char_map:
            if most_freq is None:
                most_freq = ch
            else:
                if char_map[ch] > char_map[most_freq]:
                    most_freq = ch 

        return most_freq

arr = [
    ["ABAB", 2],
    ["DDABDABDBCCDCC", 2],
    ["AAAB", 0],
    ["ABBB", 2],
    ["RARHGAAARRXXX", 7],
    ["AABABBA", 1],
    ["EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH", 7],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.characterReplacement(foo, bar)
print(res)
# print(sol.get_most_consec('A', 0, len(foo)-1))
