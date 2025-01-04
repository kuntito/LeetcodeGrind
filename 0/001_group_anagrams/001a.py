# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_map = {}
        res = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in word_map:
                word_map[sorted_word] = []
                res.append(word_map[sorted_word])

            word_map[sorted_word].append(word)

        return res



arr = [
    ["", ""],
    ["eat","tea","tan","ate","nat","bat"],
]
foo = arr[-1]
sol = Solution()
res = sol.groupAnagrams(foo)
print(res)
