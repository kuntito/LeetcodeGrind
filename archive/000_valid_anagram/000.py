# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for ch in s:
            if ch not in s_map:
                s_map[ch] = 0
            s_map[ch] += 1


        for ch in t:
            if ch in s_map:
                s_map[ch] -= 1
                if s_map[ch] == 0:
                    del s_map[ch]
            else:
                return False


        return not s_map


arr = [
    ["rat", "car"],
    ["anagram", "nagaram"],
]

foo = arr[-1]
one, two = foo
sol = Solution()
res = sol.isAnagram(one, two)
print(res)