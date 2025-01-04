# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        all_words = s.split()
        if len(pattern) != len(all_words): return False


        seen_words = set()
        bijection = {}

        dim = len(all_words)
        for idx in range(dim):
            ch = pattern[idx]
            word = all_words[idx]

            if (ch in bijection or word in seen_words):
                if ch not in bijection:
                    return False

                if bijection[ch] != word:
                    return False
                
            

            
            bijection[ch] = word
            seen_words.add(word)

        return True


arr = [
    ["abba", "dog cat cat dog"],
    ["abba", "dog cat cat fish"],
    ["aaaa", "dog cat cat dog"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordPattern(foo, bar)
print(res)