# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1        
        
    
arr = [
    ["h","e","l","l","o"],
    ["H","a","n","n","a","h"],
]
foo = arr[-1]
sol = Solution()
sol.reverseString(foo)
print(foo)