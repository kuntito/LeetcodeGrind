# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        char_map = {}

        for w in words:
            for ch in w:
                char_map[ch] = char_map.get(ch, 0) + 1

        for ch, count in char_map.items():
            if count % len(words) != 0:
                return False
                
        return True
    
arr = [
    ["ab","a"],
    ['a', 'b'],
    ["abc","aabc","bc"],
    ["aaaab","b"],
]
foo = arr[-1]
sol = Solution()
res = sol.makeEqual(foo)
print(res)