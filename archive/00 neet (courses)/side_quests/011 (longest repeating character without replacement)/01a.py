# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_map = {}
        best_len = 0

        left = 0
        most_freq = s[left]
        for idx, ch in enumerate(s):
            ch_map[ch] = ch_map.get(ch, 0) + 1
            if ch_map[ch] > ch_map[most_freq]:
                most_freq = ch

            window_len = idx - left + 1
            if window_len > (ch_map[most_freq] + k):
                ch_map[s[left]] -= 1
                left += 1
                    
            window_len = idx - left + 1
            best_len = max(best_len, window_len)

        return best_len
    
    

arr = [
    ["ABAB", 2],
    ["DDABDABDBCCDCC", 2],
    ["AAAB", 0],
    ["ABBB", 2],
    ["RARHGAAARRXXX", 7],
    ["AABABBA", 1],
    ["ABCCCCC", 2],
    ["EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH", 7],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.characterReplacement(foo, bar)
print(res)