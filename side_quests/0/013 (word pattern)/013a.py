# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False

        bijection = {}
        seen_words = set()
        for ch, w in zip(pattern, words):
            # if the character is present and word is absent
            if ch in bijection and bijection[ch] != w:
                return False
            
            # if the word is present and character is absent
            if w in seen_words and ch not in bijection:
                return False
            

            bijection[ch] = w
            seen_words.add(w)

        return True
            



arr = [
    ["aaaa", "dog cat cat dog"],
    ["aa", "dog dog"],
    ["abba", "dog dog dog dog"],
    ["abba", "dog cat cat fish"],
    ["abba", "dog cat cat dog"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordPattern(foo, bar)
print(res)