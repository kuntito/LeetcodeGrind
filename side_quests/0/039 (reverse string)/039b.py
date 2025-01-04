# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        arr = []
        while s:
            arr.append(s.pop())

        for n in arr:
            s.append(n)        
    
arr = [
    ["h","e","l","l","o"],
    ["H","a","n","n","a","h"],
]
foo = arr[-1]
sol = Solution()
sol.reverseString(foo)
print(foo)