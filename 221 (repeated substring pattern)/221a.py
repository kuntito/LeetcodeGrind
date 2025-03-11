from collections import Counter

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # convert the string to a counter

        counter = Counter(s)

        for ch, freq in counter.items():
            if len(s) % freq:
                return False

        return True
    
arr = [
    "aba",
    "abab"
]
foo = arr[-1]
sol = Solution()
res = sol.repeatedSubstringPattern(foo)
print(res)