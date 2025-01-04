# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        return " ".join(x[::-1] for x in words)


arr = [
    "Let's take LeetCode contest",
]
foo = arr[-1]
sol = Solution()
res = sol.reverseWords(foo)
print(res)