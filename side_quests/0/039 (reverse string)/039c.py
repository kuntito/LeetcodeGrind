# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        self.explore(0, len(s)-1, s)

    def explore(self, left, right, s):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        self.explore(left+1, right-1, s)
    
arr = [
    ["h","e","l","l","o"],
    ["H","a","n","n","a","h"],
]
foo = arr[-1]
sol = Solution()
sol.reverseString(foo)
print(foo)